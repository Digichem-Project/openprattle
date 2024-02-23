# OpenPrattle

A command-line tool and python library that provides a seamless interface to both the [Pybel library](https://github.com/openbabel/openbabel) and [obabel](https://github.com/openbabel/openbabel) command-line tool.

## Dependencies

# Required

Openbabel >= 3.0.0
Python >= 3.9

# Optional

JSON

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