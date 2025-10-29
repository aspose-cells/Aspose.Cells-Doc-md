---
title: 使用 JavaScript 通过 C++ 合并和拆分单元格
linktitle: 合并和分割单元格
description: Aspose.Cells 是一个用于处理电子表格文件的 JavaScript 库，支持合并和拆分单元格。本文将介绍如何使用 Aspose.Cells 库合并和拆分单元格，并提供自定义合并单元格样式的选项。
keywords: Aspose.Cells，JavaScript库，电子表格，合并单元格，拆分单元格，样式设置，自定义样式
type: docs
weight: 190
url: /zh/javascript-cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells支持此功能，还可以在工作表中合并单元格。您还可以取消合并或拆分合并的单元格。合并单元格的单元格引用是原始选择范围中左上角单元格的引用。

{{% /alert %}} 
## **介绍**
并非总是希望每行或每列中都有相同数量的单元格。例如，您可能希望在一个跨越多个列的单元格中放置标题。或者，如果创建发票，则可能希望总计列中的列数较少。将两个或多个单元格合并成一个单元格，以实现此目的。Microsoft Excel允许用户选择文件并将其合并以按照自己的方式构造电子表格。

{{% alert color="primary" %}} 

注意在合并单元格时，只会保留左上角单元格的数据。如果区域内的其他单元格中有数据，这些数据会被删除。同样，格式也基于参考单元格，因此在合并单元格时，应用于合并区域左上角单元格的格式设置将被应用于合并后的单元格。拆分时，新单元格保持其原有格式设置。

{{% /alert %}} 
## **在工作表中合并单元格**
### **在Microsoft Excel中合并单元格**
以下步骤描述如何在MS Excel中合并工作表中的单元格。

1. 将要复制的数据复制到范围内左上角的单元格中。
1. 选择要合并的单元格。
1. 要合并行或列中的单元格并将单元格内容居中，点击**合并和居中**图标上的**格式**工具栏。

### **使用Aspose.Cells合并单元格**
Aspose.Cells.Cells类具有一些实用的方法，例如`merge()`方法，可以将指定区域内的单元格合并为一个单元格。

以下示例显示了如何在工作表中合并单元格（C6:E7）。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merging Cells Example</h1>
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
            // Create a Workbook.
            const wbk = new Workbook();

            // Create a Worksheet and get the first sheet.
            const worksheet = wbk.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Merge some Cells (C6:E7) into a single C6 Cell.
            cells.merge(5, 2, 2, 3);

            // Input data into C6 Cell.
            const cell = cells.get(5, 2);
            cell.value = "This is my value";

            // Create a Style object to fetch the Style of C6 Cell.
            const style = cell.style;

            // Create a Font object
            const font = style.font;

            // Set the name.
            font.name = "Times New Roman";

            // Set the font size.
            font.size = 18;

            // Set the font color
            font.color = AsposeCells.Color.Blue;

            // Bold the text
            font.isBold = true;

            // Make it italic
            font.isItalic = true;

            // Set the background color of C6 Cell to Red
            style.foregroundColor = AsposeCells.Color.Red;
            style.pattern = AsposeCells.BackgroundType.Solid;

            // Apply the Style to C6 Cell.
            cell.style = style;

            // Saving the Workbook and providing download link
            const outputData = wbk.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **取消合并（拆分）合并的单元格**
### **使用Microsoft Excel**
以下是使用Microsoft Excel拆分合并单元格的步骤。

1. 选择已合并的单元格。
   当单元格已合并时，在**格式**工具栏上选择**合并和居中**。
1. 在**格式**工具栏上点击**合并和居中**。

### **使用Aspose.Cells**
Aspose.Cells.Cells类具有名为`unmerge()`的方法，可以将合并的单元格拆分回原始状态。该方法通过合并单元格范围的引用进行拆分。

以下示例显示了如何拆分合并的单元格（C6）。该示例使用上一个示例中创建的文件，并拆分了合并的单元格。

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Unmerge Cells Example</title>
    </head>
    <body>
        <h1>Unmerge Cells Example</h1>
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

            // Create a Workbook by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheet and get the first sheet.
            const worksheet = workbook.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Unmerge the cells at row 5, column 2 spanning 2 rows and 3 columns
            cells.unMerge(5, 2, 2, 3);

            // Save the file and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'unmergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Cells unmerged successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **高级主题**
- [在工作表中检测合并的单元格](/cells/zh/javascript-cpp/detect-merged-cells-in-a-worksheet/)
