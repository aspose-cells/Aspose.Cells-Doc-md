---
title: Datumaxel med JavaScript via C++
description: Lär dig hur man hanterar datumaxeln i Aspose.Cells for JavaScript via C++. Vår guide hjälper dig att förstå hur du arbetar med olika datumformat, tidsnivåer och tickmarkeringens frekvens.
keywords: Aspose.Cells for JavaScript via C++, datumaxel, hantera, datumformat, tidsnivåer, tickmarkeringens frekvens.
type: docs
weight: 200
url: /sv/javascript-cpp/date-axis/
---

## **Möjliga användningsscenario**
När du skapar ett diagram från arbetsbladets data som använder datum, och datumen plottas längs den horisontella (kategori) axeln i diagrammet, ändrar Aspose.Cells for JavaScript via C++ automatiskt kategoriaxeln till en datum (tids-skala) axel.
En datumsaxel visar datum i kronologisk ordning vid specifika intervall eller basenheter, såsom antalet dagar, månader eller år, även om datumen i arbetsboken inte är i sekventiell ordning eller i samma basenheter.
Som standard bestämmer Aspose.Cells basenheten för datumaxeln utifrån den minsta skillnaden mellan två datum i worksheet-data. Till exempel, om du har data för aktiekurser där den minsta skillnaden mellan datum är sju dagar, ställer Excel in basenheten till dagar, men du kan ändra basenheten till månader eller år om du vill se aktiens utveckling över en längre period.

## **Hantera datumaxeln som Microsoft Excel**
Se följande kodexempel som skapar en ny Excel-fil och placerar diagramvärden i det första arket. 
Sedan lägger vi till ett diagram och ställer in typen för [**Axis**](https://reference.aspose.com/cells/javascript-cpp/axis/) 
till [**Axis.categoryType**](https://reference.aspose.com/cells/javascript-cpp/axis/#categoryType--) och ställer sedan in basenheterna till Dagar.

![todo:image_alt_text](excel.png)

## **Exempelkod**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Date Axis Chart Example</title>
    </head>
    <body>
        <h1>Date Axis Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, CategoryType, TimeUnit, ChartTextDirectionType, FillType } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Shortcut to cells collection
            const cells = worksheet.cells;

            // Add the sample values to cells
            cells.get("A1").value = "Date";

            // 14 means datetime format
            const style = cells.style;
            style.number = 14;

            // Put values to cells for creating chart
            const cellA2 = cells.get("A2");
            cellA2.style = style;
            cellA2.value = new Date(Date.UTC(2022, 5, 26));

            const cellA3 = cells.get("A3");
            cellA3.style = style;
            cellA3.value = new Date(Date.UTC(2022, 4, 22));

            const cellA4 = cells.get("A4");
            cellA4.style = style;
            cellA4.value = new Date(Date.UTC(2022, 7, 3));

            cells.get("B1").value = "Price";
            cells.get("B2").value = 40;
            cells.get("B3").value = 50;
            cells.get("B4").value = 60;

            // Add a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 9, 6, 21, 13);
            // Access the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
            // Converted setter to property assignment (range and boolean passed as array)
            chart.chartDataRange = ["A1:B4", true];

            // Set the Axis type to Date time
            chart.categoryAxis.categoryType = CategoryType.TimeScale;
            // Set the base unit for CategoryAxis to days
            chart.categoryAxis.baseUnitScale = TimeUnit.Days;
            // Set the direction for the axis text to be vertical
            chart.categoryAxis.tickLabels.directionType = ChartTextDirectionType.Vertical;
            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = FillType.None;
            // Set max value of Y axis.
            chart.valueAxis.maxValue = 70;
            // Set major unit.
            chart.valueAxis.majorUnit = 10;

            // Saving the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DateAxis.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
