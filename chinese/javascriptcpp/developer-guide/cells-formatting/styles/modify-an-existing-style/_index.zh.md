---
title: 修改现有风格
linktitle: 修改现有风格
description: Aspose.Cells是一个JavaScript/C++库，用于处理电子表格文件，允许用户修改现有单元格样式。本文介绍如何使用Aspose.Cells库修改现有单元格样式，以满足不同的外观需求。
keywords: 修改现有样式，自定义应用程序的外观，指南，教程，帮助文档，开发文档，API参考，示例代码，下载，支持。
type: docs
weight: 90
url: /zh/javascript-cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

要将相同的格式选项应用于单元格，请创建一个新的格式样式对象。格式样式对象是格式特性的组合，如字体、字体大小、缩进、数字、边框、模式等，命名并存储为一组。应用时，该样式中的所有格式都会被应用。

您也可以使用现有的样式，将其与工作簿一起保存，并使用其格式化具有相同属性的信息。

当单元格没有明确格式化时，将应用**普通**样式（工作簿的默认样式）。除了普通样式之外，Microsoft Excel还预定义了几种样式，包括逗号、货币和百分号。

Aspose.Cells允许修改任何这些样式或您使用所需属性定义的任何其他样式。

{{% /alert %}}

## **使用Microsoft Excel**

更新Microsoft Excel 97-2003中的样式：

1. 单击**格式**菜单上的**样式**。
1. 从**样式名称**列表中选择要修改的样式。
1. 单击**修改**。
1. 使用格式单元格对话框中的选项卡选择要使用的样式选项。
1. 点击**确定**。
1. 在**样式包括**下，指定您想要的样式特征。
1. 单击**确定**以保存样式并将其应用于所选范围。

## **使用 Aspose.Cells for JavaScript 通过 C++**

以下示例演示了如何使用[**Style.update()**](https://reference.aspose.com/cells/javascript-cpp/style/#update--)方法。

### **创建和修改样式**

此示例创建一个 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象，将其应用于一块区域的单元格，并修改 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象。所做的更改会自动应用到单元格及其所应用的区域。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Style Example</h1>
        <p>Select an existing Excel file to modify or leave empty to create a new workbook.</p>
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
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            // Instantiate workbook from uploaded file or create a new one
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create a new style object.
            const style = workbook.createStyle();

            // Set the number format.
            style.number = 14;

            // Set the font color to red color.
            style.font.color = AsposeCells.Color.Red;

            // Name the style.
            style.name = "Date1";

            // Get the first worksheet cells.
            const cells = workbook.worksheets.get(0).cells;

            // Specify the style (described above) to A1 cell.
            const cellA1 = cells.get("A1");
            cellA1.style = style;

            // Create a range (B1:D1).
            const range = cells.createRange("B1", "D1");

            // Initialize styleflag object.
            const flag = new AsposeCells.StyleFlag();

            // Set all formatting attributes on.
            flag.all = true;

            // Apply the style (described above) to the range.
            range.applyStyle(style, flag);

            // Modify the style (described above) and change the font color from red to black.
            style.font.color = AsposeCells.Color.Black;

            // Done! Since the named style (described above) has been set to a cell and range, 
            // The change would be reflected(new modification is implemented) to cell(A1) and 
            // Range (B1:D1).
            style.update();

            // Save the excel file. 
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book_styles.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


### **修改现有样式**

此示例使用一个简单的模板Excel文件，其中已经应用了一个名为“Percent”的样式到一个范围中。该示例：

1. 获取样式，
1. 创建一个样式对象，并
1. 修改样式格式。

修改将自动应用于应用了样式的范围。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Named Style Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color, Utils } = AsposeCells;

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

            // Create a workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the named style "Percent" via the styles collection
            const style = workbook.styles.get("Percent");

            // Change the number format to "0.00%".
            style.number = 11;

            // Set the font color.
            style.font.color = Color.Red;

            // Update the style so ranges using this named style are updated.
            style.update();

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book2.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Style updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
