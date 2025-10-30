---
title: Calcolo della funzione IFNA con Python.NET usando Aspose.Cells
linktitle: Calcolo della funzione IFNA
type: docs
weight: 40
url: /it/python-net/calculating-ifna-function-using-aspose-cells/
description: Impara come calcolare la funzione IFNA nei file Excel usando Aspose.Cells per Python.NET. Gestisci errori #N/A e salva in modo efficiente i fogli di calcolo modificati.
keywords: Python.NET, Excel, funzione IFNA, Aspose.Cells, gestione errori, calcolo foglio di calcolo
---

{{% alert color="primary" %}}

Aspose.Cells per Python.NET supporta il calcolo della funzione Excel IFNA. La funzione IFNA restituisce un valore specificato se una formula produce errore #N/A; altrimenti restituisce il risultato della formula.

{{% /alert %}}

## **Calcolo della funzione IFNA in Python.NET**

Il seguente esempio di codice dimostra come calcolare la funzione IFNA usando Aspose.Cells per Python.NET:


## **Output della console**
 Il codice sopra produrrà il seguente output sulla console:

```
Not found
Orange
```

## **Spiegazione dei Passaggi Chiave**
1. Crea una nuova istanza di [`Workbook`](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)
2. Accedi al foglio di lavoro e alla collezione di celle
3. Popola i dati sorgente nella colonna A
4. Imposta formule VLOOKUP che possono produrre errori #N/A
5. Usa IFNA per gestire potenziali errori
6. Calcola le formule usando [`calculate_formula()`](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/)
7. Recupera e visualizza i risultati dalle celle gestite per errori
8. Salva il workbook modificato con i risultati del calcolo

```python
import os
from aspose.cells import Workbook

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Create new workbook
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Add data for VLOOKUP
cells = worksheet.cells
cells.get("A1").put_value("Apple")
cells.get("A2").put_value("Orange")
cells.get("A3").put_value("Banana")

# Access cell A5 and A6
cell_a5 = worksheet.cells.get("A5")
cell_a6 = worksheet.cells.get("A6")

# Assign IFNA formula to A5 and A6
cell_a5.formula = "=IFNA(VLOOKUP(\"Pear\",$A$1:$A$3,1,0),\"Not found\")"
cell_a6.formula = "=IFNA(VLOOKUP(\"Orange\",$A$1:$A$3,1,0),\"Not found\")"

# Calculate the formula of workbook
workbook.calculate_formula()

# Print the values of A5 and A6
print(cell_a5.string_value)
print(cell_a6.string_value)
```
{{< app/cells/assistant language="python-net" >}}
