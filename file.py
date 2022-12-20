#1

def code(list_of_strings, n):
    list_of_bytes = []
    i = 0
    while i < n:
        a = list_of_strings[i].encode('utf-8')
        list_of_bytes.append(a)
        i += 1
    return list_of_bytes

def decode(list_of_bytes, n):
    list_of_strings_2 = []
    i = 0
    while i < n:
        a = bytes.decode(list_of_bytes[i], 'utf-8')
        list_of_strings_2.append(a)
        i += 1
    return list_of_strings_2

list_of_strings = []

n = int(input("Введите количество строк, которые хотите добавить: "))
i = 0
while i < n:
    string = input("Введите строку на кирилице: ")
    list_of_strings.append(string)
    i += 1

list_of_bytes = code(list_of_strings, n)
print(list_of_bytes)
list_of_strings_2 = decode(list_of_bytes, n)
print(list_of_strings_2)

#2

with open('input.txt', 'r', encoding='utf-8') as file:
    text = []
    text = file.read()
    text = text.split(",")
C = int(text[0]) // 2
H = int(text[1]) // 6
O = int(text[2]) // 1
count = min(C,H,O)
with open('output.txt', 'w', encoding='utf-8') as file2:
    file2.write(str(count))

