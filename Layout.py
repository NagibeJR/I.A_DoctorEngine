from tkinter import *
import KNN as a
from tkinter import messagebox

def diagnosticar():
    if a.Treinar(preocupado.get(), pensamentosIntrusivos.get(), tensaoMuscular.get(), motivosPreocupa.get(), 
        medoPanico.get(), evitaSituacoesPublicas.get(), idade.get(), tremoresSuor.get(), 
        dificuldadeDormi.get()) == 1:
        messagebox.showwarning(title="Resultado do diagnóstico",
        message='Você possui ansiedade e tem risco de depressão')     
    else:
       messagebox.showinfo(title="Resultado do diagnóstico",
        message='Você não possui risco de depressão')
            
window = Tk()
preocupado = IntVar()
pensamentosIntrusivos = IntVar()
tensaoMuscular = IntVar()
motivosPreocupa = IntVar()
medoPanico = IntVar()
evitaSituacoesPublicas = IntVar()
idade = IntVar()
tremoresSuor = IntVar()
dificuldadeDormi = IntVar()

window.title("DR.MCMISSIL DIAGNOSTICANDO SUA ANSIEDADE")
width = 1100
height = 870
pos_x = (window.winfo_screenwidth() // 2) - (width // 2) 
pos_y = (window.winfo_screenheight() // 2) - (height // 2) 
window.geometry(f"{width}x{height}+{pos_x}+{pos_y}") 

def on_canvas_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

window.title("DR.MCMISSIL DIAGNOSTICANDO SUA ANSIEDADE")

frame_prin = Frame(window, bg="#9DBCD4")
frame_prin.pack(fill="both", expand=True)

canvas = Canvas(frame_prin, bg="#C0C0C0")
canvas.pack(side="left", fill="both", expand=True)

scrollbar = Scrollbar(frame_prin, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

frame_intern = Frame(canvas, bg="lavender")
canvas.create_window((0, 0), window=frame_intern, anchor="nw")

titulo1 = Label(frame_intern, 
                text="DR.MCMISSIL DIAGNOSTICANDO SUA ANSIEDADE",
                font=("Roboto", 23, "bold"),
                fg='blue',
                bg="#C0C0C0",
                border=20,
                )
titulo1.grid(column=0, row=0, columnspan=2, pady=(50, 50), padx=(200, 50), sticky="w") 

perguntas_respostas = [
    ("Você costuma se sentir excessivamente preocupado com coisas cotidianas?", preocupado),
    ("Você experimenta pensamentos intrusivos ou preocupações recorrentes que são difíceis de controlar?", pensamentosIntrusivos),
    ("Você sente tensão muscular frequente, como aperto no peito ou dor de cabeça?", tensaoMuscular),
    ("Você tem dificuldade em relaxar, mesmo quando não há motivo aparente para se preocupar?", motivosPreocupa),
    ("Você sente medo intenso ou ataques de pânico súbitos?", medoPanico),
    ("Você evita situações sociais, públicas ou específicas devido ao medo ou ansiedade?", evitaSituacoesPublicas),
    ("Você experimenta tremores, suor excessivo ou palpitações cardíacas em momentos de ansiedade?", tremoresSuor),
    ("Você tem dificuldade em dormir devido a pensamentos ansiosos?", dificuldadeDormi),
    ("Idade:", idade)
]

column = 0
line = 1
maximum_column_width = 800

for pergunta, variavel in perguntas_respostas:
    label_pergunta = Label(frame_intern, text=pergunta, font=("Roboto", 13, "bold"), bg="yellow", anchor="w")
    label_pergunta.grid(column=0, row=line, padx=(20, 5), pady=10, sticky="e")
    
    if pergunta == "Idade:":
        label_idade = Label(frame_intern, font=("Roboto", 13, "bold"), bg="#C0C0C0", anchor="w")
        label_idade.grid(column=column, row=line+1, padx=20, pady=(0, 5), sticky="w")
        
        entrada_idade = Entry(frame_intern, textvariable=idade, font=("Roboto", 13, "bold"))
        entrada_idade.grid(column=column+1, row=line, padx=20, pady=(0, 10))
    
    else:
        sim = Radiobutton(frame_intern, text="Sim", variable=variavel, value=1, font=("Roboto", 13, "bold"), bg="lightblue")
        sim.grid(column=1, row=line, padx=(10, 0), pady=10, sticky="w")
        
        nao = Radiobutton(frame_intern, text="Não", variable=variavel, value=0, font=("Roboto", 13, "bold"), bg="lightgray")
        nao.grid(column=1, row=line, padx=(80, 0), pady=10, sticky="w")

    column += 2
    
    if column * 800 >= maximum_column_width:
        column = 0
        line += 3
        
buttonDiagnostico = Button(frame_intern,
                          text='Realizar Diagnóstico',
                          fg='white',
                          bg='blue',
                          command=diagnosticar,
                          font=("Roboto", 13, "bold"),
                          relief="ridge",
                          border=20,  # Increase the border width for a more rounded appearance
                          )
buttonDiagnostico.grid(column=0, row=line, columnspan=3, pady=20, padx=20)

buttonClose = Button(frame_intern,
                     text='Fechar',
                     fg='white',
                     bg='lightsalmon',
                     command=window.quit,
                     font=("Roboto", 13, "bold"),
                     relief="ridge",
                     border=20,
                     )
buttonClose.grid(column=0, row=line+1, columnspan=3, pady=20,padx=20)

canvas.bind("<Configure>", on_canvas_configure)

window.mainloop()
