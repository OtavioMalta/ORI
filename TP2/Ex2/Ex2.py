from unidecode import unidecode
import math
import os
import re
import time

def obterVocabulario(path):
    # Abre o arquivo com o vocabulário
    f = open(path, 'r')

    # Lê o arquivo
    vocabulario = f.read()
    
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

            # Adiciona o documento
            documentos[arq] = documento
    return documentos

def calcularTF(termos, documentos):
    tfs = {}
    # Percorre os documentos
    for doc_nome, doc in documentos.items():
        tf = {}
        # Percorre os termos
        for termo in termos:
            # Conta o número de vezes que o termo aparece no documento
            count = doc.count(termo)
            if count == 0:
                tf[termo] = 0
            else:
                # Calcula o TF
                tf[termo] = 1 + math.log(count, 2)
        # Adiciona o TF do documento ao dicionário de TFs
        tfs[doc_nome] = list(tf.values())
    return tfs



def calcularIDF(termos, documentos):
    idfs = {}
    # Percorre os termos
    for termo in termos:
        count = 0
        # Percorre os documentos
        for doc in documentos.values():
            # Verifica se o termo aparece no documento
            if termo in doc:
                count += 1
        # Calcula o IDF
        idfs[termo] = math.log(len(documentos) / count, 2)
    return idfs

def calcularTFIDF(tfs, idfs):
    tfidfs = {}
    # Percorre os TFs
    for tf in tfs:
        tfidf = []
        # Percorre os IDFs
        for i in range(len(idfs)):
            # Calcula o TF-IDF
            tfidf.append(tfs[tf][i] * idfs[list(idfs.keys())[i]])
        # Adiciona o TF-IDF 
        tfidfs[tf] = tfidf
    return tfidfs

# Calcula o tempo de execução
start = time.time()
tf = calcularTF(obterVocabulario("/workspaces/ORI/TP2/Ex3/vocabulario.txt"), obtemDocumentos("/workspaces/ORI/TP2/Ex3/documentos/"))
idf = calcularIDF(obterVocabulario("/workspaces/ORI/TP2/Ex3/vocabulario.txt"), obtemDocumentos("/workspaces/ORI/TP2/Ex3/documentos/"))
tfidfs = calcularTFIDF(tf, idf)
end = time.time()

for tfidf in tfidfs:
    print(tfidf, tfidfs[tfidf] )

# printa o maior tfidf dos documentos 
#for tfidf in tfidfs:
  #  print(tfidf, max(tfidfs[tfidf]), tfidfs[tfidf].index(max(tfidfs[tfidf])))

print("Tempo de execução para calcular o TF-IDF: ", end - start)