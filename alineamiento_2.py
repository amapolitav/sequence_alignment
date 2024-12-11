from Bio import pairwise2
from Bio.pairwise2 import format_alignment


# Leer y procesar el archivo NM_000518.fasta (Homo sapiens)
with open("NM_000518.fasta", "r") as fasta_human:
    secuencia1 = fasta_human.readlines()
    cadena1 = "".join(secuencia1[1:]).replace("\n", "").replace(" ", "")

# Leer y procesar el archivo XM_508242.fasta (Pan troglodytes)
with open("XM_508242.fasta", "r") as fasta_chimp:
    secuencia2 = fasta_chimp.readlines()
    cadena2 = "".join(secuencia2[1:]).replace("\n", "").replace(" ", "")

# Imprimir las secuencias cargadas para verificar
print("Secuencia Homo sapiens (NM_000518):")
print(cadena1)
print("\nSecuencia Pan troglodytes (XM_508242):")
print(cadena2)

# Realizar el alineamiento global entre las dos secuencias
alineamientos = pairwise2.align.globalxx(cadena1, cadena2)

# Imprimir el mejor alineamiento
print("\nMejor alineamiento:")
print(format_alignment(*alineamientos[0]))

# Extraer el mejor alineamiento y calcular diferencias
alineamiento1, alineamiento2, puntuacion, inicio, fin = alineamientos[0]

# Contar las diferencias
diferencias = sum(1 for a, b in zip(alineamiento1, alineamiento2) if a != b)

# Calcular porcentaje de identidad
identidad = sum(1 for a, b in zip(alineamiento1, alineamiento2) if a == b)
porcentaje_identidad = (identidad / len(alineamiento1)) * 100

# Imprimir resultados finales
print(f"\nDiferencias totales: {diferencias}")
print(f"Porcentaje de identidad: {porcentaje_identidad:.2f}%")
