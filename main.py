import requests  # импортируем библиотеку requests
from bs4 import BeautifulSoup  # импортируем библиотеку BeautifulSoup

def parse():
    proxies = {
        'http': 'http://proxy.omgtu:8080',
        'https': 'http://proxy.omgtu:8080'
    }
    url = 'https://omgtu.ru/ecab/persons/index.php?b=10' # передаем необходимы URL адрес
    page = requests.get(url, proxies=proxies, verify = False) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    page_parsed = BeautifulSoup(page.text, 'html.parser')  # обрабатываем page, передав в качестве аргументов html-код страницы и парсер, который будет использоваться для его обработки.
    employees = page_parsed.findAll('div', style="padding: 5px; font-size: 120%;")  # находим на странице все элементы div, у которых заданы стили padding: 5px и font-size: 120%, и сохраняем их
    with open('result.txt', 'w') as f:  # создаем файл в режиме записи
        for employee in employees:  # проходимся в цикле по всем элементам списка employees
            name = employee.find('a').text.strip()  # находим в каждом элементе div первый тег 'a', получаем текст из нее методом text, удаляем лишние пробелы в начале и конце строки методом strip и сохраняем имя в переменную name.
            f.write(name + '\n')  # записываем сотрудника в файл
parse()