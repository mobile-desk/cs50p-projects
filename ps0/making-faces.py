a = input("enter here: ")

def convert(a):
    if ":)" in a:
        b = a.replace(":)", "🙂")
    elif ":(" in a:
        b = a.replace(":(", "🙁")
    else:
        b = a 

    print(b)


convert(a)