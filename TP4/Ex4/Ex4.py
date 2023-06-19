import nltk
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
from sklearn.feature_extraction.text import CountVectorizer

# Carregando o dataset
dataset = pd.read_csv(r"TP4/Tweets_Mg.csv",encoding='utf-8')

dataset.head()
dataset.count()
dataset[dataset.Classificacao=='Neutro'].count()
dataset[dataset.Classificacao=='Positivo'].count()
dataset[dataset.Classificacao=='Negativo'].count()

# Extraindo tweets e classes
tweets = dataset['Text'].values
classes = dataset['Classificacao'].values

# Stopwords
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words("portuguese")

# TF
vectorizer = CountVectorizer(analyzer="word", ngram_range=(1,2), stop_words=stopwords)
freq_tweets = vectorizer.fit_transform(tweets)

# Algortimo Naive Bayes
modelo = MultinomialNB()
modelo.fit(freq_tweets,classes)

testes = ['O governo de Minas é uma tragédia, muito ruim','Estou muito feliz com o governo de Minas esse ano','O estado de Minas Gerais decretou calamidade financeira!!!','A segurança do estado está deixando a desejar','O governador de Minas é do Novo']

# Calcula a BoW
freq_testes = vectorizer.transform(testes)

# Faz a classificação com o modelo treinado
modelo.predict(freq_testes)
print(modelo.predict(freq_testes))

# Previsões
resultados = cross_val_predict(modelo, freq_tweets, classes, cv=10)

metrics.accuracy_score(classes,resultados)
print(metrics.classification_report(classes,resultados))
print (pd.crosstab(classes, resultados, rownames=['Real'], colnames=['Predito'], margins=True))
print("Acurácia:", metrics.accuracy_score(classes, resultados))
