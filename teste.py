import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Cria as variáveis do problema
comida = ctrl.Antecedent(np.arange(0, 401, 1), 'comida')
servico = ctrl.Antecedent(np.arange(0, 41, 1), 'servico')
cantoria = ctrl.Antecedent(np.arange(0, 3001, 1), 'cantoria') 
gorjeta = ctrl.Consequent(np.arange(0, 41, 1), 'gorjeta')

# Cria automaticamente o mapeamento entre valores nítidos e difusos 
# usando uma função de pertinência padrão (triângulo)
# 1 - Precipitação acumulada
comida['low'] = fuzz.trapmf(
    comida.universe, [0, 0, 80, 120])
comida['average'] = fuzz.trimf(
    comida.universe, [105, 160, 180])
comida['average_high'] = fuzz.trimf(
    comida.universe, [170, 225, 255])
comida['high'] = fuzz.trimf(
    comida.universe, [230, 270, 310])
comida['very_high'] = fuzz.trapmf(
    comida.universe, [295, 320, 400, 400])

# 2 - Salinidade
servico['very_low'] = fuzz.trapmf(servico.universe, [0, 0, 4, 7])
servico['low'] = fuzz.trimf(servico.universe, [6, 13, 17])
servico['average_low'] = fuzz.trimf(servico.universe, [14, 19, 26])
servico['average'] = fuzz.trimf(servico.universe, [23, 29, 32])
servico['high'] = fuzz.trapmf(servico.universe, [29, 33, 40, 40])

# 3 - Fluxo do rio
cantoria['low'] = fuzz.trapmf(cantoria.universe, [0, 0, 650, 900])
cantoria['average'] = fuzz.trimf(cantoria.universe, [650, 1000, 1350])
cantoria['average_high'] = fuzz.trimf(cantoria.universe, [1200, 1400, 1750])
cantoria['high'] = fuzz.trimf(cantoria.universe, [1650, 1900, 2300])
cantoria['very_high'] = fuzz.trapmf(cantoria.universe, [2200, 2400, 3000, 3000])

# 2 - Salinidade FINAL
gorjeta['very_low'] = fuzz.trapmf(gorjeta.universe, [0, 0, 4, 7])
gorjeta['low'] = fuzz.trimf(gorjeta.universe, [6, 13, 17])
gorjeta['average_low'] = fuzz.trimf(gorjeta.universe, [14, 19, 26])
gorjeta['average'] = fuzz.trimf(gorjeta.universe, [23, 29, 32])
gorjeta['high'] = fuzz.trapmf(gorjeta.universe, [29, 33, 40, 40])

comida.view()
servico.view()
cantoria.view()
gorjeta.view()

rule1 = ctrl.Rule(comida['low'] & servico['average_low'] & cantoria['average'], gorjeta['average_low'])
rule2 = ctrl.Rule(comida['low'] & servico['average'] & cantoria['average_high'], gorjeta['average_low'])
rule3 = ctrl.Rule(comida['low'] & servico['average_low'] & cantoria['average_high'], gorjeta['low'])
rule4 = ctrl.Rule(comida['low'] & servico['average_low'] & cantoria['high'], gorjeta['low'])
rule5 = ctrl.Rule(comida['low'] & servico['low'] & cantoria['high'], gorjeta['average_low'])
rule6 = ctrl.Rule(comida['low'] & servico['average'] & cantoria['very_high'], gorjeta['low'])
rule7 = ctrl.Rule(comida['low'] & servico['average_low'] & cantoria['very_high'], gorjeta['average_low'])
rule8 = ctrl.Rule(comida['low'] & servico['low'] & cantoria['very_high'], gorjeta['average_low'])
rule9 = ctrl.Rule(comida['low'] & servico['average'] & cantoria['low'], gorjeta['average'])
rule10 = ctrl.Rule(comida['low'] & servico['average'] & cantoria['average'], gorjeta['average_low'])
rule11 = ctrl.Rule(comida['low'] & servico['low'] & cantoria['low'], gorjeta['low'])
rule12 = ctrl.Rule(comida['average'] & servico['average'] & cantoria['low'], gorjeta['average_low'])
rule13 = ctrl.Rule(comida['average'] & servico['average_low'] & cantoria['low'], gorjeta['average_low'])
rule14 = ctrl.Rule(comida['average'] & servico['average'] & cantoria['average'], gorjeta['average_low'])
rule15 = ctrl.Rule(comida['average'] & servico['average'] & cantoria['average_high'], gorjeta['average_low'])
rule16 = ctrl.Rule(comida['average'] & servico['average_low']& cantoria['average'], gorjeta['low'])
rule17 = ctrl.Rule(comida['average'] & servico['high'] & cantoria['low'], gorjeta['average'])
rule18 = ctrl.Rule(comida['average'] & servico['high'] & cantoria['average'], gorjeta['average_low'])
rule19 = ctrl.Rule(comida['average'] & servico['high'] & cantoria['average_high'], gorjeta['low'])
rule20 = ctrl.Rule(comida['average'] & servico['low'] & cantoria['average'], gorjeta['low'])
rule21 = ctrl.Rule(comida['average'] & servico['low'] & cantoria['low'], gorjeta['low'])
rule22 = ctrl.Rule(comida['average_high'] & servico['average'] & cantoria['low'], gorjeta['average_low'])
rule23 = ctrl.Rule(comida['average_high'] & servico['average_low'] & cantoria['low'], gorjeta['average_low'])
rule24 = ctrl.Rule( comida['high'] & servico['average'] & cantoria['low'], gorjeta['average_low'])
rule25 = ctrl.Rule(comida['high'] & servico['average_low'] & cantoria['low'], gorjeta['low'])
rule26 = ctrl.Rule(comida['very_high'] & servico['average'] & cantoria['low'], gorjeta['very_low'])
rule27 = ctrl.Rule(comida['very_high'] & servico['average_low'] & cantoria['low'], gorjeta['very_low'])
rule28 = ctrl.Rule(comida['very_high'] & servico['low'] & cantoria['low'], gorjeta['very_low'])

gorjeta_ctrl = ctrl.ControlSystem([
    rule1, rule2, rule3, rule4, rule5,
    rule6, rule7, rule8, rule9, rule10,
    rule11, rule12, rule13, rule14, rule15,
    rule16, rule17, rule18, rule19, rule20,
    rule21, rule22, rule23, rule24, rule25,
    rule26, rule27, rule28
])
gorjeta_simulador = ctrl.ControlSystemSimulation(gorjeta_ctrl)

# Entrando com alguns valores para qualidade da comida e do serviço
gorjeta_simulador.input['comida'] = 23
gorjeta_simulador.input['servico'] = 23
gorjeta_simulador.input['cantoria'] = 1454

# Computando o resultado
gorjeta_simulador.compute()
print(gorjeta_simulador.output['gorjeta'])

comida.view(sim=gorjeta_simulador)
servico.view(sim=gorjeta_simulador)
cantoria.view(sim=gorjeta_simulador)
gorjeta.view(sim=gorjeta_simulador)

plt.show()
