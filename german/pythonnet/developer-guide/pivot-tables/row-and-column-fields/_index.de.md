---
title: Zeilen- und Spaltenfelder zu einer PivotTable in Aspose.Cells für .NET hinzufügen
description: Erfahren Sie, wie Sie Basisfelder zu den Zeilen- und Spaltenbereichen einer PivotTable hinzufügen und PivotField-Zwischensummen mit PivotField.set_subtotals in Aspose.Cells for Python via .NET steuern.
linktitle: Zeilen- und Spaltenfelder
keywords: Aspose.Cells, Python via .NET, PivotTable, Zeilenfeld, Spaltenfeld, PivotField, set_subtotals, PivotFieldSubtotalType, Zwischensummen
type: docs
weight: 220
url: /de/python-net/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Hinzufügen eines Felds zum Zeilen- oder Spaltenbereich**
Die Methode `PivotTable.add_field_to_area(PivotFieldType field_type, string field_name)` verschiebt ein Basisfeld aus den Quelldaten in einen der vier Pivot-Bereiche. Das Argument `field_type` akzeptiert einen der folgenden `PivotFieldType`-Werte.
- `ROW` — Felder, die vertikal links platziert werden
- `COLUMN` — Felder, die horizontal oben platziert werden
- `DATA` — Felder, deren Werte aggregiert werden
- `PAGE` — Felder, die als Berichtsfilter verwendet werden
Nachdem Felder hinzugefügt wurden, können Sie über die Eigenschaften `PivotTable.row_fields` und `PivotTable.column_fields` darauf zugreifen. Jede Eigenschaft gibt eine `PivotFieldCollection` zurück. Das Feld am Index 0 von `row_fields` ist das äußerste Zeilenfeld, und nachfolgende Indizes stellen Felder dar, die darin verschachtelt sind. Die gleiche Indizierungskonvention gilt für `column_fields`.
Die Reihenfolge der Feldverschachtelung ist wichtig. Wenn Sie zuerst `Category` zum Zeilenbereich und dann `Item` hinzufügen, entsteht eine PivotTable, deren äußere Gruppierung `Category` und deren innere Gruppierung `Item` ist. Durch Umkehrung der Reihenfolge wird die Hierarchie umgekehrt.

## **PivotField-Zwischensummen**
Die Methode `PivotField.set_subtotals(PivotFieldSubtotalType subtotal_type, bool shown)` steuert, welche Zwischensummenzeilen für ein PivotField angezeigt werden. Jeder Aufruf schaltet einen einzelnen Zwischensummentyp unabhängig um. Die Übergabe von `shown = True` zeigt die Zwischensumme an, während `shown = False` sie ausblendet. Da jeder Aufruf nur einen Typ betrifft, wird durch mehrfaches Aufrufen der Methode mit unterschiedlichen `subtotal_type`-Werten eine benutzerdefinierte Untermenge von Zwischensummen aufgebaut.
Die Enumeration `PivotFieldSubtotalType` definiert die verfügbaren Zwischensummenarten.
- `AUTOMATIC` — Aspose.Cells wählt die Standardauswahl (typischerweise `SUM` für numerische Felder)
- `NONE` — unterdrückt jede Zwischensummenzeile
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STDDEV`
- `STDDEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
Zwischensummen werden nur gerendert, wenn zwei oder mehr Pivot-Felder im Zeilenbereich (oder im Spaltenbereich) vorhanden sind. Ein einzelnes Feld hat zwischen sich nichts Sinnvolles zu summieren, daher haben `set_subtotals`-Aufrufe in diesem Fall keine sichtbare Wirkung. Dieser Artikel platziert daher in jedem Beispiel zwei Zeilenfelder (`Category` außen, `Item` innen), damit die Zwischensummengrenze zwischen jeder `Category`-Gruppe sichtbar ist.
{{% /alert %}}

