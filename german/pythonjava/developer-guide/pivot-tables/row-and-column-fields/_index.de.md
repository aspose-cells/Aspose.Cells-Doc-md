---
title: Zeilen- und Spaltenfelder zu einer PivotTable in Aspose.Cells für .NET hinzufügen
description: Erfahren Sie, wie Sie Basisfelder zu den Zeilen- und Spaltenbereichen einer PivotTable hinzufügen und PivotField-Zwischensummen mit PivotField.setSubtotals in Aspose.Cells for Python via Java steuern.
linktitle: Zeilen- und Spaltenfelder
keywords: Aspose.Cells, Python via Java, PivotTable, Zeilenfeld, Spaltenfeld, PivotField, setSubtotals, PivotFieldSubtotalType, Zwischensummen
type: docs
weight: 220
url: /de/python-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Hinzufügen eines Felds zum Zeilen- oder Spaltenbereich**
Die Methode `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` verschiebt ein Basisfeld aus den Quelldaten in einen der vier Pivot-Bereiche. Das Argument `fieldType` akzeptiert einen der folgenden `PivotFieldType`-Werte.
- `ROW` — Felder, die vertikal auf der linken Seite platziert werden
- `COLUMN` — Felder, die horizontal oben platziert werden
- `DATA` — Felder, deren Werte aggregiert werden
- `PAGE` — Felder, die als Berichtsfilter verwendet werden
Nachdem Felder hinzugefügt wurden, können Sie über die Methoden `PivotTable.getRowFields()` und `PivotTable.getColumnFields()` darauf zugreifen. Jede Methode gibt eine `PivotFieldCollection` zurück. Das Feld an Index 0 von `RowFields` ist das äußerste Zeilenfeld, und die nachfolgenden Indizes stellen Felder dar, die darin verschachtelt sind. Die gleiche Indizierungskonvention gilt für `ColumnFields`.
Die Verschachtelungsreihenfolge der Felder ist wichtig. Wenn Sie zuerst `Category` zum Zeilenbereich und dann `Item` hinzufügen, entsteht eine PivotTable, deren äußere Gruppierung `Category` und deren innere Gruppierung `Item` ist. Eine Umkehrung der Reihenfolge kehrt die Hierarchie um.

## **Zwischensummen für Pivot-Felder**
Die Methode `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` steuert, welche Zwischensummenzeilen für ein Pivot-Feld angezeigt werden. Jeder Aufruf schaltet einen einzelnen Zwischensummentyp unabhängig um. Die Übergabe von `shown = true` zeigt die Zwischensumme an, während `shown = false` sie ausblendet. Da jeder Aufruf nur einen Typ betrifft, können Sie durch mehrere Aufrufe der Methode mit unterschiedlichen `subtotalType`-Werten eine benutzerdefinierte Teilmenge von Zwischensummen erstellen.
Die Enumeration `PivotFieldSubtotalType` definiert die verfügbaren Zwischensummentypen.
- `AUTOMATIC` — Aspose.Cells wählt die Standardauswahl (in der Regel `SUM` für numerische Felder)
- `NONE` — alle Zwischensummenzeilen unterdrücken
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
Zwischensummen werden nur angezeigt, wenn zwei oder mehr Pivot-Felder im Zeilenbereich (oder im Spaltenbereich) vorhanden sind. Ein einzelnes Feld hat keine sinnvolle Zwischensumme dazwischen, daher haben `setSubtotals`-Aufrufe in diesem Fall keine sichtbare Wirkung. Dieser Artikel platziert daher in jedem Beispiel zwei Zeilenfelder (`Category` außen, `Item` innen), damit die Zwischensummengrenze zwischen jeder `Category`-Gruppe sichtbar ist.
{{% /alert %}}

