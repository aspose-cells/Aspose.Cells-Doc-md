---
title: 用JavaScript通过C++设置图表系列的值格式代码
description: 学习如何在Aspose.Cells for Java脚本通过C++中设置图表系列的值格式代码。本指南将帮助您理解如何使用合适的格式代码格式化图表系列数据，从而专业、准确地展示数据。
keywords: Aspose.Cells for Java脚本通过C++实现的图表系列，值格式代码，格式化，数据展示，准确性，专业性。
linktitle: 数字格式
type: docs
weight: 100
url: /zh/javascript-cpp/set-the-values-format-code-of-chart-series/
---

## **可能的使用场景**
您可以使用[Series.valuesFormatCode](https://reference.aspose.com/cells/javascript-cpp/series/#valuesFormatCode--)属性设置图表系列的值格式代码。此属性不仅适用于基于工作表范围的系列，也适用于使用值数组创建的系列。

## **设置图表系列的值格式代码**
以下示例代码在之前没有系列的空白图表中添加系列。它使用值数组添加系列，并用[Series.valuesFormatCode](https://reference.aspose.com/cells/javascript-cpp/series/#valuesFormatCode--)属性将格式设为$#,##0，数字10000将显示为$10,000。截图显示了代码在[示例Excel文件](51740712.xlsx)和[输出Excel文件](51740713.xlsx)执行后的效果。

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **示例代码**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Series Example</h1>
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

                // Access first worksheet
                const worksheet = workbook.worksheets.get(0);

                // Access first chart
                const chart = worksheet.charts.get(0);

                // Add series using an array of values
                chart.nSeries.add("{10000, 20000, 30000, 40000}", true);

                // Access the series and set its values format code
                const series = chart.nSeries.get(0);
                series.valuesFormatCode = "$#,##0";

                // Saving the modified Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = '51740713.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Modified Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```
