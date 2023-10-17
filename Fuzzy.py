import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tkinter as tk
from tkinter import Label, Entry, Button
import matplotlib.pyplot as plt


# Map the numerical output to linguistic terms
def map_desgaste(resultado_desgaste):
    if resultado_desgaste <= 1:
        return "NENHUM"
    elif 1 < resultado_desgaste <= 40:
        return "POUCO"
    elif 40 < resultado_desgaste <= 70:
        return "MODERADO"
    else:
        return "MUITO"


# Função para calcular o desgaste
def calcular_desgaste():
    quilometro = int(entrada_quilometro.get())
    tempo = int(entrada_tempo.get())
    nivel = get_selected_nivel()

    desgaste_simulador.input["QUILOMETRAGEM RODADO"] = quilometro
    desgaste_simulador.input["TEMPO DE TROCADO"] = tempo
    desgaste_simulador.input["NIVEL DO OLEO"] = nivel
    desgaste_simulador.compute()

    resultado_desgaste = desgaste_simulador.output["DESGASTE"]
    resultado_texto = map_desgaste(resultado_desgaste)
    resultado_label.config(text=f"O grau de desgaste do motor é {resultado_texto}")


# Cria uma instância da janela
janela = tk.Tk()
janela.title("EngineDoctor")

# Variáveis Linguísticas
quilometragemRodado = ctrl.Antecedent(np.arange(0, 5001, 1), "QUILOMETRAGEM RODADO")
tempoTrocado = ctrl.Antecedent(np.arange(0, 366, 1), "TEMPO DE TROCADO")
nivelOleo = ctrl.Antecedent(np.arange(0, 3, 1), "NIVEL DO OLEO")
desgaste = ctrl.Consequent(np.arange(0, 101, 1), "DESGASTE")

# Conjuntos de Termos Linguísticos (membership function tipo trapezoidal e triangular)
quilometragemRodado["NENHUM"] = fuzz.trapmf(quilometragemRodado.universe, [0, 0, 0, 0])
quilometragemRodado["POUCO"] = fuzz.trapmf(
    quilometragemRodado.universe, [1, 1, 1000, 1500]
)
quilometragemRodado["MEDIO"] = fuzz.trapmf(
    quilometragemRodado.universe, [1000, 1500, 3000, 3500]
)
quilometragemRodado["MUITO"] = fuzz.trapmf(
    quilometragemRodado.universe, [3000, 4000, 5000, 5000]
)

tempoTrocado["POUCO"] = fuzz.trapmf(tempoTrocado.universe, [0, 0, 150, 165])
tempoTrocado["MEDIO"] = fuzz.trapmf(tempoTrocado.universe, [150, 165, 250, 265])
tempoTrocado["MUITO"] = fuzz.trapmf(tempoTrocado.universe, [250, 265, 365, 365])

nivelOleo["ABAIXO"] = fuzz.trimf(nivelOleo.universe, [0, 0, 0])
nivelOleo["MEDIDA"] = fuzz.trimf(nivelOleo.universe, [1, 1, 1])
nivelOleo["ACIMA"] = fuzz.trimf(nivelOleo.universe, [2, 2, 2])

desgaste["NENHUM"] = fuzz.trapmf(desgaste.universe, [0, 0, 0, 0])
desgaste["POUCO"] = fuzz.trapmf(desgaste.universe, [1, 1, 30, 40])
desgaste["MODERADO"] = fuzz.trapmf(desgaste.universe, [30, 40, 60, 70])
desgaste["MUITO"] = fuzz.trapmf(desgaste.universe, [60, 70, 100, 100])

rule1 = ctrl.Rule(
    quilometragemRodado["NENHUM"] & tempoTrocado["POUCO"] & nivelOleo["MEDIDA"],
    desgaste["NENHUM"],
)
rule2 = ctrl.Rule(
    quilometragemRodado["NENHUM"] & tempoTrocado["POUCO"] & nivelOleo["ABAIXO"],
    desgaste["POUCO"],
)
rule3 = ctrl.Rule(
    quilometragemRodado["NENHUM"] & tempoTrocado["POUCO"] & nivelOleo["ACIMA"],
    desgaste["POUCO"],
)
rule4 = ctrl.Rule(
    quilometragemRodado["NENHUM"] & tempoTrocado["MEDIO"] & nivelOleo["MEDIDA"],
    desgaste["NENHUM"],
)
rule5 = ctrl.Rule(
    quilometragemRodado["NENHUM"] & tempoTrocado["MEDIO"] & nivelOleo["ABAIXO"],
    desgaste["MODERADO"],
)
rule6 = ctrl.Rule(
    quilometragemRodado["NENHUM"] & tempoTrocado["MEDIO"] & nivelOleo["ACIMA"],
    desgaste["MODERADO"],
)
rule7 = ctrl.Rule(
    quilometragemRodado["NENHUM"] & tempoTrocado["MUITO"] & nivelOleo["MEDIDA"],
    desgaste["POUCO"],
)
rule8 = ctrl.Rule(
    quilometragemRodado["NENHUM"] & tempoTrocado["MUITO"] & nivelOleo["ABAIXO"],
    desgaste["MUITO"],
)
rule9 = ctrl.Rule(
    quilometragemRodado["NENHUM"] & tempoTrocado["MUITO"] & nivelOleo["ACIMA"],
    desgaste["MUITO"],
)

