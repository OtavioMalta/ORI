import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import cross_val_predict

# Árvore de Decisão
print("Árvore de Decisão")

# Carregando o dataset
dataset = pd.read_csv(r"TP4/Tweets_Mg.csv", encoding='utf-8')

dataset.head()
dataset.count()
dataset[dataset.Classificacao == 'Neutro'].count()
dataset[dataset.Classificacao == 'Positivo'].count()
dataset[dataset.Classificacao == 'Negativo'].count()

# Extraindo tweets e classes
tweets = dataset['Text'].values
classes = dataset['Classificacao'].values

# TF
vectorizer = CountVectorizer(analyzer="word", ngram_range=(1,2))
freq_tweets = vectorizer.fit_transform(tweets)

# Algoritmo Decision Tree
modelo = DecisionTreeClassifier()
modelo.fit(freq_tweets, classes)

testes = [ 'O governo de Minas é uma tragédia, muito ruim', 'Estou muito feliz com o governo de Minas esse ano', 'O estado de Minas Gerais decretou calamidade financeira!!!', 'A segurança do estado está deixando a desejar', 'O governador de Minas é do Novo']

# Calcula a BoW
freq_testes = vectorizer.transform(testes)

# Faz a classificação com o modelo treinado
modelo.predict(freq_testes)
print(modelo.predict(freq_testes))

# Previsões
resultados = cross_val_predict(modelo, freq_tweets, classes, cv=10)

metrics.accuracy_score(classes, resultados)
print(metrics.classification_report(classes, resultados))
print(pd.crosstab(classes, resultados, rownames=['Real'], colnames=['Predito'], margins=True))
print("Acurácia:", metrics.accuracy_score(classes, resultados))

# Floresta Aleatória
print("Floresta Aleatória")

# Carregando o dataset
dataset = pd.read_csv(r"TP4/Tweets_Mg.csv", encoding='utf-8')

dataset.head()
dataset.count()
dataset[dataset.Classificacao == 'Neutro'].count()
dataset[dataset.Classificacao == 'Positivo'].count()
dataset[dataset.Classificacao == 'Negativo'].count()

# Extraindo tweets e classes
tweets = dataset['Text'].values
classes = dataset['Classificacao'].values

# TF
vectorizer = CountVectorizer(analyzer="word", ngram_range=(1,2))
freq_tweets = vectorizer.fit_transform(tweets)

# Algoritmo Random Forest
modelo = RandomForestClassifier()
modelo.fit(freq_tweets, classes)

testes = [ 'O governo de Minas é uma tragédia, muito ruim', 'Estou muito feliz com o governo de Minas esse ano', 'O estado de Minas Gerais decretou calamidade financeira!!!', 'A segurança do estado está deixando a desejar', 'O governador de Minas é do Novo']

# Calcula a BoW
freq_testes = vectorizer.transform(testes)

# Faz a classificação com o modelo treinado
modelo.predict(freq_testes)
print(modelo.predict(freq_testes))

# Previsões
resultados = cross_val_predict(modelo, freq_tweets, classes, cv=10)

metrics.accuracy_score(classes, resultados)
print(metrics.classification_report(classes, resultados))
print(pd.crosstab(classes, resultados, rownames=['Real'], colnames=['Predito'], margins=True))
print("Acurácia:", metrics.accuracy_score(classes, resultados))


# SVM
print("SVM")

# Carregando o dataset
dataset = pd.read_csv(r"TP4/Tweets_Mg.csv", encoding='utf-8')

dataset.head()
dataset.count()
dataset[dataset.Classificacao == 'Neutro'].count()
dataset[dataset.Classificacao == 'Positivo'].count()
dataset[dataset.Classificacao == 'Negativo'].count()

# Extraindo tweets e classes
tweets = dataset['Text'].values
classes = dataset['Classificacao'].values

# TF
vectorizer = CountVectorizer(analyzer="word", ngram_range=(1,2))
freq_tweets = vectorizer.fit_transform(tweets)

# Algoritmo Máquinas de Vetores de Suporte (SVM)
modelo = SVC()
modelo.fit(freq_tweets, classes)

testes = [ 'O governo de Minas é uma tragédia, muito ruim', 'Estou muito feliz com o governo de Minas esse ano', 'O estado de Minas Gerais decretou calamidade financeira!!!', 'A segurança do estado está deixando a desejar', 'O governador de Minas é do Novo']

# Calcula a BoW
freq_testes = vectorizer.transform(testes)

# Faz a classificação com o modelo treinado
modelo.predict(freq_testes)
print(modelo.predict(freq_testes))

# Previsões
resultados = cross_val_predict(modelo, freq_tweets, classes, cv=10)

metrics.accuracy_score(classes, resultados)
print(metrics.classification_report(classes, resultados))
print(pd.crosstab(classes, resultados, rownames=['Real'], colnames=['Predito'], margins=True))
print("Acurácia:", metrics.accuracy_score(classes, resultados))
