---
title: Top 10 in einer PivotTable anzeigen oder filtern
linktitle: Top 10 in einer PivotTable anzeigen oder filtern
description: Erfahren Sie, wie Sie mit Aspose.Cells for Node.js via Java nur die höchst- oder niedrigst eingestuften Elemente eines Pivot-Felds anzeigen. Dieser Artikel behandelt die Methode Top10AutoShow für Excel 97-2003, das Lesen von Optionen mit Top10AutoShowSettings sowie den Top-10-Filter für Excel 2007-365 über FilterTop10.
keywords: Aspose.Cells, Node.js via Java, PivotTable, Top 10, AutoShow, top10AutoShow, getTop10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, JavaScript
type: docs
weight: 20
url: /de/nodejs-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Eine PivotTable, die jedes Element eines Zeilenfelds auflistet, kann schwer zu lesen sein, wenn das Feld Dutzende Mitglieder enthält. Ein Top-10-Bericht behält nur die höchst- oder niedrigst eingestuften Elemente und erfüllt damit genau die Anforderungen von Berichten mit Rangfolge – etwa „5 Produkte mit dem höchsten Umsatz“ oder „3 Regionen mit der niedrigsten Verkaufsanzahl“. Aspose.Cells unterstützt zwei Mechanismen dafür, die den beiden Generationen von Microsoft Excel entsprechen.
- **Excel 97-2003 AutoShow** – die Methode `PivotField.top10AutoShow()`. Dies ist die klassische Einstellung „N höchste/niedrigste Elemente anzeigen“, die direkt am Pivot-Feld gespeichert wird. Sie funktioniert in jeder Excel-Version, ob alt oder neu, da sie Bestandteil des ursprünglichen PivotTable-Formats ist.
- **Excel 2007-365 Top-10-Filter** – die Methode `PivotField.filterTop10()`. Dies ist der moderne Top-10-Wertfilter im Feldmenü („Wertfilter“). Er wird als `PivotFilter`-Objekt gespeichert, das dem Feld zugeordnet ist, und bietet eine Rangierung anhand der Elementanzahl oder des Prozentsatzes.

## **Top 10 in Excel 97-2003 anzeigen (Top10AutoShow)**
Das klassische AutoShow wird mit einem einzigen Aufruf von `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)` konfiguriert:
- `isAutoShow` – aktiviert oder deaktiviert die AutoShow-Einstellung am Feld.
- `isTop` – `true` behält die höchst eingestuften Elemente (Oben), `false` die niedrigst eingestuften Elemente (Unten).
- `count` – die Anzahl der beizubehaltenden Elemente, beispielsweise 10 für einen klassischen Top-10-Bericht.
- `rankBy` – der nullbasierte Index des **Datenfelds**, dessen Werte die Rangfolge der Elemente bestimmen. Übergeben Sie -1, um die Elemente nach dem Feld selbst zu ordnen.
Die Rangfolge kann durch ein Wertfeld oder durch das Feld selbst bestimmt werden. Im Folgenden werden zwei naheliegende Varianten gezeigt.

### **Nach einem Wertfeld ordnen**
Ordnen Sie die Elemente des Zeilenfelds nach einem gewöhnlichen Wertfeld wie `Sum of Sales`. Das folgende Beispiel erstellt eine PivotTable mit einem Zeilenfeld (`Sport`) und einem Datenfeld (`Sales`) und zeigt anschließend die 2 Sportarten mit dem höchsten Umsatz. `rankBy` ist 0, da `Sum of Sales` das Datenfeld mit dem Index 0 ist.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");```

```

### **Nach dem Feld selbst ordnen**
Ein Feld kann auch nach sich selbst geordnet werden – geben Sie -1 als `rankBy` an. Für diese Variante ist kein zusätzliches Datenfeld erforderlich; das Feld muss lediglich im Zeilen- oder Spaltenbereich der PivotTable liegen. Das folgende Beispiel zeigt die 3 Sportarten mit der niedrigsten Rangfolge, wenn nach dem Feld selbst sortiert wird. Beim Speichern dieser Einstellung wird das Attribut `rankBy` aus dem XML der PivotTable weggelassen, da -1 der Standardwert des Formats ist. `getTop10AutoShowSettings().getRankBy()` gibt -1 zurück.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the bottom 3 items ranked by the field itself (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");```
```

## **Aktuelle Optionen lesen (Top10AutoShowSettings)**
Die Methode `PivotField.getTop10AutoShowSettings()` gibt ein `PivotFieldTop10AutoShowSettings`-Objekt zurück, das die aktuell am Feld gespeicherten AutoShow-Optionen enthält. Verwenden Sie es, um zu prüfen, wie die Elemente in einer bestehenden Arbeitsmappe beziehungsweise einer gerade konfigurierten PivotTable dargestellt werden. Dies gilt auch für Arbeitsmappen, die aus einer Datei geladen wurden.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("output-top10-by-value-field.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const sportField = pivotTable.getRowFields().get(0);
const settings = sportField.getTop10AutoShowSettings();
console.log("AutoShow enabled: " + settings.isAutoShow());
console.log("Direction: " + (settings.isTop() ? "Top" : "Bottom"));
console.log("Item count: " + settings.getAutoShowCount());
console.log("Ranking data field index: " + settings.getRankBy());
```

