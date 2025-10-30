---
title: Zellen zum Microsoft Excel Formelüberwachungsfenster mit Python.NET hinzufügen
linktitle: Zellen zum Formelausblick Fenster hinzufügen
type: docs
weight: 60
url: /de/python-net/add-cells-to-microsoft-excel-formula-watch-window/
description: Erfahren Sie, wie Sie Zellen im Excel Formelüberwachungsfenster mit Aspose.Cells für Python via .NET überwachen. Enthält Codebeispiele und API Referenzen.
keywords: Python Excel, Formelüberwachungsfenster, Zellüberwachung, aspose.cells, python.net
---

## **Mögliche Verwendungsszenarien**

Das Überwachungsfenster von Microsoft Excel ist ein nützliches Werkzeug, um Zellwerte und Formeln bequem in einem eigenen Fenster zu überwachen. Sie können das *Watch Window* in Microsoft Excel öffnen, indem Sie zu *Formeln > Watch Window* navigieren. Der *Add Watch*-Button erlaubt es, Zellen zur Überwachung hinzuzufügen. Ebenso können Sie die [**Worksheet.cell_watches.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/cellwatchcollection/add/)-Methode nutzen, um Zellen programmatisch zum Watch Window mit Aspose.Cells API hinzuzufügen.

## **Zellen zur Microsoft Excel-Formelüberwachung hinzufügen**

Der folgende Beispielcode setzt Formeln für die Zellen C1 und E1 und fügt beide zum Watch Window hinzu. Das Arbeitsblatt wird als [Ausgabedatei Excel](67338481.xlsx) gespeichert. Beim Öffnen der Ausgabedatei in Excel werden beide Zellen im Watch Window wie folgt angezeigt:

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Beispielcode**

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
