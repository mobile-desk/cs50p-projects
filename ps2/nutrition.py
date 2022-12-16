fruits = {
    "apple" : 130,
    "avocado" : 50,
    "banana" : 110,
    "cantaloupe" : 50,
}

p = input("enter here: ").lower().strip()

if p in fruits.keys():
    print(f"Calories: {fruits[p]}")
else:
    pass