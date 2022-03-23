def minuscula(func):
    def texto(text):
        return func(text).lower()
    return texto
@minuscula
def texto(nombre):
    return f'HOLA {nombre}'
if __name__ == '__main__':
    print(texto('JHORDY'))