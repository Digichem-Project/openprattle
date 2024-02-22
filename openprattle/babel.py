# General imports.
import subprocess
from subprocess import CalledProcessError
import re
import os
import copy
from pathlib import Path
import logging

import openprattle

# Try and load openbabel bindings.
HAVE_PYBEL = False

try:
    from openbabel import pybel
    HAVE_PYBEL = True

except ModuleNotFoundError:
    # No bindings, carry on.
    logging.debug("Could not load python pybel bindings; falling back to obabel executable", exc_info = True)

except Exception:
    # Some other error occurred; print an error but continue.
    logging.error("Found but could not load python pybel bindings; falling back to obabel executable", exc_info = True)
    

class Openbabel_converter():
    """
    Top level class for openbabel wrappers.
    
    We support both the python interface (pybel) and running obabel directly.
    """
    
    def __init__(self, *, input_file = None, input_file_buffer = None, input_file_path = None, input_file_type = None):
        """
        Constructor for the OpenBabel converter.

        Input files can be specified in one of three ways:
         - As an open file descriptor (input_file and input_file_type)
         - As an in-memory buffer, most probably a string or bytes-like object (input_file_buffer and input_file_type)
         - As a file path (input_file_path and optionally input_file_type)
        
        :param input_file: An open file descriptor in the format given by input_file_type that should be converted.
        :param input_file_buffer: Alternartively, a buffer (unicode string or bytes) in the format given by input_file_type that should be converted.
        :param input_file_path: Alternatively, a path to a file that should be converted.
        :param input_file_type: A shortcode identifying the format of the input file. If not given but input_file_path is given, then this will be determined automatically.
        """
        
        self.input_file = input_file
        self.input_file_buffer = input_file_buffer
        self.input_file_path = input_file_path
        self.input_file_type = input_file_type
        # Currently, we always use add H because certain formats (xyz) cannot have H added.
        self.add_H = True
        
    @classmethod
    def from_file(self, *, input_file = None, input_file_buffer = None, input_file_path = None, input_file_type = None, **kwargs):
        """
        A more powerful constructor that automatically decides which concrete class to use.
        """
        # First, get out file format if it wasn't given to us.
        if input_file_type is None:
            input_file_type = self.type_from_file_name(input_file_path)
        
        # Next, decide which class
        cls = self.get_cls(input_file_type)
        
        # And return.
        return cls(
            input_file = input_file,
            input_file_buffer = input_file_buffer,
            input_file_path = input_file_path,
            input_file_type = input_file_type,
            **kwargs
        )
        
    @classmethod
    def type_from_file_name(self, input_file_name, allow_none = False):
        """
        Get the type of a file based on its file name.
        
        This method largely uses the file extension (.com, .tmol etc), with a few other simple rules.
        
        :param input_file_name: The name of the file to check.
        :param allow_none: If the type of the file cannot be determined and allow_none is False (the default), an exception is raised. Otherwise, None is returned.
        """
        try:
            input_file_name = Path(input_file_name)
        
        except TypeError:
            if allow_none:
                return None
            
            else:
                # No file given.
                raise ValueError("Could not automaticlly determine file format; no file name was given") from None
        
        # Get file extension (removing the dot character).
        extension = input_file_name.suffix[1:]
        
        if extension != "":
            # All done.
            return extension.lower()
        
        elif input_file_name.name == "coord":
            # This is a turbomole file.
            return "tmol"
        
        else:
            if allow_none:
                return None
            
            else:
                # Don't recognise the file format.
                raise ValueError("Could not determine file format of file '{}'; the file does not have an extension and is not recognised".format(input_file_name))
    
    @classmethod
    def get_cls(self, input_file_type):
        """
        Automatically get a concrete Babel_converter class that can be used to convert a file.
        
        If the pybel bindings are available and loaded successfully; then a Pybel_converter object will be returned,
        otherwise, the Obabel_converter will be returned (this requires openbabel to be installed and obabel to be in the path).
        
        The only exception is for the cdx format for which Obabel_converter is always returned (because of bug https://github.com/openbabel/openbabel/issues/1690 which still seems to be plaguing us in mid-2020).
        """
        input_file_type = input_file_type if input_file_type else ""

        if not HAVE_PYBEL or input_file_type.lower() == "cdx":
            return Obabel_converter
        
        else:
            return Pybel_converter
        
    @property
    def input_name(self):
        """
        A descriptive name of the file we are converting. Works even if converting from memory.
        """
        if self.input_file_path is not None:
            return self.input_file_path
        else:
            return "(file loaded from memory)"
        
    def convert(self, output_file_type = None):
        """
        Convert the input file wrapped by this class to the designated output_file_type.
        
        Inheriting classes should write their own implementation.
        
        :param output_file_type: The file type to convert to.
        """
        raise NotImplementedError("Abstract class Babel_converter does not have a convert() method defined (inheriting classes should write their own)")
        

