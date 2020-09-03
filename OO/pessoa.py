class Pessoa:
    def __init__(self,nome=None,idade=19):
        self.idade = idade
        self.nome=nome
    def cumprimenta(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p=Pessoa('luviola')
    print(Pessoa.cumprimenta(p))
    print(id(p))
    print(p.cumprimenta())
    print(p.nome)
    p.nome='José'
    print(p.nome)
    print(p.idade)

