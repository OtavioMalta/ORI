from unidecode import unidecode
import re


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
    palavras = unidecode(f.read().lower())
    return palavras


def bagOfWords(pathVocabulario, pathDocumento):
    bagOfWords = []
    termos = obterTermos(pathVocabulario)
    palavras = obtemDocumento(pathDocumento)

    # Percorre a lista de termos e verifica se o termo aparece no documento
    for t in termos:
        if t in palavras:
            bagOfWords.append(1)
        else:
            bagOfWords.append(0)

    # Imprime a bag of words
    print(bagOfWords)


def processarConsulta(path):
    # Abre o arquivo com as palavras da consulta
    f = open(path, 'r')

    # Remove acentos e pontuação
    # re.sub(r'[^\w\s]','',linhas) remove pontuação
    # unicode(f.read().lower()) remove acentos
    linhas = re.sub(r'[^\w\s]', '', unidecode(f.read().lower()))

    # Separa as palavras
    palavras = list(linhas.split())

    # Ordena as palavras
    palavras.sort()
    return palavras


def gerarVocabulario(pathConsulta, pathVocabulario):
    termos = []

    # Percorre a lista de palavras e adiciona as que não estão na lista de termos
    for t in processarConsulta(pathConsulta):
        if t not in termos:
            termos.append(t)
    # Abre o arquivo do vocabulário
    f = open(pathVocabulario, 'w')

    # Escreve os termos no arquivo
    for t in termos:
        f.write(t + '\n')
    f.close()
