import re

tokens = []
padroes = [
    (r'capturando_sentimentos', 'palavra_reservada'),
    (r'paixao', 'palavra_reservada'),
    (r'atracao', 'palavra_reservada'),
    (r'palavra', 'palavra_reservada'),
    (r'interesse', 'palavra_reservada'),
    (r'mostrando_afeto', 'palavra_reservada'),
    (r'desejo', 'palavra_reservada'),
    (r'desapego', 'palavra_reservada'),
    (r'felizes_para_sempre', 'palavra_reservada'),
    (r'enquanto_existir_amor', 'palavra_reservada'),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'identificador'),
    (r'\d+\.\d+', 'número_real'),
    (r'\d+', 'número_inteiro'),
    (r'[\+\-\*/]', 'op_arit'),
    (r'>=', 'op_rel'),
    (r'<=', 'op_rel'),
    (r'==', 'op_rel'),
    (r'<', 'op_rel'),
    (r'>', 'op_rel'),
    (r'=', 'atribuicao'),
    (r'\&\&', 'op_log'),
    (r'\|\|', 'op_log'),
    (r'\!', 'op_log'),
    (r'\;', ';'),
    (r'\%', '%'),
    (r'\(', 'delimitador'),
    (r'\)', 'delimitador'),
    (r'\{', 'delimitador'),
    (r'\}', 'delimitador'),
    (r'\s+', 'espaço')
]

with open('teste.txt', 'r') as arquivo:
    conteudo = arquivo.read()

i = 0
while i < len(conteudo):
    match = None

    for pattern, token_type in padroes:
        expressao_tokens = re.compile(pattern)
        match = expressao_tokens.match(conteudo, i)

        if match:
            value = match.group(0)
            tokens.append((value, token_type))
            i = match.end()
            break

    if not match:
        raise ValueError(f'Erro inesperado em {conteudo[i]}')

# Imprime os tokens encontrados
for token in tokens:
    print(token)