def number_generator(number):
    while True:
        for i in range(1, number + 1):
            yield i


def array_path(n: int, m: int) -> str:
    gen = number_generator(n)
    circular_array = []
    path = []
    while True:
        if len(circular_array) == 0:
            path = [next(gen) for _ in range(m)]
            circular_array.append(path)
        else:
            path = path + [next(gen) for _ in range(m-1)]
            circular_array.append(path)
        if path[-1] == 1:
            break
        path = [path[-1]]

    path = ''
    for i in circular_array:
        path += str(i[0])
    return path


while True:
    data = input('Введите длину массива "n" и длину обхода "m" через пробел\n'
                 'Для выхода введите "exit": ')
    if data == 'exit':
        break
    try:
        data = data.split(' ')
        n, m = map(lambda x: int(x), data)

        result = array_path(n, m)
        print("\nРезультат:", result)
        break
    except ValueError:
        print('\nНекорректно введены данные, попробуйте снова')