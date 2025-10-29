---
title: 在工作表中应用条件格式
linktitle: 在工作表中应用条件格式
description: 如何在JavaScript via C++中使用Aspose.Cells库在工作表中应用条件格式，以更好地控制单元格的外观。
keywords: Aspose.Cells，条件格式，JavaScript via C++，工作表，格式设置
type: docs
weight: 130
url: /zh/javascript-cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

本文旨在详细介绍如何向工作表的一系列单元格添加条件格式。

条件格式是Microsoft Excel中的一个高级功能，允许您对一系列单元格应用格式，并且根据单元格的值或公式的值进行格式更改。例如，单元格的背景可能显示为红色以突出显示负值，或者正值的文字颜色可能为绿色。当单元格的值满足格式条件时，将应用格式。如果单元格的值不满足格式条件，则使用单元格的默认格式。

使用Microsoft Office Automation可以应用条件格式，但这有其缺点。涉及几个原因和问题：例如，安全性，稳定性，可扩展性和速度。寻找另一个解决方案的主要原因是，Microsoft本身强烈建议不要在软件解决方案中使用Office Automation。

本文展示了如何创建一个网页应用程序，使用 Aspose.Cells API 用最简单的几行代码在单元格上添加条件格式。

{{% /alert %}}

## **使用Aspose.Cells根据单元格值应用条件格式**

1. **下载并安装Aspose.Cells**。
   1. 通过 C++ 下载 Aspose.Cells for JavaScript。
1. 在您的开发计算机上安装它。
   所有Aspose组件在安装后都处于评估模式。评估模式没有时间限制，只会在生成的文档中插入水印。
1. **创建一个项目**。
   开始你的 JavaScript 项目，初始化它。本例演示在浏览器基础的 web 应用中的使用。
1. **添加引用**。
   向你的项目中添加对 Aspose.Cells 的引用，例如通过包含如下库：
   ```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Conditional Formatting Example</title>
    </head>
    <body>
        <h1>Apply Conditional Formatting Based on Cell Value</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FormatConditionType, OperatorType, CellArea, Color } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add conditional formatting collection
            const cfCollection = worksheet.conditionalFormattings;
            const idx = cfCollection.add();
            const formatConditionCollection = cfCollection.get(idx);

            // Define the cell area to apply conditional formatting (A1)
            const area = CellArea.createCellArea(0, 0, 0, 0); // fromRow, fromCol, toRow, toCol
            formatConditionCollection.addArea(area);

            // Add a condition: Cell Value > 100
            const conditionIndex = formatConditionCollection.addCondition(
                FormatConditionType.CellValue,
                OperatorType.Greater,
                "100",
                null
            );

            const formatCondition = formatConditionCollection.get(conditionIndex);

            // Modify the style for the condition: bold and red font
            const style = formatCondition.style;
            if (!style.font) {
                style.font = {};
            }
            style.font.bold = true;
            style.font.color = Color.fromArgb(255, 255, 0, 0); // ARGB red

            // Assign modified style back (property assignment pattern)
            formatCondition.style = style;

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'conditional_formatting_result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied to cell A1 (value &gt; 100). Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

 执行上述代码时，将在输出文件（output.xls）第一个工作表的“A1”单元格应用条件格式。所应用的条件格式取决于单元格值。如果A1单元格的值在50到100之间，则背景色由于条件格式而变成红色。

## **使用Aspose.Cells根据公式应用条件格式**

1.根据公式应用条件格式（代码片段）
   以下是完成任务的代码。它在B3上应用条件格式。
