#PassengerId - Id do Passageiro
#Survived - Sobreviventes - (Chave Principal)
#Pclass - Classe que o passageiro utilizou (1ª, 2ª ou 3ª classe)
#Name - Nome do passageiro (Não manter, pois temos o campo sexo que já pode responder se homem ou mulher)
#Sex - Sexo do passageiro
#Age - Idade do passageiro
#SibSp - Quantidade de irmãos e cônjuges a bordo - 
#Parch - Quantidade de pais e filhos a bordo
#Ticket - Número da passagem
#Fare - Preço da passagem
#Cabin - Número da cabine do passageiro
#Embarked - Indica o porto no qaul o passageiro embarcou. Há apenas três valores possíveis: 
#           Cherbourg, Queenstown e Southampton, indicados pelas letras "C", "Q" e "S"

#Check directory

getwd()

#Mudar o diretório

setwd('C:/Users/oi400241/Desktop/Rafael/Curso Coti/01.R/04 - Bases/')

getwd()

#Listar os arquivos dentro do caminho especificado

list.files()

#Listar as pastas

list.files("..")

#1 - Carregar o arquivo "train" como CSV

titanic_train <- read.csv("train.csv")
head(t1)

#1.1 - Carregar o arquivo Gender Submission 

gender_sub <- read.csv("gender_submission.csv")
head(gender_sub)

#1.2 - Carregar test 

titanic_test <- read.csv("test.csv", stringsAsFactors = TRUE)
head(titanic_test)

#Checar os arquivos importados

summary(titanic_train)

str(titanic_train)

#2 - Desenvolvendo o script

#Antes de realizar a comparação entre os arquivos é necessário verificar se ambos
#possuem as mesmas informações de nome das colunas

names(titanic_train)
names(titanic_test)

#Criar a coluna para ficar igual ao titanic.train

titanic_test$Survived = N/A

#2- Instalar o Pacote

install.packages("e1071", dependencies = T)

library(e1071)

titanic_train$Survived = factor(titanic_train$Survived)
titanic_train$Pclass = factor(titanic_train$Pclass)
titanic_train$Sex = factor(titanic_train$Sex)
titanic_train$Embarked = factor(titanic_train$Embarked)

titanic_test$Survived = factor(titanic_test$Survived)
titanic_test$Pclass = factor(titanic_test$Pclass)
titanic_test$Sex = factor(titanic_test$Sex)
titanic_test$Embarked = factor(titanic_test$Embarked)

# Criação do modelo de treinamento
# Naive Bayes -> Tabela de probabibilidade

modelo <-  naiveBayes(Survived ~ .,titanic_train)
modelo

# Validação -> predict, no conjunto de de teste.
# Efetua a predição dos dados de teste.

previsoes = as.data.frame(predict(modelo, newdata=titanic_test))
previsoes

titanic_test$Survived <- previsoes

colnames(previsoes) = c("Survived")

PassengerId = titanic_test[,'PassengerId']

PassengerIdPred = cbind(PassengerId,previsoes)

# Tabela de confusão
confusao <- table(titanic_test$Survived, previsoes)
confusao

write.csv(PassengerIdPred, file = 'resultado_ticanic.csv', row.names = FALSE, quote=FALSE)