if HAVE_PYBEL:
    class Pybel_converter(Openbabel_converter):
        """
        Wrapper class for pybel
        """            
        
        def convert(self, output_file_type = None, output_file = None, *, gen3D = None, charge = None, multiplicity = None):
            """
            Convert the input file wrapped by this class to the designated output_file_type.
            
            :param output_file_type: The file type to convert to.
            :param output_file: Optional file name to write to. If not given, the converted file will be returned as a string (or binary string depending on format).
            :param gen3D: If True and the loaded molecule does not have 3D coordinates, these will be generated (this will scramble atom coordinates).
            :param charge: Optional charge of the output format.
            :param multiplicity: Optional multiplicity of the output format.
            :return: The converted file, or None if output_file is not None.
            """
            output_file = str(output_file) if output_file is not None else None

            if not output_file_type:
                output_file_type = self.type_from_file_name(output_file)

            if output_file is None and output_file_type == "png":
                raise ValueError("output_file must not be None if format is png")
            
            try:
                # Stop logging from pybel, we'll handle that ourselves.
                pybel.ob.obErrorLog.StopLogging()
                
                # For Pybel, gen3D defaults to True, because we'll only use gen3d if not already in 3D.
                gen3D = gen3D if gen3D is not None else True
                
                # Get upset if input_file_type is empty (because openbabel acts weird when it is).
                if self.input_file_type is None or self.input_file_type == "":
                    raise TypeError("Cannot convert file; input_file_type '{}' is None or empty".format(self.input_file_type))
                
                # Pybel doesn't provide a method to read from an open file, weirdly.
                # This means we need to load the whole file into memory first.
                # TODO: Investigate the pybel/openbabel lib to see if there's a better workaround.
                if self.input_file:
                    buffer = self.input_file.read()
                
                elif self.input_file_buffer:
                    buffer = self.input_file_buffer
                
                else:
                    buffer = None
                
                # Read in the molecule(s) in the given file.
                try:
                    # This is a generator.
                    # Use a different func depending on whether we're reading from file or memory.
                    if buffer:
                        # Reading from memory.
                        # TODO: Why str()?
                        molecule = pybel.readstring(self.input_file_type, str(buffer))
                    
                    else: 
                        # Readfile gives us an iterator of molecules...
                        molecules = pybel.readfile(self.input_file_type, str(self.input_file_path))
                        
                        # ...but we're only ever interested in one.
                        # Try and get the first molecule.
                        try:
                            molecule = next(molecules)
                        
                        except StopIteration:
                            raise ValueError("Cannot read file '{}'; file does not contain any molecules".format(self.input_name)) from None
                        
                        
                except Exception as e:
                    raise Exception("Failed to parse file '{}'".format(self.input_name)) from e
                
                if charge is not None:
                    molecule.OBMol.SetTotalCharge(charge)
                    
                if multiplicity is not None:
                    molecule.OBMol.SetTotalSpinMultiplicity(multiplicity)
                
                # If we got a 2D (or 1D) format, convert to 3D (but warn that we are doing so.)
                if molecule.dim != 3 and gen3D:
                    # We're missing 3D coords.
                    logging.warning("Generating 3D coordinates from {}D file '{}'; this will scramble atom coordinates".format(molecule.dim, self.input_name))
                    molecule.localopt()
                    
                if self.add_H:
                    # Add hydrogens.
                    molecule.addh()
                
                # Now convert and return
                # If the format is png, use the draw() method instead because write() is bugged.
                if output_file_type == "png":
                    molecule.draw(False, output_file)
                
                else:
                    return molecule.write(output_file_type, output_file, overwrite = True)
            
            finally:
                # Start logging again.
                pybel.ob.obErrorLog.StartLogging()


