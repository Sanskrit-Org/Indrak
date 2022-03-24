# Code of this file belongs to Indrak.Bol

import visitor
import in_tokenizer

#
#   '__', '__\nNEXT_LINE_WORD', '_','_\nNEXT_LINE_WORD'
#

class IndrakParser():
    def __init__(self, fileReader):
        self.file = fileReader
        self.yet_started = False
        self.code = self.file.FileContents.split(' ')
        self.tokenizer = in_tokenizer.IndrakTokenizer()
    def action(self):
        self.tokenizer.Analyse(self.code)
        self.tokenizer.Tokenise()
        self.tokenizer.GetResults()
        self.tokenizer.Debug()