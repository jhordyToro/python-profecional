def divisor(n: int):
    def dividendo(y: int):
        return y // n

    return dividendo 

def main():
    divisor_3 = divisor(3)
    print(divisor_3(18))
    divisor_5 = divisor(5)
    print(divisor_5(100))
    divisor_18 = divisor(18)
    print(divisor_18(54))

if __name__ == '__main__':
    main()

