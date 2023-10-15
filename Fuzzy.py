import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


quilometro = int(input('Digite a quilometragem rodada com o oleo [0..5.000]: '))
tempo = int(input('Digite quantos dias esta usando o oleo [0..365 dias]: '))
nivel = int(input('Digite o nivel do oleo[0 = abaixo| 1 = medida oky| 2 = acima]: '))

# Variáveis Linguísticas
quilometragemRodado = ctrl.Antecedent(np.arange(0,5001,1), 'QUILOMETRAGEM RODADO')
tempoTrocado = ctrl.Antecedent(np.arange(0,366,1), 'TEMPO DE TROCADO')
nivelOleo = ctrl.Antecedent(np.arange(0,3,1), 'NIVEL DO OLEO')
desgaste = ctrl.Consequent(np.arange(0,101,1), 'DESGASTE')

# Conjuntos de Termos Linguísticos (membership function tipo trapezial e triangular)
quilometragemRodado['NENHUM'] = fuzz.trapmf(quilometragemRodado.universe, [0,0,0,0])
quilometragemRodado['POUCO'] = fuzz.trapmf(quilometragemRodado.universe, [1,1,1000,1500])
quilometragemRodado['MEDIO'] = fuzz.trapmf(quilometragemRodado.universe, [1000,1500,3000,3500])
quilometragemRodado['MUITO'] = fuzz.trapmf(quilometragemRodado.universe, [3000,4000,5000,5000])

tempoTrocado['POUCO'] = fuzz.trapmf(tempoTrocado.universe, [0,0,150,165])
tempoTrocado['MEDIO'] = fuzz.trapmf(tempoTrocado.universe, [150,165,250,265])
tempoTrocado['MUITO'] = fuzz.trapmf(tempoTrocado.universe, [250,265,365,365])

nivelOleo['ABAIXO'] = fuzz.trimf(nivelOleo.universe, [0,0,0])
nivelOleo['MEDIDA'] = fuzz.trimf(nivelOleo.universe, [1,1,1])
nivelOleo['ACIMA'] = fuzz.trimf(nivelOleo.universe, [2,2,2])

desgaste['NENHUM'] = fuzz.trapmf(desgaste.universe, [0,0,0,0])
desgaste['POUCO'] = fuzz.trapmf(desgaste.universe, [1,1,30,40])
desgaste['MODERADO'] = fuzz.trapmf(desgaste.universe, [30,40,60,70])
desgaste['MUITO'] = fuzz.trapmf(desgaste.universe, [60,70,100,100])

quilometragemRodado.view()
tempoTrocado.view()
nivelOleo.view()
desgaste.view()

# Criando a Base de Regras

rule1 = ctrl.Rule(quilometragemRodado['NENHUM'] & tempoTrocado['POUCO'] & nivelOleo['MEDIDA'], desgaste['NENHUM'])
rule2 = ctrl.Rule(quilometragemRodado['NENHUM'] & tempoTrocado['POUCO'] & nivelOleo['ABAIXO'], desgaste['POUCO'])
rule3 = ctrl.Rule(quilometragemRodado['NENHUM'] & tempoTrocado['POUCO'] & nivelOleo['ACIMA'], desgaste['POUCO'])
rule4 = ctrl.Rule(quilometragemRodado['NENHUM'] & tempoTrocado['MEDIO'] & nivelOleo['MEDIDA'], desgaste['NENHUM'])
rule5 = ctrl.Rule(quilometragemRodado['NENHUM'] & tempoTrocado['MEDIO'] & nivelOleo['ABAIXO'], desgaste['MODERADO'])
rule6 = ctrl.Rule(quilometragemRodado['NENHUM'] & tempoTrocado['MEDIO'] & nivelOleo['ACIMA'], desgaste['MODERADO'])
rule7 = ctrl.Rule(quilometragemRodado['NENHUM'] & tempoTrocado['MUITO'] & nivelOleo['MEDIDA'], desgaste['POUCO'])
rule8 = ctrl.Rule(quilometragemRodado['NENHUM'] & tempoTrocado['MUITO'] & nivelOleo['ABAIXO'], desgaste['MUITO'])
rule9 = ctrl.Rule(quilometragemRodado['NENHUM'] & tempoTrocado['MUITO'] & nivelOleo['ACIMA'], desgaste['MUITO'])

