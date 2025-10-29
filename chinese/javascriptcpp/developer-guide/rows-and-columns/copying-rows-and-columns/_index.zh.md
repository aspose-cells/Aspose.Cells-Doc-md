---
title: 使用JavaScript通过C++复制行和列。
linktitle: 复制行和列
type: docs
weight: 40
url: /zh/javascript-cpp/copying-rows-and-columns/
description: 本文介绍如何通过Aspose.Cells for JavaScript通过C++ API复制行和列。
keywords: JavaScript通过C++，如何复制行和列，复制JavaScript中的行，使用JavaScript复制列，如何使用Aspose.Cells for JavaScript通过C++粘贴行和列，粘贴多行多列，如何复制粘贴单行或单列。
---

## **介绍**  

有时，您需要在不复制整个工作表的情况下复制工作表中的行和列。使用Aspose.Cells，可以在工作簿内部或工作簿之间复制行和列。  
复制行（或列）时，其中包含的数据，包括更新的引用的公式和值，注释，格式，隐藏单元格，图像以及其他绘图对象也会被复制。  

## **使用Microsoft Excel如何复制行和列**  

1. 选择要复制的行或列。  
1. 要复制行或列，请单击 **标准** 工具栏上的 **复制**，或按 **CTRL**+**C**。  
1. 选择要复制所选内容下方或右侧的行或列。  
1. 复制行或列时，单击 **已复制的单元格** 在 **插入** 菜单上。  

{{% alert color="primary" %}}  
如果您在**标准**工具栏上单击**粘贴**，或者按**Ctrl**+**V**键，而不是在**插入**菜单上单击命令，则目标单元格的任何内容都将被替换。  
{{% /alert %}}  

## **如何使用Microsoft Excel的粘贴选项粘贴行和列**  

1. 选择包含您要复制的数据或其他属性的单元格。  
1. 在主页选项卡上，单击**复制**。  
1. 单击要在其中**粘贴**所复制内容的区域中的第一个单元格。  
1. 在主页选项卡上，单击**粘贴**旁边的箭头，然后选择**粘贴**特殊。  
1. 选择您想要的**选项**。  

## **使用Aspose.Cells for JavaScript通过C++复制行和列的方法**  

## **如何复制单行**  

Aspose.Cells 提供了 [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) 方法，来自 [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) 类。该方法复制源行的所有类型数据，包括公式、数值、评论、单元格格式、隐藏单元格、图像和其他绘图对象到目标行。  

[**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) 方法的参数如下：  

- 源 [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) 对象，  
- 源行索引, 和  
- 目标行索引.  

使用此方法在工作表内或到另一个工作表复制一行。[**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) 方法的功能与 Microsoft Excel 类似。例如，你无需显式设置目标行的高度，该值也会被复制。  

下面的示例演示如何在工作表中复制一行。它使用一个模板 Microsoft Excel 文件，将第二行（包含数据、格式、批注、图片等）复制并粘贴到同一工作表的第12行。  

你可以跳过获取源行高度的步骤（使用 [**Cells.rowHeight(number, boolean, CellsUnitType)**](https://reference.aspose.com/cells/javascript-cpp/cells/#rowHeight-number-boolean-cellsunittype-) 方法）以及设置目标行高度（使用 [**Cells.rowHeight(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#rowHeight-number-number-) 方法），因为 [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) 方法会自动处理行高度。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Row</title>
    </head>
    <body>
        <h1>Copy Row Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the workbook.
            const wsTemplate = workbook.worksheets.get(0);

            // Copy the second row (index 1) with data, formatting, images and drawing objects
            // To the 16th row (index 15) in the worksheet.
            wsTemplate.cells.copyRow(wsTemplate.cells, 1, 15);

            // Save the excel file in Excel97To2003 format (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
在复制行时，重要的是注意相关的图像、图表或其他绘图对象，因为这与 Microsoft Excel 相同：  

1. 如果源行索引为5，则如果它包含在三行内（起始行索引为4，结束行索引为6），则图像、图表等会被复制。  
1. 目标行中现有的图像、图表等不会被移除。  
{{% /alert %}}  

## **如何复制多行**  

你也可以在使用 [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-) 方法复制多行时，传入一个整数参数来指定要复制的源行数。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the cells collection of first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Copy the first 3 rows to 7th row (indexes are zero-based)
            cells.copyRows(cells, 0, 6, 3);

            // Save the result and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **如何复制列**  

Aspose.Cells 提供 [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) 类中的 [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumn-cells-number-number-) 方法，该方法可以复制所有类型的数据，包括带有更新引用的公式、值、批注、单元格格式、隐藏的单元格、图片和其他绘图对象，从源列到目标列。  

[**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumn-cells-number-number-) 方法的参数如下：  

- 源 [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) 对象，  
- 源列索引, 和  
- 目标列索引.  

使用 [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumn-cells-number-number-) 方法在工作表内或到另一个工作表复制列。  

该示例将一个工作表中的列复制到另一个工作簿的工作表中。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Copy Column Example</h1>
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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const excelWorkbook1 = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the book.
            const ws1 = excelWorkbook1.worksheets.get(0);

            // Copy the first column from the first worksheet into the third column of the same worksheet.
            const cells = ws1.cells;
            cells.copyColumn(cells, cells.columns.get(0).index, cells.columns.get(2).index);

            // Autofit the column.
            ws1.autoFitColumn(2);

            // Save the excel file (Excel97To2003 format for .xls)
            const outputData = excelWorkbook1.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **如何复制多列**  

类似于 [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-) 方法，Aspose.Cells API 还提供 [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-) 方法，用于将多个源列复制到新位置。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Create an instance of Workbook class by loading the existing spreadsheet
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet's cells collection
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Copy the first 3 columns to the 7th column
            cells.copyColumns(cells, 0, 6, 3);

            // Save the result and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **如何粘贴行和列并设置粘贴选项**  

Aspose.Cells 现在提供 [**PasteOptions**](https://reference.aspose.com/cells/javascript-cpp/pasteoptions/)，使用函数 [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-) 和 [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-)。它允许设置类似于 Excel 的适当粘贴选项。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Change Chart Data Source</title>
    </head>
    <body>
        <h1>Change Chart Data Source Example</h1>
        <p>Select an Excel file (sampleChangeChartDataSource.xlsx) from your local machine.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PasteType, CopyOptions, PasteOptions } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first sheet which contains chart
            const source = workbook.worksheets.get(0);

            // Add another sheet named DestSheet
            const destination = workbook.worksheets.add("DestSheet");

            // Set CopyOptions.ReferToDestinationSheet to true
            const options = new CopyOptions();
            options.referToDestinationSheet = true;

            // Set PasteOptions
            const pasteOptions = new PasteOptions();
            pasteOptions.pasteType = PasteType.Values;
            pasteOptions.onlyVisibleCells = true;

            // Copy all the rows of source worksheet to destination worksheet which includes chart as well
            // The chart data source will now refer to DestSheet
            destination.cells.copyRows(source.cells, 0, 0, source.cells.maxDisplayRange.rowCount, options, pasteOptions);

            // Save workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeChartDataSource.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
