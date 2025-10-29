---
title: 创建分类汇总
type: docs
weight: 800
url: /zh/javascript-cpp/creating-subtotals/
description: 学习如何使用Aspose.Cells for Java脚本通过C++ API为任何重复值创建小计。
keywords: 应用小计、设置小计、添加小计、创建小计、如何向工作表添加小计 
---

{{% alert color="primary" %}}

你可以自动为工作表中的任何重复值添加小计。Aspose.Cells for Java脚本通过C++提供了帮助你以编程方式添加小计的API功能。

{{% /alert %}}

## **使用Microsoft Excel**

在Microsoft Excel中添加小计：

1. 在工作簿的第一个工作表中创建一个简单的数据列表（如下图所示），并将文件保存为 Book1.xls。
1. 选择列表中的任何单元格。
1. 从**数据**菜单中选择**小计**。将显示小计对话框。定义要使用的函数和放置小计的位置。

## **使用Aspose.Cells for Java脚本通过C++ API**

Aspose.Cells for Java脚本通过C++提供了一个类，[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)，表示一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)类包含一个[**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)集合，允许访问Excel文件中的各个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类表示。该类提供了丰富的属性和方法，用于管理工作表及其他对象。每个工作表由[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)集合组成。要在工作表中添加小计，使用[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)类的[**subtotal**](https://reference.aspose.com/cells/javascript-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-)方法。传递参数值以指定小计的计算和放置方式。

在下面的示例中，我们使用Aspose.Cells for Java脚本通过C++ API在第一个工作表中添加了小计。当代码执行后，将创建一个带有小计的工作表。

以下的代码片段展示了如何使用Aspose.Cells for Java脚本通过C++向工作表添加小计。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Subtotal Example</h1>
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

            // Instantiate a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the Cells collection in the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Create a cellarea i.e., B3:C19
            const ca = new AsposeCells.CellArea();
            ca.startRow = 2;
            ca.startColumn = 1;
            ca.endRow = 18;
            ca.endColumn = 2;

            // Apply subtotal, the consolidation function is Sum and it will be applied to
            // Second column (C) in the list
            cells.subtotal(ca, 0, AsposeCells.ConsolidationFunction.Sum, [1]);

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Subtotal applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
