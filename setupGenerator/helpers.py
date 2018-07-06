import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--projectname", required = True
                    , help = "Name of project")
parser.add_argument("-l", "--licens"
                    , required = True,  help = "Type of licens for your project")

class structureGenerator(object):


    def __init__(self, flags):
        self.flags = flags


    def generateFolders(self):
        """Generates the folders needed in the structure"""
        dirs = ["docs", "tests", self.flags.projectname]
        for i in dirs:
            os.makedirs("./{}".format(i))


    def generateFiles(self) :
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
                self.flags.projectname : files_project,
                "tests" : files_test
                }

        base_dir = os.getcwd()

        for k,v in files_dict.items():
            if not os.getcwd() is base_dir:
                os.chdir(base_dir)
            if k is not "base":
                os.chdir("{}/{}".format(base_dir,k))
            cur_dir = os.getcwd()
            for j in v:
                open("{}{}{}".format(cur_dir, "/", j), 'w+')

    def run(self):
        self.generateFolders()
        self.generateFiles()


def main():
    args = parser.parse_args()
    cmd = structureGenerator(args)
    cmd.run()

if __name__ == "__main__":
    main()
