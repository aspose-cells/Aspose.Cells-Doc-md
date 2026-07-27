---
title: Wertfelder einer PivotTable in Aspose.Cells für .NET verwalten
linktitle: Wertfelder
description: Erfahren Sie, wie Sie Basisfelder zum Datenbereich einer PivotTable hinzufügen, die Zusammenfassungsfunktion mit PivotField.function ändern und das Wertfeld auf die Zeilen- oder Spaltenachse in Aspose.Cells for Python via .NET anwenden.
keywords: Aspose.Cells, Python via .NET, PivotTable, Wertfeld, PivotField, PivotField.function, Datenfeld, PivotTable.values_field, Summe, Mittelwert
type: docs
weight: 230
url: /de/python-net/pivot-table-manage-value-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
Wertfelder sind das Herzstück jeder PivotTable, die numerischen Aggregate, die die Quelldaten zusammenfassen. In Aspose.Cells for Python via .NET wird der Datenbereich einer PivotTable befüllt, indem Basisfelder über `PivotTable.add_field_to_area` hinzugefügt werden, und jedes in diesem Bereich platzierte Feld kann eine eigene Zusammenfassungsfunktion besitzen. Wenn zwei oder mehr Datenfelder vorhanden sind, stellt Aspose.Cells ein spezielles Aggregatfeld `PivotTable.values_field` bereit, das als Basisfeld auf der Zeilen- oder Spaltenachse angezeigt werden kann, sodass Sie eine feinere Kontrolle darüber erhalten, wie Wertfelder im Layout erscheinen.
## Hinzufügen eines Felds zum Datenbereich
Das Hinzufügen eines Basisfelds zum Daten-(Werte-)Bereich ist der erste Schritt bei der Gestaltung der Aggregation Ihrer Quelldaten durch die PivotTable. Aspose.Cells stellt `PivotTable.add_field_to_area(PivotFieldType, str)` bereit, eine Überladung, die die Konstante `PivotFieldType.DATA` und den Namen der Quellspalte akzeptiert. Sobald ein Feld zum Datenbereich hinzugefügt wurde, wird es über die Sammlung `PivotTable.data_fields` in der Reihenfolge des Hinzufügens verfügbar gemacht. Standardmäßig wird eine numerische Quellspalte mit `ConsolidationFunction.SUM` zusammengefasst, während eine nicht numerische Spalte standardmäßig `Count` verwendet.
## Ändern der Zusammenfassungsfunktion
Jedes im Datenbereich platzierte Feld wird intern als Instanz von `PivotField` umschlossen, und seine Eigenschaft `function` gibt einen Wert aus der Enumeration `ConsolidationFunction` zurück. Über denselben Setter `function` können Sie zwischen den verfügbaren Aggregaten wechseln, darunter `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` und `Varp`.
{{% alert color="primary" %}}
Das Ändern von `function` wirkt sich nur auf das Aggregat aus, die Quellspalte ändert sich nicht.
{{% /alert %}}
Sie können daher ein Datenfeld als `Sum` belassen, während Sie ein zweites Datenfeld hinzufügen, das auf dieselbe Quellspalte verweist, aber `Count` oder `Average` verwendet, und das alles in einer einzigen PivotTable.
## Wertfelder auf die Zeilen- oder Spaltenachse anwenden
Wenn eine PivotTable zwei oder mehr Datenfelder enthält, stellt Aspose.Cells ein zusätzliches virtuelles Feld namens `PivotTable.values_field` bereit. Dieses virtuelle Feld repräsentiert das Aggregat aller im Datenbereich vorhandenen Datenfelder. Sie können es als Basisfeld einer PivotTable in den Zeilen- oder Spaltenbereich ziehen, was nützlich ist, um mehrere Measures nebeneinander anzuordnen.
{{% alert color="primary" %}}
`PivotTable.values_field` funktioniert nicht, wenn kein oder nur ein Wertfeld vorhanden ist.
{{% /alert %}}
Die folgenden Szenarien durchlaufen drei durchgängige Beispiele, die jede der oben beschriebenen Funktionen anhand derselben PivotTable-Struktur demonstrieren.
## Szenario 1 — Ziehen eines Basisfelds in den Wertebereich
Dieses Szenario zeigt, wie ein einzelnes Basisfeld (`Amount`) in den Datenbereich einer bestehenden PivotTable eingefügt wird. Die gemeinsame PivotTable-Struktur platziert `Category` und `Item` auf der Zeilenachse und `Year` auf der Spaltenachse. Nach der Operation erscheint `Amount` im Datenbereich und wird standardmäßig als `Sum` von `Amount` berechnet.
```python
from aspose.cells.pivot import PivotFieldType

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

# Überschriften in A1:D1
worksheet.cells[0, 0].put_value("Category")
worksheet.cells[0, 1].put_value("Item")
worksheet.cells[0, 2].put_value("Year")
worksheet.cells[0, 3].put_value("Amount")

# Datenzeilen A2:D9 mit verschachtelten Schleifen, die auf j verzweigen
for i in range(1, 9):
    for j in range(4):
        if j == 0:
            worksheet.cells[i, j].put_value("Fruit" if i <= 4 else "Vegetable")
        elif j == 1:
            if i == 1 or i == 2:
                worksheet.cells[i, j].put_value("Apple")
            elif i == 3 or i == 4:
                worksheet.cells[i, j].put_value("Banana")
            elif i == 5 or i == 6:
                worksheet.cells[i, j].put_value("Carrot")
            else:
                worksheet.cells[i, j].put_value("Daikon")
        elif j == 2:
            worksheet.cells[i, j].put_value(2020 + ((i - 1) % 2))
        elif j == 3:
            if i == 1:
                worksheet.cells[i, j].put_value(100)
            elif i == 2:
                worksheet.cells[i, j].put_value(150)
            elif i == 3:
                worksheet.cells[i, j].put_value(80)
            elif i == 4:
                worksheet.cells[i, j].put_value(90)
            elif i == 5:
                worksheet.cells[i, j].put_value(50)
            elif i == 6:
                worksheet.cells[i, j].put_value(60)
            elif i == 7:
                worksheet.cells[i, j].put_value(40)
            else:
                worksheet.cells[i, j].put_value(45)

# Pivot-Tabelle bei F3 mit dem Namen PivotTable1 hinzufügen
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Pivot-Layout: Kategorie und Element in Zeile, Jahr in Spalte, Betrag als Datenfeld
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

pivot_table.refresh_data()
pivot_table.calculate_data()
workbook.save("output_drag.xlsx")
```
## Szenario 2 — Ändern der Zusammenfassungsfunktion
Dieses Szenario beginnt mit derselben PivotTable-Struktur wie Szenario 1, fügt jedoch das Feld `Amount` zweimal zum Datenbereich hinzu. Beide Datenfelder verweisen auf dieselbe Quellspalte, jedoch wird das zweite Feld mithilfe des Setters `PivotField.function` überschrieben, sodass es `Count` anstelle der Standardeinstellung `Sum` wird.
```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells[0, j].put_value(headers[j])

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
]

for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.cells[i + 1, j].put_value(data[i][j])

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")

pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

count_field = pivot_table.data_fields[1]
count_field.function = ac.ConsolidationFunction.COUNT

pivot_table.refresh_data()
pivot_table.calculate_data()

workbook.save("output_function.xlsx")
```
## Szenario 3 — Wertfelder auf die Zeilen- oder Spaltenachse anwenden
Wenn zwei Datenfelder vorhanden sind, wird `PivotTable.values_field` nutzbar. Dieses Szenario zieht dieses virtuelle Aggregatfeld in den Spaltenbereich, sodass jedes Measure im Datenbereich als eigener Spaltenblock neben `Year` erscheint.
```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells[0, j].put_value(headers[j])

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
]

for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.cells[i + 1, j].put_value(data[i][j])

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ac.ConsolidationFunction.COUNT

# Die Wertefelder auf der Spaltenachse darstellen.
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, pivot_table.values_field.name)

pivot_table.refresh_data()
pivot_table.calculate_data()

workbook.save("output_plot.xlsx")
```
Zusammen decken diese drei Szenarien jeden Aspekt der Wertfeldmanipulation in Aspose.Cells for Python via .NET ab, von einem einzelnen Datenfeld mit der Standardeinstellung `Sum` bis hin zu einer PivotTable mit mehreren Measures, bei der das virtuelle Feld `ValuesField` das Layout auf der Zeilen- oder Spaltenachse steuert.
## Verwandte Artikel
- [Zeilen- und Spaltenfelder von PivotTables in Aspose.Cells for Python via .NET](/cells/de/python-net/row-and-column-fields/)
- [Seitenfelder in PivotTables](/cells/de/python-net/add-page-field-in-pivot-table/)
- [Aktualisieren von PivotTables in Aspose.Cells for Python via .NET](/cells/de/python-net/refresh-pivot-table/)
- [Anwenden von Stilen auf PivotTables](/cells/de/python-net/apply-style-to-pivot-table/)
{{< app/cells/assistant language="python" >}}