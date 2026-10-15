def show_menu():
    print("\n1 - Идти налево")
    print("2 - Идти направо")
    print("выход - завершить игру")


def show_status(health, turns):
    print("\nТвоё здоровье:", health, "| Ход:", turns)


def apply_damage(health, damage):
    print("Ты получаешь урон", damage, "!")
    return health - damage


def heal(health, amount):
    print("Ты восстанавливаешь", amount, "здоровья.")
    return health + amount


health = 100
turns = 0
score = 0

print("Ты входишь в тёмное подземелье.")

while True:
    show_status(health, turns)
    show_menu()

    choice = input("Твой выбор: ").lower().strip()

    if choice == "выход":
        print("Ты решил покинуть подземелье.")
        break

    if choice == "1":
        print("Ты пошёл налево и нашёл сундук!")
        action = input("Открыть или пройти мимо? ").lower().strip()

        if action == "открыть":
            print("Там золото. Победа!")
            score = score + 1
        else:
            print("Ты ушёл ни с чем.")

    elif choice == "2":
        health = apply_damage(health, 30)
        print("На тебя напал дракон.")

        if health > 0:
            rest = input("Отдохнуть? да/нет ").lower().strip()
            if rest == "да":
                health = heal(health, 20)

    else:
        print("Я тебя не понял. Попробуй ещё раз.")
        continue

    turns = turns + 1

    if health <= 0:
        print("Твоё здоровье кончилось. Игра окончена.")
        break

print("\nИгра завершена. Настоящих ходов:", turns)
print("Твой счёт:", score)
