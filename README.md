# Compilador da Linguagem do Amor

## Sumário

- [Introdução](#introdução)
- [Parte I - Analisador Léxico](#parte-i---analisador-léxico)
  - [Especificação da Linguagem](#especificação-da-linguagem)
    - [Tipos de Dados](#tipos-de-dados)
    - [Operadores](#operadores)
    - [Operadores relacionais](#operadores-relacionais)
    - [Operadores aritméticos](#operadores-aritméticos)
    - [Operador de atribuição](#operador-de-atribuição)
    - [Formação dos identificadores](#formação-dos-identificadores)
    - [Entrada e saída](#entrada-e-saída)
    - [Palavra reservada](#palavra-reservada)
    - [Programa na BNF](#programa-na-bnf)
  - [Implementação do Analisador Léxico](#implementação-do-analisador-léxico)

## Introdução

Neste trabalho, a ideia é resolver os desafios propostos para a realização de um *compilador ou interpretador* de uma **Linguagem de Programação**. Tudo que foi implementado neste compilador, são os métodos passados na matéria de Compiladores do 4 ano de Ciências da Computação da Universidade Estadual do Oeste do Paraná (UNIOESTE). O trabalho foi realizado durante todo o ano letivo da matéria sendo divido em três partes, sendo a implementação do *Analisador Léxico*, *Analisador Sintático* e por fim, o *Analisador Semântico*.

## Parte I - Analisador Léxico

Nesta primeira parte, foi caracterizado a linguagem de programação que será usada durante todo o desenvolvimento do compilador. A linguagem escolhida foi a **Linguagem do Amor** aonde todas as sua montagem tenho um cunho romântico.

### Especificação da Linguagem

#### Tipos de Dados

| Tipo de Dado | Representação |
|--------------|-----------|
| INTEIRO      | PAIXAO |
| REAL      | ATRACAO |
| STRING        | PALAVRA |
| BOOLEANO       | INTERESSE |

#### Operadores

| Operador | Representação     |
|----------|--------------------|
| && (AND) | COMBINANDO_CORACOES |
| \|\| (OR) | ESCOLHA_DO_CORACAO  |
| ! (NOT)  | DESILUSAO           |

#### Operadores relacionais

| Operador | Representação     |
|----------|--------------------|
| >        | (MAIOR)            |
| >=       | (MAIOR OU IGUAL)   |
| <        | (MENOR)            |
| <=       | (MENOR OU IGUAL)   |
| ==       | (IGUALDADE)        |
| !=       | (DIFERENTE DE)     |

#### Operadores aritméticos

| Operador | Representação     |
|----------|--------------------|
| +        | (MAIS)             |
| -        | (MENOS)            |
| *        | (MULTIPLICAÇÃO)    |
| /        | (DIVISÃO)          |

#### Operador de atribuição

| Operador | Representação     |
|----------|--------------------|
| =        | (ATRIBUIÇÃO)       |


#### Formação dos identificadores

Declaração em qualquer parte do código (todas as variáveis declaradas serão tidas como globais). Exemplo: palavra (tipo) compilador (identificador).

| Conjunto de Caracteres | Descrição                                      |
|------------------------|------------------------------------------------|
| a-Z                    | O primeiro símbolo deve pertencer a este conjunto de caracteres |
| 0-9                    | Dígitos de 0 a 9                              |
| _                      | Caractere underscore (_)                       |

#### Entrada e saída

| Entrada | Representação                                      |
|------------------------|------------------------------------------------|
| Entrada pelo teclado (SCANF) | CAPTURANDO_SENTIMENTOS |
| Saída no terminal (PRINTF)  | MOSTRANDO_AFETO        |

#### Palavra reservada

| Operador | Representação     |
|----------|--------------------|
| IF       | DESEJO             |
| ELSE     | DESAPEGO           |

| Comando | Descrição                   |
|---------|-----------------------------|
| FOR     | Executa um bloco de código repetidamente enquanto uma condição for verdadeira. |
| WHILE   | Executa um bloco de código repetidamente enquanto uma condição for verdadeira. |


| Símbolo | Representação     |
|---------|--------------------|
| ;       | Separador na estrutura de repetição contada |
| %       | Identificador de tipo na entrada e saída     |
| (       | Delimitador de início                        |
| )       | Delimitador de final                          |
| {       | Delimitador de início                        |
| }       | Delimitador de final                          |

#### Programa na BNF

| Gramática | Produção     |
|---------|--------------------|
| PROGRAMA'                | PROGRAMA                |
| PROGRAMA                 | INSTRUCOES              |
| INSTRUCOES               | INSTRUCAO INSTRUCOES    |
| INSTRUCOES               | INSTRUCAO               |
| INSTRUCAO                | DECLARACAO              |
| INSTRUCAO                | ATRIBUICAO              |
| INSTRUCAO                | ESTRUTURA_DE_DECISAO    |
| INSTRUCAO                | ESTRUTURA_DE_REPETICAO  |
| INSTRUCAO                | ENTRADA_SAIDA           |
| DECLARACAO               | TIPO identificador      |
| ATRIBUICAO               | identificador = EXPRESSAO |
| ESTRUTURA_DE_DECISAO     | desejo ( EXPRESSAO op_rel EXPRESSAO ) { INSTRUCOES } |
| ESTRUTURA_DE_DECISAO     | desapego { INSTRUCOES } |
| ESTRUTURA_DE_REPETICAO   | felizes_para_sempre ( ATRIBUICAO ; EXPRESSAO op_rel EXPRESSAO ; INCREMENTO ) { INSTRUCOES } |
| ESTRUTURA_DE_REPETICAO   | enquanto_existir_amor ( EXPRESSAO op_rel EXPRESSAO ) { INSTRUCOES } |
| ENTRADA_SAIDA            | capturando_sentimentos ( identificador ) |
| ENTRADA_SAIDA            | mostrando_afeto ( identificador ) |
| TIPO                     | paixao                  |
| TIPO                     | atracao                 |
| TIPO                     | palavra                 |
| TIPO                     | interesse               |
| EXPRESSAO                | TERMO                   |
| EXPRESSAO                | TERMO op_arit EXPRESSAO |
| TERMO                    | identificador           |
| TERMO                    | NUMERO                  |
| NUMERO                   | num_int                 |
| NUMERO                   | num_real                |
| INCREMENTO               | identificador = identificador op_arit num_int |

### Implementação do Analisador Léxico

Toda a implementação se baseia na criação de tokens que é a primeira parte do trabalho, usando a biblioteca *re* do python para a criação de expressões regulares que irão identificar os tokens da linguagem. Primeiro temos um programa base num `txt` que será lido e passado para o analisador léxico que irá identificar os tokens e criar uma lista de saída com os tokens identificados com o dicionário da linguagem.

```python
tokens = []
padroes = [
    (r'capturando_sentimentos', 'capturando_sentimentos'),
    (r'paixao', 'paixao'),
    (r'atracao', 'atracao'),
    (r'palavra', 'palavra'),
    (r'interesse', 'interesse'),
    (r'mostrando_afeto', 'mostrando_afeto'),
    (r'desejo', 'desejo'),
    (r'desapego', 'desapego'),
    (r'felizes_para_sempre', 'felizes_para_sempre'),
    (r'enquanto_existir_amor', 'enquanto_existir_amor'),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'identificador'),
    (r'\d+\.\d+', 'num_real'),
    (r'\d+', 'num_int'),
    (r'[\+\-\*/]', 'op_arit'),
    (r'>=', 'op_rel'),
    (r'<=', 'op_rel'),
    (r'==', 'op_rel'),
    (r'<', 'op_rel'),
    (r'>', 'op_rel'),
    (r'=', '='),
    (r'\;', ';'),
    (r'\(', 'parenteses_inicial'),
    (r'\)', 'parenteses_final'),
    (r'\{', 'chaves_inicial'),
    (r'\}', 'chaves_final'),
    (r'\s+', 'espaço')
]
```

## Parte II - Analisador Sintático 


Posterimente, é verificado os tokens que são "*espaços*" e remove eles da lista, pois quando for para o análisador sintático, não será necessário eles

## Utilização

Nesta seção, você pode explicar como usar o compilador da Linguagem do Amor, incluindo os comandos e opções disponíveis.

## Exemplos

Aqui, você pode fornecer alguns exemplos de código na Linguagem do Amor e mostrar como o compilador os processa.

## Contribuição

Se você deseja que outras pessoas contribuam para o compilador, pode fornecer orientações sobre como elas podem fazer isso.

## Licença

Nesta seção, você pode especificar a licença sob a qual o compilador da Linguagem do Amor é distribuído.
