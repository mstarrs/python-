#нужно найти последовательность с наибольшим GC-составом

import sys

# читаем все данные
data = sys.stdin.read()

if not data.strip():
    data = """
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
"""

# очищаем от лишних пробелов в начале и конце
data = data.strip()

# разбиваем на отдельные строки
lines = data.split('\n')

#списки для хранения названий и ДНК
nm = []   # names
dn = []   # dnas

# текущая последовательность
current_name = ""
current_dna = ""

# проходим по всем строкам
for line in lines:
    line = line.strip()
    
    #если строка начинается с >, это название
    if line.startswith('>'):
        # сохраняем предыдущую ДНК, если она есть
        if current_name != "":
            nm.append(current_name)
            dn.append(current_dna)
        
        # начинаем новую последовательность
        current_name = line[1:]  # убираем символ >
        current_dna = ""
    else:
        # добавляем строку к текущей ДНК
        current_dna = current_dna + line

# сохраняем последнюю последовательность
if current_name != "":
    nm.append(current_name)
    dn.append(current_dna)

#ищем последовательность с самым большим GC-составом
best_index = 0
best_gc = 0

for i in range(len(dn)):
    dna = dn[i]
    
    # cчитаем G и C
    gc = 0
    ccnt = 0
    
    for letter in dna:
        if letter == 'G':
            gc = gc + 1
        if letter == 'C':
            ccnt = ccnt + 1
    
    # считаем процент
    total_gc = gc + ccnt
    length = len(dna)
    gc_percent = (total_gc / length) * 100
    
    # запоминаем лучший результат
    if gc_percent > best_gc:
        best_gc = gc_percent
        best_index = i

# выводим ответ
print(nm[best_index])
print(f"{best_gc:.6f}")