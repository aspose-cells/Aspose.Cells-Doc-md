---
title: JavaScript与C++中的Z轴
description: 了解如何使用Aspose.Cells for Java脚本通过C++处理Z轴。我们的指南将帮助您理解如何配置和自定义Z轴，包括其刻度和标签，以增强您的图表效果。
keywords: Aspose.Cells for Java脚本通过C++实现的Z轴，图表，配置，定制，刻度，标签。
type: docs
weight: 210
url: /zh/javascript-cpp/z-axis/
---

## **可能的使用场景**
对于一些3D图表，如3D柱状图、3D锥体或3D金字塔，它们具有深度（系列）轴，也称为Z轴，可以进行调整。你可以指定刻度间隔、轴标签和其他操作。

## **像微软Excel一样处理主轴和次轴**
请查看以下示例代码，创建一个新Excel文件并将图表数值放在第一个工作表。然后添加图表并设置图表类型为Column3D，你也可以看到Z轴（深度轴）。 

![todo:image_alt_text](excel.png)

## **示例代码**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Example (ZAxis)</h1>
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

            // Put values to cells for creating chart
            worksheet.cells.get("A1").value = "A";
            worksheet.cells.get("B1").value = "B";
            worksheet.cells.get("C1").value = "C";
            worksheet.cells.get("A2").value = 2;
            worksheet.cells.get("A3").value = 1;
            worksheet.cells.get("B2").value = 2;
            worksheet.cells.get("B3").value = 3;
            worksheet.cells.get("C2").value = 2;
            worksheet.cells.get("C3").value = 3;

            // Add a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column3D, 9, 6, 25, 16);
            // Access the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);
            // Calculate the chart
            chart.calculate();
            // Add SeriesCollection (chart data source) to the chart ranging from "A2" cell to "C3"
            chart.setChartDataRange("A2:C3", true);
            // Hide the CategoryAxis axis
            chart.categoryAxis.isVisible = false;
            // Hide the ValueAxis axis
            chart.valueAxis.isVisible = false;

            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ZAxis.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
