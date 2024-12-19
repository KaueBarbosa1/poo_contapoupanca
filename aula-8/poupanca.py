from conta import Conta
class ContaPoupanca(Conta):

   def __init__(self, numero):
       super().__init__(numero)

   def render_juros(self, taxa):
       self.creditar(self.get_saldo() * taxa)

class CriarPoupanca:
   if __name__ == '__main__':


       conta = Conta("21.342-7")
       conta = ContaPoupanca(conta)
       conta.creditar(500.87)
       conta.debitar(45.00)
       print(conta.get_saldo())

       conta.render_juros(0.01)
       print(conta.get_saldo())

class VerificaPoupanca:
   if __name__ == '__main__':
       opcao = int(input("Escolha: [1] Conta e [2] Poupanca:"))
       if opcao == 1:
            conta = Conta("21.342-7")
       else:
           conta = ContaPoupanca("21.342-7")

       conta.creditar(500.87)
       conta.debitar(45.00)

       if isinstance(conta, ContaPoupanca):
           conta.render_juros(0.1)
           print("Saldo com juros: {}".format(conta.get_saldo()))
