import json
import xml.etree.ElementTree as ET


# Чтение данных из JSON файла
def read_json(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


# Конвертация данных из JSON в XML
def convert_json_to_xml(data):
    root = ET.Element("people")
    for person in data:
        person_element = ET.SubElement(root, "person")

        name = ET.SubElement(person_element, "name")
        name.text = person["name"]

        age = ET.SubElement(person_element, "age")
        age.text = str(person["age"])

        profession = ET.SubElement(person_element, "profession")
        profession.text = person["profession"]

        city = ET.SubElement(person_element, "city")
        city.text = person["city"]

    tree = ET.ElementTree(root)
    return tree


# Сохранение XML в файл
def save_xml(output_file, tree):
    tree.write(output_file, encoding='utf-8', xml_declaration=True)


# Основная программа
def main():
    # Путь к входному JSON файлу и выходному XML файлу
    input_file = "data.json"
    output_file = "data.xml"

    # Чтение данных из JSON
    data = read_json(input_file)

    # Конвертация данных в XML
    tree = convert_json_to_xml(data)

    # Сохранение в XML файл
    save_xml(output_file, tree)

    print(f"Данные успешно конвертированы в XML и сохранены в файл {output_file}.")


if __name__ == "__main__":
    main()
