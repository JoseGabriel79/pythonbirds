class Pessoa:
    def cumprimenta(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p=Pessoa()
    print(Pessoa.cumprimenta(p))
    print(id(p))
    print(p.cumprimenta())