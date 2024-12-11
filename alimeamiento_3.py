from Bio.Align import PairwiseAligner

# Leer y procesar las secuencias FASTA
with open("NM_000518.fasta", "r") as fasta_human:
    secuencia1 = fasta_human.readlines()
    cadena1 = "".join(secuencia1[1:]).replace("\n", "").replace(" ", "")

with open("XM_508242.fasta", "r") as fasta_chimp:
    secuencia2 = fasta_chimp.readlines()
    cadena2 = "".join(secuencia2[1:]).replace("\n", "").replace(" ", "")

# Imprimir las secuencias cargadas
print("Secuencia Homo sapiens (NM_000518):")
print(cadena1)
print("\nSecuencia Pan troglodytes (XM_508242):")
print(cadena2)

# Crear alineador
aligner = PairwiseAligner()
aligner.mode = "local"  # Alineamiento local
aligner.open_gap_score = -5  # Penalización por abrir un gap
aligner.extend_gap_score = -2  # Penalización por extender un gap

# Realizar el alineamiento
alineamientos = aligner.align(cadena1, cadena2)

# Obtener el mejor alineamiento
mejor_alineamiento = alineamientos[0]
alineamiento1 = mejor_alineamiento.target
alineamiento2 = mejor_alineamiento.query

# Imprimir alineamiento
print("\nMejor alineamiento:")
print(mejor_alineamiento)

# Contar diferencias
diferencias = sum(1 for a, b in zip(alineamiento1, alineamiento2) if a != b)

# Calcular porcentaje de identidad
identidad = sum(1 for a, b in zip(alineamiento1, alineamiento2) if a == b)
porcentaje_identidad = (identidad / len(alineamiento1)) * 100

# Imprimir resultados finales
print(f"\nDiferencias totales: {diferencias}")
print(f"Porcentaje de identidad: {porcentaje_identidad:.2f}%")
