---
title: Dölj visningen av nollvärden i kalkylbladet med JavaScript via C++
linktitle: Döljning av visning av nollvärden i kalkylarket
type: docs
weight: 50
url: /sv/javascript-cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: Denna artikel visar exempel på kod som förklarar hur man programmatisk döljer nollvärden i ett Excel ark med JavaScript biblioteket via C++.
keywords: dölj nollvärden i Excel ark i JavaScript via C++
---

{{% alert color="primary" %}} 

Ibland måste du dölja nollvärden i ett kalkylblad. Det kan vara en personlig preferens eller en formateringsstandard.

{{% /alert %}} 

För att dölja nollvärden i ett arbetsblad i Microsoft Excel (till exempel Microsoft Excel 2003):

1. Från menyn ** Verktyg ** väljer du ** Alternativ ** och väljer sedan fliken ** Visa **.
1. Avmarkera alternativet ** Nollvärden **.
1. Klicka på **OK**.

 Vänligen se följande exempel på kod som demonstrerar dölja nollor med Aspose.Cells for JavaScript via C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide Zero Values Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get First worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Hide the zero values in the sheet
            sheet.displayZeros = false;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputfile.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
