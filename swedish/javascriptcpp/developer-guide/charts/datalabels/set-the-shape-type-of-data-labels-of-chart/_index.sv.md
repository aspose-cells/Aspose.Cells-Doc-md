---
title: Ställ in typen av form på datalabels i diagram med JavaScript via C++
linktitle: Ställ in datamärkenas formtyp i diagrammet
description: Lär dig hur du ställer in formtypen för datalabels i diagram med Aspose.Cells for JavaScript via C++. Denna guide förklarar de olika formtyper som finns och visar hur du väljer den lämpliga formen för dina datalabels för att förbättra presentationen och användbarheten.
keywords: Aspose.Cells for JavaScript via C++, diagram, datalabels, formtyper, presentation, användbarhet.
type: docs
weight: 110
url: /sv/javascript-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Möjliga användningsscenario**
Du kan ändra formtypen för datalabels i diagrammet med egenskapen `DataLabels.shapeType`. Den tar värdet från `DataLabelShapeType`-enum och ändrar formen på datalabels därefter. Några av dess värden är

{{< highlight javascript >}}
 DataLabelShapeType.BentLineCallout
DataLabelShapeType.DownArrowCallout
DataLabelShapeType.Ellipse
DataLabelShapeType.LineCallout
DataLabelShapeType.Rect
etc.
{{< /highlight >}}

## **Ställ in datamärkenas formtyp i diagram**
Följande exempel ändrar formtypen för datalabels i diagrammet till `DataLabelShapeType.WedgeEllipseCallout`. Se gärna [exempel-Excel-filen](60489778.xlsx) som används i denna kod och den [utdata-Excel file](60489779.xlsx) som genereras av den. Skärmbilden visar hur koden påverkar exempel-Excel-filen.

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **Exempelkod**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Shape Type of Data Labels of Chart Example</title>
    </head>
    <body>
        <h1>Set Shape Type of Data Labels of Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first chart
            const chart = worksheet.charts.get(0);

            // Accessing the first series
            const series = chart.nSeries.get(0);

            // Set the shape type of data labels i.e. Speech Bubble Oval
            series.dataLabels.shapeType = AsposeCells.DataLabelShapeType.WedgeEllipseCallout;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSetShapeTypeOfDataLabelsOfChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Shape type set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
