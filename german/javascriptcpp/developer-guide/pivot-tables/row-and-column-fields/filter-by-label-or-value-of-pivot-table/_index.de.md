---
title: PivotTables nach Bezeichnung oder Wert filtern
linktitle: PivotTables nach Bezeichnung oder Wert filtern
description: Aspose.Cells for JavaScript via C++ unterstützt umfassende Filterfunktionen für PivotTables. Dieser Artikel erläutert, wie PivotTable-Daten mithilfe von Bezeichnungsfiltern, Datumsfiltern, Wertfiltern, Top-10-Filtern sowie durch Aus- oder Einblenden von Pivot-Elementen gefiltert werden.
keywords: Aspose.Cells, Bibliothek für JavaScript via C++, Tabellenkalkulation, PivotTable, Filter, Bezeichnungsfilter, Wertfilter, Datumsfilter, Top-10-Filter, Pivot-Element, Pivot-Element ausblenden
type: docs
weight: 10
url: /de/javascript-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells bietet fünf praktische Strategien zum Filtern der in einer PivotTable angezeigten Daten. Sie können Bezeichnungsfilter auf textbasierte Zeilen- oder Spaltenfelder anwenden, Datumsfilter verwenden, wenn das Feld ausschließlich Zellen mit Datum und Uhrzeit oder leere Zellen enthält, Wertfilter auf aggregierte Zahlen anwenden, Top-10-Filter verwenden, um nach einem Wertfeld zu rangieren, oder einzelne Pivot-Elemente mithilfe der Eigenschaft `isHidden` manuell aus- und einblenden. Jede Strategie wird über dedizierte APIs in den Klassen `PivotField` und `PivotItem` bereitgestellt.
{{% /alert %}}

## **Einführung**
PivotTables sind leistungsstarke Analysewerkzeuge, doch rohe Zusammenfassungen enthalten oft wesentlich mehr Informationen, als Sie präsentieren möchten. Das Filtern ist der primäre Mechanismus, um eine PivotTable auf die für einen bestimmten Bericht relevanten Zeilen, Spalten oder Werte einzugrenzen. Aspose.Cells for JavaScript via C++ spiegelt die in Microsoft Excel verfügbaren Filterfunktionen wider und stellt sie programmgesteuert bereit, sodass die Berichtserstellung vollständig automatisiert werden kann.
In diesem Artikel werden die folgenden Filterstrategien behandelt:
1. **Bezeichnungsfilter** – filtert die Elemente eines Zeilen- oder Spaltenfelds anhand ihrer Textbezeichnungen.
2. **Datumsfilter** – filtert Zeilen- oder Spaltenfelder, die ausschließlich Datums- und Uhrzeitwerte oder leere Werte enthalten.
3. **Wertfilter** – filtert Elemente anhand der aggregierten Werte eines Datenfelds.
4. **Top-10-Filter** – zeigt nur die obersten oder untersten N Elemente an, die anhand eines Wertfelds rangiert sind.
5. **Pivot-Elemente aus-/einblenden** – steuert die Sichtbarkeit jedes einzelnen Elements in einem Feld manuell.
Jeder Ansatz verwendet eine andere Methode der Klasse `PivotField` oder eine Eigenschaft der Klasse `PivotItem`. Nach dem Anwenden eines Filters müssen Sie `pivotCache.refresh()` auf der PivotTable aufrufen, damit die zwischengespeicherten Daten und berechneten Werte den neuen Filterzustand wiedergeben.