## **Szenario 1 — Automatische (Standard-)Zwischensummen**
Wenn Sie `set_subtotals` überhaupt nicht aufrufen, wendet Aspose.Cells die Auswahl `AUTOMATIC` auf numerische Felder an. Das folgende Beispiel bestätigt dieses Verhalten explizit, indem `set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)` auf dem äußeren Zeilenfeld `Category` aufgerufen wird.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
worksheet.cells.get(0, 0).put_value("Category")
worksheet.cells.get(0, 1).put_value("Item")
worksheet.cells.get(0, 2).put_value("Year")
worksheet.cells.get(0, 3).put_value("Amount")
worksheet.cells.get(1, 0).put_value("Fruit")
worksheet.cells.get(1, 1).put_value("Apple")
worksheet.cells.get(1, 2).put_value(2020)
worksheet.cells.get(1, 3).put_value(100)
worksheet.cells.get(2, 0).put_value("Fruit")
worksheet.cells.get(2, 1).put_value("Apple")
worksheet.cells.get(2, 2).put_value(2021)
worksheet.cells.get(2, 3).put_value(150)
worksheet.cells.get(3, 0).put_value("Fruit")
worksheet.cells.get(3, 1).put_value("Banana")
worksheet.cells.get(3, 2).put_value(2020)
worksheet.cells.get(3, 3).put_value(80)
worksheet.cells.get(4, 0).put_value("Fruit")
worksheet.cells.get(4, 1).put_value("Banana")
worksheet.cells.get(4, 2).put_value(2021)
worksheet.cells.get(4, 3).put_value(90)
worksheet.cells.get(5, 0).put_value("Vegetable")
worksheet.cells.get(5, 1).put_value("Carrot")
worksheet.cells.get(5, 2).put_value(2020)
worksheet.cells.get(5, 3).put_value(50)
worksheet.cells.get(6, 0).put_value("Vegetable")
worksheet.cells.get(6, 1).put_value("Carrot")
worksheet.cells.get(6, 2).put_value(2021)
worksheet.cells.get(6, 3).put_value(60)
worksheet.cells.get(7, 0).put_value("Vegetable")
worksheet.cells.get(7, 1).put_value("Daikon")
worksheet.cells.get(7, 2).put_value(2020)
worksheet.cells.get(7, 3).put_value(40)
worksheet.cells.get(8, 0).put_value("Vegetable")
worksheet.cells.get(8, 1).put_value("Daikon")
worksheet.cells.get(8, 2).put_value(2021)
worksheet.cells.get(8, 3).put_value(45)
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
category_field.set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)
pivot_table.calculate_data()
workbook.save("output_automatic.xlsx")
```

## **Szenario 2 — Unterdrücken aller Zwischensummen (None)**
Der Aufruf von `set_subtotals(PivotFieldSubtotalType.NONE, True)` entfernt jede Zwischensummenzeile aus der PivotTable und lässt nur die Feldzeilen sowie die Gesamtsumme am unteren Rand übrig. Dies ist nützlich, wenn Sie die rohen gruppierten Daten ohne Zusammenfassungszeilen wünschen.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells.get(0, j).put_value(headers[j])
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020, 80],
    ["Fruit",     "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45],
]
for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.cells.get(i + 1, j).put_value(data[i][j])
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
for st in [PivotFieldSubtotalType.SUM, PivotFieldSubtotalType.COUNT, PivotFieldSubtotalType.AVERAGE, PivotFieldSubtotalType.MAX, PivotFieldSubtotalType.MIN, PivotFieldSubtotalType.PRODUCT]:
    category_field.set_subtotals(st, True)
pivot_table.calculate_data()
workbook.save("output_none.xlsx")
```

