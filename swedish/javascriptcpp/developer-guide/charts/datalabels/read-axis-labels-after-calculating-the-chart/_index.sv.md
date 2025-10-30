---
title: Läs axeletiketter efter att ha beräknat diagrammet med JavaScript via C++
linktitle: Läs av axeletiketter efter att ha beräknat diagrammet
description: Lär dig hur du läser axel etiketter i Aspose.Cells for JavaScript via C++ efter att ha beräknat diagrammet. Vår guide visar hur du får åtkomst till och hämtar axel etiketter, inklusive deras formatering och position.
keywords: Aspose.Cells for JavaScript, diagram, axel etiketter, beräkning, läsning, åtkomst, hämtning, formatering, positionering, JavaScript via C++
type: docs
weight: 90
url: /sv/javascript-cpp/read-axis-labels-after-calculating-the-chart/
---

## **Möjliga användningsscenario**

Du kan läsa axelns etiketter för din diagram efter att ha beräknat dess värden med [**Chart.calculate()**](https://reference.aspose.com/cells/javascript-cpp/chart/#calculate--)-metoden. Använd propertyn [**Axis.axisTexts**](https://reference.aspose.com/cells/javascript-cpp/axis/#axisTexts--) för detta ändamål som returnerar listan över axelns etiketter.

## **Läs av axeletiketter efter att ha beräknat diagrammet**

Vänligen se följande kodexempel som laddar in den [exempel Excel-filen](ReadAxisLabels.xlsx) och läser kategoriaxlarna i diagrammet på den första arbetsbladet. Den skriver sedan ut värdena för axelmärkena på konsolen. Se konsolresultatet för kodexemplet nedan för referens.

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Read Axis Labels</title>
    </head>
    <body>
        <h1>Read Chart Category Axis Labels</h1>
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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the chart
            const chart = worksheet.charts.get(0);

            // Calculate the chart
            chart.calculate();

            // Read axis labels of category axis
            const lstLabels = chart.categoryAxis.axisTexts;

            // Display axis labels
            let html = '<h2>Category Axis Labels:</h2>';
            html += '<hr/>';
            if (!lstLabels || !lstLabels.length) {
                html += '<p>No axis labels found.</p>';
            } else {
                html += '<ul>';
                for (let i = 0; i < lstLabels.length; i++) {
                    console.log(lstLabels[i]);
                    html += `<li>${lstLabels[i]}</li>`;
                }
                html += '</ul>';
            }
            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

## **Konsoloutput**

{{< highlight javascript >}}  
 Category Axis Labels:  

\---------------------  

Iran  

China  

USA  

Brazil  

England  
{{< /highlight >}}
