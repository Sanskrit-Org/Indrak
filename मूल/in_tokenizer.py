# Sanskrit-Org  [Github]
# This file is part of Sanskrit-Org > Indrak Project
# See License for more details.

bol_IndrakTokens = {
    "लघुअंश": "लघुअंश",
    "म१": "म१",
    "म२": "म२",
    "म३": "म३",
    "म४": "म४",
    "म५": "म५",
    "म६": "म६",
    "**": "**",
    "newLine": "\n",
    "।": "।"
}

bol_TokenValue = {
    "लघुअंश": "0x00",
    "म१": "0x11",
    "म२": "0x12",
    "म३": "0x13",
    "म४": "0x14",
    "म५": "0x15",
    "म६": "0x16",
    "**": "aa",
    "newLine": "\n"
}

bol_Errors = {
    "unknownToken": "-1"
}

bol_ErrorString = {
    "-1": "Unknown or Invalid Token"
}

def GetType(key):
    here = bol_IndrakTokens.get(key, "_I_")
    if here == "_I_":
        return "_U_"
    
    v = bol_TokenValue.get(here, "_I_")
    if v == "_I_":
        return "_U_"
    
    if v == "0x00":
        return "_INST_"
    
    return "_REG_"


class BolToken():
    def __init__(self, id, original, token, error):
        self.id = id    # Index of Token in bol_Tokens
        self.token = token
        if self.token != '_VAL_':
            self.value = bol_TokenValue.get(self.token, "__invalid_val__")
        else:
            self.value = original
        self.error = error
        self.original = original

    def Debug(self):
        print(self.original+' -')
        print("\tID: {0}, Value: {1}, Error: {2}".format(
            self.id, self.value, self.error))


class IndrakTokenizer():
    def __init__(self, debugMode=False):
        self.tokenArray = []
        self.strArray = []
        self.resultArray = []
        self.commentIsPrev = 0
        self.debug = debugMode
        self.comma = False
        self.prevId = 0     # for opcodes: _INST_, for regs: _REG_

    def MatchToken(self, i, str):
        tok = "(0)"
        if ',' in str:
            nstr = str
            str = str.replace(',', '')
            self.prevId =   GetType(str)
            self.comma = True
            if self.prevId == "_REG_":
                tok = bol_IndrakTokens.get(str, "(0)")
            else:
                tok = "(0)"
                print("Comma found at Unexpected place")
        else:
            if self.comma == False:
                tok = bol_IndrakTokens.get(str, "(0)")
            else:
                if self.prevId == "_REG_":
                    tok = "_VAL_"
                    self.prevId = "_VAL_"
                    self.comma = False
                else:
                    print("Unexpected token")
                    tok = "(0)"

        error = 0
        if tok == "(0)":
            error = bol_Errors["unknownToken"]
        return BolToken(i, str, tok, error)

    def log(self, text):
        if self.debug == True:
            print('> ', text)

    def Analyse(self, _str_array):
        i = 0
        for str in _str_array:
            tok = str.split('\n')

            self.log("tokens found: {0}".format(tok))

            if len(tok) > 1:
                for l in range(0, len(tok)):
                    if tok[l] == ' ' or tok[l] == '':
                        continue

                    if l > 0:
                        if self.commentIsPrev == 1:
                            self.log("comment ended.")
                            self.commentIsPrev = 0
                    if tok[l] == bol_IndrakTokens["**"]:
                        self.log("comment begined.")
                        self.commentIsPrev = 1

                    if self.commentIsPrev == 0:
                        self.strArray.append(tok[l])
                        i += 1
                    else:
                        self.log("skipped: "+tok[l])
            else:
                if tok[0] == ' ' or tok[0] == '':
                    continue
                if tok[0] == bol_IndrakTokens["**"]:
                    self.log("comment begined.")
                    self.commentIsPrev = 1
                if self.commentIsPrev == 0:
                    i += 1
                    self.strArray.append(tok[0])
                else:
                    self.log("skipped: "+tok[0])

    def Tokenise(self):
        i = 0
        for statement in self.strArray:
            self.tokenArray.append(self.MatchToken(i, statement))
            i += 1

    def Error(self, tok):
        print("error: "+bol_ErrorString.get(tok.error,
              "_bol_error")+", code:: "+tok.original)

    def GetResults(self):
        error_found = 0
        for out in self.tokenArray:
            if out.error != 0:
                error_found = 1
                self.Error(out)
                # break
            if error_found == 0:
                self.resultArray.append(out.value)

    def Debug(self):
        self.log(self.strArray)
        if self.debug == True:
            for tok in self.tokenArray:
                tok.Debug()
        print("Output -")
        print(self.resultArray)
