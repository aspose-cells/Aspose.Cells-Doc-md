---
title: Konvertera Excel till HTML med verktygstips med JavaScript via C++  
linktitle: Konvertera Excel till HTML med verktygstips  
type: docs  
weight: 200  
url: /sv/javascript-cpp/convert-excel-to-html-with-tooltip/  
description: Lär dig hur du konverterar Excel filer till HTML format med verktygstips för fullständig textvisning med Aspose.Cells for JavaScript via C++.  
---

## **Konvertera Excel till HTML med verktygstips**

Det kan finnas fall där texten klipps av i den genererade HTML:en och du vill visa hela texten som ett verktygstips vid hovring. Aspose.Cells for JavaScript via C++ stöder detta genom att tillhandahålla [**HtmlSaveOptions.addTooltipText**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#addTooltipText--) egenskapen. Att sätta [**HtmlSaveOptions.addTooltipText**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#addTooltipText--) egenskapen till **true** kommer att lägga till hela texten som ett verktygstips i den genererade HTML:en.

Följande bild visar tooltipen i den genererade HTML-filen.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Följande kodexempel laddar [käll-Excel-filen](98107416.xlsx) och genererar [utdata-HTML-filen](98107417.zip) med verktygstips.

Exempelkod

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
