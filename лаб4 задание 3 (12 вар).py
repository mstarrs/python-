from Bio import SeqIO

# путь к файлу
f = "var12.gb" 

print(f"Чтение файла: {f}")
print("=" * 70)

# перебираем все записи в файле
for record in SeqIO.parse(f, "genbank"):
    # перебираем все признаки (features) в каждой записи
    for feature in record.features:
        if feature.type == "CDS":
            # извлекаем нуклеотидную последовательность CDS
            cds_seq = feature.extract(record.seq)
            
            # транслируем в белок (стандартный генетический код)
            protein_seq = cds_seq.translate(to_stop=True)
            
            # получаем координаты CDS
            location = feature.location
            start = location.start
            end = location.end
            
            # определяем цепь (+ или -)
            if location.strand == 1:
                strand = "+"
            else:
                strand = "-"
            
            # формируем описание для вывода
            # берём Accession и описание из record
            accession = record.id
            
            # описание: берём из record.description или из product
            if 'product' in feature.qualifiers:
                product = feature.qualifiers['product'][0]
                description = f"{accession}: {product}"
            else:
                description = f"{accession}: {record.description}"
            
            # выводим результат как в примере
            print(f"\n{description}")
            print(f"Coding sequence location = [{start}:{end}]({strand})")
            print("Translation =")
            
            # выводим белок по 60 символов в строке (как в примере)
            protein_str = str(protein_seq)
            for i in range(0, len(protein_str), 60):
                print(protein_str[i:i+60])
            print()

print("=" * 70)
print("Готово!")