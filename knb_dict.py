
"""Камень, ножницы, бумага - игра.
Модуль random. Цикл for. Счётчик. Словарь. Уcловие if, else, elif
"""

import random

my_scores = 0
comp_scores = 0

round_list = ["Первый раунд", "Второй раунд", "Третий раунд"]

for i in round_list:
    print()
    print(i)

    list_choice = ["к", "н", "б"]
    comp_choice = random.choice(list_choice)

    my_choice = (input("""Встряхните руками и выберите: камень, ножницы или бумага.
Запишите  Ваше решение в строке(к-камень, н-ножницы, б-бумага) """))

    dict_knb = {("к", "н") : "Камень затупил ножницы",("к", "б") : "Камень накрылся бумагой",
            ("н", "к") : "Ножницы затупились об камень", ("н", "б") : "Ножницы разрезали бумагу",
            ("б", "к") : "Бумага накрыла камень", ("б", "н") : "Бумага разрезана ножницами",
        ("н", "н") : "Ничья", ("к", "к") : "Ничья", ("б", "б") : "Ничья" }

    battle = (comp_choice, my_choice)
    print("Итог соревнования", battle)
    print(dict_knb[battle])

    if battle == ("к", "н") or battle == ("н", "б") or battle == ("б", "к"):
        comp_scores += 1

    elif  battle == ("к", "б") or battle == ("н", "к") or battle == ("б", "н"):
        my_scores += 1

    else:
        print("Ничья")

print(f"Компьютер - {comp_scores}, Игрок - {my_scores}")


if comp_scores < my_scores:
    print("Победа")
elif comp_scores == my_scores:
    print("Ничья")
else:
    print("Вы проиграли")