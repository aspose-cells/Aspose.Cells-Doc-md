---
title: Diskrete Gruppierung von Pivot-Feldelementen
linktitle: Diskrete Gruppierung
description: Erfahren Sie, wie Sie Pivot-Feldelemente mithilfe von DiscreteGroupItem und PivotFieldGroupOptions.DiscreteGroupItems in Aspose.Cells for .NET in benutzerdefinierte Gruppen mit Namen wie Obst und Gemüse gruppieren.
keywords: Aspose.Cells, PivotTable, diskrete Gruppierung, DiscreteGroupItem, PivotFieldGroupOptions, Pivot-Elemente gruppieren, benutzerdefinierte Gruppen, PivotField.Group, C#, Excel-PivotTable
type: docs
weight: 90
url: /de/net/discrete-group-pivot-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Verwendungsszenarien**
- Die automatische Gruppierung ordnet Elemente nach Datentyp zu, etwa Datumsangaben nach Monaten und Quartalen oder Zahlen nach Bereichen. Die diskrete Gruppierung löst das umgekehrte Problem, indem sie bestimmte, nicht zusammengehörende Elemente in benutzerdefinierte Gruppen mit Namen einordnet, beispielsweise Produkte in Obst und Gemüse, Filialen in Regionen oder Konten in Zonen. Aspose.Cells stellt die diskrete Gruppierung über die Klasse `DiscreteGroupItem` und die Eigenschaft `PivotFieldGroupOptions.DiscreteGroupItems` bereit.
- Ein `DiscreteGroupItem` besteht aus einem Gruppennamen und den zugehörigen Elementen. Die Elemente können auf zwei Arten identifiziert werden: anhand ihrer Namen (`new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" })`) oder anhand ihrer nullbasierten Positionen in den Quelldaten (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). Beide Varianten führen zum gleichen Ergebnis.
- Zur diskreten Gruppierung eines Felds im Zeilen- oder Spaltenbereich einer PivotTable werden die Optionen an `PivotField.Group(PivotFieldGroupOptions)` übergeben.

