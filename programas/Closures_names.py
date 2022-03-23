
# def name(nombre: str):
    # assert type(name) == str, 'solo puedes uyilizar nombres'
#     def counter(numero: int):
#         return nombre * numero

#     return counter

# def main():
#     nombre = name('jhordy')
#     nombre2 = name('facundo')

#     print(nombre(5))
#     print(nombre2(2))

# if __name__ == '__main__':
#     main()

#TAMBIEN SE PUEDE HACER DE LA MANERA CONTRARIA 

def contador(numero: int):
    def nombre(name: str):
        assert type(name) == str, 'solo puedes uyilizar nombres'
        return numero * name 

    return nombre

def main():
    nombre = contador(5)
    nombre2 = contador(2)

    print(nombre('jhordy'))
    print(nombre2('jhovana'))
    print(nombre(nombre2('jhordy')))
if __name__ == '__main__':
    main()