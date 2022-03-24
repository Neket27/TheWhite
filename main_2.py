import json
import requests as requests
def save_in_file(file_path,text_json):
    for printt in text_json:
        file = open(file_path, 'w')  # прописать свой путь для сохранения файла
        with file as outfile:
            json.dump(list_edited_text, outfile)
    file.close()

def get_list_dict_replacement_and_source(file_json_path):

    with open(file_json_path) as json_file: # прописать сой путь к файлу "replacement.json"
        data = json.load(json_file)

    data = sorted(data, key=lambda d: d['replacement'])#сортировка ключей от меньшей длины к большей
    data.reverse()
    return data

# Получение данных с API
response = requests.get("https://raw.githubusercontent.com/thewhitesoft/student-2022-assignment/main/data.json")
text_data = json.loads(response.text)
list_edited_text=list(text_data)

count=0
edited_text=0
for keys_data in get_list_dict_replacement_and_source('C:/Users/nikit/Desktop/replacement.json') :
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
save_in_file('C:/Users/nikit/Desktop/result.json',list_edited_text)


