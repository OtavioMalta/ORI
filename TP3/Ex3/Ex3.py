
import math
import os
import re
import time
import nltk
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

# converter letras em minúsculo, remover acentos, números e pontuação e remover stopwords usando a biblioteca do Python NTLK.
def processarConsulta(f):
    return re.findall(r'\b[A-zÀ-úü]+\b', unidecode(f.lower()))

def obtemDocumentos(pathDir, list_stopwords):
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
    
            # Remover stopwords do documento
            documento_sem_stop = [w for w in documento if w not in list_stopwords]
            
            # Adiciona o documento
            documentos[arq] = documento_sem_stop
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
    # Calcula o TF da consulta
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

def obtemStopWords(lingua):
    # Obtem stopwords em ingles
    nltk.download('stopwords')
    stopwords = nltk.corpus.stopwords.words(lingua)
    list_stopwords = set(stopwords)
    return list_stopwords


print("Digite sua consulta ou caminho:")
consulta = input()
consultaProcessada = processarConsulta(consulta)

list_stopwords = obtemStopWords('english')

documentos =obtemDocumentos("/workspaces/ORI/TP3/Ex3/documentos/", list_stopwords)
vocabulario = obterVocabulario("/workspaces/ORI/TP3/Ex3/vocabulario.txt")

tf = calcularTF(vocabulario, documentos, consultaProcessada)
idf = calcularIDF(vocabulario, documentos)
tfidfs = calcularTFIDF(tf, idf)

# Calcula o tempo de execução
start = time.time()

grauSimilaridade = grauSimilaridade(tfidfs, tfidfs["consulta"])

end = time.time()

print("Grau de similaridade: ")
freq = FreqDist(grauSimilaridade)
top5 = freq.most_common(5)
for t in top5:
    print(t[0], t[1])

print("Tempo de execução: ", end - start)
"""
 sem 0.0037736892700195312

baby i know you
    Baby,CometoMe.txt 0.2058773036242993
    EveryBreathYouTake.txt 0.10672863169181693
    BillieJean.txt 0.10466371913293618
    IKnowThere'sSomethingGoingOn.txt 0.0337644104629742
    YouandI.txt 0.021782675647699652
    Tempo de execução:  0.00840902328491211

 boy come from far away
    Maneater.txt 0.14204991546593435
    DoYouReallyWanttoHurtMe.txt 0.13435233960537202
    NeverGonnaLetYouGo.txt 0.06416824693488367
    TwilightZone.txt 0.06345167404326163
    BeatIt.txt 0.026908484441030313
    Tempo de execução:  0.008313417434692383
    
 dark side of the moon
    ShameontheMoon.txt 0.145171290676766
    TotalEclipseoftheHeart.txt 0.1334264793212374
    TwilightZone.txt 0.0896661370975466
    Baby,CometoMe.txt 0.022171699313815494
    HungryLiketheWolf.txt 0.021130476430945618
    Tempo de execução:  0.00818014144897461
    
 travel the world
    SweetDreams(AreMadeofThis).txt 0.36111974926877416
    Maniac.txt 0.044955052966491056
    Flashdance...WhataFeeling.txt 0.02400878362884771
    Maneater.txt 0.02205883084752677
    Baby,CometoMe.txt 0.0
    Tempo de execução:  0.01730942726135254
 
 sweetness break queen
    EveryBreathYouTake.txt 0.08980461204262148
    Let'sDance.txt 0.07061254471093727
    BillieJean.txt 0.05453973559914078
    HungryLiketheWolf.txt 0.050389398683351766
    Baby,CometoMe.txt 0.0
    Tempo de execução:  0.008198022842407227

"""