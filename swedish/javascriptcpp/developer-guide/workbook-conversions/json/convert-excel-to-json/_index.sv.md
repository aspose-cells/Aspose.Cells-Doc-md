---
title: Konvertera Excel till JSON med JavaScript via C++
linktitle: Konvertera Excel till JSON
type: docs
weight: 300
url: /sv/javascript-cpp/convert-excel-to-json/
description: Lär dig hur man konverterar en Excel fil till JSON med Aspose.Cells for JavaScript via C++.
keywords: Exportera arbetsbok till JSON JavaScript via C++
---

{{% alert color="primary" %}}  
Aspose.Cells stöder konvertering av en arbetsbok till JSON (JavaScript-objektnotation) fil.  
{{% /alert %}}  

## **Konvertera Excel-arbetsbok till JSON**  

Behöver inte undra hur man konverterar Excelarbetsbok till JSON, eftersom Aspose.Cells for JavaScript via C++-biblioteket ger den bästa lösningen. Aspose.Cells API erbjuder stöd för att konvertera kalkylblad till JSON-format. För att exportera arbetsboken till JSON, ange [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat/) som den andra parametern för [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-)-metoden. Du kan också använda [**JsonSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonsaveoptions/)-klassen för att specificera ytterligare inställningar för att exportera kalkylbladet till JSON.  

Följande kodexempel visar hur man exporterar en Excel-arbetsbok till JSON. Se koden för att konvertera [källdatan](sample.xlsx) till JSON-filen som genereras av koden för referens.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to JSON Example</h1>
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

            // Convert the workbook to JSON
            const outputData = workbook.save(SaveFormat.Json);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample_out.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion to JSON completed. Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```  

Följande kodexempel använder JsonSaveOptions-klassen för att specificera ytterligare inställningar och demonstrerar export av en Excel-arbetsbok till JSON. Se koden för att konvertera [källfilen](sample.xlsx) till JSON-filen som genereras av koden för referens.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Workbook to JSON Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, JsonSaveOptions, Utils } = AsposeCells;

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

            // Load your source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an options of saving the file.
            const options = new JsonSaveOptions();

            // Set the exporting range.
            options.exportArea = CellArea.createCellArea("B1", "C4");

            // Convert the workbook to json file.
            const outputData = workbook.save(SaveFormat.Json, options);

            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample_out.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```
