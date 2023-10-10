from tkinter import *
import KNN as a
from tkinter import messagebox

def diagnosticar():
    if a.Treinar(radio_preocupado.get(), radio_Pensamentos_intrusivos.get(), radio_Tensao_muscular.get(), radio_motivos_preocupa.get(), 
        radio_medo_ou_panico.get(), radio_evita_situacoes_publicas.get(), box_Idade.get(), radio_tremores_ou_suor.get(), 
        radio_dificuldade_de_dormi.get()) == 1:
        messagebox.showwarning(title="Resultado do diagnóstico",
        message='Você possui ansiedade e tem risco de depressão')     
    else:
       messagebox.showinfo(title="Resultado do diagnóstico",
        message='Você não possui risco de depressão')
            
janela = Tk()

radio_preocupado = IntVar()
radio_Pensamentos_intrusivos = IntVar()
radio_Tensao_muscular = IntVar()
radio_motivos_preocupa = IntVar()
radio_medo_ou_panico = IntVar()
radio_evita_situacoes_publicas = IntVar()
box_Idade = IntVar()
radio_tremores_ou_suor = IntVar()
radio_dificuldade_de_dormi = IntVar()

janela.title("DR.MCMISSIL DIAGNOSTICANDO SUA ANSIEDADE")
largura = 1100
altura = 750
pos_x = (janela.winfo_screenwidth() // 2) - (largura // 2) 
pos_y = (janela.winfo_screenheight() // 2) - (altura // 2) 
janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}") 

def on_canvas_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

janela.title("DR.MCMISSIL DIAGNOSTICANDO SUA ANSIEDADE")

frame_prin = Frame(janela, bg="#9DBCD4")
frame_prin.pack(fill="both", expand=True)

canvas = Canvas(frame_prin, bg="#C0C0C0")
canvas.pack(side="left", fill="both", expand=True)

scrollbar = Scrollbar(frame_prin, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

frame_intern = Frame(canvas, bg="#C0C0C0")
canvas.create_window((0, 0), window=frame_intern, anchor="nw")

titulo1 = Label(frame_intern, 
                text="DR.MCMISSIL DIAGNOSTICANDO SUA ANSIEDADE",
                font=("Roboto", 23, "bold"),
                fg='blue',
                bg="#C0C0C0",
                )
titulo1.grid(column=0, row=0, columnspan=2, pady=(50, 50), padx=(200, 50), sticky="w") 

perguntas_respostas = [
    ("Você costuma se sentir excessivamente preocupado com coisas cotidianas?", radio_preocupado),
    ("Você experimenta pensamentos intrusivos ou preocupações recorrentes que são difíceis de controlar?", radio_Pensamentos_intrusivos),
    ("Você sente tensão muscular frequente, como aperto no peito ou dor de cabeça?", radio_Tensao_muscular),
    ("Você tem dificuldade em relaxar, mesmo quando não há motivo aparente para se preocupar?", radio_motivos_preocupa),
    ("Você sente medo intenso ou ataques de pânico súbitos?", radio_medo_ou_panico),
    ("Você evita situações sociais, públicas ou específicas devido ao medo ou ansiedade?", radio_evita_situacoes_publicas),
    ("Você experimenta tremores, suor excessivo ou palpitações cardíacas em momentos de ansiedade?", radio_tremores_ou_suor),
    ("Você tem dificuldade em dormir devido a pensamentos ansiosos?", radio_dificuldade_de_dormi),
    ("Idade:", box_Idade)
]

coluna = 0
linha = 1
largura_maxima_coluna = 800

for pergunta, variavel in perguntas_respostas:
    label_pergunta = Label(frame_intern, text=pergunta, font=("Roboto", 13, "bold"), bg="white", anchor="w")
    label_pergunta.grid(column=0, row=linha, padx=(20, 5), pady=10, sticky="e")
    
    if pergunta == "Idade:":
        label_idade = Label(frame_intern, font=("Roboto", 13, "bold"), bg="#C0C0C0", anchor="w")
        label_idade.grid(column=coluna, row=linha+1, padx=20, pady=(0, 5), sticky="w")
        
        entrada_idade = Entry(frame_intern, textvariable=box_Idade, font=("Roboto", 13, "bold"))
        entrada_idade.grid(column=coluna+1, row=linha, padx=20, pady=(0, 10))
    
    else:
        radio_sim = Radiobutton(frame_intern, text="Sim", variable=variavel, value=1, font=("Roboto", 13, "bold"), bg="green")
        radio_sim.grid(column=1, row=linha, padx=(10, 0), pady=10, sticky="w")
        
        radio_nao = Radiobutton(frame_intern, text="Não", variable=variavel, value=0, font=("Roboto", 13, "bold"), bg="red")
        radio_nao.grid(column=1, row=linha, padx=(80, 0), pady=10, sticky="w")  # Ajuste o padx aqui
    

    coluna += 2
    
    if coluna * 800 >= largura_maxima_coluna:
        coluna = 0
        linha += 3
        
botaoDiagnostico = Button(frame_intern,
                          text='Realizar Diagnóstico',
                          fg='white',
                          bg='blue',
                          command=diagnosticar,
                          font=("Roboto", 13, "bold"),
                          relief="ridge",
                          border=2,
                          )
botaoDiagnostico.grid(column=0, row=linha, columnspan=3, pady=20, padx=20)

buttonClose = Button(frame_intern,
                     text='Fechar',
                     fg='white',
                     bg='Red',
                     command=janela.quit,
                     font=("Roboto", 13, "bold"),
                     relief="ridge",
                     border=2,
                     )
buttonClose.grid(column=0, row=linha+1, columnspan=3, pady=20,padx=20)

canvas.bind("<Configure>", on_canvas_configure)

janela.mainloop()
