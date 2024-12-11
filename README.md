# sequence_alignment

# Comparación de Secuencias de ADN
Este proyecto utiliza dos secuencias en formato FASTA correspondientes al gen **HBB (Hemoglobina Beta)** de *Homo sapiens* y *Pan troglodytes*. El objetivo es realizar una comparación de ambas secuencias utilizando un script en Python.

---

## Archivos incluidos

- [`NM_000518.fasta`](https://github.com/amapolitav/sequence_alignment/blob/main/NM_000518.fasta): Secuencia FASTA del gen **HBB** en *Homo sapiens* (humano).
- [`XM_508242.fasta`](https://github.com/amapolitav/sequence_alignment/blob/main/XM_508242.fasta): Secuencia FASTA del gen **HBB** en *Pan troglodytes* (chimpancé).
- [`alineamiento_prueba.py`](./alineamiento_prueba.py): Código Python para comparar las secuencias (solo compara cuando tienen igual longitud).
- [`alineamiento.py`](https://github.com/amapolitav/sequence_alignment/blob/main/alimeamiento.py): Código Python para comparar las secuencias.

---

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente:

1. Python 3.7 o superior.
2. La librería `biopython` (puedes instalarla con `pip install biopython`).

---

## Explicación del código

El script realiza los siguientes pasos:

1. **Lectura de las secuencias FASTA:** Se leen los archivos FASTA y se procesan para eliminar encabezados y espacios, obteniendo las cadenas de ADN en formato limpio.
2. **Creación del alineador:** Se utiliza `PairwiseAligner` de Biopython para realizar alineamientos locales. Se configuran penalizaciones para abrir y extender gaps.
3. **Alineamiento de secuencias:** El script realiza el alineamiento local entre las dos secuencias y selecciona el mejor alineamiento.
4. **Cálculo de diferencias:** Se cuentan las diferencias entre ambas cadenas en el mejor alineamiento.
5. **Porcentaje de identidad:** Se calcula el porcentaje de identidad basado en el número de caracteres coincidentes entre las secuencias alineadas.
6. **Impresión de resultados:** Se muestra el mejor alineamiento, el total de diferencias y el porcentaje de identidad.

---

## Ejemplo de salida

```python
Secuencia Homo sapiens (NM_000518):
ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAG

Secuencia Pan troglodytes (XM_508242):
ATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAG

Mejor alineamiento:
ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAG
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
ATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAG

Diferencias totales: 2
Porcentaje de identidad: 97.37%
```

---

## Referencias

- Secuencias obtenidas de [NCBI GenBank](https://www.ncbi.nlm.nih.gov/genbank/):
  - *Homo sapiens*: [NM_000518](https://www.ncbi.nlm.nih.gov/nuccore/NM_000518)
  - *Pan troglodytes*: [XM_508242](https://www.ncbi.nlm.nih.gov/nuccore/XM_508242)
- Herramientas adicionales:
  - [BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi) para validar alineamientos.



