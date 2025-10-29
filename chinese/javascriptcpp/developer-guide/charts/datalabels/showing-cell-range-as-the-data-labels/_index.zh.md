---
title: 使用 JavaScript 通过 C++ 将单元格范围显示为数据标签
linktitle: 将单元格范围显示为数据标签
description: 学习如何在图表中使用 Aspose.Cells for JavaScript 通过 C++ 显示单元格范围作为数据标签。我们的指南将演示如何将标签链接到数据源，并进行格式化，以在图表中提供准确且有意义的信息。
keywords: Aspose.Cells for JavaScript 通过 C++，绘图，数据标签，单元格范围，数据源，格式化，准确性，有意义的信息。
type: docs
weight: 130
url: /zh/javascript-cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}
在 Microsoft Excel 2013 中，你可以显示数据标签的单元格范围。Aspose.Cells for JavaScript 通过 C++ 支持此功能。
{{% /alert %}}

## **复选框显示单元格范围作为数据标签**

在Microsoft Excel中显示单元格范围作为数据标签：

1. 选择系列数据标签，右键单击以打开上下文菜单。  
1. 选择**格式数据标签**。标签选项会显示。  
1. 选择或清除选项 **标签包含 - 来自单元格的值**。  

以下示例代码访问图表系列数据标签并将 [**DataLabels.showCellRange**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#showCellRange--) 属性设置为 **true** ，以选择 **标签包含-来自单元格的值** 选项。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Show Range in Data Labels</title>
    </head>
    <body>
        <h1>Show Range in Data Labels Example</h1>
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

            // Create workbook from the source Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Check the "Label Contains - Value From Cells"
            const dataLabels = chart.nSeries.get(0).dataLabels;
            dataLabels.showCellRange = true;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
