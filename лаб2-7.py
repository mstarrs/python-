
test_data = """
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
"""

# загружаем данные

data = test_data.strip()

# разбиваем на строки
stroki = data.split('\n')

# тут будут храниться только последовательности ДНК (без названий)
all_seq = []

# текущая последовательность, которую собираем
cur_dna = ""

# проходим по всем строкам
for s in stroki:
    s = s.strip()  # убираем пробелы в начале и конце
    
    if not s:  # если строка пустая - пропускаем
        continue
    
    # если строка начинается с символа > - это название
    if s[0] == '>':  # .startswith('>') 
        if cur_dna != "":
            all_seq.append(cur_dna)
        
        # начинаем новую последовательность
        cur_dna = ""
    else:
        # это строка с ДНК - добавляем к текущей
        cur_dna = cur_dna + s

# cохраняем последнюю последовательность
if cur_dna != "":
    all_seq.append(cur_dna)

if len(all_seq) == 0:
    print("Ошибка: нет последовательностей!")
    exit()

# первая последовательность (по ней будем искать)
first = all_seq[0]

# Остальные последовательности (все, кроме первой)
other = []
for i in range(1, len(all_seq)):
    other.append(all_seq[i])

# ищем самую длинную подстроку

# сначала предполагаем, что ничего не нашли
found = ""
length = len(first)  # начинаем с самой большой возможной длины

# пока не нашли и длина >= 1
while found == "" and length >= 1:
    
    # Перебираем все подстроки первой последовательности такой длины
    for start in range(len(first) - length + 1):
        
        # берём подстроку от start до start+length
        podstroka = first[start:start+length]
        
        # Предполагаем, что эта подстрока подходит
        right = True
        
        # Проверяем, есть ли эта подстрока во всех остальных
        for another in other:
            if podstroka not in another:
                right = False
                break  # выходим из цикла, если не нашлось
        
        # если подходит для всех - запоминаем
        if right:
            found = podstroka
            break  # выходим из цикла по подстрокам
    
    # Уменьшаем длину для следующего круга
    length = length - 1

# выводим ответ
if found != "":
    print("Самый длинный общий мотив:")
    print(found)
else:
    print("Общих подстрок не найдено")