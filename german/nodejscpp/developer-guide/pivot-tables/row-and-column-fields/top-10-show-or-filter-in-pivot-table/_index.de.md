---
title: Top 10 in PivotTable anzeigen oder filtern
linktitle: Top 10 in PivotTable anzeigen oder filtern
description: Erfahren Sie, wie Sie mit Aspose.Cells for Node.js via C++ in einer PivotTable nur die Elemente eines Pivot-Felds mit dem höchsten oder niedrigsten Rang anzeigen. Dieser Artikel behandelt die Methode Top10AutoShow für Excel 97-2003, das Lesen der Optionen mit Top10AutoShowSettings sowie den Top-10-Filter für Excel 2007-365 über FilterTop10.
keywords: Aspose.Cells, Node.js via C++, PivotTable, Top 10, automatisches Anzeigen, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, Node.js
type: docs
weight: 20
url: /de/nodejs-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Eine PivotTable, die jedes Element eines Zeilenfelds auflistet, kann schwer lesbar sein, wenn das Feld Dutzende Elemente enthält. Ein Top-10-Bericht behält nur die Elemente mit dem höchsten oder niedrigsten Rang bei – genau das ist der Zweck von Rankingberichten, etwa „die 5 umsatzstärksten Produkte“ oder „die 3 Regionen mit der niedrigsten Verkaufsanzahl“. Aspose.Cells unterstützt hierfür zwei Mechanismen, die den beiden Generationen von Microsoft Excel entsprechen.
- **Excel 97-2003 AutoShow** — die Methode `pivotField.top10AutoShow()`. Dies ist die klassische Einstellung zum Anzeigen der obersten/untersten N-Elemente, die direkt auf dem Pivot-Feld gespeichert wird. Sie funktioniert in alten und neuen Excel-Versionen, da sie Bestandteil des ursprünglichen PivotTable-Formats ist.
- **Excel 2007-365 Top-10-Filter** — die Methode `pivotField.filterTop10()`. Dieser moderne Top-10-Wertfilter ist im Feldmenü unter „Wertfilter“ verfügbar. Er wird als `PivotFilter`-Objekt gespeichert, das dem Feld zugeordnet ist, und ermöglicht eine Rangfolge nach Elementanzahl oder Prozentsatz.

## **Top 10 in Excel 97-2003 anzeigen (top10AutoShow)**
Der klassische AutoShow wird mit einem einzigen Aufruf von `pivotField.top10AutoShow(isAutoShow, isTop, count, rankBy)` konfiguriert:
- `isAutoShow` — aktiviert oder deaktiviert die AutoShow-Einstellung am Feld.
- `isTop` — `true` behält die am höchsten rangierten Elemente (Oben), `false` die am niedrigsten rangierten (Unten).
- `count` — legt fest, wie viele Elemente beibehalten werden, beispielsweise 10 für einen klassischen Top-10-Bericht.
- `rankBy` — der nullbasierte Index des **Datenfelds**, mit dessen Werten die Elemente rangiert werden. Übergeben Sie -1, um die Elemente nach dem Feld selbst zu rangieren.
Die Rangfolge kann auf einem Wertfeld oder auf dem Feld selbst basieren. Im Folgenden werden zwei naheliegende Varianten gezeigt.

### **Nach einem Wertfeld rangieren**
Rangieren Sie die Elemente des Zeilenfelds anhand eines gewöhnlichen Wertfelds wie „Summe der Verkäufe“. Das folgende Beispiel erstellt eine PivotTable mit einem Zeilenfeld (`Sport`) und einem Datenfeld (`Sales`) und zeigt anschließend die 2 Sportarten mit dem höchsten Umsatz. `rankBy` ist 0, da „Summe der Verkäufe“ dem Datenfeld an Index 0 entspricht.

```javascript
const AsposeCells = require("aspose.cells.node");

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");```

```

### **Nach dem Feld selbst rangieren**
Ein Feld kann auch nach sich selbst rangiert werden – übergeben Sie -1 als `rankBy`. Für diese Variante ist kein zusätzliches Datenfeld erforderlich; das Feld muss lediglich im Zeilen- oder Spaltenbereich liegen. Das folgende Beispiel zeigt die 3 Sportarten, die nach dem Feld selbst am niedrigsten rangieren. Beim Speichern dieser Einstellung wird das Attribut `rankBy` aus dem XML der PivotTable ausgelassen, da -1 der Standardwert des Formats ist. `top10AutoShowSettings.getRankBy()` gibt -1 zurück.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the bottom 3 items ranked by the field itself (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");```
```

## **Aktuelle Optionen lesen (Top10AutoShowSettings)**
Der Getter `pivotField.getTop10AutoShowSettings()` gibt ein `PivotFieldTop10AutoShowSettings`-Objekt zurück, das die aktuell auf dem Feld gespeicherten AutoShow-Optionen enthält. Verwenden Sie das Objekt, um zu prüfen, wie die Elemente einer vorhandenen Arbeitsmappe oder einer gerade konfigurierten PivotTable dargestellt werden – auch bei aus einer Datei geladenen Arbeitsmappen.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("output-top10-by-value-field.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const sportField = pivotTable.getRowFields().get(0);
const settings = sportField.getTop10AutoShowSettings();
console.log("AutoShow enabled: " + settings.isAutoShow);
console.log("Direction: " + (settings.isTop ? "Top" : "Bottom"));
console.log("Item count: " + settings.getAutoShowCount());
console.log("Ranking data field index: " + settings.getRankBy());
```

