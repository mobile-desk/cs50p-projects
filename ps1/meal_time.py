b = input("What time is it? ")
def main():
    if 7 <= convert(b) <= 8:
        return "breakfast time"
    elif 12 <= convert(b) <= 13:
        print("lunch time")
    elif 18 <= convert(b) <= 19:
        print("dinner time")
    else:
        pass


def convert(time):
    j = 0
    h = time.split(":")
    for i in h:
        j += float(i)
    j /= 60
    return float(j)


if __name__ == "__main__":
    main()
