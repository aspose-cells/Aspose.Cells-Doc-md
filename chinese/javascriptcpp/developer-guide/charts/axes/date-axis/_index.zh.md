---
title: 用JavaScript通过C++管理日期轴
description: 学习如何在Aspose.Cells for JavaScript中通过C++管理日期轴。我们的指南将帮助您理解如何处理各种日期格式、时间比例和刻度标签频率。
keywords: Aspose.Cells for JavaScript via C++，日期轴，管理，日期格式，时间比例，刻度标签频率。
type: docs
weight: 200
url: /zh/javascript-cpp/date-axis/
---

## **可能的使用场景**
当你用日期数据创建图表，并且日期沿水平（类别）轴绘制时，Aspose.Cells for JavaScript通过C++会自动将类别轴更改为日期（时间尺度）轴。
日期轴以特定间隔或基本单位（例如天数、月份或年份）按年代顺序显示日期，即使工作表上的日期不是按顺序或基本单位相同。
 默认情况下，Aspose.Cells根据工作表数据中两个日期之间的最小差异确定日期轴的基本单位。例如，如果你的数据为股票价格，两个日期间的最小差异为七天，Excel会将基本单位设为天，但你可以将基本单位改为月或年，以观察股票在较长时间段内的表现。

## **处理日期轴就像处理Microsoft Excel一样**
请参阅以下示例代码，此代码创建一个新的Excel文件并将图表的值放在第一个工作表中。 
然后，我们添加一个图表并设置[**Axis**](https://reference.aspose.com/cells/javascript-cpp/axis/)的类型 
到[**Axis.categoryType**](https://reference.aspose.com/cells/javascript-cpp/axis/#categoryType--)，然后将基本单位设置为天数。

![todo:image_alt_text](excel.png)

## **示例代码**
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
