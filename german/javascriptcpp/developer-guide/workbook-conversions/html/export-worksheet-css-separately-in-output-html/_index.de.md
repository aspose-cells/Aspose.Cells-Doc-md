---
title: Arbeitsblatt CSS separat im Ausgabeb HTML mit JavaScript via C++ exportieren
linktitle: Arbeitsblatt CSS separat im ausgegebenen HTML exportieren
type: docs
weight: 80
url: /de/javascript-cpp/export-worksheet-css-separately-in-output/
description: Erfahren Sie, wie Sie beim Konvertieren einer Excel Datei in HTML mit Aspose.Cells for JavaScript über C++ die CSS Stile des Arbeitsblatts separat exportieren.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells for JavaScript über C++ bietet die Möglichkeit, die CSS-Stile des Arbeitsblatts beim Konvertieren Ihrer Excel-Datei in HTML separat zu exportieren. Bitte verwenden Sie dazu die Eigenschaft [**HtmlSaveOptions.exportWorksheetCSSSeparately**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorksheetCSSSeparately--) und setzen Sie sie beim Speichern der Excel-Datei im HTML-Format auf **true**.

## **Arbeitsblatt-CSS separat im ausgegebenen HTML exportieren**

Der folgende Beispielcode erstellt eine Excel-Datei, fügt Text in Zelle **B5** in **Rot** farbe hinzu und speichert sie dann im HTML-Format mit [**HtmlSaveOptions.exportWorksheetCSSSeparately**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorksheetCSSSeparately--)-Eigenschaft. Bitte sehen Sie die [Ausgab-HTML](60489766.zip), die vom Code generiert wurde, zur Referenz. Im Archiv finden Sie **stylesheet.css** als Ergebnis des Beispielcodes.

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Worksheet CSS Separately Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Color, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Create a new workbook
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell B5 and put value inside it
            const cell = ws.cells.get("B5");
            cell.value = "This is some text.";

            // Set the style of the cell - font color is Red
            const st = cell.style;
            st.font.color = Color.Red;
            cell.style = st;

            // Specify html save options - export worksheet css separately
            const opts = new HtmlSaveOptions();
            opts.exportWorksheetCSSSeparately = true;

            // Save the workbook in html 
            const outputData = wb.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportWorksheetCSSSeparately.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved as HTML. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Einzelarbeitsblatt-Arbeitsmappe in HTML exportieren**

Wenn eine Arbeitsmappe mit mehreren Blättern mit Aspose.Cells for JavaScript über C++ in HTML konvertiert wird, erstellt sie eine HTML-Datei zusammen mit einem Ordner, der CSS und mehrere HTML-Dateien enthält. Wenn diese HTML-Datei im Browser geöffnet wird, sind die Tabs sichtbar. Dieses Verhalten ist auch für eine Arbeitsmappe mit einem einzelnen Arbeitsblatt gewünscht, wenn sie in HTML konvertiert wird. Früher wurde für einzelne Arbeitsmappen kein separater Ordner erstellt, sondern nur eine HTML-Datei. Solche HTML-Dateien zeigen beim Öffnen im Browser keine Tabs. MS Excel erstellt auch für einzelne Blätter einen entsprechenden Ordner und HTML, daher wird dasselbe Verhalten mit Aspose.Cells APIs umgesetzt. Die Beispiel-Datei kann unter folgendem Link heruntergeladen werden:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Save Workbook as HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, EncodingType, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify HTML save options
            const options = new HtmlSaveOptions();

            // Set optional settings (converted from setters to properties)
            options.encoding = EncodingType.UTF8;
            options.exportImagesAsBase64 = true;
            options.exportGridLines = true;
            options.exportSimilarBorderStyle = true;
            options.exportBogusRowData = true;
            options.excludeUnusedStyles = true;
            options.exportHiddenWorksheet = true;

            // Save the workbook in HTML format with specified HtmlSaveOptions
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSampleSingleSheet.htm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook saved to HTML. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
