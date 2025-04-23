---
title: Utilizzo della funzione FormulaText in Aspose.Cells con Python.NET
linktitle: Uso della funzione FormulaText
type: docs
weight: 60
url: /it/python-net/using-formulatext-function-in-aspose-cells/
description: Impara come lavorare con la funzione FORMULATEXT di Excel usando Aspose.Cells per Python via .NET. Ottieni e imposta le formule delle celle programmaticamente mantenendo l integrità del foglio di calcolo.
keywords: Aspose.Cells, Python, Excel, FORMULATEXT, gestione delle formule, automazione dei fogli di calcolo
---

{{% alert color="primary" %}} 

FORMULATEXT è una funzione di Excel 2013 e versioni successive. Non è supportata da versioni precedenti come Excel 2010 o 2007, ecc. Come suggerisce il nome, visualizza il testo della formula contenuta in una cella specificata. Questo articolo dimostra come usare questa funzione con Aspose.Cells for Python via .NET.

{{% /alert %}} 

Il seguente esempio di codice dimostra l'uso di FORMULATEXT con Aspose.Cells. Il codice prima scrive una formula nella cella A1 e poi visualizza il testo della formula usando FORMULATEXT nella cella A2.

```python
from aspose.cells import Workbook

# Create a workbook object
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Put some formula in cell A1
cell_a1 = worksheet.cells.get("A1")
cell_a1.formula = "=Sum(B1:B10)"

# Get the text of the formula in cell A2 using FORMULATEXT function
cell_a2 = worksheet.cells.get("A2")
cell_a2.formula = "=FormulaText(A1)"

# Calculate the workbook
workbook.calculate_formula()

# Print the results of A2, It will now print the text of the formula inside cell A1
print(cell_a2.string_value)
```

## **Output della console**
Ecco la visualizzazione sulla console del codice di esempio sopra descritto:

{{< highlight python >}}
=SUM(B1:B10)
{{< /highlight >}}
