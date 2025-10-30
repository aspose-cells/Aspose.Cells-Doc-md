---
title: Bestäm vilken axel som finns i diagrammet med JavaScript via C++
linktitle: Bestäm vilken axel som finns i diagrammet
description: Lär dig hur du bestämmer vilken axel som finns i ett diagram skapat med Aspose.Cells for JavaScript via C++. Vår guide hjälper dig att identifiera och få tillgång till de olika axlarna i ett diagram, inklusive kategori , värde och sekundära axlar.
keywords: Aspose.Cells for JavaScript via C++, diagram, axel, existens, kategori, värde, sekundär.
type: docs
weight: 140
url: /sv/javascript-cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}  
Ibland behöver användaren veta om en viss axel finns i diagrammet. Till exempel vill de veta om en sekundär värdeaxel finns i diagrammet eller inte. Vissa diagram som Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded, etc. har inte någon axel.  

Aspose.Cells tillhandahåller [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/javascript-cpp/chart/#hasAxis-AxisType-boolean-) metod för att avgöra om diagrammet har en specifik axel eller inte.  
{{% /alert %}}  

 Följande kodexempel demonstrerar användningen av [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/javascript-cpp/chart/#hasAxis-AxisType-boolean-) för att avgöra om diagrammet har primär och sekundär kategori- och värdeaxel.  

## JavaScript-kod för att bestämma vilken axel som finns i diagrammet

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Chart Axes Example</h1>
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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Check if there are any charts before accessing
            const charts = worksheet.charts;
            if (charts.count === 0) {
                resultDiv.innerHTML = '<p>No charts found in the worksheet.</p>';
                return;
            }

            // Access the chart
            const chart = charts.get(0);

            // Determine which axis exists in chart
            let outputs = [];
            let ret = chart.hasAxis(AsposeCells.AxisType.Category, true);
            outputs.push("Has Primary Category Axis: " + ret);

            ret = chart.hasAxis(AsposeCells.AxisType.Category, false);
            outputs.push("Has Secondary Category Axis: " + ret);

            ret = chart.hasAxis(AsposeCells.AxisType.Value, true);
            outputs.push("Has Primary Value Axis: " + ret);

            ret = chart.hasAxis(AsposeCells.AxisType.Value, false);
            outputs.push("Has Secondary Value Axis: " + ret);

            resultDiv.innerHTML = '<p>' + outputs.join('</p><p>') + '</p>';
        });
    </script>
</html>
```

## Konsolutdata som genereras av exempelkoden

Körresultatet av koden visas nedan, vilket visar sant för Primär Kategori- och Värdeaxel och falskt för Sekundär Kategori- och Värdeaxel.  

{{< highlight java >}}  
Has Primary Category Axis: True  
Has Secondary Category Axis: False  
Has Primary Value Axis: True  
Has Secondary Value Axis: False  
{{< /highlight >}}
