from gen_fib import fib_coroutine, my_genn


def test_fib_1():
    my_gen = fib_coroutine(my_genn)
    gen = my_gen()
    assert gen.send(3) == [0, 1, 1], "Тривиальный случай n = 3, список [0, 1, 1]"

    
def test_fib_2():
    my_gen = fib_coroutine(my_genn)
    gen = my_gen()
    assert gen.send(5) == [0, 1, 1, 2, 3], "Пять первых членов ряда"

def test_fib_3():
    my_gen = fib_coroutine(my_genn)
    gen = my_gen()
    assert gen.send(8) == [0, 1, 1, 2, 3, 5, 8, 13], "воесмь первых членов ряда"

def test_fib_4():
    my_gen = fib_coroutine(my_genn)
    gen = my_gen()
    assert gen.send(-83) == [], "Отрицательное количество первых членов ряда Фибоначчи"

def test_fib_4():
    my_gen = fib_coroutine(my_genn)
    gen = my_gen()
    assert gen.send("www") == [], "неверный тип данных количества чисел ряда"



