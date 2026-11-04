---
title: Top 10 in PivotTable anzeigen oder filtern
linktitle: Top 10 in PivotTable anzeigen oder filtern
description: Erfahren Sie, wie Sie in Aspose.Cells for JavaScript via C++ nur die Elemente mit dem höchsten oder niedrigsten Rang eines PivotTable-Felds anzeigen. Dieser Artikel behandelt die AutoShow-Eigenschaften von Excel 97-2003 (isAutoShow und verwandte Eigenschaften), das Zurücklesen der Optionen sowie den Top-10-Filter von Excel 2007-365 über filterTop10.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, PivotTable, Top 10, automatische Anzeige, isAutoShow, isAscendShow, autoShowCount, autoShowField, filterTop10, PivotFilterType, PivotField, JavaScript
type: docs
weight: 20
url: /de/javascript-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Eine PivotTable, die jedes Element eines Zeilenfelds auflistet, kann schwer lesbar sein, wenn das Feld Dutzende Elemente enthält. Ein Top-10-Bericht behält nur die Elemente mit dem höchsten oder niedrigsten Rang bei. Genau das benötigen Ranking-Berichte, etwa „die 5 umsatzstärksten Produkte“ oder „die 3 Regionen mit den niedrigsten Verkaufszahlen“. Aspose.Cells unterstützt zwei Mechanismen dafür, die den beiden Generationen von Microsoft Excel entsprechen.
- **Excel 97-2003 AutoShow** — die vier `PivotField`-Eigenschaften `isAutoShow`, `isAscendShow`, `autoShowCount` und `autoShowField`. Dies ist die klassische Einstellung „Obere/untere N Elemente anzeigen“, die direkt am PivotTable-Feld gespeichert wird. Sie funktioniert in sämtlichen alten und neuen Excel-Versionen, da sie Teil des ursprünglichen PivotTable-Formats ist.
- **Excel 2007-365 Top-10-Filter** — die Methode `PivotField.filterTop10()`. Dies ist der moderne Top-10-Wertfilter, der im Feldmenü unter „Wertfilter“ zu finden ist. Er wird als `PivotFilter`-Objekt gespeichert, das dem Feld zugeordnet ist, und unterstützt eine Rangfolge nach Elementanzahl oder Prozentwert.

## **Top 10 in Excel 97-2003 anzeigen (AutoShow)**
Das klassische AutoShow wird mit vier Eigenschaftszuweisungen am `PivotField` konfiguriert:
- `isAutoShow` — aktiviert oder deaktiviert die AutoShow-Einstellung am Feld.
- `isAscendShow` — `false` behält die höchstplatzierten Elemente bei („Oben“), `true` behält die niedrigstplatzierten Elemente bei („Unten“).
- `autoShowCount` — Anzahl der beizubehaltenden Elemente, beispielsweise 10 für einen klassischen Top-10-Bericht.
- `autoShowField` — nullbasierter Index des **Datenfelds**, dessen Werte zur Bestimmung der Rangfolge der Elemente herangezogen werden. Übergeben Sie `-1`, um die Elemente nach dem Feld selbst zu ordnen.
Die Rangfolge kann auf einem Wertfeld oder auf dem Feld selbst basieren. Im Folgenden werden zwei natürliche Varianten gezeigt.

