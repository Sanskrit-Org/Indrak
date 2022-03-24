qtests = """लघुअंश unexcepted or unexcepted म१: 0
लघुअंश म२: 1"""

# Grammer Dictionary
gr = {
    "लघुअंश": "लघुअंश",
    "म१": "म१",
    "म२": "म२"
}

regs = {
    "म१": "०११",
    "म२": "०१२"
}

tra = {
    "लघुअंश": "००"
}

seps = {
    "शुरू": "शुरू",
    "समाप्त": "समाप्त"
}

def Parser(astr):
    astr = astr.replace(':','')
    next_name = 0
    next_val = 0
    prev_name = 0
    tokens = astr.split()
    result = []
    resultl = 0
    for tok in tokens:
        resultl+=1
        if tok == gr["लघुअंश"]:
            next_name = 1
            result.append(seps["शुरू"])
            result.append(tra["लघुअंश"])
            continue
        if tok == gr["म१"]:
            next_name = 0
            prev_name = 1
            result.append(regs["म१"])
            continue
        if tok == gr["म२"]:
            next_name = 0
            prev_name = 1
            result.append(regs["म२"])
            continue
        else:
            # if next_name == 1:
            #     print("It is Runtime Name: {0}".format(tok))
            if prev_name == 1:
                prev_name = 0
                result.append(int(tok))
                result.append(seps["समाप्त"])
            else:
                print("Unexpected token: '{0}' at col: {1}".format(tok, resultl))

    print("Result: {0}".format(result))

Parser(qtests)