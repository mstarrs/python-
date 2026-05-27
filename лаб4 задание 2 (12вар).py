from Bio import SeqIO

# путь к файлу
f = "var12.gb"

# cписок для хранения информации о каждой CDS
cds_list = []

print(f"Чтение файла: {f}")
print("-" * 60)

# gеребираем все записи в файле
for record in SeqIO.parse(f, "genbank"):
    # gеребираем все признаки (features) в каждой записи
    for feature in record.features:
        if feature.type == "CDS":   
            # извлекаем последовательность
            cds_seq = feature.extract(record.seq)
            
            # считаем GC-состав
            g_count = cds_seq.count('G')
            c_count = cds_seq.count('C')
            gc_count = g_count + c_count
            gc_percent = gc_count / len(cds_seq)   # доля 
            
            # формируем описание
            # берём Accession (record.id) и описание
            description = record.description
            # если описания нет, используем feature.qualifiers
            if 'product' in feature.qualifiers:
                product = feature.qualifiers['product'][0]
                description = f"{record.id}: {product}"
            
            # сохраняем всё в список
            cds_list.append({
                'accession': record.id,
                'description': description,
                'gc': gc_percent,
                'length': len(cds_seq)
            })

# сортируем по GC-составу (по возрастанию)
cds_list.sort(key=lambda x: x['gc'])

# выводим результат
print("\n" + "=" * 70)
print("РЕЗУЛЬТАТ: последовательности в порядке возрастания GC-состава")
print("=" * 70)
print()

for item in cds_list:
    print(f"{item['accession']}: {item['description']}, GC = {item['gc']}")
    print()

print("-" * 70)
print(f"Всего обработано CDS: {len(cds_list)}")

