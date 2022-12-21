months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input(" Date: ")
    try:
        month, day, year = date.split("/")
        if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            break
    except:
        try:
            om, od, y = date.split(" ")
            for i in range(len(months)):
                if om == months[i]:
                    month = i + 1
            day = od.replace(",","")
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
        except:
            print()
            pass


print(f"{year}-{int(month):02}-{int(day):02}")