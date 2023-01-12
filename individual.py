#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
import click
from datetime import date


@click.command()
def main():
    print("I'm a beautiful CLI ✨")
def get_worker():
    """
    Запросить данные о товаре.
    """
    name = input("Название товара? ")
    nameShop = input("Магазин? ")
    cost = int(input("Цена? "))
    # Создать словарь.
    return {
    'name': name,
    'nameShop': nameShop,
    'cost': cost,
    }

def display_workers(staff):
    """
    Отобразить список товаров.
    """
    # Проверить, что список товаров не пуст.
    if staff:
    # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 8
    )
    print(line)
    print(
    '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
    "No",
    "Название",
    "Магазин",
    "Цена"
    )
    )
    print(line)
    # Вывести данные о всех товарах.
    for idx, worker in enumerate(staff, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
            idx,
            worker.get('name', ''),
            worker.get('nameShop', ''),
            worker.get('cost', 0)
            )
            )
        print(line)
    else:
        print("Список товаров пуст.")

def select_workers(staff, period):
    """
    Выбрать товары по заданным ценам.
    """
    # Получить текущую цену.
    today = date.today()
    # Сформировать список товаров.
    result = []
    for employee in staff:
        if today.cost - employee.get('cost', today.cost) >= period:
            result.append(employee)
    # Возвратить список выбранных товаров.
    return result

def save_workers(file_name, staff):
    """
    Сохранить все товары в файл JSON.
    """
    # Открыть файл с заданным именем для записи.
    with open(file_name, "w", encoding="utf-8") as fout:
        # Выполнить сериализацию данных в формат JSON.
        # Для поддержки кирилицы установим ensure_ascii=False
        json.dump(staff, fout, ensure_ascii=False, indent=4)

def load_workers(file_name):
    """
    Загрузить все товары из файла JSON.
    """
    # Открыть файл с заданным именем для чтения.
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)

def main():
    """
    Главная функция программы.
    """
    # Список товаров.
    workers = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.
        if command == "exit":
            break
        elif command == "add":
            # Запросить данные о товаре.
            worker = get_worker()
            # Добавить словарь в список.
            workers.append(worker)
            # Отсортировать список в случае необходимости.
            if len(workers) > 1:
                workers.sort(key=lambda item: item.get('name', ''))
        elif command == "list":
            # Отобразить все товары.
            display_workers(workers)
        elif command.startswith("select "):
            # Разбить команду на части для выделения цены.
            parts = command.split(maxsplit=1)
            # Получить требуемую цену.
            period = int(parts[1])
            # Выбрать товар с заданной ценой.
            selected = select_workers(workers, period)
            # Отобразить выбранные товары.
            display_workers(selected)
        elif command.startswith("save "):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(maxsplit=1)
            # Получить имя файла.
            file_name = parts[1]
            # Сохранить данные в файл с заданным именем.
            save_workers(file_name, workers)
        elif command.startswith("load "):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(maxsplit=1)
            # Получить имя файла.
            file_name = parts[1]
            # Сохранить данные в файл с заданным именем.
            workers = load_workers(file_name)
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить товар;")
            print("list - вывести список товаров;")
            print("select <стаж> - запросить товар по цене;")
            print("help - отобразить справку;")
            print("load - загрузить данные из файла;")
            print("save - сохранить данные в файл;")
            print("exit - завершить работу с программой.")
    else:
        print(f"Неизвестная команда {command}", file=sys.stderr)

if __name__ == '__main__':
    main()