Die Getter `isAutoShow()`, `isTop()`, `getAutoShowCount()` und `getRankBy()` bilden die klassischen AutoShow-Attribute ab, die in das XML der PivotTable geschrieben werden (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`). Somit werden beim Zurücklesen genau die Werte erfasst, die von jeder Excel-Version berücksichtigt werden.

## **Hinweis**

{{% alert color="primary" %}}
- Die direkten Getter von `PivotField` – `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` und `getAutoShowField()` – sind als veraltet markiert. Verwenden Sie stattdessen das Objekt `getTop10AutoShowSettings()`: `isAutoShow()` wird zu `getTop10AutoShowSettings().isAutoShow()`, `isAscendShow()` wird zu `getTop10AutoShowSettings().isTop()`, `getAutoShowCount()` wird zu `getTop10AutoShowSettings().getAutoShowCount()` und `getAutoShowField()` wird zu `getTop10AutoShowSettings().getRankBy()`. Die Methode `top10AutoShow()` selbst ist der unterstützte Weg zum Ändern der Einstellungen.
- `top10AutoShow()` funktioniert mit Zeilen- und Spaltenfeldern. Ein Feld, das ausschließlich im Bereich der Seitenfelder (Filterbereich) liegt, kann auf diese Weise nicht eingeordnet werden, da seine Elemente nicht im PivotTable-Körper angeordnet sind.
{{% /alert %}}

## **Excel 2007-365: Top-10-Filter (FilterTop10)**
Moderne Excel-Versionen bieten Top 10 als Wertfilter im Feldmenü (Wertfilter, Top 10...) an. Aspose.Cells bildet dies mit der Methode `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)` ab, die den erstellten `PivotFilter` zurückgibt:
- `valueFieldIndex` – der nullbasierte Index des Datenfelds, dessen aggregierte Werte die Rangfolge der Elemente bestimmen.
- `type` – legt fest, was `itemCount` bedeutet. `PivotFilterType.COUNT` behält eine feste Anzahl von Elementen bei (Option „Elemente“ des Dialogfelds). `PivotFilterType.PERCENT` behält einen Prozentsatz der Elemente bei, sodass `itemCount` selbst der Prozentsatz ist – der Wert 30 bewirkt, dass die 30 Prozent mit dem höchsten Rang beibehalten werden. `PivotFilterType.SUM` basiert die Rangierung auf der kumulierten Wertabdeckung.
- `isTop` – `true` für Oben, `false` für Unten.
- `itemCount` – die Zahl N in einem Top-N-Filter; ihre Einheit hängt von `type` ab.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
const filter = sportField.filterTop10(0, AsposeCells.PivotFilterType.COUNT, true, 2);
// For a percentage-based filter instead, keep the top 30 percent of the items:
// sportField.filterTop10(0, AsposeCells.PivotFilterType.PERCENT, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");```

```

{{% alert color="primary" %}}
`top10AutoShow()` und `filterTop10()` sind zwei getrennte Funktionen. AutoShow schreibt das klassische Attribut `autoShow`, das direkt am Pivot-Feld gespeichert wird. Diese Einstellung wird von allen Excel-Versionen ab Excel 97 berücksichtigt. `filterTop10()` schreibt einen modernen `PivotFilter`-Eintrag, für den Excel 2007 oder höher erforderlich ist. Wenn eine Arbeitsmappe in einer älteren Excel-Version geöffnet wird, zeigt eine PivotTable mit dem modernen Filter stattdessen alle Elemente an. Für Dokumente, die einen vollständigen Hin- und Rücklauf durch ältere Werkzeuge benötigen, ist `top10AutoShow()` vorzuziehen; für moderne Arbeitsmappen ist `filterTop10()` vorzuziehen, da es sich mit den übrigen Wertfiltern kombinieren lässt.
{{% /alert %}}

## **Verwandte Artikel**
- [PivotTables nach Bezeichnung oder Wert filtern](/cells/de/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Zeilen- und Spaltenfelder zur PivotTable hinzufügen](/cells/de/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Pivot-Felder in der PivotTable gruppieren](/cells/de/nodejs-java/group-pivot-fields-in-the-pivot-table/)
- [PivotTable aktualisieren](/cells/de/nodejs-java/refresh-pivot-table/)
- [Seitenfeld zur PivotTable hinzufügen](/cells/de/nodejs-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}