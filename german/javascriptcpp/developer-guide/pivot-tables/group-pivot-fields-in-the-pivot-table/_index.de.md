---
title: Pivot‑Felder in der Pivot‑Tabelle gruppieren
linktitle: Pivot‑Felder in der Pivot‑Tabelle gruppieren
description: Erfahren Sie, wie Sie Zeilen‑ und Spalten‑Pivot‑Felder in einer Pivot‑Tabelle in Datumsperioden wie Monate und Quartale sowie numerische Bereiche mithilfe von PivotField.group und PivotFieldGroupOptions in Aspose.Cells for JavaScript via C++ gruppieren.
keywords: Aspose.Cells, Pivot‑Tabelle, Pivot‑Feld gruppieren, PivotField.group, PivotFieldGroupOptions, Datengruppierung, Zahlengruppierung, Monate, Quartale, numerischer Bereich, JavaScript via C++
type: docs
weight: 80
url: /de/javascript-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
- Das Gruppieren von Pivot‑Feldern ist nützlich, wenn ein Zeilen‑ oder Spalten‑Pivot‑Feld einer Pivot‑Tabelle viele unterschiedliche Elemente enthält, z. B. ein Datumsfeld mit Hunderten von Daten oder ein numerisches Feld mit vielen verstreuten Werten. Durch das Gruppieren werden diese Elemente in sinnvolle Abschnitte zusammengefasst: Daten in Monate, Quartale und Jahre sowie Zahlen in Bereiche wie 0‑1, 2‑3, 4‑5. Dadurch wird eine große Pivot‑Tabelle kompakt und leichter zu analysieren. Aspose.Cells stellt diese Möglichkeit über die Methode `PivotField.group()` (automatisches Gruppieren nach Datentyp) und `PivotField.group(PivotFieldGroupOptions)` (benutzerdefinierte Gruppierungsoptionen) bereit.
- Die Datengruppierung fasst einzelne Daten zu größeren Zeiträumen zusammen, z. B. Tage, Monate, Quartale und Jahre, und erstellt eine Zeithierarchie (z. B. Jahre, Quartale, Monate). Trends über die Zeit werden sofort sichtbar, und jede Periodenebene wird zu einem eigenen Pivot‑Feld im Zeilen‑ oder Spaltenbereich der Pivot‑Tabelle.
- Das Gruppieren ist nur für Felder möglich, die im Zeilen‑ oder Spaltenbereich einer Pivot‑Tabelle platziert sind. Ein Daten‑ (Wert‑)Feld kann nicht direkt gruppiert werden. Um ein solches Feld zu gruppieren, muss es zuerst in den Zeilen‑ oder Spaltenbereich der Pivot‑Tabelle verschoben werden.

## **Pivot‑Felder automatisch gruppieren**
Die parameterlose Überladung `PivotField.group()` prüft den Datentyp des Feldes und gruppiert es automatisch. Ein Feld, das nur Datumswerte (und leere Zellen) enthält, wird nach Monaten gruppiert. Ein Feld, das nur Zahlen (und leere Zellen) enthält, wird mithilfe eines automatischen Intervalls in numerische Bereiche gruppiert.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group Pivot Fields Automatically</title>
    </head>
    <body>
        <h1>Auto-Group a Pivot Field</h1>
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
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the second worksheet and its pivot table
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // Group the first row field automatically by its data type
                pt.rowFields.get(0).group();
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputAutoGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

## **Pivot‑Felder mit benutzerdefinierten Optionen gruppieren**
Die Klasse `PivotFieldGroupOptions` bietet benutzerdefinierte Gruppierungskonfigurationen. Für Datumsfelder setzen Sie `startDate`, `endDate` und `groupTypes`. Für numerische Felder setzen Sie `startNumber`, `endNumber` und `interval`. Die Eigenschaft `newPivotField` bestimmt, ob die Gruppierung neue Pivot‑Felder neben dem Original erstellt (siehe den Hinweis‑Abschnitt am Ende dieses Artikels).

