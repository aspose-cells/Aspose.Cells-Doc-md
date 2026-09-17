---
title: Seitenfeldlayout in Pivot-Tabelle ändern
description: Lernen Sie, wie Sie das Layout des Seitenfeldbereichs in einer Pivot-Tabelle mit Aspose.Cells for Node.js via Java steuern, einschließlich der Einstellung der Anzeigereihenfolge, der Umbruchanzahl und der Feldreihenfolge der Seitenfelder am oberen Rand der Pivot-Tabelle.
linktitle: Seitenfeldlayout in der Pivot-Tabelle ändern
keywords: Aspose.Cells, Node.js via Java Bibliothek, Tabellenkalkulation, Pivot-Tabelle, Seitenfeld, Seitenfeldreihenfolge, Umbruchanzahl, Seitenfeld verschieben
type: docs
weight: 191
url: /de/nodejs-java/change-page-field-layout/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Dieser Artikel ist eine Fortsetzung des Themas **Seitenfeld in Pivot-Tabelle hinzufügen**. Er zeigt, wie Sie das Layout des Seitenfeldbereichs — die Leiste mit Filtersteuerelementen am oberen Rand einer Pivot-Tabelle — steuern, einschließlich Anzeigereihenfolge, Umbruchanzahl und Feldneuanordnung.
{{% /alert %}}

## **Einführung**
Eine Pivot-Tabelle in Microsoft Excel stellt einen dedizierten **Seitenfeldbereich** bereit, der oberhalb des Zeilen-/Spalten-/Datenhauptteils der Tabelle liegt. Dieser Bereich wird als Leiste mit Dropdown-Filtersteuerelementen dargestellt (eines pro Seitenfeld) und ist das Element, auf das Endbenutzer klicken, um die Pivot-Tabelle nach Kriterien wie Jahr oder Region zu filtern. Aspose.Cells modelliert diesen Bereich über die `PivotTable.PageFields`-Sammlung und stellt drei Eigenschaften bereit, die steuern, wie die Leiste visuell angeordnet wird:
- `PivotTable.PageFieldOrder` (ein `Aspose.Cells.PrintOrderType`-Wert) legt fest, ob zusätzliche Seitenfelder *neben* den vorhandenen oder *unterhalb* davon platziert werden.
- `PivotTable.PageFieldWrapCount` legt fest, wie viele Seitenfelder pro Zeile oder Spalte platziert werden, bevor umgebrochen wird.
- `PivotTable.PageFields.Move(currIndex, destIndex)` ordnet die Seitenfelder neu an, ohne den Anordnungsmodus zu ändern.
Dieser Artikel führt durch drei Codebeispiele, die jede dieser Operationen an einem gemeinsamen Datensatz demonstrieren, sodass Sie die resultierenden Layouts direkt vergleichen können.

## **Quelldaten**
Alle drei folgenden Beispiele laden diese acht Zeilen Verkaufsdaten in ein Arbeitsblatt namens `PivotData`. Die Daten enthalten zwei Seitenfeldkandidaten (`Year`, `Region`), einen Zeilenfeldkandidaten (`Fruit`) und ein Maß (`Amount`), wodurch die Seitenfeldleiste sinnvoll zu prüfen ist.
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
Alle acht Zeilen werden in jedem Codebeispiel in identischer Reihenfolge gefüllt, sodass die Quelldaten zwischen den Szenarien nie abweichen — nur die Layout-Eigenschaften des Seitenfelds unterscheiden sich.

## **Beispiel 1: Über dann abwärts**
Im ersten Szenario konfigurieren wir die beiden Seitenfelder (`Year`, `Region`) so, dass sie **nebeneinander in einer einzigen Zeile** am oberen Rand der Pivot-Tabelle erscheinen. Wir weisen `Fruit` der Zeilenachse zu, platzieren `Year` zuerst und `Region` zweitens auf der Seitenachse (die Reihenfolge der `addFieldToArea`-Aufrufe bestimmt den Startindex), fügen `Amount` (Summe) als Datenfeld hinzu und setzen dann `PageFieldOrder` auf `PrintOrderType.OVER_THEN_DOWN` mit `PageFieldWrapCount = 2`. Mit `OVER_THEN_DOWN` und einer Umbruchanzahl von 2 werden die beiden Seitenfelder horizontal nebeneinander in einer einzigen Zeile am oberen Rand der Pivot-Tabelle angeordnet, sodass die Leiste eine Zeile hoch und zwei Spalten breit ist.

