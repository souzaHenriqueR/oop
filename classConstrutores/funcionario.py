
class Funcionario:
    def __init__(self,nome,sobrenome,cpf,salario,cargo):
        self.nome=nome
        self.sobrenome=sobrenome
        self.cpf=cpf
        self.salario=salario
        self.cargo=cargo

    def Info(self):
        print(f"Nome : {self.nome} {self.sobrenome}")
        print(f"cpf : {self.cpf}")
        print(f"salario R$ : {self.salario}")
        print(f"cargo : {self.cargo}")
        
        
        
    def modificarSalario(self,novoSalario):
        if (novoSalario > 0):
            self.salario = novoSalario
        
        return "Valor invalido"
    
    def modificarCargo(self,novoCargo):
        if (novoCargo != " "):
            self.cargo = novoCargo
        
if __name__ == "__main__":

    Carlos = Funcionario("Carlos","Eduardo Souza","012987344-27",1800,"Padeiro")
    Julio = Funcionario("Julio","Nascimento Costa","033986872-23",1400,"Auxiliar Enfermagem")
    Maria = Funcionario("Maria","Nunes","341753872-38",2200,"Sub gerente")

    Carlos.Info()
    print()
    Julio.Info()
    print()
    Maria.Info()
    
    Maria.modificarCargo("Analista Contábil")
    Maria.modificarSalario(3500.00)
    Carlos.modificarSalario(1800.00)
    Maria.Info()
    Carlos.Info()