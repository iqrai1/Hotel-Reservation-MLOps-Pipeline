from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-project-1",
    version="0.1",
    author="Iqra",
    packages=find_packages(),
    install_requires = requirements,
)