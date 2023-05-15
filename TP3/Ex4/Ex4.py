
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

def obtemDocumentos(pathDir, list_stopwords, stemmer):
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
            # printa o tamanho do documento 
            print(len(documento_sem_stop))
            
            # Remove sufixos e prefixos das palavras
            documento_sem_stop_stem = [stemmer.stem(t) for t in documento_sem_stop]
            print(len(documento_sem_stop_stem))
            
            # Adiciona o documento
            documentos[arq] = documento_sem_stop_stem
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
porter = nltk.PorterStemmer()

documentos =obtemDocumentos("/workspaces/ORI/TP3/Ex3/documentos/", list_stopwords, porter)
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
sem Tempo de execução:  0.004990816116333008

baby i know you
    IKnowThere'sSomethingGoingOn.txt 0.13174911847465504
    YouandI.txt 0.07902898546404573
    ShameontheMoon.txt 0.0726933746330598
    Maniac.txt 0.07184055722851151
    TwilightZone.txt 0.04962714020393172
    Tempo de execução:  0.023865938186645508

 boy come from far away
    Maneater.txt 0.18047240956646554
    DoYouReallyWanttoHurtMe.txt 0.18026849622596186
    NeverGonnaLetYouGo.txt 0.07642509234498351
    TwilightZone.txt 0.07103457091784308
    BeatIt.txt 0.029492171476380995
    Tempo de execução:  0.024404048919677734
    
 dark side of the moon
    TotalEclipseoftheHeart.txt 0.16641668317125333
    ShameontheMoon.txt 0.16536042251758754
    TwilightZone.txt 0.10473859770145312
    Baby,CometoMe.txt 0.02601266702769173
    HungryLiketheWolf.txt 0.023210425244030487
    Tempo de execução:  0.02422332763671875
    
 travel the world
    SweetDreams(AreMadeofThis).txt 0.4169556736787223
    Maniac.txt 0.06483608048282472
    DownUnder.txt 0.05227545775326763
    Flashdance...WhataFeeling.txt 0.03647749319361243
    Maneater.txt 0.03332854313889258
    Tempo de execução:  0.012621402740478516
 
 sweetness break queen
    BillieJean.txt 0.12452145487462243
    EveryBreathYouTake.txt 0.08387685367857949
    Let'sDance.txt 0.06641570430299426
    HungryLiketheWolf.txt 0.0415367290032321
    Baby,CometoMe.txt 0.0
    Tempo de execução:  0.012701034545898438

"""