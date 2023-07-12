import re

from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    new_list = list(rows)

## 1. Выполните пункты 1-3 задания.

for person in new_list[1:]:
    first_field = person[0].split()
    second_field = person[1].split()
    if len(second_field) == 2:
        person[1], person[2] = second_field
    if len(first_field) == 2:
        person[0], person[1] = first_field
    elif len(first_field) == 3:
        person[0], person[1], person[2] = first_field

pattern = r"(8|\+7)[\s]?[\(]?(\d{3})?[\)]?[\s-]?(\d{3})?[\s-]?(\d{2})?[\s-]?(\d{2})?([\s])?[\(]?(\w{3}\.\s\d{4})?[\s)]?"
pattern_repl = r"+7(\2)\3-\4-\5\6\7"

for i in new_list:
    i[5] = re.sub(pattern, pattern_repl, i[5])

data_list = []
for i in range(1):
    data_list = new_list[i]
num_elements = len(new_list[0])
dict_data = {}
for person in new_list[1:]:
    key = ' '.join(person[:2])
    if key in dict_data.keys():
        for index in range(2, len(person)):
            if len(person[index]) > 0:
                dict_data[key][index] = person[index]
    else:
        dict_data[key] = person
contacts_list = [person_data for person_data in dict_data.values()]
contacts_list.insert(0, data_list)
pprint(contacts_list)

# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',', lineterminator='\n')

# Вместо contacts_list подставьте свой список:
    datawriter.writerows(contacts_list)