rule10 = ctrl.Rule(
    quilometragemRodado["POUCO"] & tempoTrocado["POUCO"] & nivelOleo["MEDIDA"],
    desgaste["POUCO"],
)
rule11 = ctrl.Rule(
    quilometragemRodado["POUCO"] & tempoTrocado["POUCO"] & nivelOleo["ABAIXO"],
    desgaste["MODERADO"],
)
rule12 = ctrl.Rule(
    quilometragemRodado["POUCO"] & tempoTrocado["POUCO"] & nivelOleo["ACIMA"],
    desgaste["MODERADO"],
)
rule13 = ctrl.Rule(
    quilometragemRodado["POUCO"] & tempoTrocado["MEDIO"] & nivelOleo["MEDIDA"],
    desgaste["MODERADO"],
)
rule14 = ctrl.Rule(
    quilometragemRodado["POUCO"] & tempoTrocado["MEDIO"] & nivelOleo["ABAIXO"],
    desgaste["MODERADO"],
)
rule15 = ctrl.Rule(
    quilometragemRodado["POUCO"] & tempoTrocado["MEDIO"] & nivelOleo["ACIMA"],
    desgaste["MODERADO"],
)
rule16 = ctrl.Rule(
    quilometragemRodado["POUCO"] & tempoTrocado["MUITO"] & nivelOleo["MEDIDA"],
    desgaste["MODERADO"],
)
rule17 = ctrl.Rule(
    quilometragemRodado["POUCO"] & tempoTrocado["MUITO"] & nivelOleo["ABAIXO"],
    desgaste["MUITO"],
)
rule18 = ctrl.Rule(
    quilometragemRodado["POUCO"] & tempoTrocado["MUITO"] & nivelOleo["ACIMA"],
    desgaste["MUITO"],
)

rule19 = ctrl.Rule(
    quilometragemRodado["MEDIO"] & tempoTrocado["POUCO"] & nivelOleo["MEDIDA"],
    desgaste["MODERADO"],
)
rule20 = ctrl.Rule(
    quilometragemRodado["MEDIO"] & tempoTrocado["POUCO"] & nivelOleo["ABAIXO"],
    desgaste["MUITO"],
)
rule21 = ctrl.Rule(
    quilometragemRodado["MEDIO"] & tempoTrocado["POUCO"] & nivelOleo["ACIMA"],
    desgaste["MUITO"],
)
rule22 = ctrl.Rule(
    quilometragemRodado["MEDIO"] & tempoTrocado["MEDIO"] & nivelOleo["MEDIDA"],
    desgaste["MODERADO"],
)
rule23 = ctrl.Rule(
    quilometragemRodado["MEDIO"] & tempoTrocado["MEDIO"] & nivelOleo["ABAIXO"],
    desgaste["MUITO"],
)
rule24 = ctrl.Rule(
    quilometragemRodado["MEDIO"] & tempoTrocado["MEDIO"] & nivelOleo["ACIMA"],
    desgaste["MUITO"],
)
rule25 = ctrl.Rule(
    quilometragemRodado["MEDIO"] & tempoTrocado["MUITO"] & nivelOleo["MEDIDA"],
    desgaste["MUITO"],
)
rule26 = ctrl.Rule(
    quilometragemRodado["MEDIO"] & tempoTrocado["MUITO"] & nivelOleo["ABAIXO"],
    desgaste["MUITO"],
)
rule27 = ctrl.Rule(
    quilometragemRodado["MEDIO"] & tempoTrocado["MUITO"] & nivelOleo["ACIMA"],
    desgaste["MUITO"],
)

