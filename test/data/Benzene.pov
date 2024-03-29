//Povray v3 code generated by Open Babel
//Author: Steffen Reith <streit@streit.cc>
//Update (2010): Noel O'Boyle and Steven Wathen
//Date: Fri Feb 23 10:57:26 GMT 2024

//Set some global parameters for display options
#declare BAS = true;
#declare TRANS = false;

#include "colors.inc"

// create a regular point light source
light_source {
  <1.03562,5.43679,-9.15017>
  color rgb <1,1,1>    // light's color
}

// set a color of the background (sky)
background { color rgb <0.95 0.95 0.95> }

// perspective (default) camera
camera {
  location  <-0.964378,2.43679,-11.1502>
  look_at   <-0.964378,2.43679,-1.15017>
  right     x*image_width/image_height
}

//Include header for povray
#include "babel_povray3.inc"

//Use PovRay3.6
#version 3.6;

//Print name of molecule while rendering
#render "\b\b \n\n"

//Coodinates of atoms 1 - 12
#declare mol_0_pos_1 = <-1.73906,3.58846,-1.30468>;
#declare mol_0_pos_2 = <-0.741776,3.28843,-2.23496>;
#declare mol_0_pos_3 = <-1.96277,2.73749,-0.219172>;
#declare mol_0_pos_4 = <-1.18754,1.58343,-0.063056>;
#declare mol_0_pos_5 = <0.035097,2.13524,-2.08167>;
#declare mol_0_pos_6 = <-0.187159,1.28164,-0.995432>;
#declare mol_0_pos_7 = <-2.33756,4.48085,-1.42656>;
#declare mol_0_pos_8 = <-2.73647,2.97415,0.498829>;
#declare mol_0_pos_9 = <-0.574431,3.95177,-3.07253>;
#declare mol_0_pos_10 = <0.807562,1.90409,-2.80343>;
#declare mol_0_pos_11 = <0.415352,0.389307,-0.878497>;
#declare mol_0_pos_12 = <-1.3638,0.926616,0.779158>;

//Povray-description of atoms 1 - 12
#declare mol_0_atom1 = object {
	  Atom_C
	  translate mol_0_pos_1
	 }
#declare mol_0_atom2 = object {
	  Atom_C
	  translate mol_0_pos_2
	 }
#declare mol_0_atom3 = object {
	  Atom_C
	  translate mol_0_pos_3
	 }
#declare mol_0_atom4 = object {
	  Atom_C
	  translate mol_0_pos_4
	 }
#declare mol_0_atom5 = object {
	  Atom_C
	  translate mol_0_pos_5
	 }
#declare mol_0_atom6 = object {
	  Atom_C
	  translate mol_0_pos_6
	 }
#declare mol_0_atom7 = object {
	  Atom_H
	  translate mol_0_pos_7
	 }
#declare mol_0_atom8 = object {
	  Atom_H
	  translate mol_0_pos_8
	 }
#declare mol_0_atom9 = object {
	  Atom_H
	  translate mol_0_pos_9
	 }
#declare mol_0_atom10 = object {
	  Atom_H
	  translate mol_0_pos_10
	 }
#declare mol_0_atom11 = object {
	  Atom_H
	  translate mol_0_pos_11
	 }
#declare mol_0_atom12 = object {
	  Atom_H
	  translate mol_0_pos_12
	 }

//Povray-description of bonds 1 - 12
#if (BAS)
#declare mol_0_bond0 = object {
	  bond_1
	  scale <1.39643,1.0000,1.0000>
	  rotate <0.0000,0.0000,-12.4071>
	  rotate <0.0000,43.0092,0.0000>
	  translate mol_0_pos_1
	 }
#declare mol_0_bond1 = object {
	  bond_2
	  scale <1.39733,1.0000,1.0000>
	  rotate <0.0000,0.0000,-37.5173>
	  rotate <0.0000,-101.645,0.0000>
	  translate mol_0_pos_1
	 }
