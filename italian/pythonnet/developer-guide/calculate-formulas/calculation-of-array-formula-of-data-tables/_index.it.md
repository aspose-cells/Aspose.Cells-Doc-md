---
title: Calcolo della formula array delle tabelle di dati con Python.NET
linktitle: Calcolo della Formula Array delle Tabelle Dati
type: docs
weight: 70
url: /it/python-net/calculation-of-array-formula-of-data-tables/
description: Impara come calcolare le formule array per le tabelle di dati Excel usando l API Aspose.Cells per Python via .NET. Modifica e salva i fogli di calcolo programmaticamente.
keywords: Python Excel Data Tables, Formule Array Python, Aspose.Cells Python, Calcolo Tabelle di Dati Python, Automazione Excel Python
---

{{% alert color="primary" %}}

Puoi creare una tabella di dati in Microsoft Excel usando Dati > Analisi What-If > Tabella di Dati.... Aspose.Cells per Python via .NET consente di calcolare la formula array di una tabella di dati. Usa [**workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) come normale per calcolare qualsiasi tipo di formula.

{{% /alert %}}

Nell'esempio seguente, utilizziamo il [file Excel di origine](5115535.xlsx). Se cambi il valore della cella B1 a 100, i valori della Tabella di Dati (evidenziati in giallo) si aggiorneranno a 120 come mostrato negli screenshot di seguito. Il codice Python genera questo [PDF di output](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Di seguito l'implementazione Python che dimostra come generare il [PDF di output](5115538.pdf) dal [file Excel di origine](5115535.xlsx):

```python
import os
from aspose.cells import Workbook

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Create workbook from source excel file
workbook = Workbook(os.path.join(data_dir, "DataTable.xlsx"))

# Access first worksheet
worksheet = workbook.worksheets[0]

# When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
worksheet.cells.get("B1").put_value(100)

# Calculate formula, now it also calculates Data Table array formula
workbook.calculate_formula()

# Save the workbook in pdf format
workbook.save(os.path.join(data_dir, "output_out.pdf"))
```

**Spiegazione del Codice Python:**
```python
import aspose.cells as ac

# Load source workbook
workbook = ac.Workbook("5115535.xlsx")

# Calculate formulas using Python.NET API
workbook.calculate_formula()

# Save the workbook in PDF format
workbook.save("5115538.pdf", ac.SaveFormat.PDF)
```
