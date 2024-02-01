"""
01/02/2024
Nizar El Khoulfi El Harrak
ASIXcB e2 UF1
Programa que pida el nombre de filas y columnas de una matriz (que sea cuadrada). Rellenar el marco con 1 y rellenar el resto con 0.
"""

try:
    fila = int(input())
    columnas = int(input())

    matriz = [[0] * columnas for _ in range(fila)]

    if fila != columnas or fila % 2 != 0:
        print("Error: La matriz debe ser cuadrada")
    else:
        for i in range(fila):
            for j in range(columnas):
                if i == 0 or i == fila - 1 or j == 0 or j == columnas - 1:
                    matriz[i][j] = 1

        print()
        for fila in matriz:
            print(fila)

except ValueError:
    print("Solo acepto numeros")
