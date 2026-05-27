import matplotlib.pyplot as plt
import statsmodels.api as sm

# 1. загружаем данные
co2_data = sm.datasets.co2.load_pandas()
data = co2_data.data

# 2. данные co2 имеют специальный индекс с датами
#    преобразуем его в формат datetime для удобной фильтрации по годам
#    если индекс ещё не в datetime, создаём его с начальной даты
if not hasattr(data.index, 'year'):
    # для co2: начало января 1958, частота — месяцы
    data.index = pd.date_range(start='1958-01-01', periods=len(data), freq='M')

# 3. фильтруем строки за 1958–1980 годы (включительно)
mask = (data.index.year >= 1958) & (data.index.year <= 1980)
data_period = data.loc[mask]

# 4. строим график
plt.figure(figsize=(12, 5))
plt.plot(data_period.index, data_period['co2'], linewidth=2, color='darkgreen')

# 5. пастройки графика
plt.title('Динамика концентрации CO₂ (1958–1980 гг.)', fontsize=14)
plt.xlabel('Год', fontsize=12)
plt.ylabel('Концентрация CO₂ (ppm)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# 6. показываем график
plt.show()