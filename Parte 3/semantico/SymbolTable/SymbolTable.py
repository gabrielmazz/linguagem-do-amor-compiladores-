# Declara a classe SymbolTable que é responsável por armazenar os símbolos do
# compilador, aqui é feito a parte 3, sendo o analisador semântico.

class SymbolTable:
    
    def __init__(self):
        
        # Declaração da tabela de símbolos
        self.table = {}
        
        # Declaração das palavras reservadas
        self.reserved = {"paixao",
                         "atracao",
                         "palavra",
                         "interesse",
                         "combinando_coracoes",
                         "escolha_do_coracao",
                         "desilusao",
                         "capturando_sentimentos",
                         "mostrando_afeto",
                         "desejo",
                         "desapego",
                         "felizes_para_sempre",
                         "enquanto_existir_amor"}
        
    def insert(self, symbol, type):
            
        # Verifica se o símbolo já foi declarado
        if symbol in self.table:
            raise Exception(f"Erro semântico: variável {symbol} já declarada.")
        
        # Insere o símbolo na tabela
        self.table[symbol] = {"type": type}
        
    
    def lookup(self, symbol):
        
        # Verifica se o símbolo foi declarado
        if symbol not in self.table:
            raise Exception(f"Erro semântico: variável {symbol} não declarada.")
        
        return self.table[symbol]["value"]
    
    def print_table(self):
        
        # Printa a tabela de símbolos
        for symbol in self.table:
            print(f"{symbol} : {self.table[symbol]}")