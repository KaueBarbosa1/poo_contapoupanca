from conta import Conta
from poupanca import ContaPoupanca
class BancoLista:
    def __init__(self, taxa_juros=0.01):
        self.contas = [None] * 100
        self.indice = 0
        self.taxa_juros = taxa_juros

    def cadastrar(self, conta: Conta):
        self.contas[self.indice] = conta
        self.indice += 1

    def procurar_conta(self, numero):
        i = 0
        achou = False
        while achou is False and i < self.indice:
            if self.contas[i].get_numero() == numero:
                achou = True
            else:
                i += 1
        if achou is True:
            return self.contas[i]
        else:
            return None

    def debitar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.debitar(valor)
        else:
            print("conta Inexistente")

    def creditar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.creditar(valor)
        else:
            print("conta inexistente")

    def transferir(self, numero_origem, numero_destino, valor):
        conta_origem = self.procurar_conta(numero_origem)
        conta_destino = self.procurar_conta(numero_destino)
        if conta_origem and conta_destino:
            if conta_origem.get_saldo() >= valor:
                conta_origem.debitar(valor)
                conta_destino.creditar(valor)
                print("transferência realizada com sucesso")
            else:
                print("saldo insuficiente para transferência")
        else:
            print("conta origem ou destino inexistente")

    def saldo(self, numero):
        conta = self.procurar_conta(numero)
        if conta:
            return conta.get_saldo()
        else:
            print("conta inexistente")
            return None

    def render_juros(self, numero):
        conta = self.procurar_conta(numero)
        if isinstance(conta, ContaPoupanca):
            juros = conta.get_saldo() * self.taxa_juros
            conta.creditar(juros)
            print(f"Juros de {juros:.2f} aplicados a conta {numero}.")
        else:
            print("conta inexistente")

if __name__ == "__main__":
    banco = BancoLista(taxa_juros=0.02)
    conta_poupanca = ContaPoupanca("12345")
    conta_poupanca.creditar(1000)

    banco.cadastrar(conta_poupanca)
    banco.render_juros("12345")

    print(f"Saldo da conta após render juros: {banco.saldo('12345')}")