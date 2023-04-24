from unidecode import unidecode
import math
import os
import re
import time

def obterVocabulario(path):
    # Abre o arquivo com o vocabulário
    f = open(path, 'r')

    # Lê o arquivo e converte para minúsculo
    vocabulario = f.read().lower()
    
    # Separa os termos
    termos = vocabulario.split()
    return termos

def obtemDocumentos(pathDir):
    documentos = {}
    documento = []

    
    # Obtém os nomes dos arquivos e ordena em ordem alfabética
    arquivos = sorted(os.listdir(pathDir))

    # Abre multiplos arquivos de texto
    for arq in arquivos:
        if arq.endswith(".txt"):
            f = open(pathDir + arq, 'r')
            palavra = re.sub(r'[^\w\s]', '', unidecode(f.read().lower())).split()
            documento = palavra
            documentos[arq] = documento
    return documentos

def calcularTF(termos, documentos):
    tfs = {}
    for doc_nome, doc in documentos.items():
        tf = {}
        for termo in termos:
            count = doc.count(termo)
            if count == 0:
                tf[termo] = 0
            else:
                tf[termo] = 1 + math.log(count, 2)
        tfs[doc_nome] = list(tf.values())
    return tfs



def calcularIDF(termos, documentos):
    idfs = {}
    for termo in termos:
        count = 0
        for doc in documentos.values():
            if termo in doc:
                count += 1
        idfs[termo] = math.log(len(documentos) / count, 2)
    return idfs

def calcularTFIDF(tfs, idfs):
    tfidfs = {}
    for tf in tfs:
        tfidf = []
        for i in range(len(idfs)):
            tfidf.append(tfs[tf][i] * idfs[list(idfs.keys())[i]])
        tfidfs[tf] = tfidf
    return tfidfs

# Calcula o tempo de execução
start = time.time()
tf = calcularTF(obterVocabulario("/workspaces/ORI/TP2/Ex3/vocabulario.txt"), obtemDocumentos("/workspaces/ORI/TP2/Ex3/documentos/"))
idf = calcularIDF(obterVocabulario("/workspaces/ORI/TP2/Ex3/vocabulario.txt"), obtemDocumentos("/workspaces/ORI/TP2/Ex3/documentos/"))
tfidfs = calcularTFIDF(tf, idf)
end = time.time()
print("Tempo de execução para calcular o TF-IDF: ", end - start)

#for tfidf in tfidfs:
 #   print(tfidf, tfidfs[tfidf])