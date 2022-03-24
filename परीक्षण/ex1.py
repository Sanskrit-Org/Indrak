def parse(astr):
    astr=astr.replace(',','')
    astr=astr.replace('and','')    
    tokens=astr.split()
    dept=None
    number=None
    result=[]
    option=[]
    for tok in tokens:
        if tok=='or':
            result.append(option)
            option=[]
            continue
        if tok.isalpha():
            dept=tok
            number=None
        else:
            number=int(tok)
        if dept and number:
            option.append((dept,number))
    else:
        if option:
            result.append(option)
    return result

if __name__=='__main__':
    tests=[ ("CS 2110" , [[("CS", 2110)]]),
            ("CS 2110 and INFO 3300" , [[("CS", 2110), ("INFO", 3300)]]),
            ("CS 2110, INFO 3300" , [[("CS", 2110), ("INFO", 3300)]]),
            ("CS 2110, 3300, 3140", [[("CS", 2110), ("CS", 3300), ("CS", 3140)]]),
            ("CS 2110 or INFO 3300", [[("CS", 2110)], [("INFO", 3300)]]),
            ("MATH 2210, 2230, 2310, or 2940", [[("MATH", 2210), ("MATH", 2230), ("MATH", 2310)], [("MATH", 2940)]])]

    for test,answer in tests:
        result=parse(test)
        if result==answer:
            print('GOOD: {0} => {1}'.format(test,answer))
        else:
            print('ERROR: {0} => {1} != {2}'.format(test,result,answer))
            break