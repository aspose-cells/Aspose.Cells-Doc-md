---
title: Excel mit Tooltip in HTML umwandeln mit JavaScript über C++  
linktitle: Excel in HTML mit Tooltip konvertieren  
type: docs  
weight: 200  
url: /de/javascript-cpp/convert-excel-to-html-with-tooltip/  
description: Erfahren Sie, wie Sie Excel Dateien mit Tooltips für die vollständige Textanzeige mithilfe von Aspose.Cells for JavaScript über C++ in HTML Format konvertieren.  
---

## **Excel in HTML mit Tooltip konvertieren**

Es kann Fälle geben, in denen der Text im generierten HTML abgeschnitten wird, und Sie möchten den vollständigen Text als Tooltip beim Hover-Ereignis anzeigen. Aspose.Cells for JavaScript via C++ unterstützt dies durch die Bereitstellung der [**HtmlSaveOptions.addTooltipText**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#addTooltipText--)-Eigenschaft. Das Setzen der [**HtmlSaveOptions.addTooltipText**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#addTooltipText--)-Eigenschaft auf **true** fügt den vollständigen Text als Tooltip im generierten HTML hinzu.

Das folgende Bild zeigt den Tooltip in der generierten HTML-Datei.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

 Das folgende Code-Beispiel lädt die [Quellexcel-Datei](98107416.xlsx) und generiert die [Ausgabe-HTML-Datei](98107417.zip) mit Tooltip.

Beispielcode

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Add Tooltip to HTML Example</title>
    </head>
    <body>
        <h1>Add Tooltip to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HtmlSaveOptions and enable tooltip text
            const options = new HtmlSaveOptions();
            options.addTooltipText = true;

            // Save workbook as HTML with the specified options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddTooltipToHtmlSample_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file created successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
