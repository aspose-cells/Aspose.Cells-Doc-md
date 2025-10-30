---
title: Hur man skapar ett tornadodiagram med JavaScript via C++
linktitle: Hur man skapar ett tornado diagram
type: docs
weight: 73
url: /sv/javascript-cpp/create-tornado-chart/
description: Lär dig hur du skapar ett tornadodiagram med Aspose.Cells for JavaScript via C++ API.
keywords: JavaScript skapa ett tornadadiagram, lägg till ett tornadadiagram, infoga ett tornadadiagram
---

## **Introduktion**
Ett tornado diagram, även känt som en tornado graf eller tornado diagram, är en typ av datavisualisering som ofta används för känslighetsanalys i Excel. Det hjälper dig att förstå effekten av förändrande variabler på ett visst resultat eller en viss effekt.

## **Hur man skapar ett tornado diagram i Excel**
Du kan skapa ett tornado diagram i Excel genom att följa dessa steg:
1. Välj datan och gå till Infoga --> Diagram --> Infoga kolumn- eller stapeldiagram --> Staplad stolpdiagram. Klicka på det.
<br>
<img src="1.png" width=70% />
2. Ändra Y-axeln: Högerklicka på y-axeln. Klicka på formatera axeln. I etiketter, klicka på etikettposition nedrullningsalternativ och välj Låg element.
<br>
<img src="2.png" width=70% />
3. Välj vilken som helst stapel och gå till formatering. Ange en lämplig luckbredd.
<br>
<img src="3.png" width=70% />
4. Låt oss ta bort minustecknet (-) från tornado diagrammet. Välj x-axeln. Gå till formatering. I axelalternativ, klicka på nummer. I kategori, välj anpassad. I formatkoden skriv ###0,###0. Klicka på lägg till.
<br>
<img src="4.png" width=70% />
5. Klicka på y-axeln och gå till axelalternativen. I axelalternativen, kryssa i kategorier i omvänd ordning.
<br>
<img src="5.png" width=70% />

## **Hur man lägger till ett Tornadodiagram i Aspose.Cells for JavaScript via C++**
Vänligen se följande kodexempel. Den laddar den [exempelfil i Excel](sample.xlsx) som innehåller viss provdata. Sedan skapas det staplade stolpdiagrammet baserat på den initiala datan och relevanta egenskaper anges. Slutligen sparas arbetsboken till [utmatning XLSX-format](out.xlsx). Följande skärmdump visar tornado diagrammet skapat av Aspose.Cells i den resulterande Excelfilen.
<br>
<img src="6.png" width=70% />

### **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);
            const charts = sheet.charts;

            // Add bar chart
            const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
            const chart = charts.get(index);

            // Set data for bar chart
            chart.chartDataRange = "A1:C7";

            // Set properties for bar chart
            chart.title.text = "Tornado chart";
            chart.style = 2;
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;
            chart.plotArea.border.color = AsposeCells.Color.White;
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            chart.categoryAxis.tickLabelPosition = AsposeCells.TickLabelPositionType.Low;
            chart.category```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);
            const charts = sheet.charts;

            // Add bar chart
            const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
            const chart = charts.get(index);

            // Set data for bar chart
            chart.chartDataRange = "A1:C7";

            // Set properties for bar chart
            chart.title.text = "Tornado chart";
            chart.style = 2;
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;
            chart.plotArea.border.color = AsposeCells.Color.White;
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            chart.categoryAxis.tickLabelPosition = AsposeCells.TickLabelPositionType.Low;
            chart.categoryAxis.isPlotOrderReversed = true;

            chart.gapWidth = 10;

            const valueAxis = chart.valueAxis;
            valueAxis.tickLabels.numberFormat = "#,##0;#,##0";

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
