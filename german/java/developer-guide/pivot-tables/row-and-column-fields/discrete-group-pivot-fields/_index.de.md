---
title: Diskrete Gruppierung von Pivot-Feldelementen
linktitle: Diskrete Gruppierung
description: Erfahren Sie, wie Sie in Aspose.Cells for Java mit DiscreteGroupItem und PivotFieldGroupOptions.DiscreteGroupItems Elemente von Pivot-Feldern in benutzerdefinierte Gruppen mit Namen wie Obst und Gemüse gruppieren.
keywords: Aspose.Cells for Java, PivotTable, diskrete Gruppierung, DiscreteGroupItem, PivotFieldGroupOptions, Pivot-Elemente gruppieren, benutzerdefinierte Gruppen, PivotField.group, Java, Excel-PivotTable
type: docs
weight: 90
url: /de/java/discrete-group-pivot-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
- Bei der automatischen Gruppierung werden Elemente nach Datentyp gruppiert, etwa Datumsangaben nach Monaten und Quartalen oder Zahlen nach Bereichen. Die diskrete Gruppierung löst das entgegengesetzte Problem, indem sie bestimmte, unverbundene Elemente zu benutzerdefinierten Gruppen mit eigenen Namen gruppiert, beispielsweise Produkte zu den Gruppen Obst und Gemüse, Geschäfte zu Regionen oder Konten zu Zonen. Aspose.Cells stellt die diskrete Gruppierung über die Klasse `DiscreteGroupItem` und die Eigenschaft `PivotFieldGroupOptions.getDiscreteGroupItems()` bereit.
- Ein `DiscreteGroupItem` besteht aus einem Gruppennamen und den Elementen, die dazu gehören. Die Elemente können auf zwei Arten identifiziert werden: anhand ihrer Namen (`new DiscreteGroupItem("fruit", new String[] { "grape", "cherry" })`) oder anhand ihrer nullbasierten Positionen in den Quelldaten (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). Beide Formen führen zum selben Ergebnis.
- Die diskrete Gruppierung wird für ein Feld im Zeilen- oder Spaltenbereich einer PivotTable angewendet, indem die Optionen an `PivotField.group(PivotFieldGroupOptions)` übergeben werden.

## **Pivot-Feldelemente nach Elementnamen gruppieren**
Das folgende Beispiel erstellt eine kleine Verkaufsliste (Produkt, Datum und Betrag), erzeugt daraus eine PivotTable mit `product` im Zeilenbereich, `date` im Spaltenbereich und `amount` im Datenbereich und definiert anschließend anhand der Elementnamen zwei benutzerdefinierte Gruppen: `fruit` (`grape`, `cherry`) und `vegetables` (`carrot`, `potato`). Das Ergebnis zeigt ein zweistufiges Zeilenlayout: Der Gruppenname bildet die äußere Ebene, und die ursprünglichen Elemente sind darunter verschachtelt. So lassen sich Trends je benutzerdefinierter Gruppe und je Element ablesen.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook();
Worksheet sheet = wb.getWorksheets().get(0);
Cells cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
Style dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(new DateTime(2021, 2, 5));
cells.get(2, 1).putValue(new DateTime(2022, 3, 8));
cells.get(3, 1).putValue(new DateTime(2023, 4, 10));
cells.get(4, 1).putValue(new DateTime(2024, 5, 16));
for (int r = 1; r <= 4; r++) cells.get(r, 1).setStyle(dateStyle);
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
// Group specific items into custom groups by item names
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new String[] { "grape", "cherry" });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new String[] { "carrot", "potato" });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems(new DiscreteGroupItem[] { fruit, vegetable });
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

Nach `calculateData()` zeigt der Zeilenbereich der PivotTable `fruit` (`grape` 50, `cherry` 80) und `vegetable` (`carrot` 60, `potato` 70) mit der Gesamtsumme 260. In den Spaltenbeschriftungen werden weiterhin die vier Datumsangaben (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024) angezeigt.

## **Pivot-Feldelemente nach Elementindizes gruppieren**
Wenn die Elementnamen lang oder lokalisiert sind, identifiziert der zweite Konstruktor von `DiscreteGroupItem` die Elemente anhand ihres Index. Die Indizes sind nullbasierte Positionen der Elemente in der Reihenfolge ihres Auftretens in den Quelldaten und nicht in alphabetischer Reihenfolge. In den Beispieldaten oben ist `grape` Element 0, `carrot` Element 1, `potato` Element 2 und `cherry` Element 3. Daher ist `fruit` `{ 0, 3 }` und `vegetable` `{ 1, 2 }`. Das Ergebnis ist mit dem namensbasierten Beispiel identisch.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook();
Worksheet sheet = wb.getWorksheets().get(0);
Cells cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
Style dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(new DateTime(2021, 2, 5));
cells.get(2, 1).putValue(new DateTime(2022, 3, 8));
cells.get(3, 1).putValue(new DateTime(2023, 4, 10));
cells.get(4, 1).putValue(new DateTime(2024, 5, 16));
for (int r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
PivotTable pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new int[] { 0, 3 });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new int[] { 1, 2 });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems(new DiscreteGroupItem[] { fruit, vegetable });
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Hinweis**

{{% alert color="primary" %}}
- Elemente, die keiner benutzerdefinierten Gruppe zugeordnet sind, gehen nicht verloren. Sie bleiben in der PivotTable auf derselben Ebene wie die benutzerdefinierten Gruppen und bilden jeweils einen eigenen Eintrag mit einem einzelnen Element. Im obigen Beispiel bleiben `carrot` und `potato` bei der Definition nur der Gruppe `fruit` als eigenständige Einträge im Zeilenbereich neben der Gruppe `fruit`.
- Die Eigenschaft `PivotFieldGroupOptions.getNewPivotField()` steuert das Layout der diskreten Gruppierung. Standardmäßig ist ihr Wert `true`; dadurch wird das gruppierte Feld als neues äußeres Feld neben dem ursprünglichen Feld hinzugefügt und so entsteht das oben gezeigte zweistufige Layout (die Anzahl der Einträge in `getRowFields()` steigt auf 2). Setzen Sie den Wert mit `setNewPivotField(false)` auf `false`, um stattdessen das ursprüngliche Feld zu ersetzen. Der Zeilenbereich zeigt dann eine einzige Ebene, die nur die Gruppennamen mit ihren aggregierten Werten enthält: `fruit` 130 (50 + 80) und `vegetable` 130 (60 + 70).
- Die namensbasierten und indexbasierten Konstruktoren von `DiscreteGroupItem` können innerhalb desselben über `getDiscreteGroupItems()` abgerufenen Arrays kombiniert werden.
{{% /alert %}}

## **Verwandte Artikel**
- [Pivot-Felder in der PivotTable gruppieren](/cells/de/java/group-pivot-fields-in-the-pivot-table/)
- [Zeilen- und Spaltenfelder in der PivotTable hinzufügen](/cells/de/java/pivot-table-add-row-and-column-fields/)
- [PivotTables nach Bezeichnung oder Wert filtern](/cells/de/java/filter-by-label-or-value-of-pivot-table/)
- [Stil auf eine PivotTable anwenden](/cells/de/java/apply-style-to-pivot-table/)
- [PivotTable aktualisieren](/cells/de/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}