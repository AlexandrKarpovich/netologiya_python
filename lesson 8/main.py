import csv

class Client:
    def __init__(self, full_name, gender, age, device, browser, amount, region):
        self.full_name = full_name
        self.gender = gender
        self.age = float(age)  # Преобразуем возраст в число с плавающей точкой
        self.device = device
        self.browser = browser
        self.amount = float(amount)  # Преобразуем сумму в число с плавающей точкой
        self.region = region

    def describe(self):
        # Формируем описание покупателя по шаблону
        return f"Пользователь {self.full_name} {self.gender} пола, {self.age} лет совершил покупку на {self.amount} у.е. с {self.device} браузера {self.browser}. Регион, из которого совершалась покупка: {self.region}."


class ClientDataProcessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def load_data(self):
        # Загрузим данные из CSV
        clients = []
        with open(self.input_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            print("Заголовки колонок:", reader.fieldnames)  # Выводим заголовки колонок для проверки
            for row in reader:
                client = Client(
                    full_name=row['name'],
                    gender=row['sex'],
                    age=row['age'], # age как число с плавающей точкой
                    device=row['device_type'],
                    browser=row['browser'],
                    amount=row['bill'],
                    region=row['region']
                )
                clients.append(client)
        return clients

    def save_descriptions(self, clients):
        # Запишем все описания в текстовый файл
        with open(self.output_file, mode='w', encoding='utf-8') as file:
            for client in clients:
                file.write(client.describe() + "\n")


# Основная программа
def main(input_file='web_clients_correct.csv'):
    output_file = 'clients_descriptions.txt'

    processor = ClientDataProcessor(input_file, output_file)
    clients = processor.load_data()  # Загружаем данные
    processor.save_descriptions(clients)  # Записываем описания в файл

    print("Описание клиентов успешно записано в файл.")


if __name__ == "__main__":
    main()
