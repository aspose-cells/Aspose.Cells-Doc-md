---
title: Hitta typ av X och Y värden för punkter i diagramserie med JavaScript via C++
linktitle: Hitta typ av X och Y värden för punkter i diagramserier
description: Lär dig hur du avgör typen av X och Y värden i diagramseriepunkter med Aspose.Cells for JavaScript via C++. Denna guide förklarar datatyperna och hur du får åtkomst till och arbetar med dem i dina diagram.
keywords: Aspose.Cells for JavaScript via C++, diagramering, X värden, Y värden, datatyper, åtkomst, arbete med, diagramserier.
type: docs
weight: 150
url: /sv/javascript-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Möjliga användningsscenario**  
Ibland vill du veta typen av X- och Y-värden för diagrampunkter i en serie. Aspose.Cells for JavaScript via C++ tillhandahåller egenskaperna `ChartPoint.XValueType` och `ChartPoint.YValueType` som kan användas för detta ändamål. Observera att du måste anropa `Chart.calculate()`-metoden innan du kan använda dessa egenskaper effektivt.  

## **Hitta typ av X- och Y-värden för punkter i diagramserier**  
Följande exempel kod laddar filen [exempel Excel](64716905.xlsx) och kommer åt den första diagrammet i den första arbetsboken. Den anropar sedan `Chart.calculate()`, avgör typen av X- och Y-värden för den första diagrampunkten och skriver ut dem i konsolen. Se nedan exempel på konsolutmatning för referens.  

## **Exempelkod**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Find Type Of X and Y Values Of Points In Chart Series</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first chart.
            const chart = worksheet.charts.get(0);

            // Calculate chart data.
            chart.calculate();

            // Access first chart point in the first series.
            const point = chart.nSeries.get(0).points.get(0);

            // Get the types of X and Y values of chart point.
            const xValueType = point.xValueType;
            const yValueType = point.yValueType;

            // Display results
            document.getElementById('result').innerHTML = `
                <p style="color: green;">Operation completed successfully!</p>
                <p>X Value Type: ${xValueType}</p>
                <p>Y Value Type: ${yValueType}</p>
            `;
        });
    </script>
</html>
```  

## **Konsoloutput**  

{{< highlight java >}}  
 X Value Type: IsString  

Y Value Type: IsNumeric  
{{< /highlight >}}
