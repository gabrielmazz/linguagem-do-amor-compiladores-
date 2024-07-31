# Programa - Análise Sintática
# Compiladores

from rich.console import Console
from rich.table import Table
import pandas as pd
import os

# Carrega a tabela de análise sintática
def carrega_tabela(nome):
    
    # Verifica se a tabela existe na pasta
    try:
        tabela_slr = pd.read_excel(nome, sheet_name='Tabela')
    except:
        print('Erro ao carregar a tabela de análise sintática')
        return None
    
    try:
        tabela_gramatica = pd.read_excel(nome, sheet_name='Gramatica')
    except:
        print('Erro ao carregar a tabela de gramática')
        return None
    
    # Retira a primeira coluna
    tabela_slr = tabela_slr.iloc[:, 1:]
    
    # Retira a primeira linha da tabela gramatica
    tabela_gramatica = tabela_gramatica.iloc[1:]
    
    return tabela_slr, tabela_gramatica

def define_tabela():
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Pilha", style="dim", width=70)
    table.add_column("Entrada", style="dim", width=70)
    table.add_column("Ação", style="dim", width=12)

    return table

def ajusta_pilha_entrada(pilha_entrada, string):
    
    # Adiciona a string na pilha de entrada
    for i in range(len(string)):
        pilha_entrada.append(string[i])
    
    pilha_entrada.append('$')
    
    
    return pilha_entrada
      
def ajusta_pilha_analise(pilha_analise):
    pilha_analise.append('$')
    pilha_analise.append('0')
    
    return pilha_analise
   
# Funções de análise sintática
def verifica_pilha_entrada(pilha_analise, pilha_entrada, tabela):
    # Pega sempre o simbolo do topo da pilha no caso o mais a direita da lista
    pilha = pilha_analise[-1]
    
    # Pega sempre o simbolo da entrada no caso o mais a esquerda da lista
    simbolo = pilha_entrada[0]
    
    # Verifica na tabela de análise sintática se existe um caminho possível entre os dois
    # no caso tera que pega a linha que aqui sera a variavel pilha e a coluna que sera o simbolo
    # e verificar se existe um valor na tabela pegando a celula da tabela que ser a ação
    acao = tabela.at[int(pilha), str(simbolo)]
    
    return acao

def verifica_pilha_entrada_erro(pilha_analise, pilha_entrada, tabela):
    
    # Pega sempre o simbolo do topo da pilha no caso o mais a direita da lista
    pilha = pilha_analise[-1]
    
    # Percorre a linha da tabela que tem valor da "pilha" aleatoriamente para ver se existe 
    # um valor diferente de erro
    # 7	E2	E3	erro erro erro | por exemplo, ele ira pegar o valor E2 ou E3
    for i in range(len(tabela.columns)):
        if tabela.at[int(pilha), tabela.columns[i]] != 'erro':
            acao = tabela.at[int(pilha), tabela.columns[i]]
            break

    # Pega o simbolo da coluna aonde está a ação
    simbolo = tabela.columns[i]

    # Adiciona na pilha a string que foi lida da entrada
    pilha_analise.append(simbolo)
    
    # Adiciona o número do empilha na pilha de analise que seria todos os caracteres depois do E
    pilha_analise.append(acao[1:])
    
    return acao, pilha_analise, pilha_entrada

def adiciona_na_pilha(pilha_analise, pilha_entrada, acao):
    
    # Adiciona na pilha a string que foi lida da entrada
    pilha_analise.append(pilha_entrada[0])
    
    # Adiciona o número do empilha na pilha de analise que seria todos os caracteres depois do E
    pilha_analise.append(acao[1:])
    
    # Remove o primeiro caracter da pilha de entrada
    pilha_entrada.pop(0)

    return pilha_analise, pilha_entrada
    
def remove_da_pilha(pilha_analise, acao, tabela_gramatica, tabela_slr):
    
    # Pego o número da redução e vou na tabela de gramática e verifico quantos caracteres está na produção
    # e removo da pilha de analise o mesmo número de caracteres * 2 que está na produção

    # Pega o valor para ir na tabela gramatica
    aux_acao = int(acao[1:])
    
    # Pega a produção da linha - 1 na coluna 0
    producao = tabela_gramatica.iloc[aux_acao-1, 0]
    
    # Separa a produção em 3 partes, criando uma lista temporaria
    # Por exemplo PROGRAMA -> INSTRUCOES, ficaria na lista [PROGRAMA, ->, INSTRUCOES]
    # mas isso de uma forma generalizada para qualquer produção
    producao = producao.split(' ')
    
    # Junta a lista temporaria em uma string
    producao = ' '.join(producao)
         
    # Pega apenas caracteres do lado direito da produção, depois do '->' e contando um espaço
    aux = producao.split('->')[1]
    
    # Remove os espaços em branco
    aux = aux.replace(' ', '')
    
    # Multiplica por 2 para remover o número de caracteres da pilha de analise, isso vira um numero
    aux = len(aux) * 2
  
    # Remove da pilha de analise o número de caracteres que está na produção
    for i in range(aux):
        pilha_analise.pop()
        
    # Da append na string da produção mais a esquerda da gramatica e retira o ultimo caracter que é o espaço
    simbolo_aux = producao.split('->')[0] 
    simbolo_aux = simbolo_aux[:-1]
    pilha_analise.append(simbolo_aux)

    # Pego o ultimo valor da pilha de analise e o penultimo para ir na tabela de análise sintática procurar
    # o valor que está na tabela
    simbolo_aux = pilha_analise[-1]
    num_aux = pilha_analise[-2]

    # Pego o valor da tabela de análise sintática
    acao_aux = tabela_slr.at[int(num_aux), str(simbolo_aux)]

    # Adiciona na pilha de analise o valor que foi retirado da tabela
    pilha_analise.append(int(acao_aux))
    
    return pilha_analise
    
