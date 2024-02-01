"""
01/02/2024
Nizar EL Khoulfi El Harrak
ASIXcB e1 UF1
Programa que acepte 100000 palabras y calcule cual es la mas larga, la mas corta y la media de palabras. SOlo acepta palabras. Despúes copiar todas las palabras a una tupla.
"""

PALABRA = 0
TOTAL_PAL = 0
palabra_larga = ""
palabra_corta = ""

try:
    while True:
        palabra = input()

        if palabra == "\\q":
            break

        if not palabra.isnumeric() and palabra.isalpha():
            PALABRA += 1
            TOTAL_PAL += len(palabra)

            if not palabra_larga or len(palabra) > len(palabra_larga):
                palabra_larga = palabra

            if not palabra_corta or len(palabra) < len(palabra_corta):
                palabra_corta = palabra
        else:
            print("Solo palabras")

    if PALABRA > 0:
        media_palabras = TOTAL_PAL / PALABRA
        print("\nPalabra más larga:", palabra_larga)
        print("Palabra más corta:", palabra_corta)
        print("Media de longitud de palabras:", media_palabras)

except Exception as ex:
    print("Error:", str(ex))
