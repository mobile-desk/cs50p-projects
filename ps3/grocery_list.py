list = []

dict = {}

while True:
    try:
        item = input("Enter here: ").strip().upper()
        list.append(item)
    except EOFError:
        break

list.sort()
for i in list:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

for key in dict:
    print(f"{dict[key]} {key}")