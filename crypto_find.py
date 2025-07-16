'''
Программа осуществляет поиск по ключевым словам,
создаёт и сортирует список с файлами.
Ключевые слова можно добавить в строке объявления функции find_keyword_in_html_files,
в переменной keywords, в квадратных скобках, через запятую, используя кавычки.
Ключевые слова должны быть ВСЕГДА В НИЖНЕМ РЕГИСТРЕ
Для работы программы необходимо создать директорию "Поиск_по_аудитам" и поместить в неё папки,
содержащие другие папки или файлы, или непосредственно файлы.

'''

import os

def find_keyword_in_html_files(root_folder, keywords=["crypto pro", "vipnet"]):
    fout = open("crypto_find.txt", "w", encoding="utf-8")
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith(".html"):
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, "r", encoding="windows-1251") as file:
                        contents = file.read()
                        for keyword in keywords:
                            if keyword in contents.lower():
                                print(f"{keyword}: {file_path}")
                                fout.write(keyword + ' ' + file_path + '\n')
                except Exception as e:
                    print(f"Не удалось открыть директорию {file_path}: {e}")
    fout.close()
    print("Список готов")


def sort_lines_in_file(file_path, output_path=None):
    """
    Сортирует строки в файле по алфавиту.
    
    :param file_path: путь к исходному файлу
    :param output_path: путь к файлу для сохранения результата (если None, перезаписывается исходный файл)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        lines.sort()

        save_path = output_path if output_path else file_path

        with open(save_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)

        #print(f"Сортировка завершена: {save_path}")

    except Exception as e:
        print(f"Ошибка: {e}")
    print("Список отсортирован")

find_keyword_in_html_files("Поиск_по_аудитам")
sort_lines_in_file("crypto_find.txt")
