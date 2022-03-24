# Sanskrit-Org  [Github]
# This file is part of Sanskrit-Org > Indrak Project
# See License for more details.

class FileReader():
    def __init__(self, indrakSourceFile):
        self.FilePath = indrakSourceFile
        SourceFile = open(self.FilePath)
        self.FileContents = SourceFile.read()
        SourceFile.close()

    def print_contents(self):
        print(self.FileContents)
