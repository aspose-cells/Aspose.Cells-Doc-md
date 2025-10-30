---
title: Rendera Office tillägg medan du konverterar Excel till PDF med JavaScript via C++
linktitle: Rendera Office tillägg vid konvertering av Excel till PDF
type: docs
weight: 100
url: /sv/javascript-cpp/render-office-add-ins-while-converting-excel-to-pdf/
---

## **Möjliga användningsscenario**

Tidigare kunde Aspose.Cells inte rendera Office-tillägg när en Excel-fil sparas till PDF-format. Nu renderar Aspose.Cells det utan problem. Du behöver inte använda någon speciell metod eller egenskap för att rendera Office-tillägg i output-PDF:en. Spara helt enkelt din Excel-fil som PDF, så renderas Office-tillägget.

## **Rendera Office-tillägg vid konvertering av Excel till PDF**

Följande exempel kod sparar [exempel Excel-fil](60489769.xlsx) som innehåller Office-tillägg. Se [utdata PDF genererad med den tidigare versionen, dvs. 17.11](60489770.pdf) och den [nyare versionen, dvs. 17.12 och senare](60489771.pdf). Den föregående versionens utdata PDF är tom, men den nyare versionen visar Office-tillägget.

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Render Office Add-Ins to PDF Example</title>
    </head>
    <body>
        <h1>Render Office Add-Ins to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Aspose.Cells version (converted from getVersion())
            const version = AsposeCells.CellsHelper.version;

            // Save workbook to PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `output-${version}.pdf`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Saved to PDF successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
