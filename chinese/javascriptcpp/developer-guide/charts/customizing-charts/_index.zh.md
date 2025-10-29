---
title: 用JavaScript通过C++自定义图表
linktitle: 自定义图表
description: 学习如何在Aspose.Cells for Java脚本通过C++中自定义图表。我们的指南将向你展示如何修改图表布局、添加和格式化数据系列、调整轴以及应用各种格式选项，以提升图表的外观和易用性。
keywords: Aspose.Cells for Java脚本通过C++，绘图，自定义，布局，数据系列，轴，格式，外观，易用性。
type: docs
weight: 40
url: /zh/javascript-cpp/customizing-charts/
---

## **创建自定义图表**  

到目前为止，我们在讨论图表时，常常关注具有标准格式设置的标准图表。我们只定义数据源，设置一些属性，图表便会以默认格式创建。但Aspose.Cells API还支持创建自定义图表，允许开发者使用自定义格式设置来创建图表。  

开发人员可以使用Aspose.Cells在运行时创建自定义图表。  

图表由数据系列组成。Aspose.Cells中的每个数据系列由[**Series**](https://reference.aspose.com/cells/javascript-cpp/series)对象表示，而[**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection)对象作为[**Series**](https://reference.aspose.com/cells/javascript-cpp/series)对象的集合。当创建定制图表时，开发者可以自由地为不同的数据系列（收集在[**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection)对象中）使用不同类型的图表。  

下面的示例代码演示了如何创建自定义图表。在此示例中，我们将为第一个数据系列使用柱形图，为第二个系列使用折线图。结果是，我们在工作表中添加了一个柱形图，结合了一条折线图。  

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

目前，Aspose.Cells仅支持结合饼图、折线图、柱状图和堆积柱状图的自定义图表，但未来版本将支持更多图表类型。  

{{% /alert %}}
