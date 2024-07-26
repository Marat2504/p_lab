import re


def determine_position(circle, dots):
    with open(circle, 'r', encoding='utf-8') as c:
        circle_data = [re.sub(r'\n', '', item) for item in c.readlines()]
        x_circle, y_circle = list(map(lambda x: int(x), circle_data[0].split(' ')))
        radius_circle = int(circle_data[1])

    with open(dots, 'r', encoding='utf-8') as d:
        dots_data = [re.sub('\n', '', item) for item in d.readlines()]
        dots_array = []
        for i in dots_data:
            x_dot, y_dot = list(map(lambda x: int(x), i.split(' ')))
            dots_array.append([x_dot, y_dot])

    position = []
    for i in dots_array:
        calculation = ((i[0] - x_circle) ** 2 + (i[1] - y_circle) ** 2)
        if calculation < radius_circle ** 2:
            position.append(1)
        elif calculation > radius_circle ** 2:
            position.append(2)
        else:
            position.append(0)
    print('Полученный результат: ')
    for i in position:
        print(i)


while True:
    data_user = input('Укажите через пробел пути к файлам "circle.txt" и "dot.txt"\n'
               'Пример ввода ".\circle.txt .\dot.txt"\n'
                      'Для выхода введите "exit": ')
    if data_user == 'exit':
        break
    try:
        clean_data = re.sub(r'[\',\"]', '', data_user)
        circle_path, dots_path = clean_data.split()

        try:
            determine_position(circle_path, dots_path)
            break
        except FileNotFoundError:
            print('\nФайлы не найдены, попробуйте снова.\n')
    except ValueError:
        print("\nОшибка при вводе путей к файлам, попробуйте снова\n")
