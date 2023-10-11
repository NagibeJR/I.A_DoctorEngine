import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

# importando a base de dados
url = 'https://raw.githubusercontent.com/NagibeJR/I.A_PROJECT_2.0/main/Registro_de_ansiedade.csv'
baseDados = pd.read_csv(url,sep=',', encoding = 'utf-8').values

escala = preprocessing.MinMaxScaler()
#normalizando os dados
def normalizar(base):
    return escala.fit_transform(base[:,:9])

#treinando a rede Knn
def treinarKNN(atributos,diagnostico):
    modelo = KNeighborsClassifier(n_neighbors = 7) # K = 7
    modelo.fit(atributos, diagnostico)
    return modelo

def Treinar(Preocupado,Pensamentos_intrusivos,Tensao_muscular,motivos_preocupa,medo_ou_panico,evita_situacoes_publicas,Idade,tremores_ou_suor,dificuldade_de_dormi):
    dado = normalizar(baseDados)
    diagnostico = baseDados[:, 9]
    modelo = treinarKNN(dado,diagnostico)
    
    temp = [[Preocupado,Pensamentos_intrusivos,Tensao_muscular,motivos_preocupa,medo_ou_panico,evita_situacoes_publicas,Idade,tremores_ou_suor,dificuldade_de_dormi]]
    teste = escala.transform(temp)
    return modelo.predict(teste)
