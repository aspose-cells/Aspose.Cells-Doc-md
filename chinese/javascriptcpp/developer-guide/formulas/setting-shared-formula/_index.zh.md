---
title: 通过JavaScript使用C++设置共享公式
linktitle: 设置共享公式
type: docs
weight: 10
url: /zh/javascript-cpp/setting-shared-formula/
---

{{% alert color="primary" %}}

如果你想在工作表中添加一个执行某些计算的函数，本文介绍如何使用C++的JavaScript实现此任务。

{{% /alert %}}

## 使用C++的JavaScript设置共享公式

假设您有一个填充有数据的工作表，格式如下所示的样本工作表。

|**带单列数据的输入文件**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

您希望在B2中添加一个函数，用于计算第一行数据的销售税。税率为**9%**。计算销售税的公式是：**"=A2*0.09"**。本文介绍了如何使用Aspose.Cells应用此公式。

Aspose.Cells允许您使用[**Cell.formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--)属性指定一个公式。有两种选项可用于将公式添加到列中的其他单元格（B3、B4、B5等等）。

或者像你为第一个单元格所做的那样，为每个单元格设置公式，并相应更新单元格引用（A3*0.09, A4*0.09, A5*0.09 等）。这需要逐行更新单元格引用，也需要 Aspose.Cells 逐个解析每个公式，对于大型表格或复杂公式会比较耗时，也会多出一些代码，虽然循环可以略微减少这些代码。

另一种方法是使用**共享公式**。使用共享公式，公式会自动更新每行的单元格引用，使得税款可以正确计算。这种[**Cell.sharedFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#sharedFormula-string-number-number-) 方法比第一种方法更有效。

以下示例演示了如何使用它。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Apply Shared Formula</title>
    </head>
    <body>
        <h1>Apply Shared Formula Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the cells collection in the first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Apply the shared formula in the range i.e., B2:B14
            const cell = cells.get("B2");
            // Converted setSharedFormula(...) to property assignment per universal rule.
            cell.sharedFormula = { formula: "=A2*0.09", rowCount: 13, columnCount: 1 };

            // Save the excel file and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shared formula applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
