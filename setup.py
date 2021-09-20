import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="whatthefuck",                     # This is the name of the package
    version="v1.1",                        
    author = 'Shubham Rath',                     # Full name of the author
    author_email = 'shubhamrath.iiitb@gmail.com',
    description = 'Frustration made me develop this script.',
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.5',                # Minimum version requirement of the package
    py_modules=["whatthefuck"],             # Name of the python package
    package_dir={'':'whatthefuck/src'},     # Directory of the source code of the package
    install_requires=[]                     # Install other dependencies if any
)