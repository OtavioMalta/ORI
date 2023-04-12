from unidecode import unidecode
import math
import os
import re

def obterVocabulario(path):
    # Abre o arquivo com o vocabulário
    f = open(path, 'r')

    # Lê o arquivo e converte para minúsculo
    vocabulario = f.read().lower()
    
    # Separa os termos
    termos = vocabulario.split()
    return termos

def obtemDocumentos(pathDir):
    documentos = []
    documento = []

    # Abre multiplos arquivos de texto
    for arq in os.listdir(pathDir):
        if arq.endswith(".txt"):
            f = open(pathDir + arq, 'r')
            palavra = re.sub(r'[^\w\s]', '', unidecode(f.read().lower())).split()
            documento = palavra
        documentos.append(documento)
    return documentos

def calcularTF(termos, documentos):
    tfs = []
    for doc in documentos:
        tf = []
        for termo in termos:
            count = doc.count(termo)
            if count == 0:
                tf.append(0)
            else:
                 tf.append(1 + math.log(count,2))
        tfs.append(tf)
    return tfs

def calcularIDF(termos, documentos):
    idfs = []
    for termo in termos:
        count = 0
        for doc in documentos:
            if termo in doc:
                count += 1
        idfs.append(math.log(len(documentos)/count,2))
    return idfs

def calcularTFIDF(tfs, idfs):
    tfidfs = []
    for tf in tfs:
        tfidf = []
        for i in range(len(idfs)):
            tfidf.append(tf[i] * idfs[i])
        tfidfs.append(tfidf)
    return tfidfs

tf = calcularTF(obterVocabulario("/workspaces/ORI/TP2/Ex2/vocabulario.txt"), obtemDocumentos("/workspaces/ORI/TP2/Ex2/documentos/"))
idf = calcularIDF(obterVocabulario("/workspaces/ORI/TP2/Ex2/vocabulario.txt"), obtemDocumentos("/workspaces/ORI/TP2/Ex2/documentos/"))
tfidfs = calcularTFIDF(tf, idf)
for tfidf in tfidfs:
    print(tfidf )