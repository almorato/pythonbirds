class Pessoa:
    olhos = 2  # atributo de classe

    def __init__(self, *filhos, nome=None, idade=47):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    print(alan.olhos)
    print(Pessoa.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe())