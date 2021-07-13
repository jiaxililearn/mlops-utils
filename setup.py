import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="mlops_utils",
    version="0.0.1",
    author="Jiaxi Li",
    author_email="jiaxili0319@gmail.com",
    description="A tool to practice MLOps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jiaxililearn/mlops-utils",
    packages=setuptools.find_packages(),
    package_data={
        '': ['*.json'],
        'files': ['*.json'],
    },
    entry_points = {
        'console_scripts': ['mlops-utils=mlops_utils.__main__:main']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
