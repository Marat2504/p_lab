import json
import re


# создание словаря с подставленными заничения value
def update_values(obj, value_to_set):
    if isinstance(obj, dict):
        for key in obj:
            if key == 'value':
                for i in value_to_set:
                    if i['id'] == obj['id']:
                        obj['value'] = i['value']
            else:
                update_values(obj[key], value_to_set)
    elif isinstance(obj, list):
        for item in obj:
            update_values(item, value_to_set)

    return obj


# декоратор, что бы записать результат в файл json
def decorator_func(func):
    def wrapper(*args, **kwargs):
        values, test, report = func(*args, **kwargs)
        result = update_values(test, values)
        with open(report_path, 'w', encoding='utf-8') as file:
            json.dump(obj=result, fp=file, ensure_ascii=False, indent=4)
    return wrapper


# основная функция
@decorator_func
def report_function(path_values, path_test, path_report):
    with open(test_path, 'r', encoding='utf-8') as f:
        test = json.load(f)
    with open(values_path, 'r', encoding='utf-8') as f:
        values = json.load(f)['values']

    return values, test, report_path


while True:
    data_user = input('Укажите через пробел пути к файлам "values.json", "tests.json" и "report.json"\n'
               'Пример ввода ".\\values.json .\\tests.json .\\report.json"\n'
                      'Для выхода введите "exit": ')
    if data_user == 'exit':
        break
    try:
        clean_data = re.sub(r'[\',\"]', '', data_user)
        values_path, test_path, report_path = clean_data.split()

        try:
            report_function(values_path, test_path, report_path)
            print(f'\nФайл успешно записан {report_path}')
            break
        except FileNotFoundError:
            print('\nФайлы не найдены, попробуйте снова.\n')
    except ValueError:
        print("\nОшибка при вводе путей к файлам, попробуйте снова\n")

















