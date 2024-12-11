# sequence_alignment
# Comparación de Secuencias de ADN
Este proyecto utiliza dos secuencias en formato FASTA correspondientes al gen **HBB (Hemoglobina Beta)** de *Homo sapiens* y *Pan troglodytes*. El objetivo es realizar una comparación de ambas secuencias utilizando un script en Python.

---

## Archivos incluidos

- `NM_000518.fasta`: Secuencia FASTA del gen **HBB** en *Homo sapiens* (humano).
- `XM_508242.fasta`: Secuencia FASTA del gen **HBB** en *Pan troglodytes* (chimpancé).
- `alineamiento_prueba.py`: Código Python para comparar las secuencias. (solo compara cuando tienen igual longitud)
- `alimeamiento.py`: Código Python para comparar las secuencias.


---

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente:

1. Python 3.7 o superior.

---

## Explicación del código

El script realiza los siguientes pasos:
1. Carga las dos secuencias FASTA y las procesa para ignorar las líneas de encabezado.
2. Compara las secuencias carácter por carácter.
3. Imprime el número total de diferencias y su posición exacta en ambas cadenas.

    ## Ejemplo de salida
   Si las secuencias tienen diferencias, el programa imprimirá algo como esto:
   Contenido de NM_000518.fasta (Homo sapiens):
   ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAG
   Contenido de XM_508242.fasta (Pan troglodytes):
   ATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAG
   Comparando cadenas...
   Diferencia en posición 9: A != C
   Diferencia en posición 50: T != G
   Hay 2 diferencias
   
---

## Referencias
Secuencias obtenidas de NCBI GenBank:
- Homo sapiens: NM_000518
- Pan troglodytes: XM_508242
Herramientas adicionales:
BLAST para validar alineamientos.