## **Szenario 1 — Automatische (Standard-) Zwischensummen**
Wenn Sie `setSubtotals` gar nicht aufrufen, wendet Aspose.Cells die Auswahl `AUTOMATIC` auf numerische Felder an. Das folgende Beispiel bestätigt dieses Verhalten explizit, indem es `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` auf dem äußeren Zeilenfeld `Category` aufruft.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, PivotTable, PivotField, PivotFieldType, PivotFieldSubtotalType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
worksheet.getCells().get(0, 0).putValue("Category")
worksheet.getCells().get(0, 1).putValue("Item")
worksheet.getCells().get(0, 2).putValue("Year")
worksheet.getCells().get(0, 3).putValue("Amount")
worksheet.getCells().get(1, 0).putValue("Fruit")
worksheet.getCells().get(1, 1).putValue("Apple")
worksheet.getCells().get(1, 2).putValue(2020)
worksheet.getCells().get(1, 3).putValue(100)
worksheet.getCells().get(2, 0).putValue("Fruit")
worksheet.getCells().get(2, 1).putValue("Apple")
worksheet.getCells().get(2, 2).putValue(2021)
worksheet.getCells().get(2, 3).putValue(150)
worksheet.getCells().get(3, 0).putValue("Fruit")
worksheet.getCells().get(3, 1).putValue("Banana")
worksheet.getCells().get(3, 2).putValue(2020)
worksheet.getCells().get(3, 3).putValue(80)
worksheet.getCells().get(4, 0).putValue("Fruit")
worksheet.getCells().get(4, 1).putValue("Banana")
worksheet.getCells().get(4, 2).putValue(2021)
worksheet.getCells().get(4, 3).putValue(90)
worksheet.getCells().get(5, 0).putValue("Vegetable")
worksheet.getCells().get(5, 1).putValue("Carrot")
worksheet.getCells().get(5, 2).putValue(2020)
worksheet.getCells().get(5, 3).putValue(50)
worksheet.getCells().get(6, 0).putValue("Vegetable")
worksheet.getCells().get(6, 1).putValue("Carrot")
worksheet.getCells().get(6, 2).putValue(2021)
worksheet.getCells().get(6, 3).putValue(60)
worksheet.getCells().get(7, 0).putValue("Vegetable")
worksheet.getCells().get(7, 1).putValue("Daikon")
worksheet.getCells().get(7, 2).putValue(2020)
worksheet.getCells().get(7, 3).putValue(40)
worksheet.getCells().get(8, 0).putValue("Vegetable")
worksheet.getCells().get(8, 1).putValue("Daikon")
worksheet.getCells().get(8, 2).putValue(2021)
worksheet.getCells().get(8, 3).putValue(45)
pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.AUTOMATIC, True)
pivotTable.calculateData()
workbook.save("output_automatic.xlsx")
jpype.shutdownJVM()
```

## **Szenario 2 — Alle Zwischensummen unterdrücken (Keine)**
Der Aufruf von `setSubtotals(PivotFieldSubtotalType.NONE, true)` entfernt jede Zwischensummenzeile aus der PivotTable und lässt nur die Feldzeilen und die Gesamtsumme am Ende übrig. Dies ist nützlich, wenn Sie die rohen gruppierten Daten ohne Zusammenfassungszeilen wünschen.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PivotFieldSubtotalType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.getCells().get(0, j).putValue(headers[j])
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020, 80 ],
    ["Fruit",     "Banana", 2021, 90 ],
    ["Vegetable", "Carrot", 2020, 50 ],
    ["Vegetable", "Carrot", 2021, 60 ],
    ["Vegetable", "Daikon", 2020, 40 ],
    ["Vegetable", "Daikon", 2021, 45 ]
]
for i in range(len(data)):
    for j in range(len(data[0])):
        worksheet.getCells().get(i + 1, j).putValue(data[i][j])
pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.NONE, True)
pivotTable.calculateData()
workbook.save("output_none.xlsx")
jpype.shutdownJVM()
```