## **Bezeichnungsfilter**
Mit einem Bezeichnungsfilter können Sie die Elemente eines Zeilen- oder Spaltenfelds filtern, indem ihre Textbeschriftungen mit einem Muster verglichen werden. Dies ist nützlich, wenn Sie nur Produkte anzeigen möchten, deren Namen mit einem bestimmten Buchstaben beginnen, ein bestimmtes Wort enthalten oder ein anderes auf der Beschriftung basierendes Kriterium erfüllen.
Aspose.Cells stellt die Bezeichnungsfilterung über die Methode `pivotField.filterByLabel(PivotFilterType filterType, string label1, string label2)` bereit. Das Argument `filterType` legt den Vergleichsmodus fest (`CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` und so weiter). Die Argumente `label1` und `label2` liefern den Vergleichstext – übergeben Sie für `label2` den Wert `""`, wenn nur ein einzelner Vergleichswert benötigt wird (z. B. für „Beginnt mit“ oder „Enthält“).
Das folgende Beispiel lädt eine Arbeitsmappe mit einer vorhandenen PivotTable, wendet einen Bezeichnungsfilter an, sodass nur Elemente sichtbar bleiben, deren Beschriftungen mit einem angegebenen Präfix beginnen, aktualisiert die PivotTable und speichert das Ergebnis.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat } = AsposeCells;
            const fileInput = document.getElementById("fileInput");
            const runExampleButton = document.getElementById("runExample");
            const downloadLink = document.getElementById("downloadLink");
            const result = document.getElementById("result");
            AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            runExampleButton.addEventListener("click", async () => {
                try {
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select a workbook containing a pivot table.</p>';
                        return;
                    }
                    // Load the existing workbook containing a pivot table
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // Access the worksheet by index (first worksheet)
                    const worksheet = workbook.worksheets.get(0);
                    // Access the pivot table by index
                    const pivotTable = worksheet.pivotTables.get(0);
                    // Retrieve the first row PivotField
                    const rowField = pivotTable.rowFields.get(0);
                    // Apply the label filter — show only row items whose labels begin with the supplied prefix
                    rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, "B", "");
                    // Refresh and recalculate the pivot table data so the filter takes effect
                    pivotTable.pivotCache.refresh();
                    // Save the workbook back to disk
                    const outputData = workbook.save(SaveFormat.Xlsx);
                    const blob = new Blob([outputData], {
                        type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    });
                    downloadLink.href = URL.createObjectURL(blob);
                    downloadLink.download = "sample.xlsx";
                    downloadLink.style.display = "block";
                    result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
                } catch (error) {
                    console.error(error);
                    result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + "</p>";
                }
            });
        </script>
    </body>
</html>
```

## **Datumsfilter**
Datumsfilter ermöglichen es Ihnen, eine PivotTable anhand datumsbasierter Kriterien wie dem heutigen Tag, der letzten Woche, diesem Monat, dem nächsten Quartal oder einem bestimmten Datumsbereich einzugrenzen. Es handelt sich um spezielle Filter, die ausschließlich auf Felder angewendet werden können, die Datums- und Uhrzeitinformationen speichern.

{{% alert color="primary" %}}
Der Datumsfilter funktioniert nur, wenn der Zeilen- oder Spaltenbereich ausschließlich Zellen mit Datum und Uhrzeit oder leere Zellen enthält. Wenn das zugrunde liegende Feld andere Datentypen wie Zahlen oder Text enthält, liefert der Datumsfilter nicht das erwartete Ergebnis. Stellen Sie sicher, dass das Feld als Datum formatiert und alle Werte entweder gültige `DateTime`-Instanzen oder leere Zellen sind, bevor Sie diesen Filter anwenden.
Aspose.Cells stellt die Datumsfilterung über die Methode `pivotField.filterByDate(PivotFilterType, DateTime[] values)` bereit. Die Enumeration `PivotFilterType` enthält spezialisierte Datumswerte wie `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` und `Between`. Je nach ausgewähltem Filtertyp übergeben Sie einen oder zwei `DateTime`-Werte (bei `Between` das Start- und Enddatum).
Das folgende Beispiel lädt eine Arbeitsmappe mit einer PivotTable, deren Zeilenbereich ein Datumsfeld enthält, wendet einen Datumsfilter an, der die sichtbaren Elemente auf einen bestimmten Datumsbereich beschränkt, aktualisiert die PivotTable und speichert die Arbeitsmappe.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            try {
                const file = fileInput.files[0];
                if (!file) {
                    throw new Error("Source workbook not found.");
                }
                // Load the existing workbook that contains the pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the worksheet that holds the pivot table (by index)
                const worksheet = workbook.worksheets.get(0);
                // Access the pivot table by index
                const pivotTable = worksheet.pivotTables.get(0);
                // Retrieve the date PivotField from the row area
                // (Date filter only works when the row/column area contains only date-time cells or blanks)
                const dateField = pivotTable.rowFields.get(0);
                // Define the date criterion for the Between filter
                const startDate = new Date(2020, 0, 1);
                const endDate = new Date(2020, 11, 31);
                // Apply the date filter on the pivot field
                dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
                // Refresh and recalculate the pivot table so the filter takes effect
                pivotTable.pivotCache.refresh();
                // Persist the workbook
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output_filtered.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
                console.error(error);
            }
        });
    </script>
</html>
```

