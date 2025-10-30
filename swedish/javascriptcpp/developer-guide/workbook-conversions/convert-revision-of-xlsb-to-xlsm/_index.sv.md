---
title: Konvertera revision av XLSB till XLSM med JavaScript via C++
linktitle: Konvertera revision av XLSB till XLSM
type: docs
weight: 290
url: /sv/javascript-cpp/convert-revision-of-xlsb-to-xlsm/
description: Lär dig att fullständigt konvertera revisioner av XLSB filer till XLSM format med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Aspose.Cells stödjer nu fullständig konvertering av revisioner av XLSB-filer till XLSM-filer. Revisionerna finns i vägen \xl\revisions. Du kan visa dem genom att byta ut din XLSB-filändelse till ZIP. Vägen \xl\revisions innehåller filer som slutar med .bin-extensioner.

När du konverterar din XLSB-fil till en XLSM-fil med Aspose.Cells, konverteras dessa .bin-filer till framgångsrikt till .xml-filer, som visas i dessa två skärmbilder.

{{% /alert %}}

Följande kodexempel visar hur du konverterar XLSB-filen till XLSM-format med Aspose.Cells for JavaScript via C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert XLSB to XLSM Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb,.csv" />
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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsb, .xls, .xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save Workbook to XLSM format
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted XLSM File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook converted to XLSM successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
