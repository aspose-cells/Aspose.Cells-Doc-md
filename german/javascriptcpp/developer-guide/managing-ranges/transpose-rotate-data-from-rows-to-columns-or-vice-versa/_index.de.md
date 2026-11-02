---
title: Bereich transponieren
linktitle: Bereich transponieren
description: Dieser Artikel erklärt, wie Daten von Zeilen zu Spalten oder umgekehrt in Excel-Dateien mithilfe von Aspose.Cells for JavaScript via C++ transponiert oder rotiert werden, und zwar mit drei verschiedenen Ansätzen.
keywords: Aspose.Cells, JavaScript via C++, Tabellenkalkulation, Bereich transponieren, Daten rotieren, TRANSPOSE-Funktion, dynamische Array-Formel, Array-Formel, Excel TRANSPOSE, Zeilen zu Spalten
type: docs
weight: 80
url: /de/javascript-cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ unterstützt das Transponieren (Rotieren) von Daten, sodass Zeilen zu Spalten und Spalten zu Zeilen werden, auf drei verschiedene Arten. Der erste Ansatz verwendet die In‑Place‑Methode `range.transpose()` und funktioniert in jeder Excel‑Version, während der zweite `cell.setDynamicArrayFormula()` nutzt, um eine moderne dynamische Array‑Formel `=TRANSPOSE(...)` zu schreiben, die in Excel 365 oder Excel 2021 automatisch ausgibt. Der dritte Ansatz verwendet `cell.setArrayFormula()`, um eine klassische Ctrl+Shift+Enter‑(CSE‑)Array‑Formel zu schreiben, die mit älteren Excel‑Versionen kompatibel ist. Dieser Artikel führt jede Methode Schritt für Schritt mit vollständigen Code‑Beispielen aus.
{{% /alert %}}

## **Einleitung**
Das Transponieren eines Bereichs bedeutet, ihn zu rotieren, sodass eine zuvor vorhandene Zeile zu einer Spalte wird und eine zuvor vorhandene Spalte zu einer Zeile, was im Wesentlichen einer Spiegelung der Daten an ihrer Hauptdiagonalen entspricht. In Microsoft Excel führt die Arbeitsblattfunktion `TRANSPOSE` diese Operation aus, und die konzeptuelle Referenz ist unter [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) dokumentiert. Dieses Konzept kann programmgesteuert auf einen Zellenbereich angewendet werden und ist in vielen Geschäfts‑ und Berichtsszenarien nützlich.
- Umschalten von quartals‑ oder jahresweisen Verkaufsberichten, bei denen Quartale normalerweise horizontal und Regionen vertikal angeordnet sind, oder umgekehrt.
- Vertauschen der Achsenorientierung in Dashboards oder Diagrammen, sodass eine Zeitreihe vertikal anstatt horizontal verläuft.
- Umformen von Daten, die aus externen Systemen importiert wurden, damit sie dem von nachgelagerten Analysen‑ oder Berichtsvorlagen erwarteten Layout entsprechen.
Um den Rest des Artikels greifbar zu machen, verwendet jedes Beispiel die folgende kleine Verkaufs‑nach‑Region‑nach‑Quartal‑Tabelle. In der Beispiel‑Arbeitsmappe befindet sich diese Tabelle im Bereich **A1:D5**, wobei **A1** leer bleibt als linke obere Ecke, **B1:D1** die Regionsüberschriften enthält und **A2:A5** die Quartalsüberschriften.
| Region | Europa | Asien | Nordamerika |
|--------|--------|-------|-------------|
| Quartal 1 | 21704714 | 8774099 | 12094215 |
| Quartal 2 | 17987034 | 12214447 | 10873099 |
| Quartal 3 | 19485029 | 14356879 | 15689543 |
| Quartal 4 | 22567894 | 15763492 | 17456723 |
Der Artikel stellt anschließend drei verschiedene Methoden zum Transponieren dieser Daten mit Aspose.Cells for JavaScript via C++ vor, die jeweils für unterschiedliche Excel‑Versionen und Anwendungsfälle geeignet sind.

## **Ansatz 1 — Bereich in‑Place transponieren (Range.transpose)**
Verwenden Sie diesen Ansatz, wenn Sie Daten transponieren möchten, ohne die Arbeitsblattfunktion `TRANSPOSE` zu verwenden. Er funktioniert in **jeder Excel‑Version** und ist nicht von dynamischen Arrays abhängig, was ihn zur sichersten, versionsübergreifend kompatiblen Option macht. Er ist ideal, wenn Sie nur das endgültige transponierte Ergebnis benötigen und die ursprüngliche `TRANSPOSE`‑Formel nicht im Arbeitsbuch behalten müssen.

### **Verwendete API**
`Range.transpose()` ist eine Instanzmethode der Klasse `Aspose.Cells.Range`. Der Aufruf kehrt den Bereich in‑Place um, indem er Zeilen und Spalten vertauscht, sodass eine zuvor vorhandene Zeile zu einer Spalte wird und umgekehrt. Die Methode ändert die zugrunde liegenden Zellen direkt, ohne eine Formel zu schreiben.

