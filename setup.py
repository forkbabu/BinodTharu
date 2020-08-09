import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="binod", 
    version="0.0.1",
    author="Sayantan Das",
    author_email="sayantandas30011998@gmail.com",
    description="Say Binod and nothing else",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://https://github.com/forkbabu/Binod",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords='api python meme',
    install_requires=[
      'numpy'
    ],    
)
