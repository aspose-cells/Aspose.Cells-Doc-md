---
title: Utöka text från höger till vänster vid export av Excel fil till HTML med JavaScript via C++
linktitle: Expandera text från höger till vänster vid export av Excel fil till HTML
type: docs
weight: 60
url: /sv/javascript-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/
---

{{% alert color="primary" %}}

Aspose.Cells stödjer nu att expandera text från höger till vänster vid export av Excel-fil till HTML. Denna funktion har implementerats sedan v8.9.0.0. Nu om din käll-Excel-fil innehåller någon text som expanderar från höger till vänster, kommer Aspose.Cells att exportera den till HTML korrekt.

{{% /alert %}}
## **Expandera text från höger till vänster vid export av Excel-fil till HTML**
Det följande kodexemplet konverterar [provexelfilen](5115502.xlsx) till HTML. Denna skärmbild visar hur provexelfilen ser ut i Microsoft Excel 2013.

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

Denna skärmbild visar [utdata-HTML genererad med äldre version](5115509).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

Denna skärmbild visar [utdata-HTML genererad med nyare version](5115508).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

Som du kan se i skärmbilderna, expanderar den nyare versionen den högerjusterade texten till vänster korrekt precis som Microsoft Excel.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Expand Text From Right To Left Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load source excel file inside the workbook object
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Get CellsHelper version (converted from getVersion())
            const version = CellsHelper.version;

            // Save workbook in html format
            const outputData = wb.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `ExpandTextFromRightToLeft_out_${version}.html`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook converted to HTML successfully. Click the download link to get the result.</p>';
        });
    </script>
</html>
```
