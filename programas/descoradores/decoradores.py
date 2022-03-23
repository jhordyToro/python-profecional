def mayusculas(func):
    def envoltura(text):
        return func(text).upper()
    return envoltura

@mayusculas
def mensaje(nombre):
    return f'{nombre} resiviste un mensaje'

print(mensaje('Jhordy'))