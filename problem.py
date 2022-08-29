import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Cria as variáveis do problema
precipitacao_acumulada = ctrl.Antecedent(np.arange(0, 401, 1), 'precipitacao_acumulada')
salinidade = ctrl.Antecedent(np.arange(0, 41, 1), 'salinidade')
fluxo_rio = ctrl.Antecedent(np.arange(0, 3001, 1), 'fluxo_rio') 
salinidade_final = ctrl.Consequent(np.arange(0, 41, 1), 'salinidade_final') # OBS salinidade é a mesma que salinidade final!

# Cria automaticamente o mapeamento entre valores nítidos e difusos 
# usando uma função de pertinência padrão (triângulo)
# 1 - Precipitação acumulada
precipitacao_acumulada['low'] = fuzz.trapmf(precipitacao_acumulada.universe, [0, 0, 75, 125])
precipitacao_acumulada['average'] = fuzz.trimf(precipitacao_acumulada.universe, [105, 165, 190])
precipitacao_acumulada['average_high'] = fuzz.trimf(precipitacao_acumulada.universe, [170, 230, 260])
precipitacao_acumulada['high'] = fuzz.trimf(precipitacao_acumulada.universe, [225, 280, 315])
precipitacao_acumulada['very_high'] = fuzz.trapmf(precipitacao_acumulada.universe, [290, 325, 370, 370])

# 2 - Salinidade
salinidade['very_low'] = fuzz.trapmf(salinidade.universe, [0, 0, 4, 8])
salinidade['low'] = fuzz.trimf(salinidade.universe, [7, 14, 17])
salinidade['average_low'] = fuzz.trimf(salinidade.universe, [14, 20, 26])
salinidade['average'] = fuzz.trimf(salinidade.universe, [23, 29, 32])
salinidade['high'] = fuzz.trapmf(salinidade.universe, [29, 33, 37, 37])

# 3 - Fluxo do rio
fluxo_rio['low'] = fuzz.trapmf(fluxo_rio.universe, [0, 0, 650, 900])
fluxo_rio['average'] = fuzz.trimf(fluxo_rio.universe, [650, 1000, 1350])
fluxo_rio['average_high'] = fuzz.trimf(fluxo_rio.universe, [1150, 1400, 1800])
fluxo_rio['high'] = fuzz.trimf(fluxo_rio.universe, [1650, 1950, 2300])
fluxo_rio['very_high'] = fuzz.trapmf(fluxo_rio.universe, [2150, 2470, 3000, 3000])

# 2 - Salinidade FINAL
salinidade_final['very_low'] = fuzz.trapmf(salinidade_final.universe, [0, 0, 4, 8])
salinidade_final['low'] = fuzz.trimf(salinidade_final.universe, [7, 14, 17])
salinidade_final['average_low'] = fuzz.trimf(salinidade_final.universe, [14, 20, 26])
salinidade_final['average'] = fuzz.trimf(salinidade_final.universe, [23, 29, 32])
salinidade_final['high'] = fuzz.trapmf(salinidade_final.universe, [29, 33, 37, 37])

precipitacao_acumulada.view()
salinidade.view()
fluxo_rio.view()
salinidade_final.view()

