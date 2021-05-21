import setuptools

# Generating distribution files
## Install things:          python -m pip install –-user –-upgrade setuptools wheel twine
## Generate the things:     python setup.py sdist bdist_wheel

# Install on local machine
## pip install -e .
## Check if we can import it

# Upload it
## To TestPiPy:             python -m twine upload — repository testpypi dist/*
## Uninstall the local:     pip uninstall tk-imgdecide
## Install from TestPiPy:   pip install -i https://test.pypi.org/tk-imgdecide/ tk-imgdecide==0.0.1

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name             = "tk-imgdecide",
    version          = "0.1.0",
    author           = "Koen du Buf",
    description      = "Quick prototypes for manual image editing",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires  = '>=3.6',
    py_modules       = [ "imgdecide" ],
    package_dir      = {'':'src'},
    install_requires = [ ]
)
