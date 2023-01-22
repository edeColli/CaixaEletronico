class caixaEletronico:
    def __init__(self, nome):
        self.notas = [100, 50, 20, 10, 5]
        self.nome_banco = nome
        self.total_notas = 5000

    def validarValor(self, valor):
        if (valor % 5) == 0 and (valor < self.total_notas):
            return True
        else:
            return False

    def sacar(self, valor_saque):
        if self.validarValor(valor_saque):
            while valor_saque > 0:
                for nota in self.notas:
                    quantidade = 0
                    while valor_saque >= nota:
                        quantidade += 1
                        valor_saque = valor_saque - nota

                    msg = f'{quantidade} nota de R$ {nota},00'
                    if quantidade > 0:
                        self.imprimir_resultado(msg)

        else:
            print("Valor informado não pode ser sacado!")

    def imprimir_resultado(self, notas_entregues):
        print(notas_entregues)


if __name__ == '__main__':
    caixa_Eletronico = caixaEletronico("Última bank")
    valor = int(input("Valor do saque: "))
    caixa_Eletronico.sacar(valor)
