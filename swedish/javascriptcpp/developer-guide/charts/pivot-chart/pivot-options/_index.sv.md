---
title: Hur man hanterar PivotChart med PivotOptions för JavaScript via C++
linktitle: Pivotalternativ
type: docs
weight: 10
url: /sv/javascript-cpp/how-to-manage-pivotchart-with-pivotoptions/
description: Hur man hanterar PivotChart med PivotOptions i JavaScript via C++.
keywords: PivotDiagram JavaScript via C++
---

## Vad är PivotChart

En PivotChart i Excel är en grafisk representation av data skapad från en PivotTable. Den låter användare visualisera och analysera data dynamiskt genom att sammanfatta och visa information i diagramform. PivotCharts är interaktiva och kan lätt modifieras för att visa olika perspektiv av data, vilket gör det till ett kraftfullt verktyg för dataanalys och presentation i Excel.

## Hur man hanterar PivotChart med PivotOptions

Med hjälp av Aspose.Cells for JavaScript via C++, kan du använda [**PivotOptions**](https://reference.aspose.com/cells/javascript-cpp/pivotoptions/) för att hantera PivotChart.

Exempelfil och kod:
[Exempelfil](Sample.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide PivotChart ZoneFilter Example</h1>
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

            // Accessing the first worksheet and the first chart
            const worksheet = workbook.worksheets.get(0);
            const chart = worksheet.charts.get(0);
            const opt = chart.pivotOptions;

            // Hide ZoneFilter in PivotChart
            opt.dropZoneFilter = false; // HideZoneFilter

            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HideZoneFilter.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">ZoneFilter hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Med den tidigare nämnda exempelkoden kan du kontrollera resultatfilen med följande effekt, som visas i figuren:

**![Output](Output.png)**
