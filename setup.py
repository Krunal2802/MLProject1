from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def getRequirements(file_path:str)->(list[str]):
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(name='Student_performance-indicator',
      version='0.0.1',
      author='Krunal Shinde',
      author_email='krunals27920@gmail.com',
      packages=find_packages(),
      install_requires=getRequirements('requirements.txt')
      
)