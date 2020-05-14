from setuptools import find_packages
from setuptools import setup, find_packages


PACKAGE_NAME = "pymagnitude"
PACKAGE_SHORT_NAME = "magnitude"


def _requires_from_file(filename):
    return open(filename).read().splitlines()


if __name__ == "__main__":
    setup(
        name="pymagnitude",
        packages=find_packages(exclude=["tests", "tests.*"]),
        version="0.1.21.dev",
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
        install_requires=_requires_from_file("requirements.txt"),
        zip_safe=False,
    )