rule1 = ctrl.Rule(precipitacao_acumulada['low'] & salinidade['average_low'] & fluxo_rio['average'], salinidade_final['average_low'])
rule2 = ctrl.Rule(precipitacao_acumulada['low'] & salinidade['average'] & fluxo_rio['average_high'], salinidade_final['average_low'])
rule3 = ctrl.Rule(precipitacao_acumulada['low'] & salinidade['average_low'] & fluxo_rio['average_high'], salinidade_final['low'])
rule4 = ctrl.Rule(precipitacao_acumulada['low'] & salinidade['average_low'] & fluxo_rio['high'], salinidade_final['low'])
rule5 = ctrl.Rule(precipitacao_acumulada['low'] & salinidade['low'] & fluxo_rio['high'], salinidade_final['average_low'])
rule6 = ctrl.Rule(precipitacao_acumulada['low'] & salinidade['average'] & fluxo_rio['very_high'], salinidade_final['low'])
rule7 = ctrl.Rule(precipitacao_acumulada['low'] & salinidade['average_low'] & fluxo_rio['very_high'], salinidade_final['average_low'])
rule8 = ctrl.Rule(precipitacao_acumulada['low'] & salinidade['low'] & fluxo_rio['very_high'], salinidade_final['average_low'])
rule9 = ctrl.Rule(precipitacao_acumulada['low'] & salinidade['average'] & fluxo_rio['low'], salinidade_final['average'])
rule10 = ctrl.Rule(precipitacao_acumulada['low'] & salinidade['average'] & fluxo_rio['average'], salinidade_final['average_low'])
rule11 = ctrl.Rule(precipitacao_acumulada['low'] & salinidade['low'] & fluxo_rio['low'], salinidade_final['low'])
rule12 = ctrl.Rule(precipitacao_acumulada['average'] & salinidade['average'] & fluxo_rio['low'], salinidade_final['average_low'])
rule13 = ctrl.Rule(precipitacao_acumulada['average'] & salinidade['average_low'] & fluxo_rio['low'], salinidade_final['average_low'])
rule14 = ctrl.Rule(precipitacao_acumulada['average'] & salinidade['average'] & fluxo_rio['average'], salinidade_final['average_low'])
rule15 = ctrl.Rule(precipitacao_acumulada['average'] & salinidade['average'] & fluxo_rio['average_high'], salinidade_final['average_low'])
rule16 = ctrl.Rule(precipitacao_acumulada['average'] & salinidade['average_low']& fluxo_rio['average'], salinidade_final['low'])
rule17 = ctrl.Rule(precipitacao_acumulada['average'] & salinidade['high'] & fluxo_rio['low'], salinidade_final['average'])
rule18 = ctrl.Rule(precipitacao_acumulada['average'] & salinidade['high'] & fluxo_rio['average'], salinidade_final['average_low'])
rule19 = ctrl.Rule(precipitacao_acumulada['average'] & salinidade['high'] & fluxo_rio['average_high'], salinidade_final['low'])
rule20 = ctrl.Rule(precipitacao_acumulada['average'] & salinidade['low'] & fluxo_rio['average'], salinidade_final['low'])
rule21 = ctrl.Rule(precipitacao_acumulada['average'] & salinidade['low'] & fluxo_rio['low'], salinidade_final['low'])
rule22 = ctrl.Rule(precipitacao_acumulada['average_high'] & salinidade['average'] & fluxo_rio['low'], salinidade_final['average_low'])
rule23 = ctrl.Rule(precipitacao_acumulada['average_high'] & salinidade['average_low'] & fluxo_rio['low'], salinidade_final['average_low'])
rule24 = ctrl.Rule( precipitacao_acumulada['high'] & salinidade['average'] & fluxo_rio['low'], salinidade_final['average_low'])
rule25 = ctrl.Rule(precipitacao_acumulada['high'] & salinidade['average_low'] & fluxo_rio['low'], salinidade_final['low'])
rule26 = ctrl.Rule(precipitacao_acumulada['very_high'] & salinidade['average'] & fluxo_rio['low'], salinidade_final['very_low'])
rule27 = ctrl.Rule(precipitacao_acumulada['very_high'] & salinidade['average_low'] & fluxo_rio['low'], salinidade_final['very_low'])
rule28 = ctrl.Rule(precipitacao_acumulada['very_high'] & salinidade['low'] & fluxo_rio['low'], salinidade_final['very_low'])

salinidade_final_ctrl = ctrl.ControlSystem([
    rule1, rule2, rule3, rule4, rule5,
    rule6, rule7, rule8, rule9, rule10,
    rule11, rule12, rule13, rule14, rule15,
    rule16, rule17, rule18, rule19, rule20,
    rule21, rule22, rule23, rule24, rule25,
    rule26, rule27, rule28
])
salinidade_final_simulador = ctrl.ControlSystemSimulation(salinidade_final_ctrl)

# Entrando com alguns valores para qualidade da precipitacao_acumulada e do serviço
salinidade_final_simulador.input['precipitacao_acumulada'] = 13.6
salinidade_final_simulador.input['salinidade'] = 14
salinidade_final_simulador.input['fluxo_rio'] = 2016

# Computando o resultado
salinidade_final_simulador.compute()
print(salinidade_final_simulador.output['salinidade_final'])

precipitacao_acumulada.view(sim=salinidade_final_simulador)
salinidade.view(sim=salinidade_final_simulador)
fluxo_rio.view(sim=salinidade_final_simulador)
salinidade_final.view(sim=salinidade_final_simulador)

plt.show()
