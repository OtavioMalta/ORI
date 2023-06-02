
import math
import os
import re
from unidecode import unidecode
from nltk.probability import FreqDist

def obterVocabulario(path):
    # Abre o arquivo com o vocabulário
    f = open(path, 'r')

    # Lê o arquivo
    vocabulario = f.read()
    
    # Separa os termos
    termos = vocabulario.split()
    return termos

# Caso leia a consulta de um arquivo
def ObtemConsulta(path):
    # Abre o arquivo com a consulta
    f = open(path, 'r')
    return f

def processarConsulta(f):
    # retira pontuação, transforma em minúsculo e remove acentos
    return re.findall(r'\b[A-zÀ-úü]+\b', unidecode(f.lower()))

def obtemDocumentos(pathDir):
    documentos = {}
    documento = []
    # Obtém os nomes dos arquivos e ordena em ordem alfabética
    arquivos = sorted(os.listdir(pathDir))

    # Abre multiplos arquivos de texto
    for arq in arquivos:
        if arq.endswith(".txt"):
            f = open(pathDir + arq, 'r')
            
            # retira pontuação, transforma em minúsculo e remove acentos
            palavra = re.sub(r'[^\w\s]', '', unidecode(f.read().lower())).split()
            documento = palavra

            # Adiciona o documento
            documentos[arq] = documento
    return documentos

def calcularTF(termos, documentos, consulta):
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

    tf = {}
    # Percorre os termos
    for termo in termos:
        # Conta o número de vezes que o termo aparece na consulta
        count = consulta.count(termo)
        if count == 0:
            tf[termo] = 0
        else:
            # Calcula o TF
            tf[termo] = 1 + math.log(count, 2)
    # Adiciona o TF da consulta ao dicionário de tfs
    tfs["consulta"] = list(tf.values())
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
        if count == 0:
            idfs[termo] = 0
        else:
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

def  grauSimilaridade(tfidfs, consulta):
    grauSimilaridade = {}
    for tfidf in tfidfs:
        # Para não calcular o grau de similaridade da consulta com ela mesma (resultado sempre 1)
        if tfidf == "consulta":
            break
        grauSimilaridade[tfidf] = 0
        # Percorre os termos 
        for i in range(len(consulta)):
            # Calcula o produto interno 
            grauSimilaridade[tfidf] += tfidfs[tfidf][i] * consulta[i]

        # Calcula a norma 
        # Se a norma de um dos vetores for 0, o grau de similaridade é 0
        if norma(consulta) == 0 or norma(tfidfs[tfidf]) == 0:
            grauSimilaridade[tfidf] = 0
        else:
            grauSimilaridade[tfidf] /= (norma(tfidfs[tfidf]) * norma(consulta))
    return grauSimilaridade

def norma(objeto):
    norma = 0
    for o in objeto:
        norma += o ** 2
    return math.sqrt(norma)

print("Digite sua consulta:")
consulta = input()
consultaProcessada = processarConsulta(consulta)

documentos =obtemDocumentos("/workspaces/ORI/TP3/Ex2/documentos/")
vocabulario = obterVocabulario("/workspaces/ORI/TP3/Ex2/vocabulario.txt")

tf = calcularTF(vocabulario, documentos, consultaProcessada)
idf = calcularIDF(vocabulario, documentos)
tfidfs = calcularTFIDF(tf, idf)


grauSimilaridade = grauSimilaridade(tfidfs, tfidfs["consulta"])
print("Grau de similaridade: ")

freq = FreqDist(grauSimilaridade)

#imprime todos os documentos ordenados por grau de similaridade
for doc, grau in freq.most_common():
    print(doc, grau)
    
