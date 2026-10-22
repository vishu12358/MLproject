from setuptools import find_packages, setup
from typing import List
def get_requirements(file_path: str) -> List[str]:
    """This function will return the list of requirements"""
    with open(file_path) as file_obj:
        requirement= file_obj.readlines()
        requirement = [req.replace("\n", "") for req in requirement]
        if "-e ." in requirement:
            requirement.remove("-e .")
    return requirement

setup(
    name="Mlproject",
    version="0.1.0",
    author="mr_rathore",
    packages=find_packages(),
    install_requires=get_requirements("requirement.txt"),
)