```javascript
let dataDir = "output";
if (!fs.existsSync(dataDir)) fs.mkdirSync(dataDir, { recursive: true });
let workbook = new AsposeCells.Workbook();
let worksheets = workbook.getWorksheets();
let pivotDataIdx = worksheets.add("PivotData");
let pivotDataSheet = worksheets.get(pivotDataIdx);
let pivotDataCells = pivotDataSheet.getCells();
// Kopfzeilen (Zeile 0)
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");
// Zeile 1: Apfel, 2022, Norden, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);
// Zeile 2: Apfel, 2023, Norden, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);
// Zeile 3: Banane, 2022, Süden, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);
// Zeile 4: Banane, 2023, Süden, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);
// Zeile 5: Kirsche, 2022, Osten, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);
// Zeile 6: Kirsche, 2023, Osten, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);
// Zeile 7: Traube, 2022, Westen, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);
// Zeile 8: Traube, 2023, Westen, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);
// PivotTableReport-Blatt hinzufügen
let pivotTableSheetIdx = worksheets.add("PivotTableReport");
let pivotTableSheet = worksheets.get(pivotTableSheetIdx);
let pivotTables = pivotTableSheet.getPivotTables();
// Pivot-Tabelle erstellen, die aus PivotData!A1:D9 stammt und bei A1 auf PivotTableReport platziert wird
let pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);
// Felder hinzufügen
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // Frucht
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // Jahr
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // Region
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // Betrag
pivotTable.getDataFields().get(0).setFunction(AsposeCells.ConsolidationFunction.Sum);
// Layout des Seitenfeldbereichs konfigurieren: Seitenfelder zuerst horizontal anordnen, nach jeweils 2 umbrechen
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);
// Aktualisieren und berechnen
pivotTable.calculateData();
// Speichern
workbook.save(path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```

## **Beispiel 2: Abwärts dann über**
In diesem Beispiel platzieren wir `Fruit` auf der Zeilenachse, `Year` und `Region` auf der Seitenachse (mit `Year` zuerst) und `Amount` (Summe) als Datenfeld — genau wie in Beispiel 1. Dann setzen wir `PageFieldOrder` auf `PrintOrderType.DOWN_THEN_OVER` und `PageFieldWrapCount` auf `2`. Mit `DOWN_THEN_OVER` und einer Umbruchanzahl von 2 werden die beiden Seitenfelder vertikal gestapelt — `Year` oben, `Region` direkt darunter — und bilden so eine einzelne Spalte am oberen Rand der Pivot-Tabelle. Die Leiste ist daher zwei Zeilen hoch und eine Spalte breit, im Gegensatz zu Beispiel 1.

```javascript
var workbook = new AsposeCells.Workbook();
var pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
var pivotReportIdx = workbook.getWorksheets().add("PivotTableReport");
var pivotReport = workbook.getWorksheets().get(pivotReportIdx);
var headers = ["Fruit", "Year", "Region", "Amount"];
for (var c = 0; c < headers.length; c++)
{
    pivotData.getCells().get(0, c).putValue(headers[c]);
}
var data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
];
for (var r = 0; r < data.length; r++)
{
    for (var c = 0; c < data[r].length; c++)
    {
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}
var idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
var pivotTable = pivotReport.getPivotTables().get(idx);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.DownThenOver);
pivotTable.setPageFieldWrapCount(2);
pivotTable.calculateData();
workbook.save("pageFieldLayout_downThenOver.xlsx");
```

