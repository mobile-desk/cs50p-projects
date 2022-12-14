m = input("Greeting: ").lower().strip()

if m.startswith("h"):
    if m.startswith("hello"):
        print("$0")
    else:
        print("$20")
else:
    print("$100")