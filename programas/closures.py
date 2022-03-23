#nesecitamos tener una nested function
def superior(x):
    #la nested function debe referenciar un scope de orden superior
    def inferior(n):
        return x * n
    #la function que embuelve la nested debe retornarla tambien
    return inferior

if __name__ == '__main__':
    valor1 = superior(10)
    valor2 = superior(4)

    print(valor1(1))
    print(valor2(4))
    print(valor1(valor2(8)))