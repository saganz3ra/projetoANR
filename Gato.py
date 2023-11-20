from Animal import Animal
class Gato(Animal):
    def __init__(self, especie, raca, nome, cor, idade, pelo, garra):
        super().__init__(especie, raca, nome, cor, idade)
        self.pelo = pelo
        self.garra = garra

    def emitir_som(self):
        print(f'O {self.nome} esta miando!')

    def morder(self):
        print(f'O {self.nome} mordeu um funcionario!')

    def correr(self):
        print(f'O {self.nome} esta correndo, se divertindo!')
       