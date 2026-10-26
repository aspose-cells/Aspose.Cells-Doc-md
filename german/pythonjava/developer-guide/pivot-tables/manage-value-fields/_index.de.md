---
title: Wertefelder in Aspose.Cells for Python via Java
description: Erfahren Sie, wie Sie in Aspose.Cells for Python via Java Basisfelder zum Datenbereich einer PivotTable hinzufügen, die Zusammenfassungsfunktion mit PivotField.Function ändern und das Wertefeld auf die Zeilen- oder Spaltenachse setzen.
linktitle: Wertefelder
keywords: Aspose.Cells, Python via Java, PivotTable, Wertefeld, PivotField, PivotField.Function, Datenfeld, PivotTable.ValuesField, Summe, Mittelwert
type: docs
weight: 230
url: /de/python-java/manage-value-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Hinzufügen eines Felds zum Datenbereich
Das Hinzufügen eines Basisfelds zum Daten- (Werte-) Bereich ist der erste Schritt, um zu steuern, wie eine PivotTable Ihre Quelldaten aggregiert. Aspose.Cells stellt `PivotTable.addFieldToArea(PivotFieldType, string)` bereit, eine Überladung, die die Konstante `PivotFieldType.DATA` und den Namen der Quellspalte akzeptiert. Sobald ein Feld zum Datenbereich hinzugefügt wurde, wird es über die `PivotTable.DataFields`-Auflistung in der Reihenfolge bereitgestellt, in der die Felder hinzugefügt wurden. Standardmäßig wird eine numerische Quellspalte mit `ConsolidationFunction.SUM` zusammengefasst, während eine nicht numerische Spalte standardmäßig `COUNT` verwendet.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.getCells().get(0, j).putValue(h)
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.getCells().get(i + 1, j).putValue(val)
pivot_table = worksheet.getPivotTables().add("A1:D9", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Category")
pivot_table.addFieldToArea(PivotFieldType.ROW, "Item")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
workbook.save("output_drag.xlsx")
jpype.shutdownJVM()
```

## Ändern der Zusammenfassungsfunktion
Jedes im Datenbereich platzierte Feld wird intern als `PivotField`-Instanz gekapselt, und seine `Function`-Eigenschaft gibt einen Wert aus der `ConsolidationFunction`-Enumeration zurück. Mit demselben `Function`-Setter können Sie zwischen den verfügbaren Aggregaten wechseln, einschließlich `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STDDEV`, `STDDEVP`, `VAR` und `VARP`.

{{% alert color="primary" %}}
Das Ändern von `Function` wirkt sich nur auf das Aggregat aus, die Quellspalte ändert sich nicht.
Sie können daher ein Datenfeld als `SUM` belassen, während Sie ein zweites Datenfeld hinzufügen, das auf dieselbe Quellspalte abzielt, aber `COUNT` oder `AVERAGE` verwendet, alles in einer einzigen PivotTable.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, ConsolidationFunction
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.getCells().get(0, j).putValue(h)
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.getCells().get(i + 1, j).putValue(val)
pivot_table = worksheet.getPivotTables().add("A1:D9", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Category")
pivot_table.addFieldToArea(PivotFieldType.ROW, "Item")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.getDataFields().get(1).setFunction(ConsolidationFunction.COUNT)
pivot_table.calculateData()
workbook.save("output_function.xlsx")
jpype.shutdownJVM()
```

## Wertefelder auf die Zeilen- oder Spaltenachse setzen
Wenn eine PivotTable zwei oder mehr Datenfelder enthält, stellt Aspose.Cells ein zusätzliches virtuelles Feld namens `PivotTable.ValuesField` bereit. Dieses virtuelle Feld repräsentiert das Aggregat jedes Datenfelds, das sich im Datenbereich befindet. Sie können es als Basis-Pivot-Feld in den Zeilen- oder Spaltenbereich ziehen, was nützlich ist, um mehrere Kennzahlen nebeneinander anzuordnen.

{{% alert color="primary" %}}
`PivotTable.ValuesField` funktioniert nicht, wenn kein oder nur ein Wertefeld vorhanden ist.
Die folgenden Szenarien führen durch drei durchgängige Beispiele, die jede der oben beschriebenen Funktionen anhand derselben Pivot-Struktur demonstrieren.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, ConsolidationFunction
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.getCells().get(0, j).putValue(h)
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.getCells().get(i + 1, j).putValue(val)
pivot_table = worksheet.getPivotTables().add("A1:D9", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Category")
pivot_table.addFieldToArea(PivotFieldType.ROW, "Item")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.getDataFields().get(1).setFunction(ConsolidationFunction.COUNT)
pivot_table.addFieldToArea(PivotFieldType.COLUMN, pivot_table.getValuesField())
pivot_table.calculateData()
workbook.save("output_plot.xlsx")
jpype.shutdownJVM()
```

{{< app/cells/assistant language="python" >}}