### **Ein Datumsfeld nach Monaten und Quartalen gruppieren**
Das folgende Beispiel gruppiert das Datumszeilenfeld der Beispiel‑Pivot‑Tabelle nach Monaten und Quartalen zwischen einem Start‑ und Enddatum. Der Code lädt die [Beispiel‑Excel‑Datei](sampleGroupPivotFieldsInPivotTable.xlsx), führt die Gruppierung durch, berechnet die Pivot‑Tabellendaten und speichert das gruppierte Ergebnis. Der Screenshot zeigt den Effekt: Das Datumszeilenfeld ist nun nach Quartalen und Monaten gruppiert.  
Beachten Sie, dass die Reihenfolge der Werte in `options.groupTypes` ignoriert wird. Unabhängig davon, in welcher Reihenfolge die Gruppierungstypen angegeben sind, werden die gruppierten Felder immer vom größten Zeitraum zum kleinsten angezeigt: Jahre, Quartale, Monate, Tage, Stunden, Minuten, Sekunden. In diesem Beispiel werden die Monate vor den Quartalen in `options.groupTypes` aufgelistet, dennoch werden die Quartale als äußere Ebene und die Monate als innere Ebene dargestellt.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group a Date Field by Months and Quarters</title>
    </head>
    <body>
        <h1>Group a Date Pivot Field</h1>
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
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // Group the date row field by months and quarters between the given dates
                const options = new AsposeCells.PivotFieldGroupOptions();
                options.startDate = new Date(2008, 1, 1);
                options.endDate = new Date(2008, 9, 5);
                options.groupTypes = [AsposeCells.PivotGroupByType.Months, AsposeCells.PivotGroupByType.Quarters];
                pt.rowFields.get(0).group(options);
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputGroupPivotFieldsInPivotTable.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

![Pivot‑Tabelle, gruppiert nach Monaten und Quartalen](group-pivot-fields-in-the-pivot-table_1.png)

### **Ein numerisches Feld in Bereiche gruppieren**
`FieldTwo` der Beispiel‑Pivot‑Tabelle ist zunächst ein Daten‑ (Wert‑)Feld. Da nur Zeilen‑ oder Spalten‑Felder gruppiert werden können, ruft der Code zuerst `PivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` auf, um `FieldTwo` in den Zeilenbereich zu verschieben, aktualisiert die Pivot‑Tabelle und gruppiert das numerische Feld anschließend in die Bereiche 0‑1, 2‑3 und 4‑5 mithilfe von `startNumber = 0`, `endNumber = 5` und `interval = 2`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group a Numeric Field into Ranges</title>
    </head>
    <body>
        <h1>Group a Numeric Pivot Field</h1>
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
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // FieldTwo is a data field: move it to the row area first,
                // because only row/column fields can be grouped
                pt.addFieldToArea(AsposeCells.PivotFieldType.Row, "FieldTwo");
                pt.calculateData();
                // Group the numeric field into the ranges 0-1, 2-3, 4-5
                const options = new AsposeCells.PivotFieldGroupOptions();
                options.startNumber = 0;
                options.endNumber = 5;
                options.interval = 2;
                pt.rowFields.get(1).group(options);
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputNumberGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

## **Hinweis**

{{% alert color="primary" %}}
- Die Überladungen der Methode `PivotField.groupBy()` sind veraltet und aus der API entfernt. `PivotField.group()` und `PivotField.group(PivotFieldGroupOptions)` ersetzen sie.
- In Microsoft Excel ersetzt das Gruppieren eines numerischen Feldes das ursprüngliche Pivot‑Feld durch die gruppierten Bereiche, während das Gruppieren eines Datumsfeldes NEUE Pivot‑Felder (je ein Feld pro Gruppierungsebene, z. B. Quartale und Monate) neben dem Originalfeld erzeugt. Seit Aspose.Cells 26.10 verhalten sich die Methoden `PivotField.group()` analog zu Excel. Die Eigenschaft `PivotFieldGroupOptions.newPivotField` dient der Kompatibilität mit älteren Versionen: Sie ist standardmäßig für numerische Gruppierung auf **false** und für Datum‑Zeit‑Gruppierung auf **true** gesetzt; setzen Sie sie auf **false**, wenn die Datum‑Gruppierung das ursprüngliche Pivot‑Feld ersetzen soll, anstatt neue Pivot‑Felder zu erzeugen.
- Die Eigenschaft `PivotFieldGroupOptions.interval` wirkt nur bei numerischer Gruppierung und bei der Datumsgruppierung nach Tagen (z. B. Gruppierung von Daten in 7‑Tage‑Perioden); sie wird ignoriert, wenn Daten nach Monaten, Quartalen oder Jahren gruppiert werden.
{{% /alert %}}

## **Verwandte Artikel**
- [Zeilen‑ und Spalten‑Felder in Pivot‑Tabelle hinzufügen](/cells/de/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [Pivot‑Tabellen nach Beschriftung oder Wert filtern](/cells/de/javascript-cpp/filter-by-label-or-value-of-pivot-table/)
- [Seitenfeld in Pivot‑Tabelle hinzufügen](/cells/de/javascript-cpp/add-page-field-in-pivot-table/)
- [Stil auf Pivot‑Tabelle anwenden](/cells/de/javascript-cpp/apply-style-to-pivot-table/)
- [Pivot‑Tabelle aktualisieren](/cells/de/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}