from even_numbers_iterator import FibonacchiLst


def test_fibList1():
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12]
    fb_list = FibonacchiLst(lst)

    res_lst = []
    for i in fb_list:
        res_lst.append(i)
    assert res_lst == [0, 1, 2, 3, 5]

def test_fibList2():
    lst = [1, 0, 22, 13, 14, -125]
    fb_list = FibonacchiLst(lst)

    res_lst = []
    for i in fb_list:
        res_lst.append(i)
    assert res_lst == [1, 0, 13]