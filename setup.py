from __future__ import print_function

import fnmatch
import hashlib
import os
import shutil
import sys
import subprocess
import traceback
import tempfile
import zipfile
import distutils.sysconfig as dsc

from glob import glob
from setuptools import find_packages
from distutils.core import setup
from setuptools.command.install import install
from setuptools.command.egg_info import egg_info
from setuptools import setup, Distribution
from multiprocessing import Process


try:
    import pip._internal.pep425tags as pep425tags

    pep425tags.get_supported()
    raise Exception()
except Exception as e:
    import pep425tags

try:
    from urllib.request import urlretrieve
except BaseException:
    from urllib import urlretrieve


PACKAGE_NAME = "pymagnitude"
PACKAGE_SHORT_NAME = "magnitude"

# Setup path constants
PROJ_PATH = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
# THIRD_PARTY = PROJ_PATH + "/" + PACKAGE_NAME + "/third_party"
# BUILD_THIRD_PARTY = PROJ_PATH + "/build/lib/" + PACKAGE_NAME + "/third_party"
# INTERNAL = THIRD_PARTY + "/internal"

# Get the package version
__version__ = None
with open(os.path.join(PROJ_PATH, "version.py")) as f:
    exec(f.read())


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


def install_requirements():
    """Installs requirements.txt"""
    print("Installing requirements...")
    rc = subprocess.Popen(
        [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
        cwd=PROJ_PATH,
    ).wait()
    if rc:
        print("Failed to install some requirements!")
    print("Done installing requirements")


class BinaryDistribution(Distribution):
    def has_ext_modules(foo):
        return True


if __name__ == "__main__":

    setup(
        name=PACKAGE_NAME,
        packages=find_packages(exclude=["tests", "tests.*"]),
        version=__version__,
        description="A fast, efficient universal vector embedding utility package.",
        long_description="""
    About
    -----
    A feature-packed Python package and vector storage file format for utilizing vector embeddings in machine learning models in a fast, efficient, and simple manner developed by `Plasticity <https://www.plasticity.ai/>`_. It is primarily intended to be a faster alternative to `Gensim <https://radimrehurek.com/gensim/>`_, but can be used as a generic key-vector store for domains outside NLP.

    Documentation
    -------------
    You can see the full documentation and README at the `GitLab repository <https://gitlab.com/Plasticity/magnitude>`_ or the `GitHub repository <https://github.com/plasticityai/magnitude>`_.
        """,
        author="Plasticity",
        author_email="opensource@plasticity.ai",
        url="https://gitlab.com/Plasticity/magnitude",
        keywords=[
            "pymagnitude",
            "magnitude",
            "plasticity",
            "nlp",
            "natural",
            "language",
            "processing",
            "word",
            "vector",
            "embeddings",
            "embedding",
            "word2vec",
            "gensim",
            "alternative",
            "machine",
            "learning",
            "annoy",
            "index",
            "approximate",
            "nearest",
            "neighbors",
        ],
        license="MIT",
        include_package_data=True,
        # install_requires=reqs,
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Topic :: Text Processing :: Linguistic",
            "Operating System :: OS Independent",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
        # cmdclass=cmdclass,
        distclass=BinaryDistribution,
    )
