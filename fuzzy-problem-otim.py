import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Definindo as variáveis
accumulated_precipitation = ctrl.Antecedent(np.arange(
    0, 401, 1), 'accumulated_precipitation')  # Precipitação Acumulada (mm)
salinity = ctrl.Antecedent(np.arange(0, 41, 1), 'salinity')  # Salinidade (ppm)
flow_river = ctrl.Antecedent(
    np.arange(0, 3001, 1), 'flow_river')  # fluxo do rio (mm^3/s)

# Setando as variáveis de entrada, gerando funções de pertinencia de números fuzzy triangulares e trapezoidais
# 1 - Precipitação acumulada
accumulated_precipitation['low'] = fuzz.trapmf(
    accumulated_precipitation.universe, [0, 0, 80, 120])
accumulated_precipitation['average'] = fuzz.trimf(
    accumulated_precipitation.universe, [105, 160, 180])
accumulated_precipitation['average_high'] = fuzz.trimf(
    accumulated_precipitation.universe, [170, 225, 255])
accumulated_precipitation['high'] = fuzz.trimf(
    accumulated_precipitation.universe, [230, 270, 310])
accumulated_precipitation['very_high'] = fuzz.trapmf(
    accumulated_precipitation.universe, [295, 320, 400, 400])
# 2 - Salinidade
salinity['very_low'] = fuzz.trapmf(salinity.universe, [0, 0, 4, 7])
salinity['low'] = fuzz.trimf(salinity.universe, [6, 13, 17])
salinity['average_low'] = fuzz.trimf(salinity.universe, [14, 19, 26])
salinity['average'] = fuzz.trimf(salinity.universe, [23, 29, 32])
salinity['high'] = fuzz.trapmf(salinity.universe, [29, 33, 40, 40])
# 3 - Fluxo do rio
flow_river['low'] = fuzz.trapmf(flow_river.universe, [0, 0, 650, 900])
flow_river['average'] = fuzz.trimf(flow_river.universe, [650, 1000, 1350])
flow_river['average_high'] = fuzz.trimf(
    flow_river.universe, [1200, 1400, 1750])
flow_river['high'] = fuzz.trimf(flow_river.universe, [1650, 1900, 2300])
flow_river['very_high'] = fuzz.trapmf(
    flow_river.universe, [2200, 2400, 3000, 3000])

# Mostrar funções de pertinência
accumulated_precipitation.view()
salinity.view()
flow_river.view()

rule1 = ctrl.Rule(accumulated_precipitation['low'] & salinity['average_low']
                  & flow_river['average'], salinity['average_low'])
rule2 = ctrl.Rule(accumulated_precipitation['low'] & salinity['average']
                  & flow_river['average_high'], salinity['average_low'])
rule3 = ctrl.Rule(
    accumulated_precipitation['low'] & salinity['average_low'] &
    flow_river['average_high'], salinity['low'])
rule4 = ctrl.Rule(
    accumulated_precipitation['low'] & salinity['average_low'] &
    flow_river['high'], salinity['low'])
rule5 = ctrl.Rule(
    accumulated_precipitation['low'] & salinity['low'] &
    flow_river['high'], salinity['average_low'])
rule6 = ctrl.Rule(
    accumulated_precipitation['low'] & salinity['average'] &
    flow_river['very_high'], salinity['low'])
rule7 = ctrl.Rule(accumulated_precipitation['low'] &
                  salinity['average_low']
                  & flow_river['very_high'], salinity['average_low'])
rule8 = ctrl.Rule(accumulated_precipitation['low'] &
                  salinity['low']
                  & flow_river['very_high'], salinity['average_low'])
rule9 = ctrl.Rule(
    accumulated_precipitation['low'] & salinity['average'] &
    flow_river['low'], salinity['average'])
rule10 = ctrl.Rule(accumulated_precipitation['low'] &
                   salinity['average']
                   & flow_river['average'], salinity['average_low'])
rule11 = ctrl.Rule(
    accumulated_precipitation['low'] & salinity['low'] &
    flow_river['low'], salinity['low'])
rule12 = ctrl.Rule(accumulated_precipitation['average'] &
                   salinity['average'] & flow_river['low'],
                   salinity['average_low'])
rule13 = ctrl.Rule(accumulated_precipitation['average'] &
                   salinity['average_low'] & flow_river['low'],
                   salinity['average_low'])
rule14 = ctrl.Rule(accumulated_precipitation['average'] &
                   salinity['average'] & flow_river['average'],
                   salinity['average_low'])
rule15 = ctrl.Rule(accumulated_precipitation['average'] & salinity['average']
                   & flow_river['average_high'], salinity['average_low'])
rule16 = ctrl.Rule(accumulated_precipitation['average'] &
                   salinity['average_low'] & flow_river['average'],
                   salinity['low'])
rule17 = ctrl.Rule(accumulated_precipitation['average'] &
                   salinity['high'] & flow_river['low'], salinity['average'])
rule18 = ctrl.Rule(accumulated_precipitation['average'] &
                   salinity['high'] & flow_river['average'],
                   salinity['average_low'])
rule19 = ctrl.Rule(accumulated_precipitation['average'] &
                   salinity['high'] & flow_river['average_high'],
                   salinity['low'])
rule20 = ctrl.Rule(accumulated_precipitation['average'] &
                   salinity['low'] & flow_river['average'], salinity['low'])
rule21 = ctrl.Rule(accumulated_precipitation['average']
                   & salinity['low'] & flow_river['low'], salinity['low'])
rule22 = ctrl.Rule(accumulated_precipitation['average_high'] &
                   salinity['average'] & flow_river['low'],
                   salinity['average_low'])
rule23 = ctrl.Rule(accumulated_precipitation['average_high'] &
                   salinity['average_low'] & flow_river['low'],
                   salinity['average_low'])
rule24 = ctrl.Rule(
    accumulated_precipitation['high'] & salinity['average'] &
    flow_river['low'], salinity['average_low'])
rule25 = ctrl.Rule(
    accumulated_precipitation['high'] & salinity['average_low'] &
    flow_river['low'], salinity['low'])
rule26 = ctrl.Rule(accumulated_precipitation['very_high'] &
                   salinity['average'] & flow_river['low'],
                   salinity['very_low'])
rule27 = ctrl.Rule(accumulated_precipitation['very_high'] &
                   salinity['average_low'] & flow_river['low'],
                   salinity['very_low'])
rule28 = ctrl.Rule(accumulated_precipitation['very_high'] &
                   salinity['low'] & flow_river['low'], salinity['very_low'])

apply_rules = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6,
                                  rule7, rule8, rule9, rule10, rule11, rule12,
                                  rule13, rule14, rule15, rule16, rule17,
                                  rule18, rule19, rule20, rule21, rule22,
                                  rule23, rule24, rule25, rule26, rule27,
                                  rule28])
apply_rules.view()

result = ctrl.ControlSystemSimulation(apply_rules)

result.inputs({'accumulated_precipitation': 13.6,
              'salinity': 14.0, 'flow_river': 2016})

result.compute()

print(result.output['salinity'])
salinity.view(sim=result)


plt.show()
