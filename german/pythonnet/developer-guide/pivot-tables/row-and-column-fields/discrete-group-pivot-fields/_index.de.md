---
title: Diskrete Gruppierung von Pivot-Feldelementen
linktitle: Diskrete Gruppierung
description: Erfahren Sie, wie Sie mit DiscreteGroupItem und pivot_field_group_options.discrete_group_items in Aspose.Cells for Python via .NET Pivot-Feldelemente in benutzerdefinierte Gruppen wie Obst und Gemüse gruppieren.
keywords: Aspose.Cells for Python via .NET, PivotTable, diskrete Gruppierung, DiscreteGroupItem, PivotFieldGroupOptions, Pivot-Feldelemente gruppieren, benutzerdefinierte Gruppen, PivotField.group, Python, Excel-PivotTable
type: docs
weight: 90
url: /de/python-net/discrete-group-pivot-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
- Die automatische Gruppierung fasst Elemente nach Datentyp zusammen, etwa Datumswerte nach Monaten und Quartalen oder Zahlen nach Bereichen. Die diskrete Gruppierung löst das entgegengesetzte Problem, indem sie bestimmte, unverbundene Elemente zu benutzerdefinierten Gruppen mit Namen zusammenfasst, beispielsweise Produkte zu Gruppen wie Obst und Gemüse, Standorte zu Regionen oder Konten zu Zonen. Aspose.Cells stellt die diskrete Gruppierung über die Klasse `DiscreteGroupItem` und die Eigenschaft `pivot_field_group_options.discrete_group_items` bereit.
- Ein `DiscreteGroupItem` besteht aus einem Gruppennamen und den Elementen, die ihm zugehören. Die Elemente können auf zwei Arten identifiziert werden: durch ihre Namen (`DiscreteGroupItem("fruit", ["grape", "cherry"])`) oder durch ihre nullbasierten Positionen in den Quelldaten (`DiscreteGroupItem("fruit", [0, 3])`). Beide Formen führen zum selben Ergebnis.
- Die diskrete Gruppierung wird auf ein Feld im Zeilen- oder Spaltenbereich der PivotTable angewendet, indem die Optionen an `pivot_field.group(PivotFieldGroupOptions)` übergeben werden.

## **Gruppierung von Pivot-Feldelementen nach Elementnamen**
Das folgende Beispiel erstellt eine kleine Verkaufsliste (Produkt, Datum und Betrag), legt daraus eine PivotTable an, wobei `product` im Zeilenbereich, `date` im Spaltenbereich und `amount` im Datenbereich platziert wird, und definiert anschließend zwei benutzerdefinierte Gruppen anhand der Elementnamen: Obst (Traube, Kirsche) und Gemüse (Karotte, Kartoffel). Das Ergebnis zeigt einen zweistufigen Zeilenaufbau, bei dem der Gruppenname die äußere Ebene bildet und die ursprünglichen Elemente darunter verschachtelt sind. Dadurch lassen sich Trends pro benutzerdefinierter Gruppe und pro Element ablesen.

```python
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import DiscreteGroupItem, PivotFieldGroupOptions, PivotFieldType, PivotTableStyleType
wb = ac.Workbook()
sheet = wb.worksheets[0]
cells = sheet.cells
cells.get(0, 0).value = "product"
cells.get(1, 0).value = "grape"
cells.get(2, 0).value = "carrot"
cells.get(3, 0).value = "potato"
cells.get(4, 0).value = "cherry"
date_style = wb.create_style()
date_style.custom = "m/d/yyyy"
cells.get(0, 1).value = "date"
cells.get(1, 1).value = datetime(2021, 2, 5)
cells.get(2, 1).value = datetime(2022, 3, 8)
cells.get(3, 1).value = datetime(2023, 4, 10)
cells.get(4, 1).value = datetime(2024, 5, 16)
for r in range(1, 5):
    cells.get(r, 1).set_style(date_style)
cells.get(0, 2).value = "amount"
cells.get(1, 2).value = 50
cells.get(2, 2).value = 60
cells.get(3, 2).value = 70
cells.get(4, 2).value = 80
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.pivot_tables.add("=Sheet1!A1:C5", 11, 0)
pivot_table.add_field_to_area(PivotFieldType.ROW, "product")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "date")
pivot_table.add_field_to_area(PivotFieldType.DATA, "amount")
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM10
# Group specific items into custom groups using 0-based source-appearance indexes
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.discrete_group_items = [fruit, vegetable]
pivot_table.row_fields[0].group(group_options)
pivot_table.calculate_data()
wb.save("outputDiscreteGroupPivotField.xlsx")
```

