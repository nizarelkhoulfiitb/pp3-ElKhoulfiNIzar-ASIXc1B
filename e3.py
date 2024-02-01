"""
01/02/2023
Nizar El KHoulfi EL Harrak
ASIXcB e3 UF1
Encriptar una frase, siguiendo este orden "a = 0, b = 1 , ... etc" No acepta numeros y entre cada numero ha haber ":"
"""

try:
    frase = input()
    digitos = False

    for i in frase:
        if i.isdigit():
            digitos = True
            break

    if digitos:
        print("Solo acepto letras")
    else:
        frase_encriptada = ""
        previous_char = None

        for i in frase:
            if i.isalpha():
                x = ord(i.lower()) - ord('a')
                frase_encriptada += str(x) + ":"
            elif i.isspace():
                frase_encriptada += i

        print(frase_encriptada[:-1])

except:
    print("ERROR")

