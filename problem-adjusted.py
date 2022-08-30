import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Cria as variáveis do problema
precipitacao_acumulada = ctrl.Antecedent(np.arange(0, 401, 1), 'precipitacao_acumulada')
salinidade = ctrl.Antecedent(np.arange(0, 41, 1), 'salinidade')
fluxo_rio = ctrl.Antecedent(np.arange(0, 3001, 1), 'fluxo_rio') 
salinidade_final = ctrl.Consequent(np.arange(0, 41, 1), 'salinidade_final') # OBS salinidade é a mesma que salinidade final!

# 1 - Precipitação acumulada
precipitacao_acumulada['baixa'] = fuzz.trapmf(precipitacao_acumulada.universe, [0, 0, 75, 125])
precipitacao_acumulada['media'] = fuzz.trimf(precipitacao_acumulada.universe, [105, 165, 190])
precipitacao_acumulada['media_alta'] = fuzz.trimf(precipitacao_acumulada.universe, [170, 230, 260])
precipitacao_acumulada['alta'] = fuzz.trimf(precipitacao_acumulada.universe, [225, 280, 315])
precipitacao_acumulada['muito_alta'] = fuzz.trapmf(precipitacao_acumulada.universe, [290, 325, 370, 370])

# 2 - Salinidade (inicial)
salinidade['muito_baixa'] = fuzz.trapmf(salinidade.universe, [0, 0, 4, 8])
salinidade['baixa'] = fuzz.trimf(salinidade.universe, [7, 14, 17])
salinidade['media_baixa'] = fuzz.trimf(salinidade.universe, [14, 20, 28]) # modificado
salinidade['media'] = fuzz.trimf(salinidade.universe, [21, 29, 32]) # modificado
salinidade['alta'] = fuzz.trapmf(salinidade.universe, [29, 33, 37, 37])

# 3 - Fluxo do rio
fluxo_rio['baixa'] = fuzz.trapmf(fluxo_rio.universe, [0, 0, 650, 900])
fluxo_rio['media'] = fuzz.trimf(fluxo_rio.universe, [650, 1000, 1350])
fluxo_rio['media_alta'] = fuzz.trimf(fluxo_rio.universe, [1150, 1400, 1800])
fluxo_rio['alta'] = fuzz.trimf(fluxo_rio.universe, [1650, 1950, 2300])
fluxo_rio['muito_alta'] = fuzz.trapmf(fluxo_rio.universe, [2150, 2470, 3000, 3000])

# 4 - Salinidade FINAL
salinidade_final['muito_baixa'] = fuzz.trapmf(salinidade_final.universe, [0, 0, 4, 8])
salinidade_final['baixa'] = fuzz.trimf(salinidade_final.universe, [7, 14, 17])
salinidade_final['media_baixa'] = fuzz.trimf(salinidade_final.universe, [14, 20, 28]) # modificado
salinidade_final['media'] = fuzz.trimf(salinidade_final.universe, [21, 29, 32]) # modificado
salinidade_final['alta'] = fuzz.trapmf(salinidade_final.universe, [29, 33, 37, 37])

precipitacao_acumulada.view()
salinidade.view()
fluxo_rio.view()
salinidade_final.view()

