---
title: Konsolidierungsfunktion
type: docs
weight: 20
url: /de/javascript-cpp/consolidation-function/
description: Wie man die ConsolidationFunction auf Datenfelder der Pivot Tabelle mit Aspose.Cells for JavaScript via C++ anwendet.
keywords: Aspose.Cells for JavaScript via C++ Excel, Excel JavaScript Bibliothek, Verwendung der ConsolidationFunction auf Datenfelder der Pivot Tabelle mit Aspose.Cells for JavaScript via C++ Excel Bibliothek.
---

## **Konsolidierungsfunktion**

Aspose.Cells for JavaScript via C++ kann verwendet werden, um die ConsolidationFunction auf Datenfelder (oder Wertfelder) der Pivot-Tabelle anzuwenden. In Microsoft Excel können Sie mit der rechten Maustaste auf das Wertfeld klicken und die Option **Wertfeldeinstellungen...** auswählen und dann die Registerkarte **Werte zusammenfassen Nach** auswählen. Dort können Sie jede beliebige ConsolidationFunction wie Summe, Anzahl, Durchschnitt, Max, Min, Produkt, eindeutige Anzahl usw. auswählen.

Aspose.Cells for JavaScript via C++ bietet die Enumeration [**ConsolidationFunction**](https://reference.aspose.com/cells/javascript-cpp/consolidationfunction/), um die folgenden Konsolidierungsfunktionen zu unterstützen.

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

## **Wie man die ConsolidationFunction auf Datenfelder der Pivot-Tabelle mit Aspose.Cells for JavaScript via C++ anwendet**

Der folgende Code wendet die **Durchschnitt**-Konsolidierungsfunktion auf das erste Datenfeld (oder Wertefeld) und die **DistinctCount**-Konsolidierungsfunktion auf das zweite Datenfeld (oder Wertefeld) an.

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

Die DISTINCT_COUNT-Konsolidierungsfunktion wird nur von Microsoft Excel 2013 unterstützt.

{{% /alert %}}
