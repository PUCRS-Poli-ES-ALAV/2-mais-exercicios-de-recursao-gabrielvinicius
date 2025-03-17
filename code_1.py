def ex1(num):
    if num == 0:
        return 1
    return num * ex1(num - 1)


def ex2(num: int):
    if num == 0:
        return 1
    return num + ex2(num - 1)


def ex3(num: int):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return ex3(n-1) + ex3(n-2)


def ex4(k: int, j: int):
    if k > j:
        return 0
    return k + ex4(k + 1, j)


def ex5(text: str):
    if len(text) <= 1:
        return True
    elif text[0] != text[-1]:
        return False
    else:
        ex5(text[1:-1])
        return True


def ex6(num: int):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return ex6(num/2) + (n % 2)


def ex7(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + ex7(arr[1:])


def ex8(arr):
    if len(arr) == 1:
        return arr[0]
    maior = ex8(arr[1:])
    return arr[0] if arr[0] > maior else maior


def ex10(num):
    if num < 10:
        return 1
    return 1 + ex10(num // 10)
