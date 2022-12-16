name = input("Enter Here: ")
v = ""

for i in name:
    if i in ["a", "e", "i", "o", "u"]:
        pass
    else:
        v = v + i
    
print(v)