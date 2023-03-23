'''we create setup.py because of 2 reasons 
1) if we realising any type of packages
2) we are using for the MLOPS part where version control coming to picture  
ex:  1.2.4 -> error then we change 1.2.5 '''

from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "Machine Learning project"
VERSION = "0.0.1"
AUTHOR = "Yashas PS"
DESCRIPTION = "This is our Machine learning project"

REQUIREMENT_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ." #for running the project again and again we need to remove -e . orelse it will give error


def get_requirements_list() -> List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list: 
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list



setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description=DESCRIPTION,
    packages= find_packages(),
    install_requires = get_requirements_list()
)