### **Nach einem Wertfeld ordnen**
Ordnen Sie die Elemente des Zeilenfelds anhand eines gewöhnlichen Wertfelds wie „Summe von Sales“. Das folgende Beispiel erstellt eine PivotTable mit einem Zeilenfeld (`Sport`) und einem Datenfeld (`Sales`) und zeigt anschließend die 2 Sportarten mit dem höchsten Umsatz. `rankBy` ist 0, da „Summe von Sales“ das Datenfeld mit dem Index 0 ist.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            for (const sport of sports) {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            }
            const pivotTable = worksheet.pivotTables.add("=A1:C16", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // Die 2 höchsten Elemente nach "Sum of Sales" anzeigen (Index des Datenfelds 0)
            sportField.isAutoShow = true;
            sportField.isAscendShow = false;
            sportField.autoShowCount = 2;
            sportField.autoShowField = 0;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-by-value-field.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Nach dem Feld selbst ordnen**
Ein Feld kann ebenfalls nach seinen eigenen Werten geordnet werden – übergeben Sie dazu `-1` an `autoShowField`. Für diese Variante ist kein zusätzliches Datenfeld erforderlich; das Feld muss lediglich im Zeilen- oder Spaltenbereich liegen. Das folgende Beispiel zeigt die 3 Sportarten mit dem niedrigsten Rang in der Sortierung nach dem Feld selbst. Beim Speichern dieser Einstellung wird das Attribut `rankBy` aus dem XML der PivotTable weggelassen, da -1 der Standardwert des Formats ist. `autoShowField` liest -1 zurück.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            for (const sport of sports) {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            }
            const pivotTable = worksheet.pivotTables.add("=A1:C16", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // Die unteren 3 Elemente anzeigen, die nach dem Feld selbst sortiert sind (rankBy = -1)
            sportField.isAutoShow = true;
            sportField.isAscendShow = true;
            sportField.autoShowCount = 3;
            sportField.autoShowField = -1;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-by-field-itself.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Aktuelle AutoShow-Optionen auslesen**
Die `PivotField`-Eigenschaften `isAutoShow`, `isAscendShow`, `autoShowCount` und `autoShowField` geben die aktuell am Feld gespeicherten AutoShow-Optionen wieder. Verwenden Sie sie, um zu prüfen, wie die Elemente in einer vorhandenen Arbeitsmappe oder einer soeben konfigurierten PivotTable dargestellt werden – auch bei Arbeitsmappen, die aus einer Datei geladen wurden.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const pivotTable = worksheet.pivotTables.get(0);
                const sportField = pivotTable.rowFields.get(0);
                const autoShowEnabled = sportField.isAutoShow;
                const direction = sportField.isAscendShow ? "Bottom" : "Top";
                const itemCount = sportField.autoShowCount;
                const rankingDataFieldIndex = sportField.autoShowField;
                result.innerHTML =
                    '<p>AutoShow enabled: ' + autoShowEnabled + '</p>' +
                    '<p>Direction: ' + direction + '</p>' +
                    '<p>Item count: ' + itemCount + '</p>' +
                    '<p>Ranking data field index: ' + rankingDataFieldIndex + '</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

Die vier Eigenschaften bilden die klassischen AutoShow-Attributen ab, die in das XML der PivotTable geschrieben werden (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`). Die zurückgelesenen Werte entsprechen daher den Werten, die jede Excel-Version berücksichtigt.

## **Hinweis**

{{% alert color="primary" %}}
- Nachdem Sie eine beliebige AutoShow-Eigenschaft geändert haben, rufen Sie `pivotTable.calculateData()` erneut auf – die Einstellungen wirken sich erst bei der nächsten Neuberechnung auf das dargestellte Layout aus.
- Die AutoShow-Einstellungen funktionieren mit Zeilen- und Spaltenfeldern. Ein Feld, das sich ausschließlich im Seitenbereich (Filterbereich) befindet, kann auf diese Weise nicht in eine Rangfolge gebracht werden, da seine Elemente nicht im PivotTable-Körper dargestellt werden.
{{% /alert %}}

## **Excel 2007-365: Top-10-Filter (filterTop10)**
Bei modernen Excel-Versionen ist Top 10 im Feldmenü unter „Wertfilter“ > „Top 10...“ als Wertfilter verfügbar. Aspose.Cells bildet dies mit der Methode `PivotField.filterTop10(number valueFieldIndex, PivotFilterType type, boolean isTop, number itemCount)` ab, die den erstellten `PivotFilter` zurückgibt:
- `valueFieldIndex` — nullbasierter Index des Datenfelds, dessen aggregierte Werte zur Bestimmung der Rangfolge der Elemente herangezogen werden.
- `type` — bestimmt, was `itemCount` bedeutet. `PivotFilterType.Count` behält eine feste Anzahl von Elementen bei (Option „Elemente“ im Dialog). `PivotFilterType.Percent` behält einen bestimmten Anteil der Elemente bei; `itemCount` gibt diesen Anteil in Prozent an – 30 behält somit die oberen 30 Prozent. `PivotFilterType.Sum` ordnet nach der kumulierten Wertabdeckung.
- `isTop` — `true` für „Oben“, `false` für „Unten“.
- `itemCount` — der Wert N in „Top N“; die Einheit hängt von `type` ab.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            sports.forEach(sport => {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Die AutoShow-Eigenschaften und `filterTop10` sind zwei getrennte Mechanismen. AutoShow schreibt das klassische Attribut `autoShow` in das PivotTable-Feld und wird von allen Excel-Versionen ab Excel 97 berücksichtigt. `filterTop10` schreibt einen modernen `PivotFilter`-Eintrag, für den Excel 2007 oder höher erforderlich ist. Wird eine Arbeitsmappe in einer älteren Excel-Version geöffnet, zeigt eine PivotTable mit dem modernen Filter alle Elemente an. Für Dokumente, die mit Legacy-Tools verarbeitet und erneut gespeichert werden müssen, sind die AutoShow-Eigenschaften vorzuziehen; für moderne Arbeitsmappen ist `filterTop10` vorzuziehen, da es sich mit den anderen Wertfiltern kombinieren lässt.
{{% /alert %}}

## **Verwandte Artikel**
- [PivotTable-Felder in der PivotTable gruppieren](/cells/de/javascript-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}