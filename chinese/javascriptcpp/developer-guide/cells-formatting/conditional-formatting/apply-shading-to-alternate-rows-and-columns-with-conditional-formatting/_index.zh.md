---
title: 使用Aspose.Cells库在C#中应用条件格式阴影以交替显示行和列。通过调整这些条件，您可以更好地控制单元格的外观。
linktitle: 使用Aspose.Cells库在C#中应用条件格式阴影以交替显示行和列。通过调整这些条件，您可以更好地控制单元格的外观。
description: 如何通过 C++ 在 JavaScript 中使用 Aspose.Cells 库，为交替行列应用条件格式阴影。通过调整这些条件，您可以更好地控制单元格的外观。
keywords: Aspose.Cells、条件格式、通过 C++ 的 JavaScript、交替行、交替列、阴影
type: docs
weight: 30
url: /zh/javascript-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells API 提供了为 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 对象添加和操作条件格式规则的手段。这些规则可以根据条件或规则进行多样化，以达到所需的格式。本文将演示如何通过 C++ API 使用 Aspose.Cells for JavaScript，为交替行列应用阴影和条件格式规则，以及使用 Excel 的内置功能。

{{% /alert %}}

本文使用Excel内置函数，如ROW、COLUMN和MOD。以下是这些函数的一些详细信息，以便更好地理解提供的代码片段。

- **ROW()** 函数返回单元格引用的行号。如果省略引用参数，则假定引用为输入 ROW 函数的单元格地址。
- **COLUMN()** 函数返回单元格引用的列号。如果省略引用参数，则假定引用为输入 COLUMN 函数的单元格地址。
- **MOD()**函数返回一个数字被除数除后的余数，函数的第一个参数是要查找余数的数值，第二个参数是用来除以数值参数的数。如果除数为0，则会返回#DIV/0!错误。

让我们开始编写一些代码，利用 C++ API 通过 Aspose.Cells for JavaScript 实现这个目标。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Conditional Formatting</title>
    </head>
    <body>
        <h1>Conditional Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, Utils } = AsposeCells;

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
            // Create an instance of Workbook
            const book = new Workbook();

            // Access the first worksheet
            const sheet = book.worksheets.get(0);

            // Add FormatConditions to the instance of Worksheet
            let idx = sheet.conditionalFormattings.add();

            // Access the newly added FormatConditions via its index
            const conditionCollection = sheet.conditionalFormattings.get(idx);

            // Define a CellsArea on which conditional formatting will be applicable (A1 to I20)
            const area = CellArea.createCellArea("A1", "I20");

            // Add area to the instance of FormatConditions
            conditionCollection.addArea(area);

            // Add a condition to the instance of FormatConditions (Expression type)
            idx = conditionCollection.addCondition(AsposeCells.FormatConditionType.Expression);

            // Access the newly added FormatCondition via its index
            const formatCondition = conditionCollection.get(idx);

            // Set the formula for the FormatCondition
            formatCondition.formula1 = "=MOD(ROW(),2)=0";

            // Set the background color and pattern for the FormatCondition's Style
            formatCondition.style.backgroundColor = AsposeCells.Color.Blue;
            formatCondition.style.pattern = AsposeCells.BackgroundType.Solid;

            // Save the result and provide a download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


以下快照显示了加载到Excel应用程序中的结果电子表格。

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

为了将底纹应用于交替列，您只需将公式**=MOD(ROW(),2)=0**更改为**=MOD(COLUMN(),2)=0**，即不再获取行索引，而是修改公式以检索列索引。  
在这种情况下，生成的电子表格将如下所示。

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
