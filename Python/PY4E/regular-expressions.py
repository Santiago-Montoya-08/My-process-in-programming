import re

file_path = 'C:\\Users\\Lenovo\\OneDrive\\Documentos\\Programación\\Python\\PY4E\\regex_sum_2049515.txt'

with open(file_path, 'r') as file:
    data = file.read()

numbers = re.findall('[0-9]+', data)
total_sum = 0
for num in numbers:
    total_sum += int(num)

print(total_sum)
