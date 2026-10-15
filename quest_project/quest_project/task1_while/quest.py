print("Ты входишь в тёмное подземелье.")

again = "да"

while again == "да":
    health = 100
    score = 0

    print("\nПеред тобой две двери: левая и правая.")

    choice = ""
    while choice != "налево" and choice != "направо":
        choice = input("Куда идти: налево или направо? ").lower()
        if choice != "налево" and choice != "направо":
            print("Я тебя не понял. Введи 'налево' или 'направо'.")

    if choice == "налево":
        print("Ты нашёл сундук!")
        action = input("Открыть или пройти мимо? ").lower()

        if action == "открыть":
            print("Там золото. Победа!")
            score = score + 1
        else:
            print("Ты ушёл ни с чем.")

    elif choice == "направо":
        print("На тебя напал дракон. Минус 30 здоровья.")
        health = health - 30

    print("Твоё здоровье:", health)
    print("Твой счёт:", score)

    again = input("\nИграть ещё раз? да/нет ").lower()

print("Спасибо за игру!")
