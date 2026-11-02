---
title: PivotTables nach Beschriftung oder Wert filtern
linktitle: PivotTables nach Beschriftung oder Wert filtern
description: Aspose.Cells for JavaScript via C++ bietet umfassende Filterfunktionen für PivotTables. Dieser Artikel erläutert, wie PivotTable-Daten mithilfe von Beschriftungsfiltern, Datumsfiltern, Wertfiltern, Top-10-Filtern sowie durch das Aus- oder Einblenden von Pivot-Elementen gefiltert werden können.
keywords: Aspose.Cells, Bibliothek für JavaScript via C++, Tabellenkalkulation, PivotTable, Filter, Beschriftungsfilter, Wertfilter, Datumsfilter, Top-10-Filter, Pivot-Element, Pivot-Element ausblenden
type: docs
weight: 10
url: /de/javascript-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells bietet fünf praktische Strategien zum Filtern der in einer PivotTable angezeigten Daten. Sie können Beschriftungsfilter auf textbasierte Zeilen- oder Spaltenfelder anwenden, Datumsfilter verwenden, wenn das Feld ausschließlich Zellen mit Datum-Uhrzeit-Werten oder Leerzellen enthält, Wertfilter auf aggregierte Zahlen anwenden, Top-10-Filter zur Rangfolge nach einem Wertfeld verwenden oder einzelne Pivot-Elemente mithilfe der Eigenschaft `isHidden` manuell aus- und einblenden. Jede Strategie wird über dedizierte APIs in den Klassen `PivotField` und `PivotItem` bereitgestellt.
{{% /alert %}}

## **Einführung**
PivotTables sind leistungsstarke Analysewerkzeuge, die rohe Zusammenfassungen jedoch häufig weit mehr Informationen enthalten, als Sie für einen Bericht darstellen müssen. Die Filterung ist der primäre Mechanismus, mit dem sich eine PivotTable auf die für einen bestimmten Bericht relevanten Zeilen, Spalten oder Werte eingrenzen lässt. Aspose.Cells for JavaScript via C++ bietet dieselben Filterfunktionen wie Microsoft Excel und stellt sie programmgesteuert bereit, sodass sich die Berichtserstellung vollständig automatisieren lässt.
Die folgenden Filterstrategien werden in diesem Artikel behandelt:
1. **Beschriftungsfilter** — filtert Elemente von Zeilen- oder Spaltenfeldern anhand ihrer Textbeschriftungen.
2. **Datumsfilter** — filtert Zeilen- oder Spaltenfelder, die ausschließlich Datum-Uhrzeit-Werte oder Leerzellen enthalten.
3. **Wertfilter** — filtert Elemente anhand der aggregierten Werte eines Datenfelds.
4. **Top-10-Filter** — zeigt nur die obersten oder untersten N Elemente an, die anhand eines Wertfelds rangiert werden.
5. **Pivot-Elemente aus-/einblenden** — steuert die Sichtbarkeit jedes einzelnen Elements in einem Feld manuell.
Jeder Ansatz verwendet eine andere Methode der Klasse `PivotField` oder eine Eigenschaft der Klasse `PivotItem`. Nach dem Anwenden eines Filters müssen Sie `pivotCache.refresh()` für die PivotTable aufrufen, damit die zwischengespeicherten Daten und berechneten Werte den neuen Filterstatus abbilden.

