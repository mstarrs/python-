import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd

# загружаем данные
macro_data = sm.datasets.macrodata.load_pandas()
data = macro_data.data

year_int = data['year'].astype(int).astype(str)
quarter_int = data['quarter'].astype(int).astype(str)
data['date'] = pd.to_datetime(year_int + 'Q' + quarter_int)

# фильтруем строки за 1990–2009 годы
mask = (data['year'] >= 1990) & (data['year'] <= 2009)
data_period = data.loc[mask].copy()  

# строим график
plt.figure(figsize=(12, 6))

# рисуем три линии
plt.plot(data_period['date'], data_period['realgdp'], 
         label='Реальный ВВП (realgdp)', linewidth=2, color='blue')
plt.plot(data_period['date'], data_period['realcons'], 
         label='Реальное потребление (realcons)', linewidth=2, color='green')
plt.plot(data_period['date'], data_period['realgovt'], 
         label='Реальные госрасходы (realgovt)', linewidth=2, color='red')

# настройки графика
plt.title('Динамика макроэкономических показателей США (1990–2009 гг.)', fontsize=14)
plt.xlabel('Год', fontsize=12)
plt.ylabel('Млрд. долл. (в ценах 2009 г.)', fontsize=12)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)

# форматирование оси X для отображения каждого 2-го года
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y'))
plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.YearLocator(base=2))

plt.tight_layout()
plt.show()