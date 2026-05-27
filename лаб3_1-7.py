import matplotlib.pyplot as plt
import statsmodels.api as sm

# 1. эагружаем данные
ccard_data = sm.datasets.ccard.load_pandas()
data = ccard_data.data

# 2. выбираем нужные столбцы
x = data['AGE']        # возраст
y = data['AVGEXP']     # средний расход
classes = data['OWNRENT']  # 1 = владеет, 0 = не владеет

# 3. строим диаграмму рассеяния
plt.figure(figsize=(8, 6))

# Точки для владельцев жилья (класс 1)
plt.scatter(x[classes == 1], y[classes == 1],
            label='Владеет жильём', alpha=0.7, s=50, c='blue')

# Точки для невладельцев (класс 0)
plt.scatter(x[classes == 0], y[classes == 0],
            label='Не владеет жильём', alpha=0.7, s=50, c='red')

# 4. Настройка графика
plt.title("Диаграмма рассеяния для ccard (statsmodels)\nВозраст vs Средний расход")
plt.xlabel("Возраст (AGE)")
plt.ylabel("Средний расход (AVGEXP)")
plt.legend(title="Владение жильём")
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()