
import random



"""Функция с переменными. Для игры камень, ножницы, бумага"""
def f_battle():
    def f_choise( comp, my_choice = (input("""Встряхните руками и выберите: 
        камень, ножницы или бумага.
        Запишите  Ваше решение в строке(к-камень, н-ножницы, б-бумага) """))):

        battle = ("Я выбрала :", my_choice, "Компьютер : ", comp)
        print (battle)
        return my_choice, comp

    choice_list = ["к", "н", "б"]
    comp_choice = random.choice(choice_list)

    return f_choise(comp_choice)


"""Игра камень, ножницы, бумага"""
def f_knb_if():

    while True:
        print()
        choise_list = ["к", "н", "б"]
        comp_choice = random.choice(choise_list)

        my_choice = (input("""Встряхните руками и выберите: 
        камень, ножницы или бумага.
        Запишите  Ваше решение в строке(к-камень, н-ножницы, б-бумага) """))

        print(f"Результат: Вы ввели - {my_choice}, компьютер - {comp_choice}. ")


        def game(a, b):

            if a == b:
                print("Итог: Ничья!")

            if a == "к" and b == "н":
                print("Итог: Камень затупил ножницы. Вы проиграли(")

            if a == "к" and b == "б":
                print("Итог: Бумага накрыла камень. Вы выиграли)")

            if a == "н" and b == "к":
                print("Итог: Камень затупил ножницы. Вы выиграли)")

            if a == "н" and b == "б":
                print("Итог: Ножницы разрезали бумагу. Вы выиграли)")

            if a == "б" and b == "к":
                print("Итог: Бумага накрыла камень. Вы выиграли)")

            if a == "б" and b == "н":
                print("Итог: Ножницы разрезали бумагу. Вы выиграли)")

        print(game(comp_choice, my_choice))

"""Игра камень, ножницы, бумага. Вариант со словарём"""
def f_knb_dict():
    my_scores = 0
    comp_scores = 0

    round_list = ["Первый раунд", "Второй раунд", "Третий раунд"]

    for i in round_list:
        print()
        print(i)

        bat = f_battle()

        dict_knb = {("к", "н") : "Камень затупил ножницы",("к", "б") : "Камень накрылся бумагой",
                ("н", "к") : "Ножницы затупились об камень", ("н", "б") : "Ножницы разрезали бумагу",
                ("б", "к") : "Бумага накрыла камень", ("б", "н") : "Бумага разрезана ножницами",
            ("н", "н") : "Ничья", ("к", "к") : "Ничья", ("б", "б") : "Ничья" }


        print("Итог соревнования", bat)
        print(dict_knb[bat])

        if bat == ("к", "н") or bat == ("н", "б") or bat == ("б", "к"):
            comp_scores += 1

        elif  bat == ("к", "б") or bat == ("н", "к") or bat == ("б", "н"):
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



