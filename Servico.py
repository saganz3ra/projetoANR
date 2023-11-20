class Servico:
    def __init__(self, valor):
        self.valor = valor
        self.servicos = []

    def servico(self):
        print("Nossos serviços:\n"
              "Banho:        R$35,00\n"
              "Tosa:         R$30,00\n"
              "Passeio:      R$30,00\n"
              "Cortar unhas  R$25,00\n")

    def tosar(self):
        self.valor = self.valor + 30.00
        self.servicos.append("Servico de tosa:            R$30,00")

    def banhar(self):
        self.valor = self.valor + 35.00
        self.servicos.append("Servico de banho:           R$35,00")

    def passear(self):
        self.valor = self.valor + 30.00
        self.servicos.append("Servico de passeio:         R$30,00")

    def cortar_garra(self):
        self.valor = self.valor + 25.00
        self.servicos.append("Servico corte de garras:    R$25,00")

    def nota(self):
        print("Esses foram os servicos: ")
        for i in self.servicos:
            print(i)
        print("O valor a ser pago é:       R$", self.valor)

    def pausar(self):
        print("\n==========================================================\n")