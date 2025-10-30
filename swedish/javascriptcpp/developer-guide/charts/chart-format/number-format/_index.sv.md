---
title: Ställ in Värdeformatkod för diagramserie med JavaScript via C++
description: Lär dig hur du ställer in värdeformatkoden för diagramserier i Aspose.Cells for JavaScript via C++. Denna guide hjälper dig att förstå hur du formaterar dina diagramseriedata med rätt formatkod för att presentera din data korrekt och professionellt.
keywords: Aspose.Cells for JavaScript via C++, diagramserier, värdeformatkod, formatering, datapräsentation, noggrannhet, professionalism.
linktitle: Nummerformat
type: docs
weight: 100
url: /sv/javascript-cpp/set-the-values-format-code-of-chart-series/
---

## **Möjliga användningsscenario**
Du kan ställa in värdeformatkoden för diagramserier med egendomen [Series.valuesFormatCode](https://reference.aspose.com/cells/javascript-cpp/series/#valuesFormatCode--). Denna egenskap är inte bara användbar för serier baserade på området i kalkylbladet utan fungerar även bra för serier skapade med en värdearray.

## **Ställ in värdenas formatkod för diagramserier**
Följande exempel kod lägger till en serie i det tomma diagrammet som tidigare inte hade någon serie. Den lägger till serien med hjälp av en värdearray. När den har lagts till, formateras den med koden $#,##0 med egendomen [Series.valuesFormatCode](https://reference.aspose.com/cells/javascript-cpp/series/#valuesFormatCode--) och numret 10000 blir $10 000. Skärmdumpen visar effekten av koden på [exempel filen](51740712.xlsx) och [utdatafilen](51740713.xlsx) efter körning.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Exempelkod**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Series Example</h1>
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

                // Access first worksheet
                const worksheet = workbook.worksheets.get(0);

                // Access first chart
                const chart = worksheet.charts.get(0);

                // Add series using an array of values
                chart.nSeries.add("{10000, 20000, 30000, 40000}", true);

                // Access the series and set its values format code
                const series = chart.nSeries.get(0);
                series.valuesFormatCode = "$#,##0";

                // Saving the modified Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = '51740713.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Modified Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```
