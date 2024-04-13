import os.path

from setuptools import setup, find_packages

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path), 'r') as file:
        return file.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    name='mBot Controller',
    version=get_version("mbotcontroller/__init__.py"),
    packages=find_packages(),
    author="Daniel Boehm",
    license="GPLv3",
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "Topic :: Utilities"
    ],
    include_package_data=True,
    install_requires=[
        "click==8.1.7",
        "pyserial==3.5",
        "pydantic==2.7.0"
    ],
    extras_require={"dev": ["pytest==8.1.1", "pytest-cov==5.0.0"]},
    python_requires=">=3.12",
    entry_points={
        "console_scripts": [
            "mbc=mbotcontroller.mbc:cli"
        ]
    }
)