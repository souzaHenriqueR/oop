class contaBancaria:
    def __init__(self,titular_conta,saldo,valor_deposito=0,valor_saque=0):
        self.__titular_conta = titular_conta
        self.__saldo = saldo
        self.__deposito = valor_deposito
        self.__saque = valor_saque

    def get_titular_conta(self):
        print(self.__titular_conta)

    def set_titular_conta(self,nome):
        self.__titular_conta = nome

    def get_saldo(self):
        return print(self.__saldo)

    def set_depositar(self,valor_deposito):
        self.__saldo += valor_deposito

    def set_sacar(self,valor_saque):
        if ( valor_saque > self.__saldo):
            print("Saldo insuficiente")
        elif (valor_saque <= self.__saldo):
            self.__saldo -= valor_saque



if __name__ == "__main__":


    conta_cliente = contaBancaria("henrique rodrigues",2500,)

    conta_cliente.get_titular_conta()
    conta_cliente.set_titular_conta("Carlos Eduardo")
    conta_cliente.get_titular_conta()


    conta_cliente.get_saldo()
    conta_cliente.set_depositar(250)
    conta_cliente.get_saldo()

    conta_cliente.set_sacar(1500)
    conta_cliente.get_saldo()
    conta_cliente.set_sacar(5000)
