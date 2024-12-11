# Procesar el archivo NM_000518.fasta (Homo sapiens)
with open("NM_000518.fasta", "r") as fasta_human:
    # Leer todas las líneas del archivo
    secuencia1 = fasta_human.readlines()
    # Unir las líneas desde la segunda línea (ignorar el encabezado)
    cadena1 = "".join(secuencia1[1:]).replace("\n", "")
print("Contenido de NM_000518.fasta (Homo sapiens):")
print(cadena1)

# Procesar el archivo XM_508242.fasta (Pan troglodytes)
with open("XM_508242.fasta", "r") as fasta_chimp:
    # Leer todas las líneas del archivo
    secuencia2 = fasta_chimp.readlines()
    # Unir las líneas desde la segunda línea (ignorar el encabezado)
    cadena2 = "".join(secuencia2[1:]).replace("\n", "")
print("Contenido de XM_508242.fasta (Pan troglodytes):")
print(cadena2)

# Comparar las cadenas
Longitud1 = len(cadena1)
Longitud2 = len(cadena2)

if Longitud1 == Longitud2:
    print("Comparando cadenas...")
    N = 0  # Contador de diferencias
    # Recorrer cada carácter de las cadenas
    for i in range(Longitud1):
        if cadena1[i] != cadena2[i]:
            print(f"Diferencia en posición {i}: {cadena1[i]} != {cadena2[i]}")
            N += 1
    print(f"Hay {N} diferencias")
else:
    print("No se pueden comparar las cadenas: tienen longitudes diferentes.")


