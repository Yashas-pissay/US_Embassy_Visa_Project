import os # because i need a folder
from pathlib import Path # because i need to define a path
import logging

while True :
    project_name = input("Enter your project name: ")
    if project_name !='':
        break

# For example if i take house_price / components / logger / exception 
logging.info(f"Creating project by name: {project_name}")

list_of_files = [
    ".github/workflows/.gitkeep",
    ".github/workflows/main.yaml",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"config/config.yaml",
    "schema.yaml",
    "requirements.txt",
    "setup.py",
    "main.py",
    "README.md"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a new Directory at : {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f :
            pass
            logging.info(f"Creating a new file: {filename} for path {filepath}")

    else :
        logging.info(f"File is already present at: {filepath}") 