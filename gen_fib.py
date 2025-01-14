import functools

def fib_elem_gen():
    """Генератор, возвращающий элементы ряда Фибоначчи"""
    a = 0
    b = 1

    while True:
        yield a
        res = a + b
        a = b
        b = res



def my_genn():
    """Корутина для генерации последовательности Фибоначчи"""
    while True:
        num_elements = yield
        fib_sequence = []
        if isinstance(num_elements, int) and num_elements > 0:
            fib_gen = fib_elem_gen()  
            for _ in range(num_elements):
                fib_sequence.append(next(fib_gen))

        yield fib_sequence

def fib_coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        gen.send(None)
        return gen
    return inner
