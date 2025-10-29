---
title: 将文本数值数据转换为数字
type: docs
weight: 900
url: /zh/javascript-cpp/convert-text-numeric-data-to-number/
description: 学习如何通过Aspose.Cells for Java脚本通过C++ API将Excel中存储为文本的数字转换为数字。
keywords: Excel将文本转换为数字，Excel将文本转换为数字JavaScript代码，Excel将数字文本数据转换为数字，Excel将数字文本数据转换为数字JavaScript代码，Excel将数字文本转换为数字，Excel将数字文本转换为数字JavaScript代码，用JavaScript代码将数字文本转换为数字，在Excel中用JavaScript代码将数字文本转换为数字，将数字字符串转换为数字在Excel中使用JavaScript代码转换数字文本，Excel将文本数字数据转换为数字JavaScript代码，将数字字符串转换为数字JavaScript代码
---

## **可能的使用场景**
有时，你想将输入为文本的数字数据转换为数字。你可以在Microsoft Excel中通过在数字前放一个撇号（例如**'12345**）来将数字作为文本输入。这样，Excel会将数字视为字符串。Aspose.Cells for Java脚本通过C++允许你将字符串转换为数字。


## 如何将 Excel 中存储为文本的数字转换为数字
您可以按照以下几个简单步骤将存储为文本的数字转换为数字。
1. 选择任何一个具有左上角错误指示器的单元格或单元格范围。
1. 在所选单元格或单元格范围旁边，单击出现的错误按钮。在菜单上，单击转换为数字。 
<br>
<img src="4.png" width=70% />
1. 如果警报按钮不可用，请选择具有此问题的列。如果您不想转换整个列，可以选择一个或多个单元格。只需确保您选择的单元格在同一列中，否则此过程将无法工作。文本到列按钮通常用于拆分列，但也可以用于将单个文本列转换为数字。在数据选项卡上，单击文本到列。
<br>
<img src="1.png" width=70% />
1. 在弹出框中单击完成按钮。
<br>
<img src="2.png" width=70% />
1. 存储为文本的数字已转换为数字。
<br>
<img src="3.png" width=70% />

## 如何使用Aspose.Cells for Java脚本通过C++将存储为文本的数字转换为数字
Aspose.Cells for Java脚本通过C++提供了[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/javascript-cpp/cells/#convertStringToNumericValue--)方法，可用于将所有字符串或文本数字数据转换为数字。

以下截图显示了单元格**A1:A17**中的字符串数字。字符串数字对齐到左边。
<br>
<img src="5.png" width=70% />

这些字符串数字已经使用[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/javascript-cpp/cells/#convertStringToNumericValue--) 转换为数字，如下面的截图所示。您可以看到，它们现在是右对齐的。
<br>
<img src="6.png" width=70% />

## 将字符串数字数据转换为实际数字的JavaScript代码

以下示例代码说明了如何在所有工作表中将所有字符串数值数据转换为实际数值。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Strings to Numeric Values in All Sheets</h1>
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

            // Instantiate workbook object with the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access worksheets collection
            const sheets = workbook.worksheets;
            const sheetcount = sheets.count;

            // Iterate through all worksheets and convert strings to numeric values
            for (let i = 0; i < sheetcount; i++) {
                const sheet = sheets.get(i);
                sheet.cells.convertStringToNumericValue();
            }

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