## **Pivot-Feldelemente nach Elementnamen gruppieren**
Das folgende Beispiel erstellt eine kleine Verkaufsliste (Produkt, Datum und Betrag). Daraus wird eine PivotTable mit `product` im Zeilenbereich, `date` im Spaltenbereich und `amount` im Datenbereich erzeugt. Anschließend werden anhand der Elementnamen zwei benutzerdefinierte Gruppen definiert: fruit (grape, cherry) und vegetable (carrot, potato). Das Ergebnis zeigt eine zweistufige Zeilenstruktur: Der Gruppenname bildet die äußere Ebene, und die ursprünglichen Elemente sind darunter verschachtelt. Damit lassen sich Trends je benutzerdefinierter Gruppe und je Element ablesen.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook wb = new Workbook();
Worksheet sheet = wb.Worksheets[0];
Cells cells = sheet.Cells;
cells[0, 0].Value = "product";
cells[1, 0].Value = "grape";
cells[2, 0].Value = "carrot";
cells[3, 0].Value = "potato";
cells[4, 0].Value = "cherry";
Style dateStyle = wb.CreateStyle();
dateStyle.Custom = "m/d/yyyy";
cells[0, 1].Value = "date";
cells[1, 1].Value = new DateTime(2021, 2, 5);
cells[2, 1].Value = new DateTime(2022, 3, 8);
cells[3, 1].Value = new DateTime(2023, 4, 10);
cells[4, 1].Value = new DateTime(2024, 5, 16);
for (int r = 1; r <= 4; r++) cells[r, 1].SetStyle(dateStyle);
cells[0, 2].Value = "amount";
cells[1, 2].Value = 50;
cells[2, 2].Value = 60;
cells[3, 2].Value = 70;
cells[4, 2].Value = 80;
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.PivotTables.Add("=Sheet1!A1:C5", 11, 0);
pivotTable.AddFieldToArea(PivotFieldType.Row, "product");
pivotTable.AddFieldToArea(PivotFieldType.Column, "date");
pivotTable.AddFieldToArea(PivotFieldType.Data, "amount");
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleMedium10;
// Group specific items into custom groups by item names
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new string[] { "carrot", "potato" });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.DiscreteGroupItems = new DiscreteGroupItem[] { fruit, vegetable };
pivotTable.RowFields[0].Group(groupOptions);
pivotTable.CalculateData();
wb.Save("outputDiscreteGroupPivotField.xlsx");
```

Nach `CalculateData()` zeigt der Zeilenbereich der PivotTable die Gruppen fruit (grape 50, cherry 80) und vegetable (carrot 60, potato 70); die Gesamtsumme beträgt 260. Die Spaltenbeschriftungen weisen weiterhin die vier Datumsangaben (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024) aus.

## **Pivot-Feldelemente nach Elementindizes gruppieren**
Wenn die Elementnamen lang oder lokalisiert sind, identifiziert der zweite Konstruktor von `DiscreteGroupItem` die Elemente anhand ihrer Indizes. Die Indizes entsprechen den nullbasierten Positionen der Elemente in der Reihenfolge, in der sie in den Quelldaten erscheinen, und nicht deren alphabetischen Reihenfolge. In den Beispieldaten oben ist grape Element 0, carrot Element 1, potato Element 2 und cherry Element 3. Daher entspricht fruit `{ 0, 3 }` und vegetable `{ 1, 2 }`. Das Ergebnis ist mit dem namensbasierten Beispiel identisch.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook wb = new Workbook();
Worksheet sheet = wb.Worksheets[0];
Cells cells = sheet.Cells;
cells[0, 0].Value = "product";
cells[1, 0].Value = "grape";
cells[2, 0].Value = "carrot";
cells[3, 0].Value = "potato";
cells[4, 0].Value = "cherry";
Style dateStyle = wb.CreateStyle();
dateStyle.Custom = "m/d/yyyy";
cells[0, 1].Value = "date";
cells[1, 1].Value = new DateTime(2021, 2, 5);
cells[2, 1].Value = new DateTime(2022, 3, 8);
cells[3, 1].Value = new DateTime(2023, 4, 10);
cells[4, 1].Value = new DateTime(2024, 5, 16);
for (int r = 1; r <= 4; r++) cells[r, 1].SetStyle(dateStyle);
cells[0, 2].Value = "amount";
cells[1, 2].Value = 50;
cells[2, 2].Value = 60;
cells[3, 2].Value = 70;
cells[4, 2].Value = 80;
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.PivotTables.Add("=Sheet1!A1:C5", 11, 0);
pivotTable.AddFieldToArea(PivotFieldType.Row, "product");
pivotTable.AddFieldToArea(PivotFieldType.Column, "date");
pivotTable.AddFieldToArea(PivotFieldType.Data, "amount");
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleMedium10;
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data)
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new int[] { 0, 3 });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new int[] { 1, 2 });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.DiscreteGroupItems = new DiscreteGroupItem[] { fruit, vegetable };
pivotTable.RowFields[0].Group(groupOptions);
pivotTable.CalculateData();
wb.Save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Hinweis**

{{% alert color="primary" %}}
- Elemente, die keiner benutzerdefinierten Gruppe zugeordnet sind, gehen nicht verloren. Sie bleiben in der PivotTable auf derselben Ebene wie die benutzerdefinierten Gruppen, jeweils als eigener Eintrag mit einem einzigen Element. Im obigen Beispiel bleiben carrot und potato im Zeilenbereich als eigenständige Einträge neben der Gruppe fruit, wenn nur die Gruppe fruit definiert wird.
- Die Eigenschaft `PivotFieldGroupOptions.NewPivotField` steuert den Aufbau der diskreten Gruppierung. Der Standardwert ist `true`. Dadurch wird das gruppierte Feld als neues äußeres Feld neben dem ursprünglichen eingefügt und die oben gezeigte zweistufige Struktur erzeugt (`RowFields` enthält dann 2 Einträge). Setzen Sie den Wert auf `false`, wird das ursprüngliche Feld durch das gruppierte ersetzt. Der Zeilenbereich zeigt dann nur eine Ebene mit den Gruppennamen und ihren aggregierten Werten: fruit 130 (50 + 80) und vegetable 130 (60 + 70).
- Die namensbasierten und indexbasierten Konstruktoren von `DiscreteGroupItem` können innerhalb desselben `DiscreteGroupItems`-Arrays kombiniert werden.
{{% /alert %}}

## **Verwandte Artikel**
- [Pivot-Felder in der PivotTable gruppieren](/cells/de/net/group-pivot-fields-in-the-pivot-table/)
- [Zeilen- und Spaltenfelder zur PivotTable hinzufügen](/cells/de/net/pivot-table-add-row-and-column-fields/)
- [PivotTable nach Bezeichnung oder Wert filtern](/cells/de/net/filter-by-label-or-value-of-pivot-table/)
- [Formatierung auf eine PivotTable anwenden](/cells/de/net/apply-style-to-pivot-table/)
- [PivotTable aktualisieren](/cells/de/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}