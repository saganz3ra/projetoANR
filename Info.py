class Info():
    def __init__(self, especie, raca, nome, cor, idade):
        self.especie = especie
        self.raca = raca
        self.nome = nome
        self.cor = cor
        self.idade = idade

    def dados(self):
        print("Agora confime se todos os dados estão certos!")
        print(f'A especie de seu animal é: {self.especie}')
        print(f'A raça de seu {self.especie} é: {self.raca}')
        print(f'O nome de seu {self.especie} é: {self.nome}')
        print(f'A cor de seu {self.especie} é: {self.cor}')
        print(f'A idade de seu Gato é: {self.idade}')

        certo = input("\nSe está tudo certo digite sim: ")
        certo = certo.upper()
        print("\n==========================================================\n")
        if certo == "SIM":
            print(f'Seu {self.especie} está indo para seu atendimento!')

    def abrir_arquivo(self, pelo, banho, passear, garra):
        nome_arquivo = 'pedidos.txt'

        # Gravar as frases no arquivo
        with open(nome_arquivo, 'w') as nome_arquivo:
            nome_arquivo.write(f'Animal antendido: {self.especie}\n')
            nome_arquivo.write(f'Nome do {self.especie}: {self.nome}\n')
            nome_arquivo.write(f'raça do {self.especie}: {self.raca}\n')
            nome_arquivo.write(f'Cor do {self.especie}: {self.cor}\n')
            nome_arquivo.write(f'Idade do {self.especie}: {self.idade}\n')
            nome_arquivo.write(f'Serviços:\n')
            nome_arquivo.write(f'Serviço de corte de garras: {garra}\n')
            nome_arquivo.write(f'Serviço de tosa: {pelo}\n')
            nome_arquivo.write(f'Serviço de banho: {banho}\n')
            nome_arquivo.write(f'Serviço de passeio com animal: {passear}\n')
            nome_arquivo.write("Fim de relatorio!")