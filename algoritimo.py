import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

# importando a base de dados atraves do gitHub
url = 'https://raw.githubusercontent.com/NagibeJR/I.A_PROJECT_2.0/main/Registro_de_ansiedade.csv'
base_Treinamento = pd.read_csv(url,sep=',', encoding = 'utf-8').values

#normalizando os dados
min_max = preprocessing.MinMaxScaler()
#normalizando os dados
def normalizarDados(base_Treinamento):
    return min_max.fit_transform(base_Treinamento[:,:9])

#treinando a rede Knn
def treinarRedeKNN(atributos_norm,diagnostico_norm):
    modelo = KNeighborsClassifier(n_neighbors = 7)
    modelo.fit(atributos_norm, diagnostico_norm)
    return modelo

def Treinar(Preocupado,Pensamentos_intrusivos,Tensao_muscular,motivos_preocupa,medo_ou_panico,evita_situacoes_publicas,Idade,tremores_ou_suor,dificuldade_de_dormi):
    dadosT = normalizarDados(base_Treinamento)
    diagnostico_norm = base_Treinamento[:, 9]
    modelo = treinarRedeKNN(dadosT,diagnostico_norm)
    
    teste = [[Preocupado,Pensamentos_intrusivos,Tensao_muscular,motivos_preocupa,medo_ou_panico,evita_situacoes_publicas,Idade,tremores_ou_suor,dificuldade_de_dormi]]
    testeT = min_max.transform(teste)
    return modelo.predict(testeT)