rule1 = ctrl.Rule(precipitacao_acumulada['baixa'] & salinidade['media_baixa'] & fluxo_rio['media'], salinidade_final['media_baixa'])
rule2 = ctrl.Rule(precipitacao_acumulada['baixa'] & salinidade['media'] & fluxo_rio['media_alta'], salinidade_final['media_baixa'])
rule3 = ctrl.Rule(precipitacao_acumulada['baixa'] & salinidade['media_baixa'] & fluxo_rio['media_alta'], salinidade_final['baixa'])
rule4 = ctrl.Rule(precipitacao_acumulada['baixa'] & salinidade['media_baixa'] & fluxo_rio['alta'], salinidade_final['baixa'])
rule5 = ctrl.Rule(precipitacao_acumulada['baixa'] & salinidade['baixa'] & fluxo_rio['alta'], salinidade_final['media_baixa'])
rule6 = ctrl.Rule(precipitacao_acumulada['baixa'] & salinidade['media'] & fluxo_rio['muito_alta'], salinidade_final['baixa'])
rule7 = ctrl.Rule(precipitacao_acumulada['baixa'] & salinidade['media_baixa'] & fluxo_rio['muito_alta'], salinidade_final['media_baixa'])
rule8 = ctrl.Rule(precipitacao_acumulada['baixa'] & salinidade['baixa'] & fluxo_rio['muito_alta'], salinidade_final['media_baixa'])
rule9 = ctrl.Rule(precipitacao_acumulada['baixa'] & salinidade['media'] & fluxo_rio['baixa'], salinidade_final['media'])
rule10 = ctrl.Rule(precipitacao_acumulada['baixa'] & salinidade['media'] & fluxo_rio['media'], salinidade_final['media_baixa'])
rule11 = ctrl.Rule(precipitacao_acumulada['baixa'] & salinidade['baixa'] & fluxo_rio['baixa'], salinidade_final['baixa'])
rule12 = ctrl.Rule(precipitacao_acumulada['media'] & salinidade['media'] & fluxo_rio['baixa'], salinidade_final['media_baixa'])
rule13 = ctrl.Rule(precipitacao_acumulada['media'] & salinidade['media_baixa'] & fluxo_rio['baixa'], salinidade_final['media_baixa'])
rule14 = ctrl.Rule(precipitacao_acumulada['media'] & salinidade['media'] & fluxo_rio['media'], salinidade_final['media_baixa'])
rule15 = ctrl.Rule(precipitacao_acumulada['media'] & salinidade['media'] & fluxo_rio['media_alta'], salinidade_final['media_baixa'])
rule16 = ctrl.Rule(precipitacao_acumulada['media'] & salinidade['media_baixa']& fluxo_rio['media'], salinidade_final['baixa'])
rule17 = ctrl.Rule(precipitacao_acumulada['media'] & salinidade['alta'] & fluxo_rio['baixa'], salinidade_final['media'])
rule18 = ctrl.Rule(precipitacao_acumulada['media'] & salinidade['alta'] & fluxo_rio['media'], salinidade_final['media_baixa'])
rule19 = ctrl.Rule(precipitacao_acumulada['media'] & salinidade['alta'] & fluxo_rio['media_alta'], salinidade_final['baixa'])
rule20 = ctrl.Rule(precipitacao_acumulada['media'] & salinidade['baixa'] & fluxo_rio['media'], salinidade_final['baixa'])
rule21 = ctrl.Rule(precipitacao_acumulada['media'] & salinidade['baixa'] & fluxo_rio['baixa'], salinidade_final['baixa'])
rule22 = ctrl.Rule(precipitacao_acumulada['media_alta'] & salinidade['media'] & fluxo_rio['baixa'], salinidade_final['media_baixa'])
rule23 = ctrl.Rule(precipitacao_acumulada['media_alta'] & salinidade['media_baixa'] & fluxo_rio['baixa'], salinidade_final['media_baixa'])
rule24 = ctrl.Rule( precipitacao_acumulada['alta'] & salinidade['media'] & fluxo_rio['baixa'], salinidade_final['media_baixa'])
rule25 = ctrl.Rule(precipitacao_acumulada['alta'] & salinidade['media_baixa'] & fluxo_rio['baixa'], salinidade_final['baixa'])
rule26 = ctrl.Rule(precipitacao_acumulada['muito_alta'] & salinidade['media'] & fluxo_rio['baixa'], salinidade_final['muito_baixa'])
rule27 = ctrl.Rule(precipitacao_acumulada['muito_alta'] & salinidade['media_baixa'] & fluxo_rio['baixa'], salinidade_final['muito_baixa'])
rule28 = ctrl.Rule(precipitacao_acumulada['muito_alta'] & salinidade['baixa'] & fluxo_rio['baixa'], salinidade_final['muito_baixa'])

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
salinidade_final_simulador.input['precipitacao_acumulada'] = 23
salinidade_final_simulador.input['salinidade'] = 23
salinidade_final_simulador.input['fluxo_rio'] = 1454

# Computando o resultado
salinidade_final_simulador.compute()
print(salinidade_final_simulador.output['salinidade_final'])

precipitacao_acumulada.view(sim=salinidade_final_simulador)
salinidade.view(sim=salinidade_final_simulador)
fluxo_rio.view(sim=salinidade_final_simulador)
salinidade_final.view(sim=salinidade_final_simulador)

plt.show()
