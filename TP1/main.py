from funcoes import *

#EX1
# Processa a consulta(param1), ordenando e removendo as palavras repetidas, pontuação e acentos
# Escreve o vocabulário gerado no arquivo(param2)
gerarVocabulario('TP1/consulta.txt', 'TP1/vocabulario.txt')

#EX2
# Obtem os termos do vocabulário(param1) e as palavras do documento(param2)
# Gera a bag of words e imprime na tela
bagOfWords('TP1/vocabulario.txt', 'TP1/documento.txt')