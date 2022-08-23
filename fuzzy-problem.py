import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

# Definindo as variáveis
accumulated_precipitation = np.arange(0, 401, 1) # Precipitação Acumulada (mm)
salinity = np.arange(0, 41, 1) # Salinidade (ppm)
flow_river  = np.arange(0, 3001, 1) # fluxo do rio (mm^3/s)

# Setando as variáveis de entrada, gerando funções de pertinencia de números fuzzy triangulares e trapezoidais
# 1 - Precipitação acumulada
accumulated_precipitation_low = fuzz.trapmf(accumulated_precipitation, [0, 0, 80, 120])
accumulated_precipitation_average = fuzz.trimf(accumulated_precipitation, [105, 160, 180])
accumulated_precipitation_average_high = fuzz.trimf(accumulated_precipitation, [170, 225, 255])
accumulated_precipitation_high = fuzz.trimf(accumulated_precipitation, [230, 270, 310])
accumulated_precipitation_very_high = fuzz.trapmf(accumulated_precipitation, [295, 320, 400, 400])
# 2 - Salinidade 
salinity_very_low = fuzz.trapmf(salinity, [0, 0, 4, 7])
salinity_low = fuzz.trimf(salinity, [6, 13, 17])
salinity_average_low = fuzz.trimf(salinity, [14, 19, 26])
salinity_average = fuzz.trimf(salinity, [23, 29, 32])
salinity_high = fuzz.trapmf(salinity, [29, 33, 40, 40])
# 3 - Fluxo do rio
flow_river_low = fuzz.trapmf(flow_river, [0, 0, 650, 900])
flow_river_average = fuzz.trimf(flow_river, [650, 1000, 1350])
flow_river_average_high = fuzz.trimf(flow_river, [1200, 1400, 1750])
flow_river_high = fuzz.trimf(flow_river, [1650, 1900, 2300])
flow_river_very_high = fuzz.trapmf(flow_river, [2200, 2400, 3000, 3000])

# Visualização das funções de pertinência
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(10, 10))
ax0.plot(accumulated_precipitation, accumulated_precipitation_low, 'b', linewidth=1.5, label='LOW')
ax0.plot(accumulated_precipitation, accumulated_precipitation_average, 'g', linewidth=1.5, label='AVERAGE')
ax0.plot(accumulated_precipitation, accumulated_precipitation_average_high, 'r', linewidth=1.5, label='AVERAGE HIGH')
ax0.plot(accumulated_precipitation, accumulated_precipitation_high, 'c', linewidth=1.5, label='HIGH')
ax0.plot(accumulated_precipitation,accumulated_precipitation_very_high, 'm', linewidth=1.5, label='VERY HIGH')
ax0.set_title('Accumulated Precipitation in Caninéia')
ax0.legend()

ax1.plot(salinity, salinity_very_low, 'b', linewidth=1.5, label='VERY LOW')
ax1.plot(salinity, salinity_low, 'g', linewidth=1.5, label='LOW')
ax1.plot(salinity, salinity_average_low, 'r', linewidth=1.5, label='AVERAGE LOW')
ax1.plot(salinity, salinity_average, 'c', linewidth=1.5, label='AVERAGE')
ax1.plot(salinity, salinity_high, 'm', linewidth=1.5, label='HIGH')
ax1.set_title('Salinity in Caninéia')
ax1.legend()

ax2.plot(flow_river, flow_river_low, 'b', linewidth=1.5, label='LOW')
ax2.plot(flow_river, flow_river_average, 'g', linewidth=1.5, label='AVERAGE')
ax2.plot(flow_river, flow_river_average_high, 'r', linewidth=1.5, label='AVERAGE HIGH')
ax2.plot(flow_river, flow_river_high, 'c', linewidth=1.5, label='HIGH')
ax2.plot(flow_river, flow_river_very_high, 'm', linewidth=1.5, label='VERY HIGH')
ax2.set_title('Flow of the Ribeira river')
ax2.legend()

for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show()

# Aplicando as regras
rule1 = ctrl.Rule(accumulated_precipitation_low & salinity_average_low & flow_river_average, salinity_average_low)
