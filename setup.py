from setuptools import setup, find_packages

setup(
    name="utl",
    version="0.1.0",
    packages=find_packages(),
    install_requires=open('requirements.txt').read(),
    author="Lamp",
    author_email="ilovelampadaire@gmail.com",
    description="A collection of utilities.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lamps-dev/utl",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)