def aceita_da_pilha(pilha_entrada_print, somatorio_empilha, somatorio_desempilha, somatorio_erro, tabela_slr):
    
    # Printa a pilha de entrada que foi aceita com o rich
    console = Console()
    
    # Printa a tabelaSLR com o rich
    print("\n\n")

    console.print(f"Pilha de entrada aceita: [bold magenta]{pilha_entrada_print}[/bold magenta]\n")
    
    console.print(f"Somatório de empilhamento: [bold magenta]{somatorio_empilha}[/bold magenta]")
    console.print(f"Somatório de desempilhamento: [bold magenta]{somatorio_desempilha}[/bold magenta]")
    console.print(f"Somatório de erro: [bold magenta]{somatorio_erro}[/bold magenta]\n")
       
# Main
def sintatico():
    
    # String que vem do lexico MUDAR AQUI PARA A LISTA DE TOKENS
    string = '[a;]'
    
    # Carrega a tabela
    tabela_slr, tabela_gramatica = carrega_tabela('tabelaSLR.xlsx')
    
    # Cria a pilha de entrada
    pilha_entrada = []
    pilha_entrada = ajusta_pilha_entrada(pilha_entrada, string)

    # Cria a pilha de analise
    pilha_analise = []
    pilha_analise = ajusta_pilha_analise(pilha_analise)

    # Cria uma tabela com o rich para exibir a pilha de entrada
    table = define_tabela()
    # Exibe a tabela
    console = Console()
    
    # Adiciona uma nova linha com os valores atualizados
    table.add_row(f"[yellow]{str(pilha_analise)}[/yellow]", f"[yellow]{str(pilha_entrada)}[/yellow]", '[yellow]Inicio[/yellow]')
    table.add_row("", "", "")

    # Variaveis de print
    pilha_entrada_print = string

    # Começa a análise sintática
    condicao = True
    
    somatorio_empilha = 0
    somatorio_desempilha = 0
    somatorio_erro = 0
    controle_erro = False
    acao_erro = ''
    while condicao:

        # Verifica se existe um caminho possível
        acao = verifica_pilha_entrada(pilha_analise, pilha_entrada, tabela_slr)
            
    #     if acao == 'erro':
    #         table.add_row(f"[red]{str(pilha_analise)}[/red]", f"[red]{str(pilha_entrada)}[/red]", f"[red]Erro -> {acao_erro}[/red]")
    #    else:
    #         if acao == 'AC':
    #             table.add_row(f"[green]{str(pilha_analise)}[/green]", f"[green]{str(pilha_entrada)}[/green]", f"[green]{acao}[/green]")
    #         else:
    #             table.add_row(str(pilha_analise), str(pilha_entrada), acao)
                
        
        
        # Verifica se a ação é um shift (Empilha) ou um reduce (Desempilha)
        # Ele pega o primeiro caracter da ação que é o que vai indicar o que fazer
        if acao[0] == 'E': # Empilha 
            
            somatorio_empilha += 1
            
            # Adiciona na pilha de analise o valor que foi empilhado
            pilha_analise, pilha_entrada = adiciona_na_pilha(pilha_analise, pilha_entrada, acao)
            
            table.add_row(str(pilha_analise), str(pilha_entrada), acao)
            
            # Adiciona uma linha vazia como se fosse um "\n"
            table.add_row("", "", "")
            
            console.print(table)
            
        elif acao[0] == 'R': # Desempilha     
            
            somatorio_desempilha += 1
            
            pilha_analise = remove_da_pilha(pilha_analise, acao, tabela_gramatica, tabela_slr)
            
            table.add_row(str(pilha_analise), str(pilha_entrada), acao)
            
            # Adiciona uma linha vazia como se fosse um "\n"
            table.add_row("", "", "")
            
            console.print(table)
             
        elif acao == 'erro': # Erro -> Modo panico 
            
            somatorio_erro += 1
             
            # Tratar o erro, será pesquisar na mesma linha da tabelaSLR se existe um valor diferente de erro
            # e provavelmente será um empilha, executara essa ação 
            acao, pilha_analise, pilha_entrada = verifica_pilha_entrada_erro(pilha_analise, pilha_entrada, tabela_slr)
            
            acao_erro = acao
            
            table.add_row(f"[red]{str(pilha_analise)}[/red]", f"[red]{str(pilha_entrada)}[/red]", f"[red]Erro -> {acao_erro}[/red]")
            
            # Adiciona uma linha com as informações antes de corrigir o erro
            table.add_row("", "", "")
            
            controle_erro = True
              
        elif acao == 'AC':
            
            # Apaga o terminal
            os.system('cls' if os.name == 'nt' else 'clear')
            
            table.add_row(f"[green]{str(pilha_analise)}[/green]", f"[green]{str(pilha_entrada)}[/green]", f"[green]{acao}[/green]")
            
            console.print(table)
                
            condicao = False
            
            aceita_da_pilha(pilha_entrada_print, somatorio_empilha, somatorio_desempilha, somatorio_erro, tabela_slr)            
            
            
if __name__ == "__main__":
    sintatico()