---
title: Berechnung der MINIFS und MAXIFS Funktionen von Excel 2016 mit JavaScript via C++
description: Dieser Artikel führt vor, wie die Aspose.Cells Bibliothek verwendet wird, um MINIFS und MAXIFS Funktionen in Microsoft Excel 2016 mit JavaScript via C++ zu berechnen. Laden Sie eine vorhandene Excel Datei oder erstellen Sie eine neue und verwenden Sie die Aspose.Cells Methoden, um diese Funktionen zu berechnen und die Ergebnisse auf der Festplatte zu speichern.
keywords: Aspose.Cells, Excel, 2016, MINIFS Funktion, MAXIFS Funktion, Berechnung JavaScript via C++
type: docs
weight: 300
url: /de/javascript-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Mögliche Verwendungsszenarien**
Microsoft Excel 2016 unterstützt MINIFS- und MAXIFS-Funktionen. Diese Funktionen werden in Excel 2013 oder früheren Versionen nicht unterstützt. Aspose.Cells for JavaScript via C++ unterstützt ebenfalls die Berechnung dieser Funktionen. Der folgende Screenshot zeigt die Verwendung dieser Funktionen. Bitte lesen Sie die roten Kommentare im Screenshot, um zu verstehen, wie diese Funktionen funktionieren.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Berechnung der Excel 2016 MINIFS- und MAXIFS-Funktionen**
Der folgende Beispielcode lädt die [Beispieldatei Excel](5115149.xlsx) und ruft die Methode [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) auf, um die Formelfeldberechnung über Aspose.Cells for JavaScript via C++ durchzuführen, und speichert dann die Ergebnisse in der [Ausgabedatei PDF](5115154.pdf).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>MINIFS and MAXIFS Calculation to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your source workbook containing MINIFS and MAXIFS functions
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Perform Aspose.Cells formula calculation
            workbook.calculateFormula();

            // Save the calculations result in pdf format
            const options = new PdfSaveOptions();
            options.onePagePerSheet = true;

            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputMINIFSAndMAXIFS.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Calculation and conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
