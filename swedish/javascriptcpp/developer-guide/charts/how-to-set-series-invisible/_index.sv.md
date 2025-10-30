---
title: Hur man gör serie osynlig med JavaScript via C++
linktitle: Hur man sätter serien osynlig
description: Lär dig hur man gör serier osynliga i Excel diagram med Aspose.Cells for JavaScript via C++. 
keywords: Excel diagram, Serie, Osynlig, IsFiltered JavaScript via C++.
type: docs
weight: 74
url: /sv/javascript-cpp/how-to-set-series-invisible/
---

## Hur man ställer in serie som osynlig i Excel-diagram

I Excel-diagram kan du högerklicka på ett diagram, klicka på "Välj data" och i pop-up-fönstret kan du ställa in om en serie är synlig genom att markera eller avmarkera den. Du kan ladda ner följande [exempelfil](SeriesFiltered.xlsx) och använda den i Excel enligt figuren för att uppnå denna funktion. Nästa steg är att visa dig hur du uppnår detta med Aspose.Cells-biblioteket.

![todo:image_alt_text](series-invisible.png)

## Hur man ställer in serie som osynlig med Aspose.Cells 

Vi använder följande kod för att göra serie osynlig med Aspose.Cells:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Modify Chart Series Color Variation</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet and its charts
            const charts = workbook.worksheets.get(0).charts;
            const chart = charts.get("Chart 1");

            // Access filtered NSeries and NSeries collections (properties instead of getters)
            const nSeriesFiltered = chart.filteredNSeries;
            const nSeries = chart.nSeries;

            // Set IsColorVaried on series (converted from setIsColorVaried to property assignment)
            nSeries.get(1).isColorVaried = true;
            nSeries.get(0).isColorVaried = true;

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Du kan hämta följande [Inmatningsfil](SeriesFiltered.xlsx) och [Utdatafil](output.xlsx).

Som visas i figuren nedan har de två första serierna, som ursprungligen var synliga, blivit osynliga i utdatafilen.
![todo:image_alt_text](output.png)
