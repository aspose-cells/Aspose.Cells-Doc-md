---
title: Diskrete Gruppierung von Pivot-Feldelementen
linktitle: Diskrete Gruppierung
description: Erfahren Sie, wie Sie in Aspose.Cells for Python via Java mit der DiscreteGroupItem-Klasse und der Methode PivotFieldGroupOptions.getDiscreteGroupItems Pivot-Feldelemente in benutzerdefinierte Gruppen mit Namen wie Obst und Gemüse gruppieren.
keywords: Aspose.Cells, PivotTable, diskrete Gruppierung, DiscreteGroupItem, PivotFieldGroupOptions, Pivot-Feldelemente gruppieren, benutzerdefinierte Gruppen, PivotField.group, Python via Java, Excel-PivotTable
type: docs
weight: 90
url: /de/python-java/discrete-group-pivot-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
- Die automatische Gruppierung fasst Elemente nach Datentyp zusammen, etwa Datumsangaben nach Monaten und Quartalen oder Zahlen nach Bereichen. Die diskrete Gruppierung löst das entgegengesetzte Problem: Sie fasst bestimmte, nicht verwandte Elemente in benutzerdefinierte Gruppen mit eigenen Namen zusammen, beispielsweise Produkte zu den Gruppen „Obst“ und „Gemüse“, Filialen zu Regionen oder Konten zu Zonen. Aspose.Cells bietet die diskrete Gruppierung mithilfe der Klasse `DiscreteGroupItem` und der Methode `PivotFieldGroupOptions.getDiscreteGroupItems()` an.
- Eine Instanz von `DiscreteGroupItem` besteht aus einem Gruppennamen und den zugehörigen Elementen. Die Elemente können auf zwei Arten identifiziert werden: durch ihre Namen (`DiscreteGroupItem("fruit", ["grape", "cherry"])`) oder durch ihre nullbasierten Positionen in den Quelldaten (`DiscreteGroupItem("fruit", [0, 3])`). Beide Formen führen zum gleichen Ergebnis.
- Eine diskrete Gruppierung wird auf ein Pivot-Feld im Zeilen- oder Spaltenbereich einer PivotTable angewendet, indem die Optionen an `PivotField.group(PivotFieldGroupOptions)` übergeben werden.

## **Pivot-Feldelemente nach Elementnamen gruppieren**
Das folgende Beispiel erstellt eine kleine Liste mit Verkaufsdaten (Produkt, Datum und Betrag), erzeugt daraus eine PivotTable mit `product` im Zeilenbereich, `date` im Spaltenbereich und `amount` im Datenbereich und definiert anschließend anhand von Elementnamen zwei benutzerdefinierte Gruppen: Obst (Traube, Kirsche) und Gemüse (Karotte, Kartoffel). Das Ergebnis zeigt einen zweistufigen Aufbau des Zeilenbereichs: Der Gruppenname bildet die äußere Ebene, und die ursprünglichen Elemente sind darunter verschachtelt. So lassen sich Trends je benutzerdefinierter Gruppe und je Element ablesen.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    DiscreteGroupItem,
    PivotFieldGroupOptions,
    PivotFieldType,
    PivotTableStyleType,
)
GregorianCalendar = jpype.JPackage("java.util").GregorianCalendar
def create_date(year, month, day):
    calendar = GregorianCalendar(year, month - 1, day)
    return calendar.getTime()
wb = Workbook()
sheet = wb.getWorksheets().get(0)
cells = sheet.getCells()
cells.get(0, 0).putValue("product")
cells.get(1, 0).putValue("grape")
cells.get(2, 0).putValue("carrot")
cells.get(3, 0).putValue("potato")
cells.get(4, 0).putValue("cherry")
date_style = wb.createStyle()
date_style.setCustom("m/d/yyyy")
cells.get(0, 1).putValue("date")
cells.get(1, 1).putValue(create_date(2021, 2, 5))
cells.get(2, 1).putValue(create_date(2022, 3, 8))
cells.get(3, 1).putValue(create_date(2023, 4, 10))
cells.get(4, 1).putValue(create_date(2024, 5, 16))
for r in range(1, 5):
    cells.get(r, 1).setStyle(date_style)
