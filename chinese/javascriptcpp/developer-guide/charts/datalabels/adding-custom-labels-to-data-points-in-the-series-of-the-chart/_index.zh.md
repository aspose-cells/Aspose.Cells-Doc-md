---
title: 通过 C++ 在图表系列的数据显示点中添加自定义标签
linktitle: 向图表系列的数据点添加自定义标签
description: 学习如何使用 Aspose.Cells for JavaScript 通过 C++ 在图表系列数据点中添加自定义标签。本指南将演示如何修改标签的外观、位置和格式，同时将它们与您的数据源关联以确保准确展示。
keywords: Aspose.Cells for JavaScript 通过 C++、制图、自定义标签、数据点、系列、外观、位置、格式、数据源、表现。
type: docs
weight: 100
url: /zh/javascript-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/
---

{{% alert color="primary" %}}

您可以向图表系列的数据点添加自定义标签。Aspose.Cells提供了[**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--)属性以添加这些自定义标签。本文将解释如何使用此属性向图表系列的数据点添加自定义标签。

{{% /alert %}}

以下代码创建了**用数据标记连接的散点图**，并向**系列**的**数据点**添加了**自定义标签**，每个标签显示**系列名称**和**点名称**。你可以用任何其他文字替代。

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Put data
            sheet.cells.get(0, 0).value = 1;
            sheet.cells.get(0, 1).value = 2;
            sheet.cells.get(0, 2).value = 3;

            sheet.cells.get(1, 0).value = 4;
            sheet.cells.get(1, 1).value = 5;
            sheet.cells.get(1, 2).value = 6;

            sheet.cells.get(2, 0).value = 7;
            sheet.cells.get(2, 1).value = 8;
            sheet.cells.get(2, 2).value = 9;

            // Generate the chart
            const chartIndex = sheet.charts.add(ChartType.ScatterConnectedByLinesWithDataMarker, 5, 1, 24, 10);
            const chart = sheet.charts.get(chartIndex);

            chart.title.text = "Test";
            chart.categoryAxis.title.text = "X-Axis";
            chart.valueAxis.title.text = "Y-Axis";

            chart.nSeries.categoryData = "A1:C1";

            // Insert series 1
            chart.nSeries.add("A2:C2", false);

            let series = chart.nSeries.get(0);

            let pointCount = series.points.count;
            for (let i = 0; i < pointCount; i++) {
                const pointIndex = series.points.get(i);
                pointIndex.dataLabels.text = "Series 1" + "\n" + "Point " + i;
            }

            // Insert series 2
            chart.nSeries.add("A3:C3", false);

            series = chart.nSeries.get(1);

            pointCount = series.points.count;
            for (let i = 0; i < pointCount; i++) {
                const pointIndex = series.points.get(i);
                pointIndex.dataLabels.text = "Series 2" + "\n" + "Point " + i;
            }

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