## **Beschriftungsfilter**
Mit einem Beschriftungsfilter können Sie die Elemente eines Zeilen- oder Spaltenfelds filtern, indem Sie deren Textbeschriftungen mit einem Muster vergleichen. Dies ist nützlich, wenn Sie nur Produkte anzeigen möchten, deren Namen mit einem bestimmten Buchstaben beginnen, ein bestimmtes Wort enthalten oder ein anderes auf den Beschriftungen basierendes Kriterium erfüllen.
Aspose.Cells stellt die Beschriftungsfilterung über die Methode `pivotField.filterByLabel(PivotFilterType filterType, string label1, string label2)` bereit. Das Argument `filterType` legt den Vergleichsmodus fest (`CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` usw.). Die Argumente `label1` und `label2` geben den Vergleichstext an. Übergeben Sie `""` für `label2`, wenn lediglich ein einzelner Wert verglichen werden soll, beispielsweise bei „Beginnt mit“ oder „Enthält“.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer vorhandenen PivotTable, wendet einen Beschriftungsfilter an, sodass nur Elemente sichtbar bleiben, deren Beschriftungen mit einem vorgegebenen Präfix beginnen, aktualisiert die PivotTable und speichert das Ergebnis.

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
                    // Die vorhandene Arbeitsmappe laden, die eine Pivot-Tabelle enthält
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // Auf das Arbeitsblatt über den Index zugreifen (erstes Arbeitsblatt)
                    const worksheet = workbook.worksheets.get(0);
                    // Auf die Pivot-Tabelle über den Index zugreifen
                    const pivotTable = worksheet.pivotTables.get(0);
                    // Das erste PivotField für Zeilen abrufen
                    const rowField = pivotTable.rowFields.get(0);
                    // Den Beschriftungsfilter anwenden – nur Zeilenelemente anzeigen, deren Beschriftungen mit dem angegebenen Präfix beginnen
                    rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, "B", "");
                    // Die Daten der Pivot-Tabelle aktualisieren und neu berechnen, damit der Filter wirksam wird
                    pivotTable.refreshData();
                    // Die Arbeitsmappe wieder auf der Festplatte speichern
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
Mit Datumsfiltern können Sie eine PivotTable anhand datumsbezogener Kriterien wie heute, letzte Woche, diesen Monat, das nächste Quartal oder einen bestimmten Datumsbereich eingrenzen. Es handelt sich um spezialisierte Filter, die ausschließlich mit Feldern funktionieren, in denen Datum-Uhrzeit-Informationen gespeichert sind.

{{% alert color="primary" %}}
Der Datumsfilter funktioniert nur, wenn der Zeilen- oder Spaltenbereich ausschließlich Zellen mit Datum-Uhrzeit-Werten oder Leerzellen enthält. Wenn das zugrunde liegende Feld andere Datentypen wie Zahlen oder Text enthält, liefert der Datumsfilter nicht das erwartete Ergebnis. Stellen Sie sicher, dass das Feld als Datum formatiert ist und alle Werte gültige `DateTime`-Instanzen oder leere Zellen sind, bevor Sie diesen Filter anwenden.
Aspose.Cells stellt die Datumsfilterung über die Methode `pivotField.filterByDate(PivotFilterType, DateTime[] values)` bereit. Die Aufzählung `PivotFilterType` enthält spezialisierte Datumswerte wie `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` und `Between`. Je nach ausgewähltem Filtertyp übergeben Sie einen oder zwei `DateTime`-Werte. Für `Between` übergeben Sie das Start- und Enddatum.
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
                // Laden Sie die vorhandene Arbeitsmappe, die die Pivot-Tabelle enthält
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Greifen Sie auf das Arbeitsblatt zu, das die Pivot-Tabelle enthält (nach Index)
                const worksheet = workbook.worksheets.get(0);
                // Greifen Sie auf die Pivot-Tabelle nach Index zu
                const pivotTable = worksheet.pivotTables.get(0);
                // Rufen Sie das Datums-PivotField aus dem Zeilenbereich ab
                // (Der Datumsfilter funktioniert nur, wenn der Zeilen-/Spaltenbereich ausschließlich Zellen mit Datum-Uhrzeit-Werten oder leere Zellen enthält)
                const dateField = pivotTable.rowFields.get(0);
                // Definieren Sie das Datumskriterium für den Between-Filter
                const startDate = new Date(2020, 0, 1);
                const endDate = new Date(2020, 11, 31);
                // Wenden Sie den Datumsfilter auf das Pivot-Feld an
                dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
                // Aktualisieren und berechnen Sie die Pivot-Tabelle neu, damit der Filter wirksam wird
                pivotTable.refreshData();
                // Speichern Sie die Arbeitsmappe
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
Wertfilter arbeiten mit den aggregierten Werten, die eine PivotTable in ihrem Datenbereich berechnet. Anstatt Textbeschriftungen abzugleichen, vergleichen sie numerische Summen mit einem Schwellenwert. Typische Anwendungsfälle sind die Anzeige nur von Produkten, deren Umsatzsumme einen Zielbetrag überschreitet, oder nur von Regionen, deren Transaktionsanzahl in einem bestimmten Bereich liegt.
Aspose.Cells stellt die Wertfilterung über die Methode `pivotField.filterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)` bereit. Der Parameter `valueFieldIndex` gibt an, welches Datenfeld ausgewertet werden soll. Verwenden Sie dazu `pivotTable.getDataFields().indexOf(dataField)` oder durchlaufen Sie die Auflistung, um die Position zu ermitteln. Der Parameter `filterType` kann unter anderem die Werte `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` und `ValueLessThanOrEqual` annehmen. Die beiden Argumente vom Typ `double` legen den Schwellenwert bzw. die Schwellenwerte fest.
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
                // Finde den Index des Datenfelds manuell, da PivotFieldCollection keine IndexOf-Methode hat
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
                pivotTable.refreshData();
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
Der Top-10-Filter ist eine spezialisierte Form des Wertfilters, die auf Grundlage eines ausgewählten Wertfelds nur die N Elemente mit den höchsten oder niedrigsten Werten beibehält. Er wird häufig für Ranking-Berichte wie „die zehn umsatzstärksten Produkte“ oder „die fünf Regionen mit der niedrigsten Verkaufsanzahl“ verwendet.

