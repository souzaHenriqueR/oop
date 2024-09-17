class Empresa:
    def __init__(self,nome,cnpj,endereco,servico):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.servico = servico

    def Info(self):
        print(f"Nome da empresa : {self.nome} ")
        print(f"CPNJ : {self.cnpj}")
        print(f"Endereço : {self.endereco}")
        print(f"Presta o seguinte serviço : {self.servico}")



if __name__ == "__main__":
    
    Termolar = Empresa("termolar","01298623-0001-87","Av Otto Nyemier", "Fabricação de garrafas termicas")
    Tharamps = Empresa("Tharamps","03476411-0001-77","Jundiai São Paulo","Fabricação de modulos de som")
    Nestle = Empresa("Nestle","09623488-0001-81","Curitiba Parana","Fabricação de chocolates")

    Termolar.Info()
    print()
    Tharamps.Info()
    print()
    Nestle.Info()