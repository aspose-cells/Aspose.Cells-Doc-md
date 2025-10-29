---
title: 使用JavaScript通过C++自适应调整行列宽。
linktitle: 自动调整行和列
type: docs
weight: 20
url: /zh/javascript-cpp/autofit-rows-and-columns/
description: 本文展示了如何使用Aspose.Cells for JavaScript通过C++自动调整单元格范围内的行、列、合并单元格的行以及整行的宽度。
keywords: JavaScript通过C++自动调整行宽，JavaScript通过C++自动调整列宽，JavaScript通过C++自动调整范围内行宽，JavaScript通过C++自动调整合并单元格行宽
---

{{% alert color="primary" %}}  
Microsoft Excel允许用户根据内容自动调整单元格的宽度和高度。此功能也通过Aspose.Cells for JavaScript通过C++提供，开发者可以在运行时自动调整单元格的尺寸。  
{{% /alert %}}  

## **自动调整**  

Aspose.Cells 提供了 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 类，表示一个 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 类包含一个 [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) 集合，可以访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类提供了管理工作表的多种属性和方法。本文介绍了如何使用 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类自动调整行或列宽。  

### **自动调整行 - 简单**  

最简单的自动调整行宽和列高的方法是调用[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类的[**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-)方法。[**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-)方法以行索引作为参数，调整特定行。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - AutoFit Row</title>
    </head>
    <body>
        <h1>AutoFit Row Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Auto-fitting the 3rd row of the worksheet (row index 1 is the 2nd row; original code used 1)
            worksheet.autoFitRow(1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row auto-fitted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **如何在单元格范围内自动调整行**  

一行由多个列组成。Aspose.Cells允许开发者通过调用[**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-number-number-)方法的重载版本，根据该行中某个范围的单元格内容自动调整行高。参数如下：  

- **行索引**，即要自动调整的行的索引。  
- **第一个列索引**，即行的第一个列的索引。  
- **最后列索引**，指行的最后一列的索引。  

[**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-number-number-)方法会检查该行所有列的内容，然后自动调整行高。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - AutoFit Row</title>
    </head>
    <body>
        <h1>Auto-Fit Row Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Auto-fitting the 3rd row of the worksheet (row index 1, startColumn 0, endColumn 5)
            worksheet.autoFitRow(1, 0, 5);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row auto-fitted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **如何在一系列单元格中自动调整列**  

一列由许多行组成。通过调用接受以下参数的 [**autoFitColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumn-number-) 方法的重载版本，可以根据某个范围内的单元格内容自动调整列宽：  

- **列索引**，要自动调整的列的索引。  
- **第一行索引**，列的第一行的索引。  
- **最后行索引**，列的最后一行的索引。  

[**autoFitColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumn-number-)方法会检查该列所有行的内容，然后自动调整列宽。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells AutoFit Column Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Auto-fitting the Column of the worksheet (column index 4)
            worksheet.autoFitColumn(4);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column auto-fitted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **如何为合并单元格自动调整行高**  

使用 Aspose.Cells，即使单元格已合并，也可以自动调整行的宽度，使用 [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) API。[**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) 类提供 [**AutoFitterOptions.autoFitMergedCellsType()**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#autoFitMergedCellsType--) 属性，可用于自动调整合并单元格的行宽。[**AutoFitterOptions.autoFitMergedCellsType()**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#autoFitMergedCellsType--) 接受 [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/javascript-cpp/autofitmergedcellstype) 枚举，其成员如下。  

- None：忽略合并的单元格。  
- FirstLine：只扩展第一行的高度。  
- 最后一行：只扩展最后一行的高度。  
- 每行：只扩展每一行的高度。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Autofit Rows for Merged Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoFitterOptions, AutoFitMergedCellsType } = AsposeCells;

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

            // Create or load workbook
            let wb;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                wb = new Workbook();
            }

            // Get the first (default) worksheet
            const worksheet = wb.worksheets.get(0);

            // Create a range A1:B1
            const range = worksheet.cells.createRange(0, 0, 1, 2);

            // Merge the cells
            range.merge();

            // Insert value to the merged cell A1
            const cell = worksheet.cells.get(0, 0);
            cell.value = "A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end";

            // Create a style object
            const style = cell.style;

            // Set wrapping text on
            style.isTextWrapped = true;

            // Apply the style to the cell
            cell.style = style;

            // Create an object for AutoFitterOptions
            const options = new AutoFitterOptions();

            // Set auto-fit for merged cells
            options.autoFitMergedCellsType = AutoFitMergedCellsType.EachLine;

            // Autofit rows in the sheet (including the merged cells)
            worksheet.autoFitRows(options);

            // Save the Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AutofitRowsforMergedCells.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
你还可以尝试使用接受行/列范围和 [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) 实例的 [**autoFitRows**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRows-number-number-AutoFitterOptions-) 和 [**autoFitColumns**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumns-number-number-AutoFitterOptions-) 方法的重载版本，以按您的需求自动调整选定的行/列。  

上述方法的签名如下：  

1. autoFitRows（int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) 选项)  
1. autoFitColumns（int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) 选项)  
{{% /alert %}}  

## **重要知识**  

{{% alert color="primary" %}}  
如果单元格被合并，那么自动调整方法将不会应用，这与 Microsoft Excel 中的行为相同。你可以通过使用自动筛选 API 来绕过这一点。此外，如果单元格中的文本换行，也不会应用 [**autoFitColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumn-number-) 方法。还需要注意的是，*autoFit* 方法是耗时的。因此，应尽可能少调用这些方法，以确保你的应用效率。  
{{% /alert %}}  

## **高级主题**  
- [为合并单元格自动调整行高](/cells/zh/javascript-cpp/autofit-rows-for-merged-cells/)
