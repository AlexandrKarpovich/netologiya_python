# validate_car_number.py
import re

def replace_latin_with_cyrillic(car_id):
    # Словарь для замены латинских букв на кириллические
    latin_to_cyrillic = {
        'A': 'А',
        'B': 'Б',
        'C': 'С',
        'E': 'Е',
        'K': 'К',
        'M': 'М',
        'H': 'Н',
        'O': 'О',
        'P': 'Р',
        'Y': 'У',
        'X': 'Х'
    }

    # Заменяем все латинские буквы, если они есть в словаре
    for latin, cyrillic in latin_to_cyrillic.items():
        car_id = car_id.replace(latin, cyrillic)

    return car_id


def validate_car_number(car_id):
    # Сначала заменяем латинские буквы на кириллические
    car_id = replace_latin_with_cyrillic(car_id)

    # Регулярное выражение для проверки транспортного номера
    # Только кириллические буквы (А-ЯЁ), цифры (0-9), формат: 1 буква, 3 цифры, 2 буквы, 2-3 цифры
    pattern = r'^([А-ЯЁ])(\d{3})([А-ЯЁ]{2})(\d{2,3})$'

    # Проверяем, совпадает ли строка с шаблоном
    match = re.match(pattern, car_id)

    if match:
        # Если номер валиден, выводим номер и регион
        number = match.group(1) + match.group(2) + match.group(3)
        region = match.group(4)
        return f"Номер {number} валиден. Регион: {region}."
    else:
        return "Номер не валиден."
