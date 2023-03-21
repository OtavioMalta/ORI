from unidecode import unidecode

#Abre o arquivo com o vocabulário 
f=open('vocabulario.txt', 'r')

#Lê o arquivo e converte para minúsculo
vocabulario = f.read().lower()

#Separa os termos
termos = vocabulario.split()

#Abre o arquivo com o documento
f=open('documento.txt', 'r')

#Lê o arquivo e converte para minúsculo
palavras = unidecode(f.read().lower())

bagOfWords = []

#Percorre a lista de termos e verifica se o termo aparece no documento
for t in termos:
    if(t in palavras):
        bagOfWords.append(1)
    else:
        bagOfWords.append(0)

#Imprime a bag of words
print(bagOfWords)
