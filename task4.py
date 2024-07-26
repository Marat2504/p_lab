import re


def min_steps(file: str) -> int:
    with open(file, 'r', encoding='utf-8') as f:
        content = list(f.readlines())
        numbers = [int(re.sub(r'\n', '', item)) for item in content]
        average = round(sum(numbers)/len(numbers))
        count = 0
        for i in numbers:
            count += abs(average - i)
        return count


while True:
    data_user = input('Укажите путь к файлу "numbers.txt"\n'
               'Пример ввода ".\\numbers.txt"\n'
                      'Для выхода введите "exit": ')
    if data_user == 'exit':
        break
    try:
        clean_data = re.sub(r'[\',\"]', '', data_user)
        try:
            result = min_steps(clean_data)
            print('\nПолученный результат:', result)
            break
        except FileNotFoundError:
            print('\nФайл не найден, попробуйте снова.\n')
    except Exception:
        print("\nОшибка при вводе пути к файлу, попробуйте снова\n")