Die vier Eigenschaften entsprechen den klassischen AutoShow-Attributen, die in das XML der PivotTable geschrieben werden (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`). Die zurückgelesenen Werte entsprechen daher den Werten, die jede Excel-Version berücksichtigt.

## **Hinweis**

{{% alert color="primary" %}}
- Die direkten Getter `isAutoShow`, `getIsAscendShow()`, `getAutoShowCount()` und `getAutoShowField()` von `PivotField` sind als veraltet markiert. Verwenden Sie stattdessen das `Top10AutoShowSettings`-Objekt: `pivotField.isAutoShow` wird zu `top10AutoShowSettings.isAutoShow`, `pivotField.getIsAscendShow()` wird zu `top10AutoShowSettings.isTop`, `pivotField.getAutoShowCount()` wird zu `top10AutoShowSettings.getAutoShowCount()` und `pivotField.getAutoShowField()` wird zu `top10AutoShowSettings.getRankBy()`. Die Methode `pivotField.top10AutoShow()` selbst ist die unterstützte Methode zum Ändern der Einstellungen.
- `top10AutoShow()` funktioniert mit Zeilen- und Spaltenfeldern. Ein Feld, das sich ausschließlich im Seitenbereich (Filterbereich) befindet, kann auf diese Weise nicht rangiert werden, da seine Elemente nicht im PivotTable-Körper angeordnet sind.
{{% /alert %}}

## **Excel 2007-365: Top-10-Filter (filterTop10)**
Moderne Excel-Versionen stellen Top 10 im Feldmenü als Wertfilter bereit (Wertfilter, Top 10...). Aspose.Cells bildet diesen Filter mit der Methode `pivotField.filterTop10(valueFieldIndex, type, isTop, itemCount)` ab, die den erstellten `PivotFilter` zurückgibt:
- `valueFieldIndex` — der nullbasierte Index des Datenfelds, mit dessen aggregierten Werten die Elemente rangiert werden.
- `type` — legt fest, was `itemCount` bedeutet. `PivotFilterType.Count` behält eine feste Anzahl von Elementen bei (Option „Elemente“ im Dialog). `PivotFilterType.Percent` behält einen Prozentsatz der Elemente bei, sodass `itemCount` der Prozentsatz selbst ist – mit einem `itemCount` von 30 werden die obersten 30 Prozent beibehalten. `PivotFilterType.SUM` rankiert die Elemente anhand der kumulierten Wertabdeckung.
- `isTop` — `true` für „Oben“, `false` für „Unten“.
- `itemCount` — der Wert N in „Top N“; seine Einheit hängt von `type` ab.

```javascript
const AsposeCells = require("aspose.cells.node");

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
const filter = sportField.filterTop10(0, AsposeCells.PivotFilterType.Count, true, 2);
// For a percentage-based filter instead, keep the top 30 percent of the items:
// sportField.filterTop10(0, AsposeCells.PivotFilterType.Percent, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");```

```

{{% alert color="primary" %}}
`top10AutoShow` und `filterTop10` sind zwei getrennte Funktionen. AutoShow schreibt das klassische `autoShow`-Attribut, das direkt auf dem Pivot-Feld gespeichert wird. Diese Einstellung wird von allen Excel-Versionen ab Excel 97 berücksichtigt. `filterTop10` schreibt einen modernen `PivotFilter`-Eintrag, der Excel 2007 oder eine neuere Version erfordert. Wird eine Arbeitsmappe in einer älteren Excel-Version geöffnet, fällt eine PivotTable, die den modernen Filter verwendet, auf die Anzeige aller Elemente zurück. Für Dokumente, die mithilfe von Tools für ältere Versionen hin- und zurück verarbeitet werden müssen, ist `top10AutoShow` vorzuziehen; für moderne Arbeitsmappen ist `filterTop10` vorzuziehen, da der Filter sich mit den anderen Wertfiltern kombinieren lässt.
{{% /alert %}}

## **Verwandte Artikel**
- [PivotTables nach Bezeichner oder Wert filtern](/cells/de/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [Zeilen- und Spaltenfelder zur PivotTable hinzufügen](/cells/de/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Pivot-Felder in der PivotTable gruppieren](/cells/de/nodejs-cpp/group-pivot-fields-in-the-pivot-table/)
- [PivotTable aktualisieren](/cells/de/nodejs-cpp/refresh-pivot-table/)
- [Seitenfeld zur PivotTable hinzufügen](/cells/de/nodejs-cpp/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}