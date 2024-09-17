
class Remedio:
    def __init__(self,nome,tarja,valor,laboratorio,estoque = 0):
        self.nome=nome
        self.tarja=tarja
        self.valor=valor
        self.laboratorio=laboratorio
        self.estoque=estoque

    def Info(self):
        print(f"Nome medicamento : {self.nome}")
        print(f"Tarja : {self.tarja}")
        print(f"preço R$ : {self.valor}")
        print(f"Laboratorio : {self.laboratorio}")
        print(f"Quantidade em estoque : {self.estoque}")
    
    def infoEstoque(self):
        print(self.estoque)  
              
    def modificarValor(self,novoValor):
        if (novoValor >= 0):
            self.valor = novoValor
        
        return "Valor não pode ser negativo"
    
    def modificarEstoque(self,estoqueAtual):
        if (estoqueAtual >= 0):
            self.estoque = estoqueAtual
        
        return "estoque não pode ser negativo"
    
    def adicionarEstoque(self,adicionarEstoque):
        if (adicionarEstoque > 0):
            self.estoque += adicionarEstoque
    
    def diminuirEstoque(self,diminuirEstoque):
        if (diminuirEstoque <= self.estoque):
            self.estoque -= diminuirEstoque
                     
            
        
    
    
if __name__ == "__main__":
    
    Paracetamol = Remedio("Paracetamol","amarela","8.99","Ultrafarma",350)
    Dramin = Remedio("Dramin","amarela",20.00,"Bayer",40)
    Diazepam = Remedio("Diazepam","preta",89.99,"Bayer",35)

    Paracetamol.Info()
    print()
    Dramin.Info()
    print()
    Diazepam.Info()
    
    Paracetamol.infoEstoque()
    
    Paracetamol.diminuirEstoque(50)
    Paracetamol.infoEstoque()
    
    Paracetamol.modificarValor(14.99)
    