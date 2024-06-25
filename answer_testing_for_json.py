# Работа с JSON: добавить супергероев (2+) и отсортировать всех супергероев по возрасту, результат работы - новый JSON (superhero_new.json) с отсортированными данными.

# Добавление новых героев
import json
import operator

new_data = {"name": "Ivan", "age": 19, "secretIdentity": "Dan Juk", "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]}, {"name": "Vera", "age": 80, "secretIdentity": "Dan", "powers": ["Radiation resistance"]}

INPUT_FILE = 'SuperHero.json'
OUTPUT_FILE = 'superhero_new.json'
SORT_FILE = 'superhero_new_sorted.json'

# Открытие файла
def open_json():

    with open(INPUT_FILE, encoding='utf8') as file:
        read_json = file.read()
        data = json.loads(read_json)
    return data

OPEN = open_json() 

# Добавление новых значений в файл
def append_json():

    OPEN['members'] += new_data

    with open(OUTPUT_FILE, 'w', encoding='utf8') as outfile:
        data_new_data = outfile.write(json.dumps(OPEN, sort_keys=True, ensure_ascii=False,indent=4))
    return data_new_data

APPEND = append_json() 

# Сортировка нового файла в порядке возрастания по возрасту 
def sort_json():

    with open('superhero_new.json', encoding='utf8') as file:
        read_json = file.read()
        OPEN = json.loads(read_json)
        # sorted(read_json,key=lambda x : x['members'].get['age',0], reverse=True)

    sort_members = sorted(OPEN["members"],key=operator.itemgetter("age"))  
    OPEN["members"] = sort_members

    with open('superhero_new_sorted.json', 'w', encoding='utf8') as outfile:
        data_new_data_sort = outfile.write(json.dumps(OPEN, sort_keys=True, ensure_ascii=False, indent=4))
    return data_new_data_sort
    
SORT = sort_json()

# def comprasion_file_json_and_new_file():

#     result = filecmp.cmp(OPEN,APPEND)
#     return result
#     # result = filecmp.cmp(f1, f2, shallow=False)
#     # print(result) 


# def comprasion_file_json_and_new_file():
#     result = filecmp.cmp(OPEN,APPEND)
#     return result

# def comprasion_file_json_and_new_file():
#     pass


if "__main__" == __name__:
    open_json()
    append_json()
    sort_json()