## **Szenario 3 — Benutzerdefinierte Zwischensummen-Untermenge (Summe + Durchschnitt)**
Sie sind nicht auf einen einzelnen Zwischensummentyp beschränkt. Jeder `set_subtotals`-Aufruf wirkt unabhängig auf einen Typ. Wenn Sie die Methode also zweimal aufrufen — einmal mit `SUM` und einmal mit `AVERAGE` — erhalten Sie eine benutzerdefinierte Untermenge von zwei Zwischensummenzeilen für jede `Category`-Gruppe.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
worksheet.cells.get("A1").put_value("Category")
worksheet.cells.get("B1").put_value("Item")
worksheet.cells.get("C1").put_value("Year")
worksheet.cells.get("D1").put_value("Amount")
worksheet.cells.get(1, 0).put_value("Fruit")
worksheet.cells.get(1, 1).put_value("Apple")
worksheet.cells.get(1, 2).put_value(2020)
worksheet.cells.get(1, 3).put_value(100)
worksheet.cells.get(2, 0).put_value("Fruit")
worksheet.cells.get(2, 1).put_value("Apple")
worksheet.cells.get(2, 2).put_value(2021)
worksheet.cells.get(2, 3).put_value(150)
worksheet.cells.get(3, 0).put_value("Fruit")
worksheet.cells.get(3, 1).put_value("Banana")
worksheet.cells.get(3, 2).put_value(2020)
worksheet.cells.get(3, 3).put_value(80)
worksheet.cells.get(4, 0).put_value("Fruit")
worksheet.cells.get(4, 1).put_value("Banana")
worksheet.cells.get(4, 2).put_value(2021)
worksheet.cells.get(4, 3).put_value(90)
worksheet.cells.get(5, 0).put_value("Vegetable")
worksheet.cells.get(5, 1).put_value("Carrot")
worksheet.cells.get(5, 2).put_value(2020)
worksheet.cells.get(5, 3).put_value(50)
worksheet.cells.get(6, 0).put_value("Vegetable")
worksheet.cells.get(6, 1).put_value("Carrot")
worksheet.cells.get(6, 2).put_value(2021)
worksheet.cells.get(6, 3).put_value(60)
worksheet.cells.get(7, 0).put_value("Vegetable")
worksheet.cells.get(7, 1).put_value("Daikon")
worksheet.cells.get(7, 2).put_value(2020)
worksheet.cells.get(7, 3).put_value(40)
worksheet.cells.get(8, 0).put_value("Vegetable")
worksheet.cells.get(8, 1).put_value("Daikon")
worksheet.cells.get(8, 2).put_value(2021)
worksheet.cells.get(8, 3).put_value(45)
pivot_tables = worksheet.pivot_tables
pivot_index = pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
category_field.set_subtotals(PivotFieldSubtotalType.SUM, True)
category_field.set_subtotals(PivotFieldSubtotalType.AVERAGE, True)
pivot_table.calculate_data()
workbook.save("output_custom.xlsx")
```

## **Zusammenfassung**

Die drei Szenarien unterscheiden sich nur in einem Punkt: den `set_subtotals`-Aufrufen. Alles Weitere — der Datensatz, die Felder und die Bereiche, denen diese zugewiesen sind — ist identisch, was die Layouts direkt vergleichbar macht.
- **Platzieren von Feldern.** `PivotTable.add_field_to_area(PivotFieldType.ROW, fieldName)` verschiebt eine Quellspalte in einen Bereich. Innerhalb eines Bereichs bestimmt die Reihenfolge der Aufrufe die Anzeigereihenfolge, sodass der erste Aufruf die äußerste Gruppe bildet. Subtotals erfordern zwei oder mehr Felder im gleichen Bereich: Bei einem einzelnen Feld gibt es zwischen den Gruppen nichts, worauf eine Subtotalbildung erfolgen könnte.
- **Szenario 1 — automatische Subtotals.** Wenn `set_subtotals` nicht aufgerufen wird, überlässt dies die Entscheidung Excel, das automatisch seinen eigenen Standard-Subtotal-Typ für numerische Felder anwendet. Ein Aufruf von `set_subtotals` mit `PivotFieldSubtotalType.AUTOMATIC` protokolliert diese Entscheidung explizit statt sie implizit zu belassen.
- **Szenario 2 — keine Subtotals.** `set_subtotals` mit `PivotFieldSubtotalType.NONE` deaktiviert den Standard-Subtotal-Typ, sodass das PivotTable weiterhin die Feldzeilen und die Gesamtsumme behält, jedoch die Zwischensubtotalzeilen weglässt, die Excel andernfalls dazwischen einfügen würde.
- **Szenario 3 — eine ausgewählte Teilmenge.** Jeder Aufruf schaltet genau einen Subtotal-Typ um, und die Aufrufe summieren sich auf, anstatt sich gegenseitig zurückzusetzen. Ein erstes Aufrufen mit `PivotFieldSubtotalType.SUM` und ein zweites mit `PivotFieldSubtotalType.AVERAGE` lassen somit beide aktiviert, und das PivotTable gibt sowohl einen Summen-Subtotal, einen Durchschnitts-Subtotal sowie die Gesamtsumme aus.

{{% alert color="primary" %}}
Nichts an Subtotals ist auf den Zeilenbereich beschränkt. Die gleichen `set_subtotals`-Aufrufe für ein Feld, das aus `PivotTable.ColumnFields` entnommen wird, erzeugen die gleichen drei Layouts auf der Spaltenachse, da die Einstellung zum Pivot-Feld selbst gehört und nicht zur Achse, auf der es sich befindet.
{{% /alert %}}
## **Verwandte Artikel**

- [Seitenfelder in Pivot-Tabellen](/cells/de/python-net/add-page-field-in-pivot-table/)
- [Aktualisieren von Pivot-Tabellen in Aspose.Cells für Python via .NET](/cells/de/python-net/refresh-pivot-table/)
- [Anwenden von Stilen auf Pivot-Tabellen](/cells/de/python-net/apply-style-to-pivot-table/)
{{< app/cells/assistant language="python-net" >}}