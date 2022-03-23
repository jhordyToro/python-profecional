def funcion(func):
    def darck(*args, **kwargs):
        func(*args, **kwargs)
        return print('soy tu padre Luke')
    return darck

@funcion
def Luke():
    print('quien eres tu dark blader')

Luke() 
