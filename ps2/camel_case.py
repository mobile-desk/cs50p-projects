name = input("CamelCase: ")
v=""

for i in name:
    if i.isupper():
        g = "_" + i.lower()
        v = v+g  
    else:
        v = v + i

print(v)