---
title: Ändra storlek på diagrammets datalabels form för att passa texten med JavaScript via C++
linktitle: Ändra diagrammets datamärkenes form för att passa texten
description: Lär dig hur man ändrar storlek på datalabels formen i ett diagram för att passa texten i Aspose.Cells for JavaScript via C++. Vår guide visar hur man justerar storleken och formen på etikettbehållaren för att säkerställa att texten visas korrekt utan skärning eller överlappning.
keywords: Aspose.Cells for JavaScript via C++, diagram, datalabels, formändring, textpassning, skärning, överlappning.
type: docs
weight: 220
url: /sv/javascript-cpp/resize-chart-s-data-label-shape-to-fit-text/
---

{{% alert color="primary" %}}  
Excel-programmet tillhandahåller alternativet **Ändra form för att passa text** för diagrammets datamärken för att öka storleken på formen så att texten passar inuti den.  
{{% /alert %}}  

## **Hur man ändrar diagrammets mikroform för att passa texten i Microsoft Excel**  

Detta alternativ kan nås via Excel-gränssnittet genom att välja någon av datalabels på diagrammet. Högerklicka och välj menyn **Format Data Labels**. Under fliken **Storlek & Egenskaper** expanderar du **Anpassning** för att visa relaterade egenskaper inklusive **Ändra storlek på formen för att fixa texten**.  

## **Hur man ändrar storlek på diagrammets datalabels form för att passa texten med Aspose.Cells for JavaScript via C++**  

För att efterlikna Excels funktion för att ändra storlek på datalabelsformer för att passa texten har Aspose.Cells API:erna exponerat den booleska egenskapen [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#isResizeShapeToFitText--). Följande kod visar ett enkelt exempel på hur du använder egenskapen [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#isResizeShapeToFitText--).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Chart Data Labels Resize Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet that contains the Chart
            const sheet = workbook.worksheets.get(0);

            for (let c = 0; c < sheet.charts.count; c++) {
                // Access the Chart
                const chart = sheet.charts.get(c);

                for (let index = 0; index < chart.nSeries.count; index++) {
                    // Access the DataLabels of indexed NSeries
                    const labels = chart.nSeries.get(index).dataLabels;

                    // Set ResizeShapeToFitText property to true
                    labels.isResizeShapeToFitText = true;
                }

                // Calculate Chart
                chart.calculate();
            }

            // Save the result
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
