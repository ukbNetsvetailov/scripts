'''
Сортирует строки и удаляет повторы.
Входной файл - sort_and_uniq.txt (строка 18)
'''

def sort_and_deduplicate_file(filename):
	with open(filename, 'r', encoding='utf-8') as f:
		lines = f.readlines()

	# Удаляем пробелы/переводы строк, удаляем дубликаты, сортируем
	unique_sorted_lines = sorted(set(line.strip() for line in lines if line.strip()))

	with open(filename, 'w', encoding='utf-8') as f:
		for line in unique_sorted_lines:
			f.write(line + '\n')

# Пример использования
sort_and_deduplicate_file('sort_and_uniq.txt')