{{% alert color="primary" %}}
Der Top-10-Filter ist nur wirksam, wenn die PivotTable im Datenbereich ein oder mehrere Wertfelder enthält. Ohne mindestens ein Wertfeld gibt es keine aggregierte Kennzahl, nach der die Elemente rangiert werden können, und der Filter kann nicht angewendet werden.
Aspose.Cells stellt die Top-10-Filterung über die Methode `pivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)` bereit. Der Parameter `valueFieldIndex` ist der Index des Datenfelds, dessen aggregierte Werte die Elemente einordnen. `filterType` legt die Einheit von `itemCount` fest: `Count` behält eine feste Anzahl von Elementen bei, während `Percent` einen Prozentsatz der Elemente beibehält, sodass `itemCount` selbst den Prozentsatz darstellt. `isTop` gibt an, ob die obersten Elemente (`true`) oder die untersten Elemente (`false`) beibehalten werden sollen. `itemCount` legt fest, wie viele Elemente oder welcher Prozentsatz beibehalten wird.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer PivotTable, die ein Wertfeld enthält, wendet einen Top-10-Filter an, um nur die zehn Elemente mit der höchsten Umsatzsumme beizubehalten, aktualisiert die PivotTable und speichert die Arbeitsmappe.
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
                // Die vorhandene Arbeitsmappe laden, die die Pivot-Tabelle enthält
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Auf das Arbeitsblatt zugreifen, das die Pivot-Tabelle enthält (Index 0)
                const worksheet = workbook.worksheets.get(0);
                // Über den Index auf die Pivot-Tabelle zugreifen
                const pivotTable = worksheet.pivotTables.get(0);
                // Bestätigen, dass im Datenbereich mindestens ein Wert-PivotField vorhanden ist
                if (pivotTable.dataFields.count === 0) {
                    throw new Error("Pivot table has no value (data) PivotField.");
                }
                const valueField = pivotTable.dataFields.get(0);
                // Das Zielzeilen-PivotField abrufen (das Feld, auf das die Top-10-Funktion angewendet werden soll)
                const rowField = pivotTable.rowFields.get(0);
                // Das erste (und einzige) Datenfeld befindet sich bei Index 0; die Top-10-Funktion rankt danach.
                const valueFieldIndex = 0;
                // Den Top-10-Filter auf das Zeilenfeld anwenden:
                //   - valueFieldIndex = 0 — das Datenfeld, das zum Ranken der Elemente verwendet wird
                //   - filterType  = PivotFilterType.Count (eine feste Anzahl von Elementen beibehalten;
                //     PivotFilterType.Percent würde 10 als "Top 10 Prozent" interpretieren)
                //   - isTop       = true (Top N; false würde Bottom N bedeuten)
                //   - itemCount   = 10
                rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
                // Die Daten der Pivot-Tabelle aktualisieren und neu berechnen, damit der Filter wirksam wird
                pivotTable.refreshData();
                // Die Arbeitsmappe speichern
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