#declare mol_0_bond2 = object {
	  bond_1
	  scale <1.399,1.0000,1.0000>
	  rotate <0.0000,0.0000,-55.5799>
	  rotate <0.0000,-11.3859,0.0000>
	  translate mol_0_pos_3
	 }
#declare mol_0_bond3 = object {
	  bond_2
	  scale <1.39888,1.0000,1.0000>
	  rotate <0.0000,0.0000,-55.5241>
	  rotate <0.0000,-11.1615,0.0000>
	  translate mol_0_pos_2
	 }
#declare mol_0_bond4 = object {
	  bond_1
	  scale <1.39927,1.0000,1.0000>
	  rotate <0.0000,0.0000,-37.592>
	  rotate <0.0000,-101.564,0.0000>
	  translate mol_0_pos_5
	 }
#declare mol_0_bond5 = object {
	  bond_2
	  scale <1.40041,1.0000,1.0000>
	  rotate <0.0000,0.0000,12.4449>
	  rotate <0.0000,-137.015,0.0000>
	  translate mol_0_pos_6
	 }
#declare mol_0_bond6 = object {
	  bond_1
	  scale <1.0814,1.0000,1.0000>
	  rotate <0.0000,0.0000,55.6107>
	  rotate <0.0000,168.49,0.0000>
	  translate mol_0_pos_1
	 }
#declare mol_0_bond7 = object {
	  bond_1
	  scale <1.08173,1.0000,1.0000>
	  rotate <0.0000,0.0000,12.6373>
	  rotate <0.0000,-137.138,0.0000>
	  translate mol_0_pos_3
	 }
#declare mol_0_bond8 = object {
	  bond_1
	  scale <1.08145,1.0000,1.0000>
	  rotate <0.0000,0.0000,37.834>
	  rotate <0.0000,78.7012,0.0000>
	  translate mol_0_pos_2
	 }
#declare mol_0_bond9 = object {
	  bond_1
	  scale <1.08216,1.0000,1.0000>
	  rotate <0.0000,0.0000,-12.3335>
	  rotate <0.0000,43.0564,0.0000>
	  translate mol_0_pos_5
	 }
#declare mol_0_bond10 = object {
	  bond_1
	  scale <1.08303,1.0000,1.0000>
	  rotate <0.0000,0.0000,-55.4794>
	  rotate <0.0000,-10.9834,0.0000>
	  translate mol_0_pos_6
	 }
#declare mol_0_bond11 = object {
	  bond_1
	  scale <1.08249,1.0000,1.0000>
	  rotate <0.0000,0.0000,-37.3554>
	  rotate <0.0000,-101.82,0.0000>
	  translate mol_0_pos_4
	 }
#end //(BAS-Bonds)

#if (CST)
#declare mol_0_bond0 = object {
	  union {
	   object {
	    bond_1
	    pigment{color Color_Car}
	    scale <0.698213,1.0000,1.0000>
	    rotate <0.0000,0.0000,-12.4071>
	    rotate <0.0000,43.0092,0.0000>
	    translate mol_0_pos_1
	   }
	   object {
	    bond_1
	    pigment{color Color_Car}
	    scale <0.698213,1.0000,1.0000>
	    rotate <0.0000,0.0000,167.593>
	    rotate <0.0000,43.0092,0.0000>
	    translate mol_0_pos_2
	   }
	  }
	 }

#declare mol_0_bond1 = object {
	  union {
	   object {
	    bond_2
	    pigment{color Color_Car}
	    scale <0.698664,1.0000,1.0000>
	    rotate <0.0000,0.0000,-37.5173>
	    rotate <0.0000,-101.645,0.0000>
	    translate mol_0_pos_1
	   }
	   object {
	    bond_2
	    pigment{color Color_Car}
	    scale <0.698664,1.0000,1.0000>
	    rotate <0.0000,0.0000,142.483>
	    rotate <0.0000,-101.645,0.0000>
	    translate mol_0_pos_3
	   }
	  }
	 }

