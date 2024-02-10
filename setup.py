from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "CLI option chooser"
LONG_DESCRIPTION = "Lets user choose from a list of options through cli."

setup(
    name="get_choice",
    version=VERSION,
    author="Crebuo",
    author_email="curlusername@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=["python", "get_choice"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
