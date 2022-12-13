def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    h = d.replace("$", "").strip()
    return float(h)


def percent_to_float(p):
    v = p.replace("%", "").strip()
    v = float(v)
    v /= 100
    return v


main()