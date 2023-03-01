from datetime import datetime

import controller


def my_comander():
    com_list = ['Создать новую заметку', 'Изменить заметку', 'Посмотреть определенную заметку по id',
                'Посмотреть определенную заметку по дате', 'Удалить определенную заметку',
                'Посмотреть все заметки', 'Выход']
    print("Введите номер команды: ")
    for i, com in enumerate(com_list, start=1):
        print(f'{i}. {com}')
    number = int(input('\n'))
    if 0 < number < 8:
        return number
    else:
        print("Некоректный ввод")
        return 7

def find_note():
    find_note = int(input("Введите id"))
    return find_note

def create_note():
    new_note = {"id": ""}
    new_note['title'] = input('Ввод заголовка: ')
    new_note['text'] = input('Ввод текста: ')
    new_note['date'] = datetime.now().strftime("%d-%m-%Y")
    print(new_note)
    return new_note

def update_note(all_note, input_id):
    for i in all_note:
        if i['id'] == int(input_id):
            i['title'] = input('Введите новый заголовок: ')
            i['text'] = input('Введите новый текст: ')
            i['date'] = datetime.now().strftime("%d-%m-%Y")


def print_all_note(view):
    view_not_print = []

    for i in range(len(view)):
        notes = list(view[i].values())
        notes.pop(0)
        view_not_print.append(notes)

        # Доработать
        print(view_not_print)

def delete_note(all_notes, id): # Подождать Императора
    index = None
    for i in range(len(all_notes)):
        if all_notes[i]['id'] == id:
            index = i
            break
    del all_notes[index]
    print("Запись удалена")











