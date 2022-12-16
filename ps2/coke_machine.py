coke = 50
coin = [25, 10, 5]
total = 0

while True:
    print(f"amount due: {coke - total} ")
    money = int(input("insert coin: "))
    if money in coin:
        total += money
        if total >= coke:
            if total > coke:
                print(f"change owed: {total - coke}" )
                break
            else:
                print(f"change owed: {coke -total}" )
                break
        else:
            continue
    else:
        continue