from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("requirements-dev.txt") as f:
    dev_requirements = f.read().splitlines()

setup(
    name="geogcoordconverter",
    version="0.0.5",
    author="Ardie Orden",
    author_email="ardieorden@gmail.com",
    description="geogcoordconverter: Conversion tool for DMS, "
                "decimal degrees, and meters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ardieorden/geographic-coordinate-converter",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    tests_require=dev_requirements,
    extras_require={'test': dev_requirements}
)
