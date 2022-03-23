def caja(func):
    def bordes(text):
        print(' ' + '_' * (1 + len(text)))
        print('/' + '_' * len(text) + '/|')
        print('|' + ' ' * len(text) + '||')
        func('|' + text + '||')
        print('|' + '_' * len(text) + '|/')
    return bordes
@caja
def texto(parrafo):
    print(parrafo)

def main():
    parrafo = input('escribe algo ')
    texto(parrafo)

if __name__ == '__main__':
    main()