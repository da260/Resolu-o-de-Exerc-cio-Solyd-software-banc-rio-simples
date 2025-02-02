# cria a conta do cliente
class conta :
    def __init__(self, saldo, limite,):
        self.saldo = saldo
        self.limite = 0 - limite
        
# cria a função depositar 
    def depositar(self, quant):
        if quant > 0:
            self.saldo += quant
            print("Foi depositado: ", quant)
        else:
            print("Erro no deposito")    

# cria a função consulta saldo
    def consulta_saldo (self):
        return self.saldo

# cria a função sacar    
    def sacar(self, quant):
        if self.saldo - quant < self.limite:
            print("Saldo insuficiente")
        else:    
            self.saldo -= quant
            print("Foi sacado: ", quant)
