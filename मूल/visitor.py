# Code of this file belongs to Indrak.Bol

class FileReader():
    def __init__(self, indrakSourceFile):
        self.FilePath = indrakSourceFile
        SourceFile = open(self.FilePath)
        self.FileContents = SourceFile.read()
        SourceFile.close()
    def print_contents(self):
        print(self.FileContents)