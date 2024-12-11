# Abrir y procesar el archivo NM_000518.fasta (Homo sapiens)
with open("NM_000518.fasta", "r") as fasta_human:
    secuencia1 = fasta_human.readlines()
    cadena1 = "".join(secuencia1[1:]).replace("\n", "")
print("Contenido de NM_000518.fasta (Homo sapiens):")
print(cadena1)

# Abrir y procesar el archivo XM_508242.fasta (Pan troglodytes)
with open("XM_508242.fasta", "r") as fasta_chimp:
    secuencia2 = fasta_chimp.readlines()
    cadena2 = "".join(secuencia2[1:]).replace("\n", "")
print("Contenido de XM_508242.fasta (Pan troglodytes):")
print(cadena2)

# Ajustar las longitudes si son diferentes
if len(cadena1) != len(cadena2):
    print("Las secuencias tienen longitudes diferentes.")
    # Opción 1: Recortar al mínimo común
    min_length = min(len(cadena1), len(cadena2))
    cadena1 = cadena1[:min_length]
    cadena2 = cadena2[:min_length]
    print(f"Las secuencias se recortaron a {min_length} caracteres.")
    # Opción 2: Rellenar con gaps (descomenta si prefieres esta opción)
    # max_length = max(len(cadena1), len(cadena2))
    # cadena1 = cadena1.ljust(max_length, '-')
    # cadena2 = cadena2.ljust(max_length, '-')

# Comparar las cadenas
Longitud1 = len(cadena1)
Longitud2 = len(cadena2)

if Longitud1 == Longitud2:
    print("Comparando cadenas...")
    N = 0  # Contador de diferencias
    for i in range(Longitud1):
        if cadena1[i] != cadena2[i]:
            print(f"Diferencia en posición {i}: {cadena1[i]} != {cadena2[i]}")
            N += 1
    print(f"Hay {N} diferencias")
else:
    print("No se pueden comparar las cadenas.")