#declare mol_0_bond2 = object {
	  union {
	   object {
	    bond_1
	    pigment{color Color_Car}
	    scale <0.699502,1.0000,1.0000>
	    rotate <0.0000,0.0000,-55.5799>
	    rotate <0.0000,-11.3859,0.0000>
	    translate mol_0_pos_3
	   }
	   object {
	    bond_1
	    pigment{color Color_Car}
	    scale <0.699502,1.0000,1.0000>
	    rotate <0.0000,0.0000,124.42>
	    rotate <0.0000,-11.3859,0.0000>
	    translate mol_0_pos_4
	   }
	  }
	 }

#declare mol_0_bond3 = object {
	  union {
	   object {
	    bond_2
	    pigment{color Color_Car}
	    scale <0.699441,1.0000,1.0000>
	    rotate <0.0000,0.0000,-55.5241>
	    rotate <0.0000,-11.1615,0.0000>
	    translate mol_0_pos_2
	   }
	   object {
	    bond_2
	    pigment{color Color_Car}
	    scale <0.699441,1.0000,1.0000>
	    rotate <0.0000,0.0000,124.476>
	    rotate <0.0000,-11.1615,0.0000>
	    translate mol_0_pos_5
	   }
	  }
	 }

#declare mol_0_bond4 = object {
	  union {
	   object {
	    bond_1
	    pigment{color Color_Car}
	    scale <0.699635,1.0000,1.0000>
	    rotate <0.0000,0.0000,-37.592>
	    rotate <0.0000,-101.564,0.0000>
	    translate mol_0_pos_5
	   }
	   object {
	    bond_1
	    pigment{color Color_Car}
	    scale <0.699635,1.0000,1.0000>
	    rotate <0.0000,0.0000,142.408>
	    rotate <0.0000,-101.564,0.0000>
	    translate mol_0_pos_6
	   }
	  }
	 }

#declare mol_0_bond5 = object {
	  union {
	   object {
	    bond_2
	    pigment{color Color_Car}
	    scale <0.700206,1.0000,1.0000>
	    rotate <0.0000,0.0000,12.4449>
	    rotate <0.0000,-137.015,0.0000>
	    translate mol_0_pos_6
	   }
	   object {
	    bond_2
	    pigment{color Color_Car}
	    scale <0.700206,1.0000,1.0000>
	    rotate <0.0000,0.0000,192.445>
	    rotate <0.0000,-137.015,0.0000>
	    translate mol_0_pos_4
	   }
	  }
	 }

#declare mol_0_bond6 = object {
	  union {
	   object {
	    bond_1
	    pigment{color Color_Car}
	    scale <0.540698,1.0000,1.0000>
	    rotate <0.0000,0.0000,55.6107>
	    rotate <0.0000,168.49,0.0000>
	    translate mol_0_pos_1
	   }
	   object {
	    bond_1
	    pigment{color Color_H}
	    scale <0.540698,1.0000,1.0000>
	    rotate <0.0000,0.0000,235.611>
	    rotate <0.0000,168.49,0.0000>
	    translate mol_0_pos_7
	   }
	  }
	 }

#declare mol_0_bond7 = object {
	  union {
	   object {
	    bond_1
	    pigment{color Color_Car}
	    scale <0.540866,1.0000,1.0000>
	    rotate <0.0000,0.0000,12.6373>
	    rotate <0.0000,-137.138,0.0000>
	    translate mol_0_pos_3
	   }
	   object {
	    bond_1
	    pigment{color Color_H}
	    scale <0.540866,1.0000,1.0000>
	    rotate <0.0000,0.0000,192.637>
	    rotate <0.0000,-137.138,0.0000>
	    translate mol_0_pos_8
	   }
	  }
	 }

#declare mol_0_bond8 = object {
	  union {
	   object {
	    bond_1
	    pigment{color Color_Car}
	    scale <0.540727,1.0000,1.0000>
	    rotate <0.0000,0.0000,37.834>
	    rotate <0.0000,78.7012,0.0000>
	    translate mol_0_pos_2
	   }
	   object {
	    bond_1
	    pigment{color Color_H}
	    scale <0.540727,1.0000,1.0000>
	    rotate <0.0000,0.0000,217.834>
	    rotate <0.0000,78.7012,0.0000>
	    translate mol_0_pos_9
	   }
	  }
	 }