class Obabel_converter(Openbabel_converter):
    """
    Wrapper class for openbabel.
    
    Unlike Babel_converter (which wraps the openbabel python interface), Openbabel_wrapper uses subprocess.run() 
    """
    
    # The regex we'll use to check obabel converted successfully.
    #obabel_success = re.compile(r"\b(?!0\b)\d*\b molecules? converted")
    obabel_fail = re.compile(r"\b0 molecules converted")
    
    # 'Path' to the obabel executable.
    obabel_execuable = "obabel"        
    
    def convert(self, output_file_type, output_file = None, *, gen3D = None, charge = None, multiplicity = None):
        """
        Convert the input file wrapped by this class to the designated output_file_type.
         
        :param output_file_type: The file type to convert to.
        :param output_file: Optional file name to write to. If not given, the converted file will be returned as a string (or binary string depending on format).
        :param gen3D: If True and the loaded molecule does not have 3D coordinates, these will be generated (this will scramble atom coordinates).        
        :param charge:  Optional charge of the output format.
        :param multiplicity: Optional multiplicity of the output format.
        :return: The converted file, or None if output_file is not None.
        """
        output_file = str(output_file) if output_file is not None else None

        if not output_file_type:
            output_file_type = self.type_from_file_name(output_file)
        
        # For Obabel, gen3D defaults to False, because we can't determine ahead of time whether we're in 3D or not (unless format is cdx, which is always 2D).
        if gen3D is None:
            if self.input_file_type.lower() == "cdx":
                gen3D = True
            else:
                gen3D = False
        
        if charge is not None:
            # We can't set charge with obabel sadly.
            logging.warning("Unable to set charge '{}' of molecule loaded from file '{}' with obabel converter".format(charge, self.input_name))
            
        if multiplicity is not None:
            # We can't set charge with obabel sadly.
            logging.warning("Unable to set multiplicity '{}' of molecule loaded from file '{}' with obabel converter".format(multiplicity, self.input_name))
        
        # Run
        return self.run_obabel(output_file_type, output_file, gen3D = gen3D)
        
    def run_obabel(self, output_file_type, output_file, *, gen3D):
        """
        Run obabel, converting the input file wrapped by this class to the designated output_file_type.
        
        :param output_file_type: The file type to convert to.
        :param output_file: Optional file name to write to. If not given, the converted file will be returned as a string (or binary string depending on format).
        :param gen3D: If True and the loaded molecule does not have 3D coordinates, these will be generated (this will scramble atom coordinates).
        :return: The converted file.
        """
        # The signature we'll use to run obabel.
        sig = [self.obabel_execuable]
        
        # Add the input path if we're reading from file.
        if self.input_file_path:
            sig.append(str(self.input_file_path))
            
        # Now add the input and output switches.
        sig.extend([
             "-o", output_file_type,
             "-i", self.input_file_type
        ])
        
        # Add gen3D command if we've been asked to.
        if gen3D:
            logging.warning("Generating 3D coordinates from file '{}'; this will scramble atom coordinates".format(self.input_name))
            sig.append("--gen3D")
        
        # Add H if we've been asked.    
        if self.add_H:
            sig.append("-h")
            
        # If a file to write to has been given, set it.
        if output_file is not None:
            sig.extend(['-O', output_file])
        
        # There are several openbabel bugs re. the chem draw format; one of them occurs when we are frozen and have set the BABEL_LIBDIR env variable.
        # The workaround is to temp unset BABEL_LIBDIR.
        # Get our current environment.
        env = copy.copy(os.environ)
        # Now delete BABEL_LIBDIR if we are frozen.
        if openprattle.frozen:
            try:
                # TODO: Test this is still a problem?
                pass
                #del env['BABEL_LIBDIR']
            
            except KeyError:
                # The BABEL_LIBDIR isn't set.
                pass
        
        # GO.
        done_process = subprocess.run(
             sig,
             # If we're reading from buffer, specify here:
             input = self.input_file_buffer,
             # If we're reading from an open file, specify that here:
             stdin = self.input_file,
             stdout = subprocess.PIPE,
             stderr = subprocess.PIPE,
             # TODO: Using universal newlines is probably not safe here; some formats are binary (.cdx etc...)
             universal_newlines = True,
             check = True,
             env = env
         )
        
        # Sadly, openbabel doesn't appear to make use of return codes all the time.
        # We'll do basic error checking on whether our output contains a certain string.
        #if not self.obabel_success.search(done_process.stderr):
        if self.obabel_fail.search(done_process.stderr):
            raise Exception("obabel command did not appear to complete successfully") from CalledProcessError(done_process.returncode, " ".join(done_process.args), done_process.stdout, done_process.stderr)
        
        # Return our output.
        return done_process.stdout if output_file is None else None


