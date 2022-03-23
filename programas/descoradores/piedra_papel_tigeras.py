import random

def juego(func):
    def envoltorio(mano):
        jugadas = ['piedra','papel','tigeras']
        pc = random.choice(jugadas)
        print(f'la PC juega {pc}')
        func(mano)
        if pc == 'tigeras' and mano == 'piedra' \
            or pc == 'piedra' and mano == 'papel'\
            or pc == 'papel' and mano == 'tigeras':
            print('ganaste')
        elif pc == mano:
            print('empate')
        else:
            print('perdiste')
    return envoltorio




@juego
def humano(mano):
    print(f'tu jugada es {mano}')

def main():
    mano = input('cual es tu jugada? ')
    mano.lower()
    humano(mano)


if __name__ == '__main__':
    main()
