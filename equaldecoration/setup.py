import setuptools


setuptools.setup(
    name="equaldecoration",
    version="0.0.1",
    author="Amir Jevnisek",
    author_email="mypythoncourseamir@gmail.com",
    description="A small example package",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'printing_types': [
            'equal = equaldecoration.equaldecoration:pretty_eqauls_printing',
        ],
    }
)
