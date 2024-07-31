import lexico.lexico_re as lr
import sintatico.sintatico as st
import time
from rich.console import Console
from rich.markdown import Markdown
import os

if __name__ == "__main__":

    mark = """---"""
    md = Markdown(mark)

    # Apaga o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    console = Console()
    
    console.print(md)
    console.print("Trabalho de Compiladores - Linguagem do Amor", style="bold")
    console.print("Gabriel Mazzuco e Rodrigo Rocha", style="italic")    
    
    console.print(md)
    console.print(f"Parte I - Analisador léxico:\n", style="bold underline green")
    
    # Chama o analisador léxico
    tempo_lexico = time.time()
    lista_tokens = lr.lexico()
    tempo_lexico = time.time() - tempo_lexico

    console.print(f"\nPilha de entrada: [bold magenta]{lista_tokens}[/bold magenta]\n")

    console.print(md)
    console.print(f"Parte II - Analisador Sintático:\n", style="bold underline green")
    
    # Chama o analisador sintático
    tempo_sintatico = time.time()    
    st.sintatico(lista_tokens)
    tempo_sintatico = time.time() - tempo_sintatico
    
    console.print(md)
    
    # Arrendo os tempos para 2 casas decimais
    tempo_lexico = round(tempo_lexico, 5)
    tempo_sintatico = round(tempo_sintatico, 5)
    
    console.print(f"Tempo gasto no analisador léxico: {tempo_lexico} s", style="bold green")
    console.print(f"Tempo gasto no analisador sintático: {tempo_sintatico} s", style="bold green")
    print("\n")