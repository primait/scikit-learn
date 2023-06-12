"""Utility for testing presence and usability of .pxd files in the installation

Usage:
------
python check_pxd_in_installation.py path/to/install_dir/of/primakit-learn
"""

import os
import sys
import pathlib
import tempfile
import textwrap
import subprocess


pklearn_dir = pathlib.Path(sys.argv[1])
pxd_files = list(pklearn_dir.glob("**/*.pxd"))

print("> Found pxd files:")
for pxd_file in pxd_files:
    print(" -", pxd_file)

print("\n> Trying to compile a cython extension cimporting all corresponding modules\n")
with tempfile.TemporaryDirectory() as tmpdir:
    tmpdir = pathlib.Path(tmpdir)
    # A cython test file which cimports all modules corresponding to found
    # pxd files.
    # e.g. pklearn/tree/_utils.pxd becomes `cimport pklearn.tree._utils`
    with open(tmpdir / "tst.pyx", "w") as f:
        for pxd_file in pxd_files:
            to_import = str(pxd_file.relative_to(pklearn_dir))
            to_import = to_import.replace(os.path.sep, ".")
            to_import = to_import.replace(".pxd", "")
            f.write("cimport pklearn." + to_import + "\n")

    # A basic setup file to build the test file.
    # We set the language to c++ and we use numpy.get_include() because
    # some modules require it.
    with open(tmpdir / "setup_tst.py", "w") as f:
        f.write(
            textwrap.dedent(
                """
            from setuptools import setup, Extension
            from Cython.Build import cythonize
            import numpy

            extensions = [Extension("tst",
                                    sources=["tst.pyx"],
                                    language="c++",
                                    include_dirs=[numpy.get_include()])]

            setup(ext_modules=cythonize(extensions))
            """
            )
        )

    subprocess.run(
        ["python", "setup_tst.py", "build_ext", "-i"], check=True, cwd=tmpdir
    )

    print("\n> Compilation succeeded !")
