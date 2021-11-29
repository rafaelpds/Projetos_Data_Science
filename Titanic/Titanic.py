# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:55:32 2019

@author: OI400241
"""

import pandas as pd
import numpy as np

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

train.head()
train.columns

from sklearn.ensemble import RandomForestClassifier

modelo = RandomForestClassifier(n_estimators= 1000, n_jobs = -1, random_state = 0)

#1º Modelo Utilizar os campos de Age e Sexo
variaveis = ['Sex_binario', 'Age']

train['Sex'].value_counts()

#Avaliar o campo Sexo

train['Sex'].head()
def transformar_sexo(valor):
    if valor == 'female':
        return 1
    else:
        return 0
    
train['Sex_binario'] = train['Sex'].map(transformar_sexo)
test['Sex_binario'] = test['Sex'].map(transformar_sexo)

train['Sex_binario'].head()

#Criando o X e Y
x = train[variaveis]
y = train['Survived']

x.head()
y.head()

x = x.fillna(-1)

modelo.fit(x,y)

#Criando o modelo de teste
x_prev = test[variaveis]
x_prev.head()

x_prev = x_prev.fillna(-1)

p = modelo.predict(x_prev)
p

###################
#Criar a validação
###################

from sklearn.model_selection import train_test_split

?train_test_split

x_falso = np.arange(10)
x_falso

#Colocar o seed igual a para poder trazer o mesmo resultado
np.random.seed(0)
x_treino, x_valid, y_treino, y_valid = train_test_split(x, y, test_size = 0.5)
x_treino.shape, x_valid.shape, y_treino.shape, y_valid.shape
x_valid

modelo.fit(x_treino, y_treino)
p = modelo.predict(x_valid)

np.mean(y_valid == p)

#Considerando que todas as mulheres sobrevivam

p = (x_valid['Sex_binario'] == 1).astype(np.int64)
p

np.mean(y_valid == p)

y_valid

##Validação Cruzada - Modelo melhor do que o anterior

#Criar o submission
test.head()

sub = pd.Series(p, index = test['PassengerId'], name = 'Survived')
sub.shape

sub.to_csv("answer.csv", header = True)

