---
title: Aggiungi Celle alla Finestra di Monitoraggio delle Formule di Microsoft Excel con Python.NET
linktitle: Aggiungi celle alla finestra di watch della formula
type: docs
weight: 60
url: /it/python-net/add-cells-to-microsoft-excel-formula-watch-window/
description: Impara come monitorare le celle nella Finestra di Monitoraggio delle Formule di Excel usando Aspose.Cells per Python via .NET. Include esempi di codice e riferimenti API.
keywords: python excel, finestra di monitoraggio delle formule, monitoraggio celle, aspose.cells, python.net
---

## **Possibili Scenari di Utilizzo**

La Finestra di Monitoraggio di Microsoft Excel è uno strumento utile per monitorare comodamente i valori delle celle e le formule in una finestra dedicata. Puoi aprire la *Finestra di Monitoraggio* in Microsoft Excel navigando su *Formule > Finestra di Monitoraggio*. Il pulsante *Aggiungi Monitoraggio* consente di aggiungere celle per l'ispezione. Allo stesso modo, puoi usare il metodo [**Worksheet.cell_watches.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/cellwatchcollection/add/) per aggiungere programmaticamente celle alla Finestra di Monitoraggio usando l'API Aspose.Cells.

## **Aggiungere celle alla finestra di visualizzazione della formula di Microsoft Excel**

Il seguente esempio di codice imposta le formule nelle celle C1 ed E1, e poi aggiunge entrambe alla Finestra di Monitoraggio. Salva il workbook come [file Excel di output](67338481.xlsx). Aprendo il file di output in Excel, entrambe le celle appariranno nella Finestra di Monitoraggio come mostrato:

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Codice di Esempio**

```python
from aspose.cells import Workbook, SaveFormat

# Create empty workbook.
wb = Workbook()

# Access first worksheet.
ws = wb.worksheets[0]

# Put some integer values in cell A1 and A2.
ws.cells.get("A1").put_value(10)
ws.cells.get("A2").put_value(30)

# Access cell C1 and set its formula.
c1 = ws.cells.get("C1")
c1.formula = "=Sum(A1,A2)"

# Add cell C1 into cell watches by name.
ws.cell_watches.add(c1.name)

# Access cell E1 and set its formula.
e1 = ws.cells.get("E1")
e1.formula = "=A2*A1"

# Add cell E1 into cell watches by its row and column indices.
ws.cell_watches.add(e1.row, e1.column)

# Save workbook to output XLSX format.
wb.save("outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", SaveFormat.XLSX)
```
{{< app/cells/assistant language="python-net" >}}