#declare mol_0_bond9 = object {
	  union {
	   object {
	    bond_1
	    pigment{color Color_Car}
	    scale <0.541079,1.0000,1.0000>
	    rotate <0.0000,0.0000,-12.3335>
	    rotate <0.0000,43.0564,0.0000>
	    translate mol_0_pos_5
	   }
	   object {
	    bond_1
	    pigment{color Color_H}
	    scale <0.541079,1.0000,1.0000>
	    rotate <0.0000,0.0000,167.667>
	    rotate <0.0000,43.0564,0.0000>
	    translate mol_0_pos_10
	   }
	  }
	 }

#declare mol_0_bond10 = object {
	  union {
	   object {
	    bond_1
	    pigment{color Color_Car}
	    scale <0.541513,1.0000,1.0000>
	    rotate <0.0000,0.0000,-55.4794>
	    rotate <0.0000,-10.9834,0.0000>
	    translate mol_0_pos_6
	   }
	   object {
	    bond_1
	    pigment{color Color_H}
	    scale <0.541513,1.0000,1.0000>
	    rotate <0.0000,0.0000,124.521>
	    rotate <0.0000,-10.9834,0.0000>
	    translate mol_0_pos_11
	   }
	  }
	 }

#declare mol_0_bond11 = object {
	  union {
	   object {
	    bond_1
	    pigment{color Color_Car}
	    scale <0.541247,1.0000,1.0000>
	    rotate <0.0000,0.0000,-37.3554>
	    rotate <0.0000,-101.82,0.0000>
	    translate mol_0_pos_4
	   }
	   object {
	    bond_1
	    pigment{color Color_H}
	    scale <0.541247,1.0000,1.0000>
	    rotate <0.0000,0.0000,142.645>
	    rotate <0.0000,-101.82,0.0000>
	    translate mol_0_pos_12
	   }
	  }
	 }

#end // (CST-Bonds)


//All atoms of molecule mol_0
#ifdef (TRANS)
#declare mol_0_atoms = merge {
#else
#declare mol_0_atoms = union {
#end //(End of TRANS)
	  object{mol_0_atom1}
	  object{mol_0_atom2}
	  object{mol_0_atom3}
	  object{mol_0_atom4}
	  object{mol_0_atom5}
	  object{mol_0_atom6}
	  object{mol_0_atom7}
	  object{mol_0_atom8}
	  object{mol_0_atom9}
	  object{mol_0_atom10}
	  object{mol_0_atom11}
	  object{mol_0_atom12}
	 }

//Bonds only needed for ball and sticks or capped sticks models
#if (BAS | CST)
#declare mol_0_bonds = union {
	  object{mol_0_bond0}
	  object{mol_0_bond1}
	  object{mol_0_bond2}
	  object{mol_0_bond3}
	  object{mol_0_bond4}
	  object{mol_0_bond5}
	  object{mol_0_bond6}
	  object{mol_0_bond7}
	  object{mol_0_bond8}
	  object{mol_0_bond9}
	  object{mol_0_bond10}
	  object{mol_0_bond11}
	 }
#end


//Definition of molecule mol_0
#if (SPF)
#declare mol_0 = object{
	  mol_0_atoms
#else
#declare mol_0 = union {
	  object{mol_0_atoms}
#if (BAS | CST)//(Not really needed at moment!)
#if (TRANS)
	  difference {
	   object{mol_0_bonds}
	   object{mol_0_atoms}
	  }
#else
	  object{mol_0_bonds}
#end //(End of TRANS)
#end //(End of (BAS|CST))
#end //(End of SPF)
//	  bounded_by {
//	   box {
//	    <-5.73647,-3,-6.07253>
//	    <3.80756,7.48085,3.77916>
	 }

//Center of molecule mol_0 (bounding box)
#declare mol_0_center = <0.964452,-2.24042,1.14668>;

mol_0
