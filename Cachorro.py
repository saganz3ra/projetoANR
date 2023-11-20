from Animal import Animal
class Cachorro(Animal):
    def __init__(self, especie, raca, nome, cor, idade, vacinas, pelo, garra):
        super().__init__ (especie, raca, nome, cor, idade)
        self.vacinas = vacinas
        self.pelo = pelo

    def emitir_som(self):
        print(f'O {self.nome}, está latindo')

    def morder(self):
        print(f'O {self.nome} acaba de morder um funcionario!')

    def correr(self):
        print(f'O {self.nome} está correndo, se divertindo!')