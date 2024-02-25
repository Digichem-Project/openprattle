# OpenPrattle

A command-line tool and python library that provides a seamless interface to both the [Pybel library](https://github.com/openbabel/openbabel/tree/master/scripts/python) and [obabel](https://github.com/openbabel/openbabel) command-line tool.

## Dependencies

### Required

Openbabel >= 3.0.0

Python >= 3.9

### Optional

JSON (for printing in JSON format with the --readable and --writable options)

pytest (for running the unit tests)

## Usage

OpenPrattle provides both a python library and command-line tool.

### Library

Files are interconverted using converter objects, each of which represents a supported backend.
To automatically get a suitable converter object, use `openprattle.Openbabel_converter.from_file()`:

```
from openprattle import Openbabel_converter

my_file = "Benzene.xyz"
converter = Openbabel_converter.from_file(input_file_path = my_file)
```

By default, the format of the input file is determined automatically from its extension. The format
can be explicitly specified with `input_file_type`:

```
converter = Openbabel_converter.from_file(input_file_path = my_file, input_file_type = "xyz")
```

`Openbabel_converter.from_file()` will favour the Pybel backend if it is available, except when
converting files in formats that are not supported by Pybel. To explicitly choose a backend, use
the `backend` option:

```
converter = Openbabel_converter.from_file(
    input_file_path = my_file,
    input_file_type = "xyz",
    backend = "Pybel" # Either 'Pybel', 'Obabel', or 'Auto'
)
```

Or use the appropriate class directly.

```
from openprattle import Obabel_converter, Pybel_converter

my_file = "Benzene.xyz"
obabel = Obabel_converter(
    input_file_path = my_file
)
pybel = Pybel_converter(
    input_file_path = my_file
)
```

In addition to reading from a file path, all the converters can read from an open file descriptor
using `input_file`:

```
with open("Benzene.xyz") as my_file:
    converter = Openbabel_converter.from_file(
        input_file = my_file,
        input_file_type = "xyz",
    )
```

Or from a memory buffer using `input_file_buffer`:

```
with open("Benzene.xyz") as my_file:
    buffer = my_file.read()

converter = Openbabel_converter.from_file(
    input_file_buffer = buffer,
    input_file_type = "xyz",
)
```

Whenever the `input_file` or `input_file_buffer` options are used, the file type must be specified
with `input_file_type`.

Once an appropriate converter object has been obtained, the file can be converted by calling `convert()`:

```
converter = Openbabel_converter.from_file(input_file_path = "Benzene.xyz")
converter.convert("cml", "Benzene.cml")
```

`convert()` can either write to a file (using `output_file`), or return the converted file as a buffer
(if `output_file` is omitted):

```
converter = Openbabel_converter.from_file(input_file_path = "Benzene.xyz")
output_file = converter.convert("cml")
print(output_file)
```

A limited subset of formats support molecular charge and multiplicity information. These can be set
using the ``charge`` and ``multiplicity`` options:

```
converter = Openbabel_converter.from_file(input_file_path = "Benzene.xyz")
converter.convert("cml", "Benzene.cml", charge = 1, multiplicity = 2)
```

The following is a non-exhaustive list of formats that do support charge and multiplicity:
 - com (Gaussian input)
 - dalmol (DALTON input)
 - gau (Gaussian input)
 - gjc (Gaussian input)
 - gjf (Gaussian input)
 - gzmat (Gaussian Z-Matrix Input)

Of these, only dalmol is both a readable and writable format.

> [!IMPORTANT]
> Currently, OpenPrattle is not aware of which formats will preserve the specified charge
> and multiplicity. If an unsupported format is chosen, any charge and multiplicity information
> will be silently discarded.

Charge and multiplicity are only supported with the `Pybel_converter` backend. This means that to
convert from a format that is not supported by pybel (most noticeably ChemDraw's .cdx), two
conversions should be performed in sequence:
```
from openprattle import Openbabel_converter, Pybel_converter

intermediate = Openbabel_converter.from_file(input_file_path = "Benzene.cdx").convert("xyz")
final = Pybel_converter(input_file_buffer = "intermediate", input_file_type = "xyz").convert(
    "com",
    charge = 1,
    multiplicity = 2
)
```

1D (eg, SMILES) and 2D (eg, ChemDraw) can be converted to 3D structures using Openbabel's
[`gen3D` option](https://open-babel.readthedocs.io/en/latest/3DStructureGen/SingleConformer.html#gen3d).
Gen3D performs a rapid geometry optimisation using a molecular force field. While this is normally useful
for generating a good starting geometry for further optimisations, it is rarely desirable for coordinates
that are already in three-dimensions.

The default behaviour in OpenPrattle (`gen3D = 'auto'`) is to convert geometries to three-dimensions so
long as the coordinates are not already in 3D. The function to determine the input geometry dimensions
is exposed by pybel, but not by the obabel command-line tool. This means that automatic conversion with
gen3D will only occur when using the Pybel backend, unless the input format is exclusively non-3D (such
as ChemDraw's cdx).

The 3D conversion can be explicitly requested or disabled by using `gen3D = True` or `gen3D = False`
respectively.

```
output = Openbabel_converter.from_file(input_file_path = "Benzene.cdx").convert("xyz", gen3D = True)
```

## Why?

On the surface, the pybel library and obabel tool appear to offer the same functionality. However, there are important instances where each offers functionality over the other. For example, pybel allows for the molecular charge and multiplicity to be set in some output formats, obabel does not.
Conversely, obabel can read from ChemDraw (.cdx) files, while pybel cannot.

In addition, the programmer may not know ahead of time whether pybel and/or obabel will be available on the target system.
OpenPrattle allows for this scenario.

## Name?

A light-hearted pun; 'prattle' and 'babel' are approximate synonyms.

## Licensing

[OpenBabel](https://github.com/openbabel/openbabel) is licensed under GPL 2.0. Because OpenPrattle depends on the pybel library, it too must be licensed under the GPL.
If this is not suitable for your needs, check out [FreePrattle](https://github.com/Digichem-Project/freeprattle) instead.