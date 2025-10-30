---
title: Konsolideringsfunktion
type: docs
weight: 20
url: /sv/javascript-cpp/consolidation-function/
description: Hur man tillämpar ConsolidationFunction på datafält i pivottabell med Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells for JavaScript via C++ Excel, Excel JavaScript bibliotek, ConsolidationFunction på datafält i pivottabell med Aspose.Cells for JavaScript via C++ Excel bibliotek.
---

## **Konsolideringsfunktion**

Aspose.Cells for JavaScript via C++ kan användas för att tillämpa ConsolidationFunction på datafält (eller värdefält) i pivottabellen. I Microsoft Excel kan du högerklicka på värdefältet och sedan välja **Värdefältinställningar...** och sedan välja fliken **Sammanfatta värden efter**. Därifrån kan du välja vilken ConsolidationFunction du vill ha såsom Summa, Antal, Medel, Max, Min, Produkt, Distinkt antal osv.

Aspose.Cells for JavaScript via C++ tillhandahåller [**ConsolidationFunction**](https://reference.aspose.com/cells/javascript-cpp/consolidationfunction/)-enumerationen för att stödja följande sammanfattningsfunktioner.

- ConsolidationFunction.Average
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums
- ConsolidationFunction.DistinctCount
- ConsolidationFunction.Max
- ConsolidationFunction.Min
- ConsolidationFunction.Product
- ConsolidationFunction.StdDev
- ConsolidationFunction.StdDevp
- ConsolidationFunction.Sum
- ConsolidationFunction.Var
- ConsolidationFunction.Varp

## **Hur man tillämpar ConsolidationFunction på datafält i pivottabell med Aspose.Cells for JavaScript via C++**

Följande kod tillämpar **Medelvärde** konsolideringsfunktion på det första datafältet (eller värdefältet) och **DistinktAntal** konsolideringsfunktion på det andra datafältet (eller värdefältet).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PivotTable Consolidation Function</title>
    </head>
    <body>
        <h1>Apply Consolidation Function to PivotTable</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet of the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access the first pivot table of the worksheet
            const pivotTable = worksheet.pivotTables.get(0);

            // Apply Average consolidation function to first data field
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Average;

            // Apply DistinctCount consolidation function to second data field
            pivotTable.dataFields.get(1).function = AsposeCells.ConsolidationFunction.DistinctCount;

            // Calculate the data to make changes affect
            pivotTable.calculateData();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PivotTable consolidation functions applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

DISTINCT_COUNT konsolideringsfunktion stöds endast av Microsoft Excel 2013.

{{% /alert %}}
