---
title: Hantera axlar för Excel diagram med JavaScript via C++
description: Lär dig hur du konfigurerar diagramaxlar i Aspose.Cells for JavaScript via C++. Vår guide visar dig hur du justerar primära och sekundära axlar, ställer in deras intervall och ändrar deras egenskaper för att förbättra dina diagram.
keywords: Aspose.Cells for JavaSkript via C++, diagramaxlar, konfiguration, primära axlar, sekundära axlar, intervall, egenskaper.
linktitle: Axlar
type: docs
weight: 50
url: /sv/javascript-cpp/chart-axes/
---

{{% alert color="primary" %}}  

I Excel-diagram finns det 3 typer av axlar:  
1. Horisontell (Kategori) Axel : X-Axel  
2. Vertikal (Värde) Axel : Y-axel  
3. Djup (Serie) Axel : Z-axel  

{{% /alert %}}  

## **Axelealternativ**  
Aspose.Cells for JavaSkript via C++ möjliggör också att hantera diagramaxlar i realtid. Med objektet [Axis](https://reference.aspose.com/cells/javascript-cpp/axis/) kan du ändra alla inställningar för Axis som i Excel.  

|![todo:image_alt_text](chart_axes.png)|  

## **Hantera X- och Y-axlar**  
I Excel-diagram är horisontella och vertikala axlar de två mest populära att använda.  

Följande kodsnutt visar hur man ställer in alternativen för X- och Y-axlar.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Chart Axes</title>
    </head>
    <body>
        <h1>Chart Axes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

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

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = "Series1";
            worksheet.cells.get("A2").value = 50;
            worksheet.cells.get("A3").value = 100;
            worksheet.cells.get("A4").value = 150;
            worksheet.cells.get("B1").value = "Series2";
            worksheet.cells.get("B2").value = 60;
            worksheet.cells.get("B3").value = 32;
            worksheet.cells.get("B4").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.chartDataRange = ["A1:B4", true];

            // Hiding X axis
            chart.categoryAxis.isVisible = false;

            // Setting max value of Y axis
            chart.valueAxis.maxValue = 200;
            // Setting major unit
            chart.valueAxis.majorUnit = 50;

            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_axes.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to download the file.</p>';
        });
    </script>
</html>
```  

## **Fortsatta ämnen**  
- [Ändra riktning för ticketiketter](/cells/sv/javascript-cpp/change-tick-label-direction/)  
- [Bestäm vilken axel som finns i diagrammet](/cells/sv/javascript-cpp/determine-which-axis-exists-in-the-chart/)  
- [Hantera automatiska enheter för diagramaxeln som Microsoft Excel](/cells/sv/javascript-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)  
- [Läs av axeletiketter efter att ha beräknat diagrammet](/cells/sv/javascript-cpp/read-axis-labels-after-calculating-the-chart/)  
- [Hur man ställer in kategoriaxel i Excel-diagram](/cells/sv/javascript-cpp/how-to-set-category-axis/)
