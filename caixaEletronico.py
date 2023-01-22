class caixaEletronico:
    def __init__(self, nome):
        self.notas = {100: 10, 50: 25, 20: 100, 10: 200, 5: 200}
        self.nome_banco = nome
        self.total_notas = 0

        for k, v in self.notas.items():
            valor = k * v
            self.total_notas = self.total_notas + valor

    def validarValor(self, valor):
        if (valor % 5) == 0 and (valor < self.total_notas):
            return True
        else:
            return False

    def sacar(self, valor_saque):
        sacado = []
        saque_efetuado = True
        if self.validarValor(valor_saque):
            while valor_saque > 0:
                for nota in self.notas:
                    quantidade = 0
                    quantidade_de_notas_no_caixa = self.notas[nota]
                    while valor_saque >= nota:
                        quantidade += 1
                        if quantidade_de_notas_no_caixa >= quantidade:
                            valor_saque = valor_saque - nota
                        else:
                            quantidade -= 1
                            break

                    if quantidade > 0:
                        sacado.append(f'{quantidade} nota de R$ {nota},00')

                if (len(self.notas) == 5 and valor_saque > 0):
                    print('Saldo insuficiente, não foi possível realiza o saque')
                    saque_efetuado = False

            if saque_efetuado:
                self.imprimir_resultado(sacado)
        else:
            print("Valor informado não pode ser sacado!")

    def imprimir_resultado(self, notas_entregues):
        print(', '.join(notas_entregues))


if __name__ == '__main__':
    caixa_Eletronico = caixaEletronico("Última bank")
    valor = int(input("Valor do saque: "))
    caixa_Eletronico.sacar(valor)
