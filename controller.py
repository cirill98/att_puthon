from datetime import datetime

import view
import file_manager


def last_id(data): # создание новой заметки в конце
    id_list = [int(i["id"]) for i in data]
    if len(id_list) != 0:
        return max(id_list) + 1
    else:
        return 1

def what_id_note(what_find, data):
    index = 0
    target = 0
    for note in data:
        if note['id'] == what_find:
            target = index
        index += 1
    return data[target]

def what_date_note(what_find, data):
    index = 0
    target = 0
    for note in data:
        if datetime.strptime(note['date'], '%d-%m-%Y').date() == what_find:
            target = index
        index += 1
    return data[target]



def main_logic():
    is_running = True
    notes = file_manager.load_data()
    while is_running:
        pos = view.my_comander()
        if pos == 1:
            create_find = view.create_note()
            create_find["id"] = last_id(notes)
            notes.append(create_find)

        elif pos == 2:
            view.update_note(notes, int(input('Введите id: ')))
        elif pos == 3:
            what_id = int(input("Введите id: "))
            target = what_id_note(what_id, notes)
            print(target)
        elif pos == 4:
            what_data = datetime.strptime(input("Введите дату: "), '%d-%m-%Y').date()
            target = what_date_note(what_data, notes)
            print(target)
        elif pos == 5:
            view.delete_note(notes, int(input('Введите id: ')))
        elif pos == 6:
            for i in notes:
                print(i)
        elif pos == 7:
            is_running = False
            file_manager.save_data(notes)
        else:
            print("Команде не распознана")
