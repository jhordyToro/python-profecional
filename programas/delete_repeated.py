#ELIMINANDO ELEMENTOS REPETIDOS EN UNA LISTA DE LA MANERA TRADICIONAL
# def nose(list):
#     list_repeate = []
#     for element in list:
#         if element not in list_repeate:
#             list_repeate.append(element)

#     return list_repeate

# def main():
#     list = [1,1,2,2,4]
#     print(nose(list))

# if __name__ == '__main__':
#     main()


#ELIMINANDO ELEMENTOS REPETIDOS EN UNA LISTA CON SETS

def sets(lista):
    lista_repeate = set(lista)
    lista = list(lista_repeate)
    return lista

def main():
    list = [1,1,2,2,3,3,4]
    print(sets(list))

if __name__ == '__main__':
    main()