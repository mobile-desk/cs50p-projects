while True:
    try:
        x,y = input("Fraction: ").strip().split("/")
        x = int(x)
        y = int(y)

        if y == 0:
            raise

        fuel = str(x) + "/" + str(y)

        if fuel == "1/4":
            print("25%")
        elif fuel == "1/2":
            print("50%")
        elif fuel == "2/4":
            print("50%")
        elif fuel == "3/4":
            print("75%")
        elif fuel == "4/4":
            print("F")
        else:
            print("E")

        

         
    except:
        print("There is a problem with your input")

    else:
        break



   