## **Wertfilter**
Wertfilter arbeiten mit den aggregierten Werten, die eine PivotTable in ihrem Datenbereich berechnet. Statt Textbeschriftungen abzugleichen, vergleichen sie numerische Summen mit einem Schwellenwert. Typische Anwendungsfälle umfassen die Anzeige ausschließlich von Produkten, deren Gesamtumsatz einen Zielbetrag übersteigt, oder von Regionen, deren Transaktionsanzahl innerhalb eines Bereichs liegt.
Aspose.Cells stellt die Wertfilterung über die Methode `pivotField.filterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)` bereit. Der Parameter `valueFieldIndex` gibt an, welches Datenfeld ausgewertet werden soll (verwenden Sie `pivotTable.getDataFields().indexOf(dataField)` oder durchlaufen Sie die Auflistung, um die Position zu ermitteln). Der Parameter `filterType` kann Werte wie `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` und `ValueLessThanOrEqual` annehmen. Die beiden `double`-Argumente liefern den bzw. die Schwellenwerte.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer PivotTable, wendet einen Wertfilter an, der nur Elemente beibehält, deren aggregierter Umsatz einen numerischen Schwellenwert überschreitet, aktualisiert die PivotTable und speichert die Arbeitsmappe.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            const downloadLink = document.getElementById('downloadLink');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select a workbook file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const pivotTable = worksheet.pivotTables.get(0);
                const rowField = pivotTable.rowFields.get(0);
                const dataField = pivotTable.dataFields.get(0);
                // Find the data field index manually since PivotFieldCollection doesn't have IndexOf
                let dataFieldIndex = -1;
                for (let i = 0; i < pivotTable.dataFields.count; i++) {
                    if (pivotTable.dataFields.get(i) === dataField) {
                        dataFieldIndex = i;
                        break;
                    }
                }
                if (dataFieldIndex >= 0) {
                    rowField.filterByValue(
                        dataFieldIndex,
                        AsposeCells.PivotFilterType.ValueGreaterThan,
                        5000,
                        Number.MAX_VALUE
                    );
                }
                pivotTable.pivotCache.refresh();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

## **Top-10-Filter**
Der Top-10-Filter ist eine spezialisierte Form des Wertfilters, die auf Grundlage eines ausgewählten Wertfelds nur die N höchsten oder niedrigsten Elemente beibehält. Er wird häufig für Berichte zur Rangfolge wie „die 10 umsatzstärksten Produkte“ oder „die 5 Regionen mit der niedrigsten Verkaufsanzahl“ verwendet.

{{% alert color="primary" %}}
Der Top-10-Filter ist nur wirksam, wenn die PivotTable im Datenbereich ein oder mehrere Wertfelder enthält. Ohne mindestens ein Wertfeld gibt es keine aggregierte Kenngröße, anhand derer die Elemente rangiert werden können, und der Filter kann nicht angewendet werden.
Aspose.Cells stellt die Top-10-Filterung über die Methode `pivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)` bereit. Der Parameter `valueFieldIndex` ist der Index des Datenfelds, dessen aggregierte Werte für die Rangfolge der Elemente verwendet werden. `filterType` legt die Einheit fest, in der `itemCount` angegeben ist (`Count` behält eine feste Anzahl von Elementen bei, `Percent` behält einen Prozentsatz der Elemente bei, sodass `itemCount` selbst der Prozentsatz ist). `isTop` gibt an, ob die obersten Elemente (`true`) oder die untersten Elemente (`false`) beibehalten werden sollen, und `itemCount` legt fest, wie viele Elemente oder welcher Prozentsatz beibehalten wird.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer PivotTable, die ein Wertfeld enthält, wendet einen Top-10-Filter an, der nur die 10 höchsten Elemente nach der Summe des Umsatzes beibehält, aktualisiert die PivotTable und speichert die Arbeitsmappe.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            try {
                const file = fileInput.files[0];
                if (!file) {
                    result.textContent = "Please select an input workbook.";
                    return;
                }
                // Load the existing workbook that contains the pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the worksheet that holds the pivot table (index 0)
                const worksheet = workbook.worksheets.get(0);
                // Access the pivot table by index
                const pivotTable = worksheet.pivotTables.get(0);
                // Confirm there is at least one value PivotField in the data area
                if (pivotTable.dataFields.count === 0) {
                    throw new Error("Pivot table has no value (data) PivotField.");
                }
                const valueField = pivotTable.dataFields.get(0);
                // Retrieve the target row PivotField (the field we want to apply Top 10 on)
                const rowField = pivotTable.rowFields.get(0);
                // The first (and only) data field is at index 0; Top 10 ranks by it.
                const valueFieldIndex = 0;
                // Apply the Top 10 filter on the row field:
                //   - valueFieldIndex = 0 — the data field used to rank items
                //   - filterType  = PivotFilterType.Count (keep a fixed number of items;
                //     PivotFilterType.Percent would interpret 10 as "top 10 percent")
                //   - isTop       = true (top N; false would mean bottom N)
                //   - itemCount   = 10
                rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
                // Refresh the pivot table data and recalculate it so the filter takes effect
                pivotTable.pivotCache.refresh();
                // Save the workbook
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.textContent = `Error: ${error.message || error}`;
            }
        });
    </script>
