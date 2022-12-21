menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

order = []

sum = 0.00

while True:
    try:
        item = input("Item: ").strip().title()
        if item in menu.keys():
            h = menu[item]
            sum += h
            print(f"Total = ${sum:.2f}")
        #order = order.append(item)
    except EOFError:
        break


#for i in order:
#    if i in menu.keys():
#        h = menu[i]
#        sum += h