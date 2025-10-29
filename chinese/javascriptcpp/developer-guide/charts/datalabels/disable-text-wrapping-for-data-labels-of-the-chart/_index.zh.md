---
title: 使用 C++ 通过 JavaScript 禁用图表数据标签的文字换行
description: 学习如何在使用 Aspose.Cells for JavaScript 通过 C++ 绘制的图表中禁用数据标签的文字换行。本指南将展示如何防止长标签重叠，提供更清晰易读的图表显示。
keywords: Aspose.Cells for JavaScript 通过 C++、制图、数据标签、文字换行、重叠、易读性、显示。
type: docs
weight: 70
url: /zh/javascript-cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013允许用户在图表的数据标签中换行或取消换行。默认情况下，图表的数据标签中的文字是处于换行状态。

Aspose.Cells 提供一个 [**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#isTextWrapped--) 属性，您可以设置为 true 或 false 以分别启用或禁用数据标签的文本换行。

{{% /alert %}}

下面的代码示例显示了如何禁用图表数据标签的文字换行。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Data Label Text Wrapping</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by loading uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Disable the Text Wrapping of Data Labels in all Series
            chart.nSeries.get(0).dataLabels.isTextWrapped = false;
            chart.nSeries.get(1).dataLabels.isTextWrapped = false;
            chart.nSeries.get(2).dataLabels.isTextWrapped = false;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
