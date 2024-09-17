
class Livro:
    def __init__(self,titulo,isbn,valor,autor,editora,estoque=0):
        self.titulo=titulo
        self.isbn=isbn
        self.valor=valor
        self.autor=autor
        self.editora=editora
        self.estoque=estoque

    def Info(self):
        print(f"Titulo : {self.titulo}")
        print(f"ISBN : {self.isbn}")
        print(f"preço R$ : {self.valor}")
        print(f"autor : {self.autor}")
        print(f"editora : {self.editora}")
        print(f"estoque : {self.estoque}")
        
        
    def modificarValor(self,novoValor):
        if (novoValor >= 0):
            self.valor = novoValor
        
        return "Valor não pode ser negativo" 
    
    def infoEstoque(self):
        print(self.estoque)  
              
    def modificarValor(self,novoValor):
        if (novoValor >= 0):
            self.valor = novoValor
        
        return "Valor não pode ser negativo"
    
    def adicionarEstoque(self,adicionarEstoque):
        if (adicionarEstoque > 0):
            self.estoque += adicionarEstoque
    
    def diminuirEstoque(self,diminuirEstoque):
        if (diminuirEstoque <= self.estoque):
            self.estoque -= diminuirEstoque 
        
        
    
    
    

if __name__ == "__main__":

    Pulp = Livro("Pulp",989876-22,9.99,"Charles Bukowski","Charles Newman",23)
    aCabana = Livro("A Cabana",876698-81,20.00,"Joseph Kristen","Gente",13)
    OsElementos = Livro("Os elementos",796921-27,75.00,"Euclides","Unesp",20)

    Pulp.Info()
    print()
    aCabana.Info()
    print()
    OsElementos.Info()
    
    
    Pulp.modificarValor(55)
    Pulp.adicionarEstoque(22)
    Pulp.diminuirEstoque(15)
    
    
    Pulp.Info()