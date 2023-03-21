from unidecode import unidecode
import re

#Abre o arquivo com as palavras da consulta
f=open('consulta.txt', 'r')

#Remove acentos e pontuação
# re.sub(r'[^\w\s]','',linhas) remove pontuação
# unicode(f.read().lower()) remove acentos
linhas =  re.sub(r'[^\w\s]','',unidecode(f.read().lower()))

#Separa as palavras
palavras = list(linhas.split())

#Ordena as palavras
palavras.sort()

termos = []

#Percorre a lista de palavras e adiciona as que não estão na lista de termos
for p in palavras:
    if(p not in termos):
        termos.append(p)

#Abre o arquivo do vocabulário
f=open('vocabulario.txt', 'w')

#Escreve as termos no arquivo
for t in termos:
    f.write(t + '\n')

f.close()