rule28 = ctrl.Rule(
    quilometragemRodado["MUITO"] & tempoTrocado["POUCO"] & nivelOleo["MEDIDA"],
    desgaste["MUITO"],
)
rule29 = ctrl.Rule(
    quilometragemRodado["MUITO"] & tempoTrocado["POUCO"] & nivelOleo["ABAIXO"],
    desgaste["MUITO"],
)
rule30 = ctrl.Rule(
    quilometragemRodado["MUITO"] & tempoTrocado["POUCO"] & nivelOleo["ACIMA"],
    desgaste["MUITO"],
)
rule31 = ctrl.Rule(
    quilometragemRodado["MUITO"] & tempoTrocado["MEDIO"] & nivelOleo["MEDIDA"],
    desgaste["MUITO"],
)
rule32 = ctrl.Rule(
    quilometragemRodado["MUITO"] & tempoTrocado["MEDIO"] & nivelOleo["ABAIXO"],
    desgaste["MUITO"],
)
rule33 = ctrl.Rule(
    quilometragemRodado["MUITO"] & tempoTrocado["MEDIO"] & nivelOleo["ACIMA"],
    desgaste["MUITO"],
)
rule34 = ctrl.Rule(
    quilometragemRodado["MUITO"] & tempoTrocado["MUITO"] & nivelOleo["MEDIDA"],
    desgaste["MUITO"],
)
rule35 = ctrl.Rule(
    quilometragemRodado["MUITO"] & tempoTrocado["MUITO"] & nivelOleo["ABAIXO"],
    desgaste["MUITO"],
)
rule36 = ctrl.Rule(
    quilometragemRodado["MUITO"] & tempoTrocado["MUITO"] & nivelOleo["ACIMA"],
    desgaste["MUITO"],
)

# Criação do Controlador Nebuloso e Simulação
desgaste_ctrl = ctrl.ControlSystem(
    [
        rule1,
        rule2,
        rule3,
        rule4,
        rule5,
        rule6,
        rule7,
        rule8,
        rule9,
        rule10,
        rule11,
        rule12,
        rule13,
        rule14,
        rule15,
        rule16,
        rule17,
        rule18,
        rule19,
        rule20,
        rule21,
        rule22,
        rule23,
        rule24,
        rule25,
        rule26,
        rule27,
        rule28,
        rule29,
        rule30,
        rule31,
        rule32,
        rule33,
        rule34,
        rule35,
        rule36,
    ]
)
desgaste_simulador = ctrl.ControlSystemSimulation(desgaste_ctrl)


# Plot do gráfico
def exibir_grafico():
    quilometragemRodado.view(sim=desgaste_simulador)
    tempoTrocado.view(sim=desgaste_simulador)
    nivelOleo.view(sim=desgaste_simulador)
    desgaste.view(sim=desgaste_simulador)
    plt.show()


# Cria um frame para organizar os widgets
frame = tk.Frame(janela)
frame.pack(padx=50, pady=50)

# Label para o título
titulo_label = tk.Label(
    frame,
    text="EngineDoctor - Diagnóstico de Desgaste do Motor",
    font=("Helvetica", 20),
    fg="#1473e6",
)
titulo_label.pack(side="top", padx=50, pady=50)

# Label e entrada para Quilometragem
quilometragem_label = tk.Label(
    frame,
    text="Quilometragem rodada com o óleo",
    font=("Helvetica", 14),
)
quilometragem_label.pack(pady=5)
entrada_quilometro = tk.Entry(frame)
entrada_quilometro.pack(pady=5)

# Label e entrada para Tempo
tempo_label = tk.Label(frame, text="Dias de uso do óleo", font=("Helvetica", 14))
tempo_label.pack(pady=5)
entrada_tempo = tk.Entry(frame)
entrada_tempo.pack(pady=5)

# Label Nível do Óleo
nivel_label = tk.Label(frame, text="Nível do óleo", font=("Helvetica", 14))
nivel_label.pack(pady=5)

# Create a variable to store the selected oil level
selected_nivel = tk.StringVar()
selected_nivel.set("medida ok")  # Set the default option to "medida ok"

# Create an OptionMenu with options and map them to numeric values
nivel_options = tk.OptionMenu(frame, selected_nivel, "abaixo", "medida ok", "acima")
nivel_options.pack(pady=5)


# Function to convert the selected option to a numeric value
def get_selected_nivel():
    nivel_mapping = {"abaixo": 0, "medida ok": 1, "acima": 2}
    return nivel_mapping[selected_nivel.get()]


# Botão para calcular o desgaste
calcular_botao = tk.Button(
    frame, text="Calcular Desgaste", command=calcular_desgaste, bg="#1473e6", fg="white"
)
calcular_botao.pack(pady=30)

# Botão para exibir o gráfico
exibir_grafico_botao = tk.Button(
    frame, text="Exibir Gráfico", command=exibir_grafico, bg="#1473e6", fg="white"
)
exibir_grafico_botao.pack(pady=15)

# Label para exibir o resultado
resultado_label = tk.Label(frame, text="", font=("Helvetica", 16), fg="red")
resultado_label.pack(pady=10)

# Inicia o loop principal da interface
janela.mainloop()
