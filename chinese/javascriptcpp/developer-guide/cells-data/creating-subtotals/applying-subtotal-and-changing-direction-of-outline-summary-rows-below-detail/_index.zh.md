---
title: 应用小计并更改大纲摘要行的方向，而不是详细信息下面的行
type: docs
weight: 100
url: /zh/javascript-cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: 学习如何使用Aspose.Cells for JavaScript通过C++应用小计并更改详细内容下的轮廓摘要行的方向。
keywords: 应用小计，添加小计，更改详细下面概要行的方向，更改详细右边概要列的方向，创建小计并更改详细下面概要行的方向
---

{{% alert color="primary" %}}

本文将解释如何对数据应用小计并更改大纲摘要行下面的方向。

你可以使用[**Worksheet.cells.subtotal()**](https://reference.aspose.com/cells/javascript-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-boolean-boolean-boolean-)方法对数据应用小计。它接受以下参数。

- **单元格区域** - 应用小计的范围
- **按组** - 按零为基础的整数偏移量分组
- **功能** - 小计功能。
- **TotalList** - 一个从零开始的字段偏移量数组，指示要添加小计的字段。
- **Replace** - 指示是否替换当前的小计
- **分页符** - 表示是否在组之间添加分页符
- **SummaryBelowData** - 指示是否在数据下方添加摘要。

此外，您可以使用 Worksheet.Outline.SummaryRowBelow 属性，在下图所示的 Microsoft Excel 中通过“数据 > 大纲 > 设置”来控制大纲摘要行在细节下方的方向。

![todo:image_alt_text](1.png)

{{% /alert %}}

## 源文件和输出文件的图像

下图显示了示例代码中使用的源Excel文件，其中包含列A和B中的一些数据。

![todo:image_alt_text](2.png)

下图显示了示例代码生成的输出Excel文件。如您所见，对范围A2:B11应用了小计，并且大纲的方向是细节下方的摘要行。

![todo:image_alt_text](3.png)

## JavaScript应用小计和更改大纲摘要行的方向



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Subtotal Example</title>
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
        const { Workbook, SaveFormat, CellArea, ConsolidationFunction, Utils } = AsposeCells;

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

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the Cells collection in the first worksheet
            const cells = worksheet.cells;

            // Create a cellarea i.e., A2:B11
            const ca = CellArea.createCellArea("A2", "B11");

            // Apply subtotal, the consolidation function is Sum and it will applied to Second column (B) in the list
            cells.subtotal(ca, 0, ConsolidationFunction.Sum, [1], true, false, true);

            // Set the direction of outline summary
            worksheet.outline.summaryRowBelow = true;

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Subtotal applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
