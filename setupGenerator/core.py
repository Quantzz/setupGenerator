import os
import subprocess
import argparse
import requests


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--projectname", required = True
                    , help = "Name of project")
parser.add_argument("-l", "--licens"
                    , required = True,  help = "Type of licens for your project")
parser.add_argument("-y", "--year"
                    , required = True,  help = "Year of copyright for LICENSE")
parser.add_argument("-o", "--author"
                    , required = True,  help = "Author of library for LICENSE")

class structureGenerator(object):
    """WILL WRITE COMMENTS LATER...MAYBE"""

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
                "LICENSE.txt",
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
                if j is "LICENSE.txt":
                    with open("{}{}{}".format(cur_dir, "/", j), 'wb') as f:
                        licens = subprocess.check_output(
                                'lice {} -y={} -o=\"{}\"'.format(self.flags.licens,
                                                             int(self.flags.year),
                                                             str(self.flags.author)),
                                                             shell=True
                                                            )
                        f.write(licens)
                else:
                    with open("{}{}{}".format(cur_dir, "/", j), 'w+') as f:
                        if j is "setup.py":
                            r = requests.get('https://raw.githubusercontent.com/kennethreitz/setup.py/master/setup.py')
                            f.write(r.text)


    def run(self):
        self.generateFolders()
        self.generateFiles()


def main():
    args = parser.parse_args()
    cmd = structureGenerator(args)
    cmd.run()

if __name__ == "__main__":
    main()
