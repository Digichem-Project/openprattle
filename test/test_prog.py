"""Test the oprattle program."""

import subprocess
from pathlib import Path

import pytest

from test import DATA


def run(signature):
    """Run a program."""

    return subprocess.run(
        signature,

    )

@pytest.mark.parametrize("input_file_type", ["cml", "xyz", "cdx"])
@pytest.mark.parametrize("backend", [None, "Pybel", "Obabel"])
def test_conversion(input_file_type, backend, tmp_path):
    """Test simple file conversion."""
    
    input_file_path = Path(DATA, "Benzene." + input_file_type)
    output_file_path = Path(tmp_path, "Benzene.xyz")

    signature = [
        "oprattle",
        "{}".format(input_file_path),
        "-O", "{}".format(output_file_path)
    ]

    if backend:
        signature.extend([
            "--backend",
            backend
        ])

    run(signature)