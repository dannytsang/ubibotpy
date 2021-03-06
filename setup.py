import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ubibotpy", # Replace with your own username
    version="0.0.1",
    author="Danny Tsang",
    author_email="danny@tsang.uk",
    description="Python implementation for Ubibot APIs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dannytsang/ubibotpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6'
)