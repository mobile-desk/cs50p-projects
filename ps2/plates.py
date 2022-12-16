
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0].isalpha():
        if s[1].isalpha():
            if 1 < len(s) < 7:

                for x in s:
                    if x == "0":
                        ds = s.index(x)
                        #before x
                        ml = s[ds - 1]
                        jjj = s[:ds]
                        for al in jjj:
                            if al.isnumeric() and al != "0":
                                if x.isnumeric():
                                    xxx = s.index(x)
                                    m = s[xxx - 1]
                                    llll = s[m:]
                                    for q in llll:
                                        if q.isalpha():
                                            return False
                                    #if m.isnumeric():
                                    #    return True

                                else:
                                    #add any puctuation that is not present
                                    bb = [".",",","/","!","(",")","-","[","]","{","}",";",":","'",'"',"\\",""]
                                    for aa in s:
                                        if aa in bb:
                                            return False
                                        else:
                                            return True


                            else:
                                return False
            else:
                return False 
        else:
            return False
    else:
        return False

main()