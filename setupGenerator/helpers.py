import os
import argparse

def generateFolders(project_name):
    """Generates the folders needed in the structure"""
    dirs = ["docs", "tests", project_name]
    for i in dirs:
        os.makedirs("./{}".format(i))

    return

def generateFiles(project_name, licens, index):
    """Generates standard files for a python project in recommended locations"""   
    files_base = [
            "README.md",
            "LICENS",
            "setup.py",
            "requirements.txt"
            ]

    files_docs = [
            "conf.py",
            "index.md"
            ]

    files_project = [
            "__init__.py",
            "main.py",
            "helpers.py"
            ]

    files_test = [
            "test_basic.py",
            "test_advanced.py"
            ]

    files_dict = {
            "base" : files_base,
            "docs" : files_docs,
            project_name : files_project,
            "tests" : files_test
            }

    for k,v in files_dict.items():
        if k is not "base":
            os.chdir("./{}".format(k))
        cur_dir = os.getcwd()
        for j in v:
            open("{}{}{}".format(cur_dir, "/", j), 'w+') 
                

        return

if __name__ == "__main__":
    generateFolders("structureSetup")
    generateFiles("structureSetup", 1, 2)
