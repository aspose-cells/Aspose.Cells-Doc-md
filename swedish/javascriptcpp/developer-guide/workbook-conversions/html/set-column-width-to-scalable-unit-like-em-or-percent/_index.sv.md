---
title: Sätt kolumnbredd till skalbara enheter som em eller procent med JavaScript via C++
linktitle: Ställ in kolumnbredd till skalbar enhet som em eller procent
type: docs
weight: 130
url: /sv/javascript-cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Lär dig hur man sätter kolumnbredd till skalbara enheter som em eller procent i Aspose.Cells for JavaScript via C++. Förbättra presentationen av genererade HTML tabeller.
---

Att generera en HTML-fil från ett kalkylblad är mycket vanligt. Storleken på kolumnerna är definierad i "pt," vilket fungerar i många fall. Men det kan finnas tillfällen där denna fasta storlek inte är nödvändig. Till exempel, om en behållar-panelbredd är 600px, där den här HTML-sidan visas, kan du få ett horisontellt rullningsfält om den genererade tabellens bredd är större. Det krävdes att denna fasta storlek skulle ändras till en skalbar enhet som em eller procent för att få en bättre presentation. Följande kodexempel kan användas där [**HtmlSaveOptions.widthScalable**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#widthScalable--) är inställd på **true** för att skapa skalbar bredd.

Källfilen och utdatafiler kan laddas ned från följande länkar:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Scalable Columns to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, HtmlSaveOptions, SaveFormat } = AsposeCells;

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

            // Specify Html Save Options
            const options = new HtmlSaveOptions();

            // Set the property for scalable width (converted from setWidthScalable)
            options.widthScalable = true;

            // Specify image save format (converted from setExportImagesAsBase64)
            options.exportImagesAsBase64 = true;

            // Save the workbook in Html format with specified Html Save Options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outsampleForScalableColumns.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted to HTML successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
