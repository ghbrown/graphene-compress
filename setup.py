

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='sheetsparse',  
    version='0.0.0',
    scripts=['bin/sheetsparse'] ,
    author="Gabriel H. Brown",
    author_email="gabriel.h.brown@gmail.com",
    description="Generate sparse representations of point data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ghbrown/sheetSparse",
    packages=setuptools.find_packages(),
    #include_package_data = True, #include non-Python files specified in MANIFEST.in
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
    ],
    keywords=[
        "scientific",
        "engineering",
        "sparse approximation",
        "spectral",
        "point cloud",
        "coordinates",
        "molecular dynamics",
        "atomistic",
    ],
    install_requires=[
        "numpy",
        "matplotlib",
        "ase",
    ],
 )
