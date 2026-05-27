# популяция кроликов: F(n) = F(n-1) + F(n-2) * k

data = input().split()
n = int(data[0])
k = int(data[1])

rabbits = [0] * (n + 2)  # массив для хранения результатов по месяцам

rabbits[1] = 1  # первый месяц: 1 пара

if n >= 2:
    rabbits[2] = 1  # второй месяц: всё ещё 1 пара

# рекуррентное соотношение для месяцев 3 и выше
for month in range(3, n + 1):
    rabbits[month] = rabbits[month - 1] + (rabbits[month - 2] * k)

print(rabbits[n])