## **Szenario 3 — Benutzerdefinierte Zwischensummenteilmenge (Summe + Durchschnitt)**
Sie sind nicht auf einen einzelnen Zwischensummentyp beschränkt. Jeder `setSubtotals`-Aufruf wirkt unabhängig auf einen Typ. Wenn Sie die Methode zweimal aufrufen — einmal mit `SUM` und einmal mit `AVERAGE` — erhalten Sie eine benutzerdefinierte Teilmenge von zwei Zwischensummenzeilen für jede `Category`-Gruppe.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableCollection, PivotTable, PivotFieldType, PivotField, PivotFieldSubtotalType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
worksheet.getCells().get("A1").putValue("Category")
worksheet.getCells().get("B1").putValue("Item")
worksheet.getCells().get("C1").putValue("Year")
worksheet.getCells().get("D1").putValue("Amount")
worksheet.getCells().get(1, 0).putValue("Fruit")
worksheet.getCells().get(1, 1).putValue("Apple")
worksheet.getCells().get(1, 2).putValue(2020)
worksheet.getCells().get(1, 3).putValue(100)
worksheet.getCells().get(2, 0).putValue("Fruit")
worksheet.getCells().get(2, 1).putValue("Apple")
worksheet.getCells().get(2, 2).putValue(2021)
worksheet.getCells().get(2, 3).putValue(150)
worksheet.getCells().get(3, 0).putValue("Fruit")
worksheet.getCells().get(3, 1).putValue("Banana")
worksheet.getCells().get(3, 2).putValue(2020)
worksheet.getCells().get(3, 3).putValue(80)
worksheet.getCells().get(4, 0).putValue("Fruit")
worksheet.getCells().get(4, 1).putValue("Banana")
worksheet.getCells().get(4, 2).putValue(2021)
worksheet.getCells().get(4, 3).putValue(90)
worksheet.getCells().get(5, 0).putValue("Vegetable")
worksheet.getCells().get(5, 1).putValue("Carrot")
worksheet.getCells().get(5, 2).putValue(2020)
worksheet.getCells().get(5, 3).putValue(50)
worksheet.getCells().get(6, 0).putValue("Vegetable")
worksheet.getCells().get(6, 1).putValue("Carrot")
worksheet.getCells().get(6, 2).putValue(2021)
worksheet.getCells().get(6, 3).putValue(60)
worksheet.getCells().get(7, 0).putValue("Vegetable")
worksheet.getCells().get(7, 1).putValue("Daikon")
worksheet.getCells().get(7, 2).putValue(2020)
worksheet.getCells().get(7, 3).putValue(40)
worksheet.getCells().get(8, 0).putValue("Vegetable")
worksheet.getCells().get(8, 1).putValue("Daikon")
worksheet.getCells().get(8, 2).putValue(2021)
worksheet.getCells().get(8, 3).putValue(45)
pivotTables = worksheet.getPivotTables()
pivotTable = pivotTables.add("A1:D9", 2, 5)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.SUM, True)
categoryField.setSubtotals(PivotFieldSubtotalType.AVERAGE, True)
pivotTable.calculateData()
workbook.save("output_custom.xlsx")
jpype.shutdownJVM()
```

## **Zusammenfassung**
Die drei Szenarien unterscheiden sich lediglich in den `setSubtotals`-Aufrufen. Alles andere – der Datensatz, die Felder sowie die Bereiche, denen sie zugeordnet sind – ist identisch, was die Layouts unmittelbar vergleichbar macht.
- **Platzieren von Feldern.** `PivotTable.addFieldToArea(PivotFieldType.ROW, fieldName)` verschiebt eine Quellspalte in einen Bereich. Innerhalb eines Bereichs bestimmt die Reihenfolge der Aufrufe die Anzeigereihenfolge, sodass der erste Aufruf die äußere Gruppierung darstellt. Zwischen-summieren erfordert zwei oder mehr Felder im gleichen Bereich: Bei einem einzelnen Feld gibt es zwischen den Gruppen nichts, für das eine Zwischensumme gebildet werden könnte.
- **Szenario 1 – automatische Zwischensummen.** Wenn `setSubtotals` nicht aufgerufen wird, übernimmt Excel die Entscheidung undwendet automatisch seine eigene Standard-Zwischensumme auf numerische Felder an. Ein Aufruf von `setSubtotals` mit `PivotFieldSubtotalType.AUTOMATIC` dokumentiert diese Entscheidung explizit, statt sie implizit zu belassen.
- **Szenario 2 – keine Zwischensummen.** `setSubtotals` mit `PivotFieldSubtotalType.NONE` deaktiviert die Standard-Zwischensumme, sodass das Pivot-Table die Feldzeilen sowie die Gesamtsumme behält, aber die Zwischensummenzeilen weglässt, die Excel andernfalls dazwischen einfügen würde.
- **Szenario 3 – eine ausgewählte Teilmenge.** Jeder Aufruf schaltet genau einen Zwischensummentyp um und die Aufrufe addieren sich vielmehr als dass sie sich gegenseitig zurücksetzen. Ein erstes Maliges Aufrufen mit `PivotFieldSubtotalType.SUM` und ein zweites Maliges mit `PivotFieldSubtotalType.AVERAGE` lässt daher beide aktiviert, so dass das Pivot-Table eine Summen-Zwischensumme, eine Durchschnitts-Zwischensumme und eine Gesamtsumme darstellt.

{{% alert color="primary" %}}
Nichts bezüglich der Zwischensummen ist spezifisch für den Zeilenbereich. Die gleichen `setSubtotals`-Aufrufe auf einem Feld, das aus `PivotTable.ColumnFields` stammt, erzeugen dieselben drei Layouts auf der Spaltenachse, da die Einstellung zum Pivot-Feld gehört und nicht zur Achse, auf der es sich befindet.
{{% /alert %}}

## **Verwandte Artikel**
- [Seitenfelder in Pivot-Tabellen](/cells/de/python-java/add-page-field-in-pivot-table/)
- [Aktualisieren von Pivot-Tabellen in Aspose.Cells für Python via Java](/cells/de/python-java/refresh-pivot-table/)
- [Anwenden von Stilen auf Pivot-Tabellen](/cells/de/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}