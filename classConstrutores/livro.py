
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

if __name__ == "__main__":

    Pulp = Livro("Pulp",989876-22,9.99,"Charles Bukowski","Charles Newman",23)
    aCabana = Livro("A Cabana",876698-81,20.00,"Joseph Kristen","Gente",13)
    OsElementos = Livro("Os elementos",796921-27,75.00,"Euclides","Unesp",20)

    Pulp.Info()
    print()
    aCabana.Info()
    print()
    OsElementos.Info()