cinemaLists = {
    "A Nightmare On Elm Street": [12, 10],
    "Awakenings": [12, 10],
    "A League Of Their Own": [14, 10],
    "A Bronx Tale": [10, 10],
    "A Time To Kill": [14, 10],
    "Hotel Transylvania": [5, 10],
    "Corpse Bride": [5, 10],
    "The Land Before Time": [5, 10],
    "Jurassic Park": [10, 10],
    "Home Alone": [5, 10]
}
print(cinemaLists.keys())

while True:
    choice = input("What film would you like to watch? ").strip().title()
    if choice in cinemaLists:
        age = int(input("What's your age? ").strip())
        if age >= cinemaLists[choice][0]:
            seats = int(input("How many tickets would you lke to book: "))
            if seats <= cinemaLists[choice][1]:
                print("You may proceed.")
                cinemaLists[choice][1] -= seats
                print(cinemaLists[choice][1])
            else:
                print(f"sorry There are no tickets availible.Only {cinemaLists[choice][1]} seats are left.")
        else:
            print("You are a kid.")
    else:
        print("We don't have the film.")