## **Pivot-Elemente durch Aus- oder Einblenden filtern**
Zusätzlich zu den strukturierten Filter-APIs ermöglicht Aspose.Cells die direkte Steuerung der Sichtbarkeit jedes einzelnen Pivot-Elements. Indem Sie die Auflistung `pivotField.getPivotItems()` eines `PivotField` durchlaufen und die Eigenschaft `isHidden` umschalten, können Sie bestimmte Elemente gezielt ausblenden, ohne einen formelbasierten Filter anzuwenden. Durch Festlegen von `pivotItem.isHidden = true` wird das Element in der PivotTable ausgeblendet. Durch Festlegen von `pivotItem.isHidden = false` wird es wieder eingeblendet und sichtbar gemacht.
Dieser Ansatz ist nützlich, wenn die Filterregel unregelmäßig oder elementspezifisch ist, beispielsweise wenn eine kleine Anzahl benannter Kategorien in einem bestimmten Bericht nicht angezeigt werden soll. Das folgende Beispiel lädt eine PivotTable, blendet ein bestimmtes Element anhand seines Namens aus, veranschaulicht das Einblenden, aktualisiert die PivotTable und speichert die Arbeitsmappe.

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
                // Eine vorhandene Arbeitsmappe laden, die eine Pivot-Tabelle enthält
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Auf das erste Arbeitsblatt zugreifen, das die Pivot-Tabelle enthält
                const sheet = workbook.worksheets.get(0);
                // Auf die Pivot-Tabelle nach Index zugreifen (die erste Pivot-Tabelle im Arbeitsblatt)
                const pivotTable = sheet.pivotTables.get(0);
                // Das Ziel-PivotField abrufen (das erste Zeilenbeschriftungsfeld, in dem wir Elemente ausblenden/einblenden)
                const pivotField = pivotTable.rowFields.get(0);
                // Die PivotItems-Sammlung des ausgewählten PivotFields durchlaufen
                const itemCount = pivotField.pivotItems.count;
                for (let i = 0; i < itemCount; i++) {
                    const item = pivotField.pivotItems.get(i);
                    // Pivot-Elemente ausblenden, die einem bestimmten Namen/Kriterium entsprechen
                    if (item.name === "Item1" || item.name === "Item2") {
                        item.isHidden = true;
                    }
                    // Einblenden demonstrieren: Ein zuvor ausgeblendetes Pivot-Element wieder anzeigen
                    if (item.name === "Item3") {
                        item.isHidden = false;
                    }
                }
                // Die Pivot-Tabelle aktualisieren und neu berechnen, damit die Änderungen wirksam werden
                pivotTable.refreshData();
                // Arbeitsmappe speichern — ausgeblendete Elemente bleiben in den zugrunde liegenden Daten
                // werden jedoch aus der angezeigten Pivot-Tabellenausgabe ausgeschlossen
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
Aspose.Cells for JavaScript via C++ bietet einen vollständigen Satz an PivotTable-Filterfunktionen, die den in Microsoft Excel verfügbaren Funktionen entsprechen. Beschriftungs-, Datums- und Wertfilter decken die häufigsten Analyseszenarien ab, während der Top-10-Filter für Ranking-Berichte verwendet wird. Wenn die Filterregel unregelmäßig ist, bietet die Eigenschaft `pivotItem.isHidden` eine flexible Ausweichmöglichkeit auf Elementebene. Durch die Kombination dieser Strategien, beispielsweise durch die Anwendung eines Beschriftungsfilters und das anschließende Ausblenden bestimmter Elemente, lassen sich vollständig im Code präzise zugeschnittene PivotTable-Berichte erstellen.

{{< app/cells/assistant language="javascript-cpp" >}}