## **Beispiel 3: Ein Seitenfeld verschieben**
Im dritten Szenario behalten wir diesen Datensatz und die Feldzuordnung bei, legen ein neutrales Layout fest (`OVER_THEN_DOWN` mit einer Umbruchanzahl von `2`) und demonstrieren dann die `PageFields.Move`-Operation. Der Aufruf `Move(0, 1)` verschiebt das Seitenfeld bei Index 0 (`Year`) auf Position 1, und das Seitenfeld, das sich auf Position 1 befand (`Region`), rückt auf Position 0. Nach diesem Aufruf ist `Region` das erste Seitenfeld und `Year` das zweite. Der Umbruch- und Anordnungsmodus bleiben unverändert, sodass die Leiste weiterhin horizontal nebeneinander dargestellt wird — nur die Reihenfolge der beiden Dropdowns wurde vertauscht.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const dataSheet = workbook.getWorksheets().get(0);
dataSheet.setName("PivotData");
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Year");
dataSheet.getCells().get("C1").putValue("Region");
dataSheet.getCells().get("D1").putValue("Amount");
dataSheet.getCells().get("A2").putValue("Apple");
dataSheet.getCells().get("B2").putValue(2022);
dataSheet.getCells().get("C2").putValue("North");
dataSheet.getCells().get("D2").putValue(150);
dataSheet.getCells().get("A3").putValue("Apple");
dataSheet.getCells().get("B3").putValue(2023);
dataSheet.getCells().get("C3").putValue("North");
dataSheet.getCells().get("D3").putValue(180);
dataSheet.getCells().get("A4").putValue("Banana");
dataSheet.getCells().get("B4").putValue(2022);
dataSheet.getCells().get("C4").putValue("South");
dataSheet.getCells().get("D4").putValue(120);
dataSheet.getCells().get("A5").putValue("Banana");
dataSheet.getCells().get("B5").putValue(2023);
dataSheet.getCells().get("C5").putValue("South");
dataSheet.getCells().get("D5").putValue(140);
dataSheet.getCells().get("A6").putValue("Cherry");
dataSheet.getCells().get("B6").putValue(2022);
dataSheet.getCells().get("C6").putValue("East");
dataSheet.getCells().get("D6").putValue(200);
dataSheet.getCells().get("A7").putValue("Cherry");
dataSheet.getCells().get("B7").putValue(2023);
dataSheet.getCells().get("C7").putValue("East");
dataSheet.getCells().get("D7").putValue(220);
dataSheet.getCells().get("A8").putValue("Grape");
dataSheet.getCells().get("B8").putValue(2022);
dataSheet.getCells().get("C8").putValue("West");
dataSheet.getCells().get("D8").putValue(90);
dataSheet.getCells().get("A9").putValue("Grape");
dataSheet.getCells().get("B9").putValue(2023);
dataSheet.getCells().get("C9").putValue("West");
dataSheet.getCells().get("D9").putValue(110);
const pivotSheetIdx = workbook.getWorksheets().add("PivotTableReport");
const pivotSheet = workbook.getWorksheets().get(pivotSheetIdx);
const pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable");
const pivotTable = pivotSheet.getPivotTables().get(pivotIdx);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.DATA, 3);
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);
pivotTable.getPageFields().move(0, 1);
pivotTable.calculateData();
workbook.save("pageFieldLayout_move.xlsx");
```

## **Verwandte Artikel**
- [Seitenfeld in Pivot-Tabelle hinzufügen](/cells/de/nodejs-java/add-page-field-in-pivot-table/) — die übergeordnete Seite, die vorstellt, wie Seitenfelder zu einer Pivot-Tabelle hinzugefügt werden.
- [Zeilen- und Spaltenfelder in Pivot-Tabelle](/cells/de/nodejs-java/row-and-column-fields/) — behandelt die Zuordnung von Feldern zu den Zeilen- und Spaltenachsen und ergänzt die hier gezeigte Seitenachsen-Arbeit.
- [Wertfelder in Pivot-Tabelle verwalten](/cells/de/nodejs-java/manage-value-fields/) — beschreibt, wie der Daten- (Wert-)Bereich konfiguriert wird, einschließlich der `Sum`-Aggregation, die in diesem Artikel verwendet wird.
- [Pivot-Tabelle aktualisieren](/cells/de/nodejs-java/refresh-pivot-table/) — erläutert `refreshData` und `calculateData`, die nach dem Neuordnen der Seitenfelder erforderlich sind.
- [Stil auf Pivot-Tabelle anwenden](/cells/de/nodejs-java/apply-style-to-pivot-table/) — zeigt, wie die gerenderte Pivot-Tabelle formatiert wird, nachdem die Seitenfeldleiste angeordnet wurde.

{{< app/cells/assistant language="nodejs-java" >}}