rule10 = ctrl.Rule(quilometragemRodado['POUCO'] & tempoTrocado['POUCO'] & nivelOleo['MEDIDA'], desgaste['POUCO'])
rule11 = ctrl.Rule(quilometragemRodado['POUCO'] & tempoTrocado['POUCO'] & nivelOleo['ABAIXO'], desgaste['MODERADO'])
rule12 = ctrl.Rule(quilometragemRodado['POUCO'] & tempoTrocado['POUCO'] & nivelOleo['ACIMA'], desgaste['MODERADO'])
rule13 = ctrl.Rule(quilometragemRodado['POUCO'] & tempoTrocado['MEDIO'] & nivelOleo['MEDIDA'], desgaste['MODERADO'])
rule14 = ctrl.Rule(quilometragemRodado['POUCO'] & tempoTrocado['MEDIO'] & nivelOleo['ABAIXO'], desgaste['MODERADO'])
rule15 = ctrl.Rule(quilometragemRodado['POUCO'] & tempoTrocado['MEDIO'] & nivelOleo['ACIMA'], desgaste['MODERADO'])
rule16 = ctrl.Rule(quilometragemRodado['POUCO'] & tempoTrocado['MUITO'] & nivelOleo['MEDIDA'], desgaste['MODERADO'])
rule17 = ctrl.Rule(quilometragemRodado['POUCO'] & tempoTrocado['MUITO'] & nivelOleo['ABAIXO'], desgaste['MUITO'])
rule18 = ctrl.Rule(quilometragemRodado['POUCO'] & tempoTrocado['MUITO'] & nivelOleo['ACIMA'], desgaste['MUITO'])

rule19 = ctrl.Rule(quilometragemRodado['MEDIO'] & tempoTrocado['POUCO'] & nivelOleo['MEDIDA'], desgaste['MODERADO'])
rule20 = ctrl.Rule(quilometragemRodado['MEDIO'] & tempoTrocado['POUCO'] & nivelOleo['ABAIXO'], desgaste['MUITO'])
rule21 = ctrl.Rule(quilometragemRodado['MEDIO'] & tempoTrocado['POUCO'] & nivelOleo['ACIMA'], desgaste['MUITO'])
rule22 = ctrl.Rule(quilometragemRodado['MEDIO'] & tempoTrocado['MEDIO'] & nivelOleo['MEDIDA'], desgaste['MODERADO'])
rule23 = ctrl.Rule(quilometragemRodado['MEDIO'] & tempoTrocado['MEDIO'] & nivelOleo['ABAIXO'], desgaste['MUITO'])
rule24 = ctrl.Rule(quilometragemRodado['MEDIO'] & tempoTrocado['MEDIO'] & nivelOleo['ACIMA'], desgaste['MUITO'])
rule25 = ctrl.Rule(quilometragemRodado['MEDIO'] & tempoTrocado['MUITO'] & nivelOleo['MEDIDA'], desgaste['MUITO'])
rule26 = ctrl.Rule(quilometragemRodado['MEDIO'] & tempoTrocado['MUITO'] & nivelOleo['ABAIXO'], desgaste['MUITO'])
rule27 = ctrl.Rule(quilometragemRodado['MEDIO'] & tempoTrocado['MUITO'] & nivelOleo['ACIMA'], desgaste['MUITO'])

rule28 = ctrl.Rule(quilometragemRodado['MUITO'] & tempoTrocado['POUCO'] & nivelOleo['MEDIDA'], desgaste['MUITO'])
rule29 = ctrl.Rule(quilometragemRodado['MUITO'] & tempoTrocado['POUCO'] & nivelOleo['ABAIXO'], desgaste['MUITO'])
rule30 = ctrl.Rule(quilometragemRodado['MUITO'] & tempoTrocado['POUCO'] & nivelOleo['ACIMA'], desgaste['MUITO'])
rule31 = ctrl.Rule(quilometragemRodado['MUITO'] & tempoTrocado['MEDIO'] & nivelOleo['MEDIDA'], desgaste['MUITO'])
rule32 = ctrl.Rule(quilometragemRodado['MUITO'] & tempoTrocado['MEDIO'] & nivelOleo['ABAIXO'], desgaste['MUITO'])
rule33 = ctrl.Rule(quilometragemRodado['MUITO'] & tempoTrocado['MEDIO'] & nivelOleo['ACIMA'], desgaste['MUITO'])
rule34 = ctrl.Rule(quilometragemRodado['MUITO'] & tempoTrocado['MUITO'] & nivelOleo['MEDIDA'], desgaste['MUITO'])
rule35 = ctrl.Rule(quilometragemRodado['MUITO'] & tempoTrocado['MUITO'] & nivelOleo['ABAIXO'], desgaste['MUITO'])
rule36 = ctrl.Rule(quilometragemRodado['MUITO'] & tempoTrocado['MUITO'] & nivelOleo['ACIMA'], desgaste['MUITO'])

# Criando o Controlador Nebuloso, definindo os Entradas e calculando o Resultado

desgaste_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27,rule28,rule29,rule30,rule31,rule32,rule33,rule34,rule35,rule36])
desgaste_simulador = ctrl.ControlSystemSimulation(desgaste_ctrl)


# Entrando com alguns valores para quilometragem, tempo de troca e nivel do oleo
desgaste_simulador.input['QUILOMETRAGEM RODADO'] = quilometro
desgaste_simulador.input['TEMPO DE TROCADO'] = tempo
desgaste_simulador.input['NIVEL DO OLEO'] = nivel

#Computando o resultado
desgaste_simulador.compute()

# Apresentando Graficamente o Resultado

quilometragemRodado.view(sim=desgaste_simulador)
tempoTrocado.view(sim=desgaste_simulador)
nivelOleo.view(sim=desgaste_simulador)
desgaste.view(sim=desgaste_simulador)
print("O grau de desgaste é de", desgaste_simulador.output['DESGASTE'], "%")