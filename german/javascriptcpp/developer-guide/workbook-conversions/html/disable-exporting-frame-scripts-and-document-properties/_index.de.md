---
title: Deaktivieren des Exports von Frame Skripten und Dokumenteigenschaften mit JavaScript via C++
linktitle: Deaktivieren des Exportierens von Rahmen Skripten und Dokumenteigenschaften
type: docs
weight: 310
url: /de/javascript-cpp/disable-exporting-frame-scripts-and-document-properties/
description: Erfahren Sie, wie Sie den Export von Frame Skripten und Dokumenteigenschaften beim Konvertieren eines Arbeitsbuchs in HTML mit Aspose.Cells for JavaScript via C++ deaktivieren.
--- 

{{% alert color="primary" %}}

Aspose.Cells exportiert Frame-Skripte und Dokumenteigenschaften beim Konvertieren eines Arbeitsbuchs in HTML. Die Version 8.6.0 von Aspose.Cells for JavaScript via C++ führt eine Option ein, mit der der Export von Frame-Skripten und Dokumenteigenschaften optional deaktiviert werden kann. Bitte verwenden Sie die Eigenschaft `HtmlSaveOptions.exportFrameScriptsAndProperties`, um den Export zu deaktivieren.

{{% /alert %}}

## **Deaktivieren des Exports von Rahmen-Skripten und Dokumenteigenschaften**

Der folgende Beispielcode ermöglicht es Ihnen, den Export von Rahmen-Skripten und Dokumenteigenschaften zu deaktivieren. Nach der Konvertierung einer Arbeitsmappe in HTML enthält die Ausgabedatei keine Rahmen-Skripte und Dokumenteigenschaften.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;

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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Disable exporting frame scripts and document properties
            const options = new HtmlSaveOptions();
            options.exportFrameScriptsAndProperties = false;

            // Save workbook as HTML
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
