---
title: 在Aspose.Cells for JavaScript通过C++中使用FormulaText函数
linktitle: 在Aspose.Cells中使用FormulaText函数
description: 本文介绍了如何使用Aspose.Cells库中的FormulaText函数处理Microsoft Excel中的公式。学习如何获取和设置单元格的公式文本，以及使用JavaScript通过C++保存修改后的Excel文件。
keywords: Aspose.Cells，Excel，FormulaText函数，JavaScript通过C++
type: docs
weight: 60
url: /zh/javascript-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText是Excel 2013及更高版本中的函数，不支持Excel 2010或2007等早期版本。正如其名称所示，它打印给定单元格中存在的公式的文本。本文将向您展示如何使用Aspose.Cells for JavaScript通过C++利用此函数。

{{% /alert %}} 

以下示例代码展示了在Aspose.Cells for JavaScript通过C++中使用FormulaText的方法。代码首先在A1单元格写入公式，然后在A2单元格使用FormulaText打印公式文本。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - FormulaText</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put some formula in cell A1
            const cellA1 = worksheet.cells.get("A1");
            cellA1.formula = "=Sum(B1:B10)";

            // Get the text of the formula in cell A2 using FORMULATEXT function
            const cellA2 = worksheet.cells.get("A2");
            cellA2.formula = "=FormulaText(A1)";

            // Calculate the workbook
            workbook.calculateFormula();

            // Print the results of A2, It will now print the text of the formula inside cell A1
            console.log(cellA2.stringValue);

            resultDiv.innerHTML = `<p style="color: green;">Operation completed successfully! Formula text: ${cellA2.stringValue}</p>`;
        });
    </script>
</html>
```
## **控制台输出**


{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
