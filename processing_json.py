# метод для добавления словаря в json файл
def write_json(id, title, author, year, status):
    data = {'id': id, 'title': title, 'author': author, 'year': year, 'status': status}
    data = str(data).replace('\'', '"')
    with open('books.json', 'rb') as jsonFile:
        json_obj = jsonFile.read().decode('utf-8')
    with open('books.json', 'wb') as jsonFile:
        if len(json_obj) > 2 and json_obj[0] == '[':
            result = f"{json_obj[:-1]}, {data}]"
        else:
            result = f"[{data}]"
        jsonFile.write(bytes(result, 'utf-8'))



# метод для преобразования json файла в список словарей (предусматривает только два типа данных значений словаря: строковый и целочисенный)
def read_json():
    with open('books.json', 'rb') as jsonFile:
        json_obj = jsonFile.read().decode('utf-8').replace('[', '').replace(']', '')
        number_lines = json_obj.count('}')
        list_line = list()
        if number_lines:
            for number in range(number_lines):
                line = json_obj[json_obj.find('{') + 1:json_obj.find('}')]
                dict_line = dict()
                while line:
                    name = line[line.find('"') + 1:line.find(':')-1]
                    line = line[line.find(':')+2:]
                    if line[0] == '"':
                        line = line[1:]
                        dict_line[name] = line[:line.find('"')]
                        line = line[line.find('"')+1:]
                    else:
                        if line.find(',') == -1:
                            dict_line[name] = int(line)
                            break
                        else:
                            dict_line[name] = int(line[:line.find(',')])
                list_line.append(dict_line)
                json_obj = json_obj[json_obj.find('}') + 1:]

        return list_line


write_json(1, "Мастер и Маргарита", "Михаил Булгаков", 1967, "в наличии")
print(read_json())
