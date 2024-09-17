from datetime import date


class Usuario:
    def __init__(self,nomeUsuario,senha,email,dataNasc):
        self.nomeUsuario = nomeUsuario
        self.senha = senha
        self.email = email
        self.dataNasc = dataNasc
        
    
    def info(self):
        print(f"Nome de usuario : {self.nomeUsuario}")
        print(f"email : {self.email}")
        print(f"data de nascimento : {self.dataNasc}")
        print(f"Senha atual : {self.senha}")

    def alterarSenha(self):
        
        senhaAtual = self.senha
        def validarSenha(self):
            tentativaSenha = input("Informe a senha atual : ")
            
            if (tentativaSenha != senhaAtual):
                return False
            
            return True    
               
        if validarSenha(self):            
            novaSenha = input("Informe qual será a nova senha : ")
            novaSenhaVerificacao = input("Digite a mesma senha novamente : ")
            
            if (novaSenha != novaSenhaVerificacao):
                return False
            
            elif (novaSenha == novaSenhaVerificacao):
                self.senha = novaSenha                          
                                
                             
                    
                                                      
if __name__ == "__main__":
    
    user1 = Usuario("f4ther","123","henrique@gmail.com",date(2001,4,9))
    user1.info()
    
    user1.alterarSenha()
    user1.info()