Nach `calculate_data()` zeigt der Zeilenbereich der PivotTable Obst (Traube 50, Kirsche 80) und Gemüse (Karotte 60, Kartoffel 70) sowie die Gesamtsumme 260. Die Spaltenbeschriftungen behalten die vier Datumswerte (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Gruppierung von Pivot-Feldelementen nach Elementindizes**
Wenn die Elementnamen lang oder lokalisiert sind, identifiziert der zweite Konstruktor von `DiscreteGroupItem` die Elemente nach Index. Die Indizes entsprechen den nullbasierten Positionen der Elemente in der Reihenfolge, in der sie in den Quelldaten erscheinen, und nicht ihrer alphabetischen Reihenfolge. In den obigen Beispieldaten ist Traube das Element 0, Karotte das Element 1, Kartoffel das Element 2 und Kirsche das Element 3. Somit entspricht Obst `{ 0, 3 }` und Gemüse `{ 1, 2 }`. Das Ergebnis ist mit dem namensbasierten Beispiel identisch.

```python
import aspose.cells as ac
from aspose.cells.pivot import DiscreteGroupItem, PivotFieldGroupOptions, PivotFieldType, PivotTableStyleType
from datetime import datetime
wb = ac.Workbook()
sheet = wb.worksheets[0]
cells = sheet.cells
cells.get(0, 0).value = "product"
cells.get(1, 0).value = "grape"
cells.get(2, 0).value = "carrot"
cells.get(3, 0).value = "potato"
cells.get(4, 0).value = "cherry"
date_style = wb.create_style()
date_style.custom = "m/d/yyyy"
cells.get(0, 1).value = "date"
cells.get(1, 1).value = datetime(2021, 2, 5)
cells.get(2, 1).value = datetime(2022, 3, 8)
cells.get(3, 1).value = datetime(2023, 4, 10)
cells.get(4, 1).value = datetime(2024, 5, 16)
for r in range(1, 5):
    cells.get(r, 1).set_style(date_style)
cells.get(0, 2).value = "amount"
cells.get(1, 2).value = 50
cells.get(2, 2).value = 60
cells.get(3, 2).value = 70
cells.get(4, 2).value = 80
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.pivot_tables.add("=Sheet1!A1:C5", 11, 0)
pivot_table.add_field_to_area(PivotFieldType.ROW, "product")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "date")
pivot_table.add_field_to_area(PivotFieldType.DATA, "amount")
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM10
# grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
# (zero-based positions in the order the items appear in the source data)
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.discrete_group_items = [fruit, vegetable]
pivot_table.row_fields[0].group(group_options)
pivot_table.calculate_data()
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx")
```

## **Hinweis**

{{% alert color="primary" %}}
- Elemente, die keiner benutzerdefinierten Gruppe zugewiesen sind, gehen nicht verloren. Sie bleiben in der PivotTable auf derselben Ebene wie die benutzerdefinierten Gruppen erhalten, jeweils als eigener Einzeleintrag. Wenn im obigen Beispiel nur die Obstgruppe definiert wird, bleiben Karotte und Kartoffel im Zeilenbereich als eigenständige Einträge neben der Obstgruppe erhalten.
- Die Eigenschaft `pivot_field_group_options.new_pivot_field` steuert den Aufbau der diskreten Gruppierung. Ihr Standardwert ist `True`. Dadurch wird das gruppierte Feld als neues äußeres Feld neben dem Originalfeld eingefügt, sodass der oben gezeigte zweistufige Aufbau entsteht (`row_fields` erhöht sich auf 2). Setzen Sie den Wert auf `False`, um stattdessen das Originalfeld zu ersetzen. Der Zeilenbereich zeigt dann nur noch eine Ebene mit den Gruppennamen und ihren aggregierten Werten: Obst 130 (50 + 80) und Gemüse 130 (60 + 70).
- Die namens- und indexbasierten Konstruktoren von `DiscreteGroupItem` können innerhalb derselben Liste `discrete_group_items` kombiniert werden.
{{% /alert %}}

## **Verwandte Artikel**
- [Pivot-Felder in der PivotTable gruppieren](/cells/de/python-net/group-pivot-fields-in-the-pivot-table/)
- [Zeilen- und Spaltenfelder zur PivotTable hinzufügen](/cells/de/python-net/pivot-table-add-row-and-column-fields/)
- [PivotTables nach Beschriftung oder Wert filtern](/cells/de/python-net/filter-by-label-or-value-of-pivot-table/)
- [Stil auf eine PivotTable anwenden](/cells/de/python-net/apply-style-to-pivot-table/)
- [PivotTable aktualisieren](/cells/de/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}