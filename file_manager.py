import pandas as pd
def save_data(data):
    data_l = pd.DataFrame(data)
    data_l.to_csv('note_book.csv', index=False, sep=';')

def load_data():
    list = []
    data = pd.read_csv('note_book.csv', sep=';')
    for index, row in data.iterrows():
        note = {}
        note['id'] = int(row['id'])
        note['title'] = row['title']
        note['text'] = row['text']
        note['date'] = row['date']
        list.append(note)
    return list
