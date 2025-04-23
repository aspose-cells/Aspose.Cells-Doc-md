---
title: Ajouter des cellules à la fenêtre de surveillance des formules de Microsoft Excel avec Python.NET
linktitle: Ajouter des cellules à la fenêtre de surveillance des formules
type: docs
weight: 60
url: /fr/python-net/add-cells-to-microsoft-excel-formula-watch-window/
description: Apprenez comment surveiller les cellules dans la fenêtre de surveillance des formules d Excel en utilisant Aspose.Cells pour Python via .NET. Inclut des exemples de code et des références API.
keywords: python excel, fenêtre de surveillance des formules, surveillance des cellules, aspose.cells, python.net
---

## **Scénarios d'utilisation possibles**

La fenêtre d'observation de Microsoft Excel est un outil utile pour surveiller facilement les valeurs et les formules des cellules dans une fenêtre dédiée. Vous pouvez ouvrir la *Fenêtre d'observation* dans Microsoft Excel en naviguant vers *Formules > Fenêtre d'observation*. Le bouton *Ajouter une observation* permet d'ajouter des cellules pour inspection. De même, vous pouvez utiliser la méthode [**Worksheet.cell_watches.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/cellwatchcollection/add/) pour ajouter programmétiquement des cellules à la Fenêtre d'observation en utilisant l'API Aspose.Cells.

## **Ajouter des cellules à la fenêtre de surveillance des formules Microsoft Excel**

Le code d'exemple suivant définit des formules pour les cellules C1 et E1, puis ajoute les deux à la Fenêtre d'observation. Il enregistre le classeur sous [fichier Excel de sortie](67338481.xlsx). Lors de l'ouverture du fichier de sortie dans Excel, les deux cellules apparaîtront dans la Fenêtre d'observation comme indiqué :

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Code d'exemple**

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
