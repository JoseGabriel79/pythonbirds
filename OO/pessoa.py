class Pessoa:
    def __init__(self,*filhos,nome=None,idade=19):
        self.idade = idade
        self.nome=nome
        self.filhos=list(filhos)
    def cumprimenta(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    jose=Pessoa(nome='José')
    luciano=Pessoa(jose,nome='Luciano')
    print(Pessoa.cumprimenta(luciano))
    print(id(luciano))
    print(luciano.cumprimenta())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)

