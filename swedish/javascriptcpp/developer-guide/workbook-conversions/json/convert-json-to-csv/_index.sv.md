---
title: Konvertera JSON till CSV med JavaScript via C++
linktitle: Konvertera JSON till CSV
type: docs
weight: 210
url: /sv/javascript-cpp/convert-json-to-csv/
description: Lär dig hur man konverterar JSON data till CSV med Aspose.Cells for JavaScript via C++.
---

## **Konvertera JSON till CSV**

Aspose.Cells for JavaScript via C++ stödjer konvertering av enkel och nästlad JSON till CSV. För detta tillhandahåller API:t [**JsonLayoutOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions) och [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility)-klass. [**JsonLayoutOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions)-klassen ger alternativen för JSON-layout som [**JsonLayoutOptions.arrayAsTable**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions/#arrayAsTable--) (bearbetar arrayen som ett bord). [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility)-klassen bearbetar JSON med layoutalternativen som ställts in med [**JsonLayoutOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions)-klassen.

Följande kodexempel visar användningen av klasserna [**JsonLayoutOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions) och [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility) för att ladda [käljsonfil](104398869.json) och generera [utdata CSV-fil](104398870.csv).

### **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells JSON to CSV Example</title>
    </head>
    <body>
        <h1>Import JSON to CSV Example</h1>
        <input type="file" id="fileInput" accept=".json" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, JsonLayoutOptions, JsonUtility, Utils } = AsposeCells;

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
                resultDiv.innerHTML = '<p style="color: red;">Please select a JSON file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const jsonText = await file.text();

            // Create empty workbook
            const workbook = new Workbook();

            // Get Cells from first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Set JsonLayoutOptions
            const importOptions = new JsonLayoutOptions();
            importOptions.convertNumericOrDate = true;
            importOptions.arrayAsTable = true;
            importOptions.ignoreTitle = true;

            // Import JSON data into worksheet cells starting at A1 (0,0)
            JsonUtility.importData(jsonText, cells, 0, 0, importOptions);

            // Save Workbook as CSV
            const outputData = workbook.save(SaveFormat.Csv);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SampleJson_out.csv';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CSV File';

            resultDiv.innerHTML = '<p style="color: green;">JSON imported and CSV prepared. Click the download link to get the CSV file.</p>';
        });
    </script>
</html>
```
