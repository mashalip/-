""""Надо ввести букву 'к', 'н' или 'б'"""

import random

my_scores = 0
comp_scores = 0

my_choice = ""
comp_choice = ""

raund = ["Первый раунд", "Второй раунд", "Третий раунд"]
for i in raund:
    print()
    print(i)

    list_choice = ["к", "н", "б"]
    comp_choice = random.choice(list_choice)

    my_choice = (input("""Встряхните руками и выберите: камень, ножницы или бумага.
Запишите  Ваше решение в строке(к-камень, н-ножницы, б-бумага) """))

    print(f"Результат: Вы ввели - {my_choice}, компьютер - {comp_choice}. ")

    if comp_choice == my_choice:
        print(f"Игрок - {my_scores} баллов, компьютер - {comp_scores} баллов")
        print("Итог: Победила дружба")

    elif comp_choice == "к" :
        if my_choice == "н":
            my_scores += 0
            comp_scores += 1
            print(f"Игрок - {my_scores} баллов, компьютер - {comp_scores}")
            print("Итог: Камень компьютера затупил Ваши ножницы. Один бал компьютеру")
        else:
            my_scores += 1
            comp_scores += 0
            print(f"Игрок - {my_scores} баллов, компьютер - {comp_scores}")
            print("Итог: Ваша бумага накрыла камень компьютера. Вы получили один балл")


    elif comp_choice == "н":
        if my_choice == "к":
            my_scores += 1
            comp_scores += 0
            print(f"Игрок - {my_scores} баллов, компьютер - {comp_scores}")
            print("Итог: Ваш камень затупил ножницы компьютера. Вы получили один балл")
        else:
            my_scores += 0
            comp_scores += 1
            print(f"Игрок - {my_scores} баллов, компьютер - {comp_scores}")
            print("Итог: Ножницы компьютера разрезали Вашу бумагу. Один бал компьютеру")


    elif comp_choice == "б":
        if my_choice == "к":
            my_scores += 0
            comp_scores += 1
            print(f"Игрок - {my_scores} баллов, компьютер - {comp_scores}")
            print("Итог: Бумага компьютера накрыла Ваш камень. Один балл компьютеру)")
        else:
            my_scores += 1
            comp_scores += 0
            print(f"Игрок - {my_scores} баллов, компьютер - {comp_scores}")
            print("Итог: Ножницы разрезали бумагу. Вы получили один балл")


print(f"Вы заработали {my_scores} очков, компьютер - {comp_scores} очков")

if comp_scores < my_scores:
    print("Ура! Победа!")

elif comp_scores < my_scores:
    print('К сожалению Вы проиграли')

else:
    print('Ничья')




