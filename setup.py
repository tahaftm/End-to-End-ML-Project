from setuptools import find_packages,setup

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path):
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","" )for req in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="MLmodel",
    author="Taha",
    author_email="tahatariq@gmail.com",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
