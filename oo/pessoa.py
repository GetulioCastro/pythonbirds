class Pessoa:
    def cumprimentar(self):
        return f'Olá Mundo! {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())

