#este valor solo esta esperando que le entregen un valor de tipo entero y espera retornar un bool
def primo(numero: int) -> bool:
    if numero % 2 == 0:
        return True
    else:
        return False

def main():
    #si le mandamos un str en ves de un int con Typing y mypy el error se levantara en tiempo de compilacion
    #en la terminal y con la libreria de mypy instalada y con los metodos typing con el comando "mypy <nombre del programa> --check-untyped-defs" 
    numero = 50
    primos = primo(numero)
    print(f'el numero {numero} {"es" if primos else "no es"} primo')

if __name__ == '__main__':
    main()