cells.get(0, 2).putValue("amount")
cells.get(1, 2).putValue(50.0)
cells.get(2, 2).putValue(60.0)
cells.get(3, 2).putValue(70.0)
cells.get(4, 2).putValue(80.0)
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0)
pivot_table.addFieldToArea(PivotFieldType.ROW, "product")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "date")
pivot_table.addFieldToArea(PivotFieldType.DATA, "amount")
pivot_table.setPivotTableStyleType(
    PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
)
# Group specific items into custom groups by item names
fruit = DiscreteGroupItem("fruit", ["grape", "cherry"])
vegetable = DiscreteGroupItem("vegetable", ["carrot", "potato"])
group_options = PivotFieldGroupOptions()
group_options.setDiscreteGroupItems([fruit, vegetable])
pivot_table.calculateData()
pivot_table.getRowFields().get(0).group(group_options)
wb.save("outputDiscreteGroupPivotField.xlsx")
jpype.shutdownJVM()
```

Nach `calculateData()` zeigt der Zeilenbereich der PivotTable Obst (Traube 50, Kirsche 80) und Gemüse (Karotte 60, Kartoffel 70); die Gesamtsumme beträgt 260. Als Spaltenbeschriftungen bleiben die vier Datumsangaben (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024) erhalten.

## **Pivot-Feldelemente nach Elementindizes gruppieren**
Wenn die Elementnamen lang oder lokalisiert sind, identifiziert der zweite Konstruktor von `DiscreteGroupItem` die Elemente anhand ihres Index. Bei den Indizes handelt es sich um nullbasierte Positionen der Elemente in der Reihenfolge, in der sie in den Quelldaten erscheinen, nicht um alphabetische Positionen. In den Beispieldaten oben ist Traube Element 0, Karotte Element 1, Kartoffel Element 2 und Kirsche Element 3; Obst wird daher durch `{ 0, 3 }` und Gemüse durch `{ 1, 2 }` angegeben. Das Ergebnis ist identisch mit dem des namensbasierten Beispiels.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotFieldType,
    PivotTableStyleType,
)
Date = jpype.JClass("java.util.Date")
DiscreteGroupItem = jpype.JClass("com.aspose.cells.DiscreteGroupItem")
PivotFieldGroupOptions = jpype.JClass("com.aspose.cells.PivotFieldGroupOptions")
wb = Workbook()
sheet = wb.getWorksheets().get(0)
cells = sheet.getCells()
cells.get(0, 0).putValue("product")
cells.get(1, 0).putValue("grape")
cells.get(2, 0).putValue("carrot")
cells.get(3, 0).putValue("potato")
cells.get(4, 0).putValue("cherry")
date_style = wb.createStyle()
date_style.setCustom("m/d/yyyy")
cells.get(0, 1).putValue("date")
cells.get(1, 1).putValue(Date(2021 - 1900, 2 - 1, 5))
cells.get(2, 1).putValue(Date(2022 - 1900, 3 - 1, 8))
cells.get(3, 1).putValue(Date(2023 - 1900, 4 - 1, 10))
cells.get(4, 1).putValue(Date(2024 - 1900, 5 - 1, 16))
for r in range(1, 5):
    cells.get(r, 1).setStyle(date_style)
cells.get(0, 2).putValue("amount")
cells.get(1, 2).putValue(50.0)
cells.get(2, 2).putValue(60.0)
cells.get(3, 2).putValue(70.0)
cells.get(4, 2).putValue(80.0)
pivot_table = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0)
pivot_table.addFieldToArea(PivotFieldType.ROW, "product")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "date")
pivot_table.addFieldToArea(PivotFieldType.DATA, "amount")
pivot_table.setPivotTableStyleType(
    PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
)
pivot_table.calculateData()
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.setDiscreteGroupItems([fruit, vegetable])
pivot_table.getRowFields().get(0).group(group_options)
pivot_table.calculateData()
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx")
jpype.shutdownJVM()
```

## **Hinweis**

{{% alert color="primary" %}}
- Elemente, die keiner benutzerdefinierten Gruppe zugeordnet sind, gehen nicht verloren. Sie bleiben in der PivotTable auf derselben Ebene wie die benutzerdefinierten Gruppen und werden dort jeweils als eigener Eintrag mit einem einzelnen Element dargestellt. Wenn im Beispiel nur die Gruppe „Obst“ definiert wird, bleiben Karotte und Kartoffel als eigenständige Einträge im Zeilenbereich neben der Gruppe „Obst“ erhalten.
- Die Methoden `PivotFieldGroupOptions.getNewPivotField()` und `setNewPivotField()` steuern das Layout der diskreten Gruppierung. Der Standardwert von `getNewPivotField()` ist `true`. Dadurch wird das gruppierte Feld als neues äußeres Feld neben dem ursprünglichen Feld hinzugefügt, sodass das oben gezeigte zweistufige Layout entsteht (`getRowFields()` enthält anschließend 2 Einträge). Mit `setNewPivotField(false)` wird stattdessen das ursprüngliche Feld ersetzt; der Zeilenbereich zeigt dann nur eine Ebene mit den Gruppennamen und ihren aggregierten Werten: Obst 130 (50 + 80) und Gemüse 130 (60 + 70).
- Die namensbasierten und indexbasierten Konstruktoren von `DiscreteGroupItem` können innerhalb derselben `getDiscreteGroupItems()`-Sammlung kombiniert werden.
{{% /alert %}}

## **Verwandte Artikel**
- [Pivot-Felder in der PivotTable gruppieren](/cells/de/python-java/group-pivot-fields-in-the-pivot-table/)
- [Zeilen- und Spaltenfelder in einer PivotTable hinzufügen](/cells/de/python-java/pivot-table-add-row-and-column-fields/)
- [PivotTables nach Beschriftung oder Wert filtern](/cells/de/python-java/filter-by-label-or-value-of-pivot-table/)
- [Stil auf eine PivotTable anwenden](/cells/de/python-java/apply-style-to-pivot-table/)
- [PivotTable aktualisieren](/cells/de/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}