### **Schritte**
1. Öffnen Sie die Quell‑Arbeitsmappe mit `LoadOptions`, die auf das `.xlsx`‑Format eingestellt ist, indem Sie `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` aufrufen.
2. Rufen Sie das erste Arbeitsblatt aus der Arbeitsmappe mit `workbook.getWorksheets().get(0)` ab.
3. Greifen Sie über `worksheet.getCells()` auf die Zellsammlung des Arbeitsblatts zu.
4. Erstellen Sie den Quell‑Bereich, der **A1:D5** abdeckt, indem Sie `cells.createRange("A1:D5")` aufrufen.
5. Rufen Sie `source.transpose()` auf, um den Bereich in‑Place zu rotieren und Zeilen mit Spalten zu vertauschen.
6. Speichern Sie die Arbeitsmappe mit `workbook.save(outputFile)`.
Nach dem Transponieren enthält dieser Anker‑Bereich die rotierten Daten. Die erste Zeile lautet (leer, **Europa**, **Asien**, **Nordamerika**) und die erste Spalte lautet (leer, **Quartal 1**, **Quartal 2**, **Quartal 3**, **Quartal 4**). Jede ursprüngliche Verkaufsspalte wird zu einer Zeile im transponierten Bereich.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an .xlsx file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                const source = cells.createRange("A1:D5");
                source.transpose();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "transposed.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = '<p style="color: red;">An error occurred while processing the file.</p>';
            }
        });
    </script>
</html>
```

## **Ansatz 2 — Transponieren mit einer dynamischen Array‑Formel (Excel 365 / 2021)**
Verwenden Sie diesen Ansatz, wenn Sie die Formel `=TRANSPOSE(A1:D5)` als Live‑Formel im Ausgabearbeitsbuch erhalten möchten, sodass das Ergebnis automatisch aktualisiert wird, wenn sich die Quelldaten ändern, und die Ziel‑Excel‑Datei in **Excel 365 / Excel 2021 oder neuer** geöffnet wird, wo dynamische Arrays und der Spill‑Operator unterstützt werden.

### **Verwendete API**
`Cell.setDynamicArrayFormula(formula, options, calculateValue)` ist eine Methode der Klasse `Aspose.Cells.Cell`, die die Zellformel als **dynamische Array‑Formel** festlegt. Excel wertet die Formel einmal aus und gibt das Ergebnis automatisch in die benachbarten Zellen aus. Der dritte Parameter, wenn er auf `true` gesetzt ist, veranlasst Aspose.Cells, die resultierenden Werte bereits beim Schreiben zu berechnen.

### **Schritte**
1. Laden Sie die Quell‑Arbeitsmappe mit `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Rufen Sie das erste Arbeitsblatt ab und greifen Sie auf dessen Zellsammlung zu.
3. Platzieren Sie die dynamische Array‑Formel in Zelle **A6**, direkt unter dem Quell‑Bereich, indem Sie `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true)` aufrufen.
4. Das Argument `new FormulaParseOptions()` verwendet die Standardeinstellungen von `FormulaParseOptions`, und das dritte Argument `true` weist Aspose.Cells an, die Formel als dynamisches Array zu behandeln und zu evaluieren, sodass die ausgegebenen Werte in die Arbeitsmappe geschrieben werden.
5. Speichern Sie die Arbeitsmappe mit `workbook.save(outputFile)`.
Zelle **A6** enthält die Formel `=TRANSPOSE(A1:D5)` und Excel gibt das Ergebnis automatisch in den Bereich **A6:E9** aus, ein 4 Zeilen‑mal‑5 Spalten‑Block, der den transponierten Daten entspricht.

{{% alert color="primary" %}}
Dieser Ansatz funktioniert **nur in Excel 365 / 2021 oder neuer**. Ältere Excel‑Versionen geben dynamische Array‑Formeln nicht korrekt aus.
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
        const { Workbook, FormulaParseOptions } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            await initialization;
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            const workbook = new Workbook(new Uint8Array(await fileInput.files[0].arrayBuffer()));
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A6").setDynamicArrayFormula(
                "=TRANSPOSE(A1:D5)",
                new FormulaParseOptions(),
                true
            );
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_transpose_dynamic.xlsx";
            downloadLink.style.display = "block";
            result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Ansatz 3 — Transponieren mit einer klassischen Array‑Formel (CSE)**
Verwenden Sie diesen Ansatz, wenn Sie eine `TRANSPOSE`‑Formel im Arbeitsbuch erhalten möchten, die Ziel‑Excel‑Datei jedoch in **älteren Excel‑Versionen (vor 2021, einschließlich 2019, 2016, 2013 usw.)** geöffnet werden kann, in denen das Ausgeben dynamischer Arrays nicht unterstützt wird. Die klassische CSE‑(Ctrl+Shift+Enter‑)Array‑Formel ist die legacy‑kompatible Alternative, die alle Excel‑Versionen auswerten können.

