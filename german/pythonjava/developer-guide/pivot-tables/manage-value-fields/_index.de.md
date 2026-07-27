---
title: Wertefelder in Aspose.Cells for Python via Java
linktitle: Wertefelder
description: Erfahren Sie, wie Sie in Aspose.Cells for Python via Java Basisfelder zum Datenbereich einer PivotTable hinzufügen, die Zusammenfassungsfunktion mit PivotField.Function ändern und das Wertefeld auf die Zeilen- oder Spaltenachse setzen.
keywords: Aspose.Cells, Python via Java, PivotTable, Wertefeld, PivotField, PivotField.Function, Datenfeld, PivotTable.ValuesField, Summe, Mittelwert
type: docs
weight: 230
url: /de/python-java/manage-value-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Hinzufügen eines Felds zum Datenbereich

Das Hinzufügen eines Basisfelds zum Daten- (Werte-) Bereich ist der erste Schritt, um zu steuern, wie eine PivotTable Ihre Quelldaten aggregiert. Aspose.Cells stellt `PivotTable.addFieldToArea(PivotFieldType, string)` bereit, eine Überladung, die die Konstante `PivotFieldType.DATA` und den Namen der Quellspalte akzeptiert. Sobald ein Feld zum Datenbereich hinzugefügt wurde, wird es über die `PivotTable.DataFields`-Auflistung in der Reihenfolge bereitgestellt, in der die Felder hinzugefügt wurden. Standardmäßig wird eine numerische Quellspalte mit `ConsolidationFunction.SUM` zusammengefasst, während eine nicht numerische Spalte standardmäßig `COUNT` verwendet.

## Ändern der Zusammenfassungsfunktion

Jedes im Datenbereich platzierte Feld wird intern als `PivotField`-Instanz gekapselt, und seine `Function`-Eigenschaft gibt einen Wert aus der `ConsolidationFunction`-Enumeration zurück. Mit demselben `Function`-Setter können Sie zwischen den verfügbaren Aggregaten wechseln, einschließlich `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STDDEV`, `STDDEVP`, `VAR` und `VARP`.

{{% alert color="primary" %}}
Das Ändern von `Function` wirkt sich nur auf das Aggregat aus, die Quellspalte ändert sich nicht.
{{% /alert %}}

Sie können daher ein Datenfeld als `SUM` belassen, während Sie ein zweites Datenfeld hinzufügen, das auf dieselbe Quellspalte abzielt, aber `COUNT` oder `AVERAGE` verwendet, alles in einer einzigen PivotTable.

## Wertefelder auf die Zeilen- oder Spaltenachse setzen

Wenn eine PivotTable zwei oder mehr Datenfelder enthält, stellt Aspose.Cells ein zusätzliches virtuelles Feld namens `PivotTable.ValuesField` bereit. Dieses virtuelle Feld repräsentiert das Aggregat jedes Datenfelds, das sich im Datenbereich befindet. Sie können es als Basis-Pivot-Feld in den Zeilen- oder Spaltenbereich ziehen, was nützlich ist, um mehrere Kennzahlen nebeneinander anzuordnen.

{{% alert color="primary" %}}
`PivotTable.ValuesField` funktioniert nicht, wenn kein oder nur ein Wertefeld vorhanden ist.
{{% /alert %}}

Die folgenden Szenarien führen durch drei durchgängige Beispiele, die jede der oben beschriebenen Funktionen anhand derselben Pivot-Struktur demonstrieren.

## Szenario 1 — Ziehen eines Basisfelds in den Wertebereich

Dieses Szenario zeigt, wie ein einzelnes Basisfeld (`Amount`) in den Datenbereich einer bestehenden PivotTable eingefügt wird. Die gemeinsame Pivot-Struktur platziert `Category` und `Item` auf der Zeilenachse und `Year` auf der Spaltenachse. Nach der Operation erscheint `Amount` im Datenbereich und wird standardmäßig als `Summe` von `Amount` berechnet.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)

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
        worksheet.cells.get(i + 1, j).put_value(val)

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

pivot_table.calculate_data()
workbook.save("output_drag.xlsx")
```

## Szenario 2 — Ändern der Zusammenfassungsfunktion

Dieses Szenario beginnt mit derselben Pivot-Struktur wie Szenario 1, fügt aber das Feld `Amount` zweimal zum Datenbereich hinzu. Beide Datenfelder verweisen auf dieselbe Quellspalte, jedoch wird das zweite Feld mit dem `PivotField.Function`-Setter überschrieben, sodass es `Count` anstelle der Standardeinstellung `Sum` wird.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, ConsolidationFunction

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)

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
        worksheet.cells.get(i + 1, j).put_value(val)

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT

pivot_table.calculate_data()
workbook.save("output_function.xlsx")
```

## Szenario 3 — Wertefelder auf die Zeilen- oder Spaltenachse setzen

Mit zwei vorhandenen Datenfeldern wird `PivotTable.ValuesField` verwendbar. Dieses Szenario zieht das virtuelle Aggregatfeld in den Spaltenbereich, sodass jede Kennzahl im Datenbereich als eigener Spaltenblock neben `Year` erscheint.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, ConsolidationFunction

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)

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
        worksheet.cells.get(i + 1, j).put_value(val)

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT
pivot_table.add_field_to_area(PivotFieldType.COLUMN, pivot_table.values_field.name)

pivot_table.calculate_data()
workbook.save("output_plot.xlsx")
```

Zusammen decken diese drei Szenarien alle Aspekte der Manipulation von Wertefeldern in Aspose.Cells for Python via Java ab, von einem einzelnen Datenfeld mit der Standard-`Summe` bis hin zu einer Multi-Measure-Pivot, bei der das virtuelle `ValuesField` das Layout auf der Zeilen- oder Spaltenachse steuert.

{{< app/cells/assistant language="python" >}}
