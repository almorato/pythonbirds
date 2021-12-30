class Pessoa:
    olhos = 2  # atributo de classe

    def __init__(self, *filhos, nome=None, idade=47):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    abner = Pessoa(nome='Abner')
    alan = Pessoa(abner, nome='Alan')
    print(alan.cumprimentar())
    print(alan.nome)
    print(alan.idade)
    for filho in alan.filhos:
        print(filho.nome)

    print(alan.__dict__)  # mantém apenas os atributos de instância
    print(abner.__dict__)