### **Verwendete API**
`Cell.setArrayFormula(arrayFormula, nRows, nColumns)` ist eine Methode der Klasse `Aspose.Cells.Cell`, die einer Ankerzelle eine **klassische Array‑(CSE‑)Formel** zuweist und die Dimensionen des resultierenden Arrays deklariert. Aspose.Cells schreibt den Marker für die Mehrzellen‑Array‑Formel, sodass Excel die Formel als einzelne Array‑Expression auswertet, die den deklarierten Bereich füllt.

### **Schritte**
1. Laden Sie die Quell‑Arbeitsmappe wie in den vorherigen Ansätzen beschrieben.
2. Rufen Sie das erste Arbeitsblatt ab und greifen Sie auf dessen Zellsammlung zu.
3. Rufen Sie `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)` auf. Das zweite Argument `4` gibt die Anzahl der Zeilen des Ziel‑Arrays an und das dritte Argument `5` die Anzahl der Spalten.
4. Speichern Sie die Arbeitsmappe mit `workbook.save(outputFile)`.
Zelle **A6** ist der Anker der Array‑Formel und das ausgewertete Array erstreckt sich über 4 Zeilen × 5 Spalten, beginnend bei A6, und entspricht den transponierten Abmessungen der Quelle A1:D5. Excel schreibt einen einzelnen Array‑Formel‑Marker über den resultierenden Bereich, sodass ältere Excel‑Versionen ihn korrekt auswerten.

{{% alert color="primary" %}}
CSE‑Array‑Formeln sind die klassische Excel‑Methode, um einen `TRANSPOSE`‑Ausdruck auszuwerten, und dieser Ansatz ist universell mit allen Excel‑Versionen kompatibel.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                await initialization;
                const fileInput = document.getElementById('fileInput');
                const downloadLink = document.getElementById('downloadLink');
                const result = document.getElementById('result');
                const file = fileInput.files[0];
                if (!file) {
                    throw new Error("Please select an XLSX workbook.");
                }
                // Laden Sie die Quellarbeitsmappe mit xlsx LoadOptions
                const loadOptions = new LoadOptions(AsposeCells.LoadFormat.Xlsx);
                const workbook = new Workbook(
                    new Uint8Array(await file.arrayBuffer()),
                    loadOptions
                );
                // Greifen Sie auf das erste Arbeitsblatt und seine Zellen‑Sammlung zu
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // Setzen Sie die klassische CSE-Array-Formel in Zelle A6.
                // Die Formel =TRANSPOSE(A1:D5) dreht den 5‑zeiligen x 4‑spaltigen Quellbereich
                // in ein 4‑zeiliges x 5‑spaltiges Array. Das zweite Argument (4) ist die Anzahl der Zeilen
                // und das dritte Argument (5) ist die Anzahl der Spalten des resultierenden Arrays.
                // Aspose.Cells schreibt den CSE-Array-Formel-Marker, sodass Excel ihn auswertet als
                // eine einzelne Mehrzellen-Array-Formel, kompatibel mit älteren Excel-Versionen
                // (2019, 2016, 2013 usw.), die kein dynamisches Array‑Spilling unterstützen.
                cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
                // Speichern Sie die Arbeitsmappe, damit der Array‑Formel‑Marker beibehalten wird
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                document.getElementById('result').innerHTML =
                    '<p style="color: red;">Error: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

## **Vergleich — Wann welcher Ansatz verwendet werden sollte**
| Ansatz | API / Methode | Excel‑Version | Quellformel erhalten? | Ausgabe‑Bereich |
|--------|----------------|---------------|-----------------------|-----------------|
| Ansatz 1 — In‑Place‑Transponieren | `range.transpose()` | Alle Excel‑Versionen | Nein (nur Werte) | Ursprünglicher Anker‑Bereich, 5×4 |
| Ansatz 2 — Dynamische Array‑Formel | `cell.setDynamicArrayFormula()` | Excel 365 / 2021+ | Ja (dynamisch ausgebreitet) | Aus dem Anker ausgebreitet |
| Ansatz 3 — Klassische Array‑Formel (CSE) | `cell.setArrayFormula()` | Alle Excel‑Versionen | Ja (mehrzellige Array‑Formel) | Explizite Größe, 4×5 |
Verwenden Sie **Ansatz 1**, wenn Sie eine schnelle, versionsübergreifende Transformation benötigen und nur die transponierten Werte in die Datei schreiben wollen. Verwenden Sie **Ansatz 2**, wenn moderne Excel‑Versionen garantiert sind und Sie die Formel live behalten sowie bei Änderungen der Quelle aktualisieren möchten. Verwenden Sie **Ansatz 3**, wenn Sie die größtmögliche Kompatibilität mit einer erhaltenen Formel über alle Excel‑Versionen hinweg benötigen, einschließlich der älteren Versionen, die keine dynamischen Arrays unterstützen.

{{< app/cells/assistant language="javascript-cpp" >}}