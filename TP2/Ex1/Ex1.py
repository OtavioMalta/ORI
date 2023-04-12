from unidecode import unidecode
import os
import re

def obtemDocumentos(pathDir):
    termos = ""

    # Abre multiplos arquivos de texto
    for arq in os.listdir(pathDir):
        if arq.endswith(".txt"):
            f = open(pathDir + arq, 'r')
            palavra = re.sub(r'[^\w\s]', '',unidecode(f.read().lower()))
            termos = termos + " " + palavra
    return termos

def gerarVocabulario(termos, pathVocabulario):
    # Remove acentos e pontuação
    # re.sub(r'[^\w\s]','',linhas) remove pontuação
    # unicode(f.read().lower()) remove acentos
    linhas = re.sub(r'[^\w\s]', '', unidecode(termos.lower()))
    # Separa as palavras
    palavras = list(linhas.split())

    vocabulario = []
    # Percorre a lista de palavras e adiciona as que não estão na lista de termos
    for p in palavras:
        if p not in vocabulario:
            vocabulario.append(p)
    # Abre o arquivo do vocabulário
    f = open(pathVocabulario, 'w')

    # Escreve os termos no arquivo
    for v in vocabulario:
        f.write(v + '\n')
    f.close()


def obterTermos(path):
    # Abre o arquivo com o vocabulário
    f = open(path, 'r')

    # Lê o arquivo e converte para minúsculo
    vocabulario = f.read().lower()
    
    # Separa os termos
    termos = vocabulario.split()
    return termos


def obtemDocumento(path):
    # Abre o arquivo com o documento
    f = open(path, 'r')

    # Lê o arquivo e converte para minúsculo
    palavras = unidecode(f.read().lower()).split()
    return palavras

def bagOfWords(pathVocabulario, pathDocumentos):
    termos = obterTermos(pathVocabulario)

    for arq in os.listdir(pathDocumentos):
        bagOfWords = []
        if arq.endswith(".txt"):
            f = open(pathDocumentos + arq, 'r')
            palavras = re.sub(r'[^\w\s]', '',unidecode(f.read().lower())).split()
            
            # Percorre a lista de termos e verifica se o termo aparece no documento
            for t in termos:
                if t in palavras:
                    bagOfWords.append(1)
                else:
                    bagOfWords.append(0)

            # Imprime a bag of words
            print(bagOfWords)
        

#1)
termos = obtemDocumentos('TP2/Ex1/arquivos/')

#2 e 3)
gerarVocabulario(termos, 'TP2/Ex1/vocabulario.txt')

#4)
bagOfWords('TP2/Ex1/vocabulario.txt', 'TP2/Ex1/arquivos/')