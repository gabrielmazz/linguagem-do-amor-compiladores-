
#Para execução do código é necessário que o arquivo de texto esteja
#no mesmo diretório do código

#Para interpretar esse código é necessário usar a seguinte linha de comando:
#python3 lexico_re.py

import re
from rich.console import Console
from rich.syntax import Syntax

def lexico():

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

    # Abre o arquivo de texto (código de teste)
    with open('lexico/codigo_teste.txt', 'r') as arquivo:
        conteudo = arquivo.read()


    i = 0
    # Percorre o conteúdo do arquivo de texto separando os tokens
    while i < len(conteudo):
        match = None

        # Percorre os padrões de tokens
        for pattern, token_type in padroes:
            expressao_tokens = re.compile(pattern)
            match = expressao_tokens.match(conteudo, i)
            print(match)
            if match:
                value = match.group(0)
                tokens.append((value, token_type))
                i = match.end()
                break

        if not match:
            raise ValueError(f'Erro inesperado em {conteudo[i]}')

    console = Console()
    syntax = Syntax(conteudo, "python")
    console.print("Código utilizado:\n", style="bold green")
    console.print(syntax) 
    
    # Cria uma lista com os tokens pegando apenas a 2 posição de cada token
    lista_tokens = [i[1] for i in tokens]
    
    # Verifica o token chamado "espaço" e remove da lista
    lista_tokens = [i for i in lista_tokens if i != 'espaço']
    
    return lista_tokens