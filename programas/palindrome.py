def palindrome(palabra: str) -> bool:
    palabra.replace(' ','').lower()
    palabra_invertida = palabra[::-1]
    return palabra == palabra_invertida

def main():
    palabra = 'mile'
    palindrom = palindrome(palabra)
    print(f'la palabra {"es" if palindrom else "no es"} un palindrome')

if __name__ == '__main__':
    main()