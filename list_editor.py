'''
Преобразует список вида
	Покровская 
	Марина Александровна
	Козачевская 
	Людмила Ивановна
	Гореликова 
	Елена Николаевна
в (и сортирует)
	Е.Н. Гореликова
	Л.И. Козачевская
	М.А. Покровская
Входной файл - dirty_list.txt
Выходной файл - good_list.txt
Название файлов можно изменить в строках 18, 19, 54
'''

with open("dirty_list.txt", "r", encoding="utf-8") as infile, \
	 open("good_list.txt", "w", encoding="utf-8") as outfile:
	
	lines = [line.strip() for line in infile if line.strip()]  # убрать пустые строки
	seen = set()  # для хранения уникальных полных ФИО

	for i in range(0, len(lines), 2):
		try:
			last_name = lines[i]
			first_middle = lines[i + 1]
			full_name = f"{last_name} {first_middle}"

			if full_name in seen:
				continue  # пропустить повторяющиеся

			seen.add(full_name)

			first_name, middle_name = first_middle.split()
			result = f"{first_name[0]}.{middle_name[0]}. {last_name}"
			outfile.write(result + "\n")

		except (IndexError, ValueError):
			outfile.write(f"Ошибка в строках: {lines[i:i+2]}\n")

def sort_and_deduplicate_file(filename):
	with open(filename, 'r', encoding='utf-8') as f:
		lines = f.readlines()

	# Удаляем пробелы/переводы строк, удаляем дубликаты, сортируем
	unique_sorted_lines = sorted(set(line.strip() for line in lines if line.strip()))

	with open(filename, 'w', encoding='utf-8') as f:
		for line in unique_sorted_lines:
			f.write(line + '\n')

# Пример использования
sort_and_deduplicate_file("good_list.txt")
