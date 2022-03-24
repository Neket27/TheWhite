# Внимание!!!
# Для запуска программы нужно прописать свои пути для файла "replacement.json" и где будет сохранён файл вывода данных(см. комент. ниже).
import json
import requests as requests
# Получение данных с API
response = requests.get("https://raw.githubusercontent.com/thewhitesoft/student-2022-assignment/main/data.json")
data_json = json.loads(response.text)

text_data=data_json
# Получение данных с файла
# with open('C:/Users/nikit/Desktop/data.json') as json_file:
#     text_data = json.load(json_file)

with open('C:/Users/nikit/Desktop/replacement.json') as json_file: # прописать сой путь к файлу "replacement.json"
    data = json.load(json_file)

data = sorted(data, key=lambda d: d['replacement'])
data.reverse()

list_edited_text=list(text_data)
count=0
edited_text=0
for keys_data in data:
    len_key=len(keys_data['replacement'])
    text_data.clear()
    text_data = list(list_edited_text)

    count = 0
    replacement = (keys_data['replacement'])
    source = (keys_data['source'])


    while count < len(text_data):
        if str(replacement) in str(text_data[count]):

            if source != None:
                if source != 'null':
                    edited_text = text_data[count].replace(str(replacement), str(source))
                    list_edited_text[count] = edited_text
            else:
                edited_text = text_data[count].replace(str(replacement), "")
                list_edited_text[count] = edited_text
        count = count + 1


list_edited_text=list(filter(None, list_edited_text))

print("==================================================")
for printt in list_edited_text:
    print(printt)
    file = open('C:/Users/nikit/Desktop/result.json', 'w')# прописать свой путь для сохранения файла
    with file as outfile:
        json.dump(list_edited_text, outfile)
file.close()



