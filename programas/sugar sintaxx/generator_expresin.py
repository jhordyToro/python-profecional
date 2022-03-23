import time 

def fibonacci(num_max: int) -> int:
    num_max = num_max
    n1 = 0
    n2 = 1
    contador = 0
    while True:
        if contador == 0:
            contador += 1
            yield n1
        elif contador == 1:
            contador += 1
            yield n2
        else:
            n3 = n1 + n2
            if n3 >= num_max:
                raise StopIteration
            else:    
                n1,n2 =  n2,n3
                yield n3

if __name__ == '__main__':
    num = int(input('hasta que punto quiere que llegue el fibonacci? '))
    value = fibonacci(num)
    for element in value:
        print(element)
        time.sleep(0.05)