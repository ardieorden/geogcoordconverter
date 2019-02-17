import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geogcoordconverter",
    version="0.0.5",
    author="Ardie Orden",
    author_email="ardieorden@gmail.com",
    description="geogcoordconverter: Conversion tool for DMS, decimal degrees, and meters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ardieorden/geographic-coordinate-converter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)