</html>
```

## **Filtern durch Aus- oder Einblenden von Pivot-Elementen**
Zusätzlich zu den strukturierten Filter-APIs ermöglicht Aspose.Cells die direkte Steuerung der Sichtbarkeit jedes einzelnen Pivot-Elements. Indem Sie die Auflistung `pivotField.getPivotItems()` eines `PivotField` durchlaufen und die Eigenschaft `isHidden` umschalten, können Sie bestimmte Elemente gezielt ausblenden, ohne einen formelbasierten Filter anzuwenden. Das Festlegen von `pivotItem.isHidden = true` blendet das Element aus der PivotTable aus; das Festlegen von `pivotItem.isHidden = false` blendet es ein und macht es wieder sichtbar.
Dieser Ansatz ist nützlich, wenn die Filterregel unregelmäßig oder elementspezifisch ist, etwa wenn eine kleine Anzahl namentlich angegebener Kategorien ausgeblendet werden soll, die in einem bestimmten Bericht nicht erscheinen dürfen. Das folgende Beispiel lädt eine PivotTable, blendet ein bestimmtes Element nach Namen aus, zeigt, wie es wieder eingeblendet wird, aktualisiert die PivotTable und speichert die Arbeitsmappe.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            const file = document.getElementById('fileInput').files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select a workbook containing a pivot table.</p>';
                return;
            }
            try {
                // Load an existing workbook containing a pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the first worksheet which contains the pivot table
                const sheet = workbook.worksheets.get(0);
                // Access the pivot table by index (the first pivot table on the sheet)
                const pivotTable = sheet.pivotTables.get(0);
                // Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
                const pivotField = pivotTable.rowFields.get(0);
                // Iterate through the PivotItems collection of the selected PivotField
                const itemCount = pivotField.pivotItems.count;
                for (let i = 0; i < itemCount; i++) {
                    const item = pivotField.pivotItems.get(i);
                    // Hide pivot items that match a specific name/criterion
                    if (item.name === "Item1" || item.name === "Item2") {
                        item.isHidden = true;
                    }
                    // Demonstrate unhiding: re-show a previously hidden pivot item
                    if (item.name === "Item3") {
                        item.isHidden = false;
                    }
                }
                // Refresh and recalculate the pivot table so changes take effect
                pivotTable.pivotCache.refresh();
                // Save the workbook — hidden items stay in the underlying data
                // but are excluded from the displayed pivot table output
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output_pivot_filtered.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

## **Zusammenfassung**
Aspose.Cells for JavaScript via C++ bietet einen vollständigen Satz an Filterfunktionen für PivotTables, die den in Microsoft Excel verfügbaren Funktionen entsprechen. Bezeichnungs-, Datums- und Wertfilter decken die häufigsten Analyseszenarien ab, während der Top-10-Filter Berichte zur Rangfolge ermöglicht. Wenn die Filterregel unregelmäßig ist, bietet die Eigenschaft `pivotItem.isHidden` eine flexible Alternative auf Elementebene. Durch die Kombination dieser Strategien – beispielsweise indem Sie einen Bezeichnungsfilter anwenden und anschließend bestimmte Elemente ausblenden – können Sie vollständig im Code präzise zugeschnittene PivotTable-Berichte erstellen.

{{< app/cells/assistant language="javascript-cpp" >}}