import csv

def main():
    # Открываем файл для чтения
    with open('visit_log.csv', mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Пропускаем заголовок

        # Открываем файл для записи
        with open('funnel.csv', mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)

            # Записываем заголовок в новый файл
            writer.writerow(['user_id', 'source', 'category'])

            # Проходим по строкам исходного файла
            for row in reader:
                user_id, source, category = row

                # Если категория не пустая, то записываем строку в новый файл
                if category:  # Категория покупки существует
                    writer.writerow([user_id, source, category])

    print("Обработка завершена. Данные записаны в funnel.csv")


if __name__ == "__main__":
    main()
