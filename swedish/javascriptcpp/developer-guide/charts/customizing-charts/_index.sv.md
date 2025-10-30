---
title: Anpassa diagram med JavaScript via C++
linktitle: Anpassa diagram
description: Lär dig hur du anpassar diagram i Aspose.Cells for JavaScript via C++. Vår guide visar hur du modifierar diagramlayout, lägger till och formaterar dataserier, justerar axlar och använder olika formateringsalternativ för att förbättra utseendet och användbarheten.
keywords: Aspose.Cells for JavaScript via C++, diagram, anpassning, layout, dataserier, axlar, formatering, utseende, användbarhet.
type: docs
weight: 40
url: /sv/javascript-cpp/customizing-charts/
---

## **Skapa Anpassade Diagram**  

Hittills, när vi diskuterat diagram, har vi tittat på standarddiagram med sina standardformatinställningar. Vi definierar bara datakällan, sätter ett par egenskaper, och diagrammet skapas med dess standardformatinställningar. Men Aspose.Cells API:er stödjer också att skapa anpassade diagram som låter utvecklare skapa diagram med egna formatinställningar.  

Utvecklare kan skapa anpassade diagram vid körning med Aspose.Cells.  

Ett diagram består av en dataserie. Varje dataserie i Aspose.Cells representeras av ett [**Series**](https://reference.aspose.com/cells/javascript-cpp/series)-objekt medan [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection)-objekt fungerar som en samling av [**Series**](https://reference.aspose.com/cells/javascript-cpp/series)-objekt. När man skapar ett anpassat diagram har utvecklare friheten att använda olika typer av diagram för olika dataserier (samlade i [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection)-objektet).  

Exempelkoden nedan visar hur man skapar anpassade diagram. I det här exemplet kommer vi att använda ett stapeldiagram för den första dataserien och ett linjediagram för den andra serien. Resultatet är att vi lägger till ett stapeldiagram, kombinerat med ett linjediagram, till arbetsbladet.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            // Ensure Aspose.Cells is initialized
            await readyPromise;

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("A4").value = 110;
            worksheet.cells.get("B1").value = 260;
            worksheet.cells.get("B2").value = 12;
            worksheet.cells.get("B3").value = 50;
            worksheet.cells.get("B4").value = 100;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.nSeries.add("A1:B4", true);

            // Setting the chart type of 2nd NSeries to display as line chart
            chart.nSeries.get(1).type = ChartType.Line;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  

För närvarande stöder Aspose.Cells endast anpassade diagram som kombinerar pip-, linje-, kolumn- och stapeldiagram, men fler diagram kommer att stödas i framtida versioner.  

{{% /alert %}}
