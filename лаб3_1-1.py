# импортируем нужные библиотеки
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# 1. загружаем данные
iris = load_iris()
data = iris.data          
target = iris.target      
feature_names = iris.feature_names
class_names = iris.target_names

# 2. выбираем нужные столбцы (факторы)
# индексы: 0 — sepal length (cm), 1 — sepal width (cm)
x = data[:, 0]   # длина чашелистика
y = data[:, 1]   # ширина чашелистика

# 3. строим диаграмму рассеяния с цветом по классам
plt.figure(figsize=(8, 6))

# для каждого класса (0, 1, 2) рисуем свои точки
for class_idx in range(3):
# выбираем точки, принадлежащие текущему классу
    mask = (target == class_idx)
    plt.scatter(x[mask], y[mask],
                label=class_names[class_idx],
                alpha=0.7,  
                s=50)        

# 4. настраиваем внешний вид графика
plt.title("Диаграмма рассеяния для Iris (sklearn)\nДлина чашелистика vs Ширина чашелистика")
plt.xlabel("Длина чашелистика (cм)")
plt.ylabel("Ширина чашелистика (cм)")
plt.legend(title="Вид ириса")
plt.grid(True, linestyle='--', alpha=0.5)

# 5. показываем график
plt.tight_layout()
plt.show()