class Openbabel_formats():
    """
    ABC for classes that retrieve available formats.
    """

    def read(self):
        """
        Retrieve supported input (read) formats.

        The return value is a dictionary of formats. Each key is the format shortcode (which can be used as input_file_type). Each value is a description of the format.
        """
        raise NotImplementedError("Implement in subclass")

    def write(self):
        """
        Retrieve supported write (output) formats.

        The return value is a dictionary of formats. Each key is the format shortcode (which can be used as output_file_type elsewhere in this module). Each value is a description of the format.
        """
        raise NotImplementedError("Implement in subclass")

if HAVE_PYBEL:
    class Pybel_formats(Openbabel_formats):
        """
        Class for retrieving the supported file formats from pybel.
        """

        def read(self):
            """
            Retrieve supported input (read) formats.

            The return value is a dictionary of formats. Each key is the format shortcode (which can be used as input_file_type). Each value is a description of the format.
            """
            return pybel.informats

        def write(self):
            """
            Retrieve supported write (output) formats.

            The return value is a dictionary of formats. Each key is the format shortcode (which can be used as output_file_type elsewhere in this module). Each value is a description of the format.
            """
            return pybel.outformats
            

class Obabel_formats(Openbabel_formats):
    """
    Class for retrieving the supported file formats from obabel.
    """
    
    # Bit of a hack.
    obabel_execuable = Obabel_converter.obabel_execuable
    
    def run(self, readwrite):
        """
        """
        if readwrite not in ["read", "write"]:
            raise ValueError("readwrite must be one of either 'read' or 'write'")
        
        # The signature we'll use to run obabel.
        sig = [
            self.obabel_execuable,
            "-L",
            "formats",
            readwrite
        ]
        
        # GO.
        done_process = subprocess.run(
             sig,
             stdout = subprocess.PIPE,
             stderr = subprocess.PIPE,
             universal_newlines = True,
             check = True, # Obabel doesn't use return codes properly, but this doesn't hurt.
         )
        
        # The output should look like this:
        # abinit -- ABINIT Output Format
        # acesout -- ACES output format
        # acr -- ACR format
        # ...
        try:
            formats = {}
            for line in done_process.stdout.splitlines():
                code, desc = (part.strip() for part in line.split("--"))
                formats[code] = desc
                
        except Exception as e:
            # Output was bad.
            raise Exception("Failed to parse stdout from obabel command") from e
        
        return formats

    
    def read(self, refresh = False):
        """
        Retrieve supported input (read) formats.

        The return value is a dictionary of formats. Each key is the format shortcode (which can be used as input_file_type). Each value is a description of the format.
        """
        if refresh:
            try:
                del self.__class__._read
            
            except AttributeError:
                pass
        
        try:
            return self.__class__._read
        
        except AttributeError:
            # Cache miss.
            self.__class__._read = self.run("read")
            return self.__class__._read
        
    def write(self, refresh = False):
        """
        Retrieve supported write (output) formats.

        The return value is a dictionary of formats. Each key is the format shortcode (which can be used as output_file_type elsewhere in this module). Each value is a description of the format.
        """
        if refresh:
            try:
                del self.__class__._write
            
            except AttributeError:
                pass
        
        try:
            return self.__class__._write
        
        except AttributeError:
            # Cache miss.
            self.__class__._write = self.run("write")
            return self.__class__._write

def formats():
    if HAVE_PYBEL:
        return Pybel_formats()
    
    else:
        return Obabel_formats()