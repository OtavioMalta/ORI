# TP3 - Pré-processamento usando o nltk e modelo vetorial
Considere o código "pre_processamento.ipynb" disponível no Microsoft Teams - Geral.

### 1) Execute o código passo a passo usando o Google Colab e crie um pequeno relatório (PDF) explicando o que foi feito. Explique a importância de pré-processamento, o conceito de stopwords e as diferenças entre stemming e lemmatization.

### 2) Escolha um outro corpus em português, diferente dos livros do Machado de Assis (dê uma olhada aqui: https://www.nltk.org/howto/portuguese_en.html) e re-execute o código. Selecione agora um outro corpus, agora em inglês, e re-execute o código. Tome o cuidado na seleção das stopwords - em português ou em inglês.

Submissão: envie o relatório PDF e os arquivos .ipynb modificados.

------

## Exercício 2

Reuse os códigos das atividades anteriores para implementar o modelo vetorial. O código deve receber como parâmetro:

### 1) um arquivo texto contendo o vocabulário da coleção

### 2) o diretório contendo os documentos

### 3) uma consulta feita pelo usuário

O programa deverá exibir na tela (console) o grau de similaridade de cada documento da coleção para a consulta feita pelo usuário ordenado de forma descrescente. Não se esqueça de identificar o documento ao imprimi-lo na tela (doc1.txt, por exemplo).

Observações:

* Na parte 1, somente faça os seguintes pré-processamentos: converter letras em minúsculo, remover acentos, números e pontuação.

* Teste o seu código usando como base a coleção de quatro documentos do livro (to do). Não se esqueça que o denominador da fórmula do produto vetorial é o produto das duas normas (documento e consulta). No livro ele fez a conta com somente a norma do documento. Uma pequena diferença é esperada.

Submissão: i) envie o arquivo .py e ii) um print do console com o resultado obtido na coleção do livro.


---

## Exercício 3

Ajuste o código do Exercício 2 para fazer os seguintes pré-processamentos: converter letras em minúsculo, remover acentos, números e pontuação e remover stopwords usando a biblioteca do Python NTLK.

Submissão: envie o arquivo .py.

------

## Exercício 4

Elabore 5 consultas para a base de dados das músicas construída no TP-2. Submeta tais consultas para o programa já ajustado (Exercício 3). Salve o Top 5 de documentos com maior grau de similaridade para cada uma das consultas em uma planilha.

Altere o código do seu programa e inclua o Stemming usando o algoritmo de Porter presente na biblioteca NTLK. Submeta novamente as 5 consultas para o seu novo programa. Foi possível notar alguma mudança nos rankings para o Top 5 de documentos? Discuta os resultados.

Submissão: i) envie o arquivo .py; ii) a planilha com os resultados das consultas para as duas execuções - sem Stemming e com Stemming. Esse arquivo deverá se chamar "top10.xls"; iii) um PDF com as suas discussões/comentários sobre os resultados obtidos - sem stemming e com stemming. Esse arquivo deverá se chamar "discussao.pdf"

---

## Exercício 5

Use as consultas elaboradas no exercício 4 para encontrar o tempo gasto para gerar o ranking, ou seja, calcular o grau de similaridade entre a consulta e todos os documentos da coleção. Em média, quanto tempo o seu programa leva para gerar um ranking de uma dada consulta? Esse tempo varia de uma consulta para outra? Compare o seu tempo médio com o tempo médio de pelo menos outros três colegas. Discuta os resultados encontrados.

---

Instruções gerais: as respostas devem ser enviadas em um arquivo .zip chamado "TP3_nome_sobrenome.zip". O arquivo deverá ter os seguintes diretórios: "Ex1", "Ex2", "Ex3", "Ex4" e "Ex5". Dentro de cada diretório deve constar cada uma das respostas indicadas cima. IMPORTANTE: caso o arquivo resposta não respeite essa organização/nomenclatura e não possua cada um dos itens solicitados, a nota do TP será 0.

