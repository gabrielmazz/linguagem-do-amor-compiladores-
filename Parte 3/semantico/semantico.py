from semantico.SymbolTable.SymbolTable import SymbolTable

def semantico(lista_tokens):
    
    print(lista_tokens)

    print("\n\n")
    
    # Instancia a tabela de símbolos
    symbol_table = SymbolTable()
    
    # Insere uma palavra
    symbol_table.insert("salve", "palavra")
    symbol_table.insert("a", "paixao")
    symbol_table.insert("variavel", "atracao")
    
    # Printa a tabela de símbolos
    symbol_table.print_table()
    