---
title: 如何通过C++的JavaScript设置系列不可见
linktitle: 如何设置系列不可见
description: 了解如何在Excel图表中使用Aspose.Cells for JavaScript通过C++设置系列不可见。 
keywords: 利用C++的JavaScript实现Excel图表系列、隐藏、是否过滤。
type: docs
weight: 74
url: /zh/javascript-cpp/how-to-set-series-invisible/
---

## 如何在Excel图表中设置系列不可见

在Excel图表中，你可以右键点击图表，选择"选择数据"，在弹出窗口中，通过勾选或取消勾选系列来设置是否显示该系列。你可以下载下面的[示例文件](SeriesFiltered.xlsx)，在Excel中操作实现此功能。接下来，我们将告诉你如何使用Aspose.Cells库实现此功能。

![todo:image_alt_text](series-invisible.png)

## 如何使用Aspose.Cells设置系列不可见 

我们使用以下代码来将系列设置为不可见：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Modify Chart Series Color Variation</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet and its charts
            const charts = workbook.worksheets.get(0).charts;
            const chart = charts.get("Chart 1");

            // Access filtered NSeries and NSeries collections (properties instead of getters)
            const nSeriesFiltered = chart.filteredNSeries;
            const nSeries = chart.nSeries;

            // Set IsColorVaried on series (converted from setIsColorVaried to property assignment)
            nSeries.get(1).isColorVaried = true;
            nSeries.get(0).isColorVaried = true;

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

你可以获取以下[输入文件](SeriesFiltered.xlsx)和[输出文件](output.xlsx)。

如下图所示，原本可见的前两个系列在输出文件中变成了隐藏。
![todo:image_alt_text](output.png)
