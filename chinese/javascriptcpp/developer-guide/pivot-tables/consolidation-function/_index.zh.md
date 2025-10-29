---
title: 合并函数
type: docs
weight: 20
url: /zh/javascript-cpp/consolidation-function/
description: 如何用Aspose.Cells for Java脚本通过C++将合并函数应用到数据透视表的数据字段。
keywords: Aspose.Cells for Java脚本通过C++，Excel JavaScript库，使用Aspose.Cells for Java脚本通过C++将合并函数应用到数据透视表的数据字段。
---

## **合并函数**

Aspose.Cells for Java脚本通过C++可以用来对数据透视表的值字段（数据字段）应用合并函数。在Microsoft Excel中，你可以右键点击值字段，然后选择**值字段设置...**，再切换到**汇总值方式**标签，从中选择任何你喜欢的合并函数，比如求和、计数、平均值、最大值、最小值、乘积、不重复计数等。

Aspose.Cells for Java脚本通过C++提供[**ConsolidationFunction**](https://reference.aspose.com/cells/javascript-cpp/consolidationfunction/)枚举，以支持以下合并函数。

- ConsolidationFunction.Average
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums
- ConsolidationFunction.DistinctCount
- ConsolidationFunction.Max
- ConsolidationFunction.Min
- ConsolidationFunction.Product
- ConsolidationFunction.StdDev
- ConsolidationFunction.StdDevp
- ConsolidationFunction.Sum
- ConsolidationFunction.Var
- ConsolidationFunction.Varp

## **如何使用Aspose.Cells for Java脚本通过C++将合并函数应用到数据透视表的数据字段**

以下代码将**平均值**整合函数应用于第一个数据字段（或数值字段），将**不重复计数**整合函数应用于第二个数据字段（或数值字段）。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PivotTable Consolidation Function</title>
    </head>
    <body>
        <h1>Apply Consolidation Function to PivotTable</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet of the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access the first pivot table of the worksheet
            const pivotTable = worksheet.pivotTables.get(0);

            // Apply Average consolidation function to first data field
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Average;

            // Apply DistinctCount consolidation function to second data field
            pivotTable.dataFields.get(1).function = AsposeCells.ConsolidationFunction.DistinctCount;

            // Calculate the data to make changes affect
            pivotTable.calculateData();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PivotTable consolidation functions applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Microsoft Excel 2013仅支持DISTINCT_COUNT合并函数。

{{% /alert %}}
