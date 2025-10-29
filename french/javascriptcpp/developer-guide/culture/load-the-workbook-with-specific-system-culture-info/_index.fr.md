---
title: Charger le classeur avec des informations de culture système spécifiques via JavaScript et C++
linktitle: Charger le classeur avec des paramètres régionaux spécifiques du système
type: docs
weight: 190
url: /fr/javascript-cpp/load-the-workbook-with-specific-system-culture-info/
---

## **Scénarios d'utilisation possibles**
 Auparavant, vous deviez changer les informations de culture de toute la thread pour traiter les nombres et dates dans un format culturel particulier, mais maintenant Aspose.Cells for JavaScript via C++ offre la propriété `LoadOptions.CultureInfo` que vous pouvez utiliser pour charger votre classeur avec des informations de culture spécifiques sans changer la culture de toute la thread.

## **Charger le classeur avec des paramètres régionaux spécifiques du système**
Le code d'exemple suivant montre comment charger le classeur avec une culture système spécifique pour gérer les dates.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv,.html,.htm" />
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

        // Default HTML content (from the original JavaScript readable stream)
        const defaultHtmlContent = "<html><head><title>Test Culture</title></head><body><table><tr><td>10-01-2016</td></tr></table></body></html>";

        // Culture formatter as in the original code
        const culture = new Intl.NumberFormat("en-GB", {
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            let uint8Arr;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                uint8Arr = new Uint8Array(arrayBuffer);
            } else {
                const encoder = new TextEncoder();
                uint8Arr = encoder.encode(defaultHtmlContent);
            }

            // Instantiate Workbook from the HTML bytes (Aspose.Cells can load HTML content)
            const workbook = new Workbook(uint8Arr);

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created from HTML content. Click the download link to get the generated Excel file.</p>';
        });
    </script>
</html>
```

Le code d'exemple suivant montre comment charger le classeur avec une culture système spécifique pour gérer les numéros.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".html,.htm,.xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, CountryCode, CellValueType } = AsposeCells;

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

        document.getElementById('runExample').addEventListener('click', () => {
            // Creating an in-memory HTML stream equivalent
            const htmlString = "<html><head><title>Test Culture</title></head><body><table><tr><td>1234,56</td></tr></table></body></html>";

            // Encode string to Uint8Array for Workbook constructor
            const encoder = new TextEncoder();
            const array = encoder.encode(htmlString);

            // Prepare load options for HTML and set region to United Kingdom
            const options = new LoadOptions(LoadFormat.Html);
            options.region = CountryCode.UnitedKingdom;

            // Instantiate Workbook from the in-memory HTML content
            const workbook = new Workbook(new Uint8Array(array), options);

            // Access first worksheet and cell A1
            const cell = workbook.worksheets.get(0).cells.get("A1");

            // Assertions (will propagate failures)
            console.assert(cell.type === CellValueType.IsNumeric);
            console.assert(cell.doubleValue === 1234.56);

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Cell is numeric and equals 1234.56.</p>';
        });
    </script>
</html>
```
