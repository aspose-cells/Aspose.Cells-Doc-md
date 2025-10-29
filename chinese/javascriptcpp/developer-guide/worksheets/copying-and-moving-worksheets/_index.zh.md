---
title: 使用 JavaScript 通过 C++ 复制和移动工作表的示例代码，描述了如何在工作簿内以及跨工作簿以编程方式复制和移动工作表。
linktitle: 复制和移动工作表
type: docs
weight: 10
url: /zh/javascript-cpp/copying-and-moving-worksheets/
description: This article includes sample code and describes how to copy and move worksheets programmatically both within an Excel workbook and across Excel workbooks using the JavaScript via C++ API.
keywords: 复制工作表 JavaScript，移动工作表 JavaScript
---

{{% alert color="primary" %}}

有时，您确实需要一些具有共同格式和数据的工作表。例如，如果您在季度预算上工作，您可能希望创建一个包含具有相同列标题、行标题和公式的工作表的工作簿。有一种方法可以做到这一点：先创建一个工作表，然后进行复制。

Aspose.Cells for JavaScript 通过 C++ 支持在工作簿内或之间复制和移动工作表。包含数据、格式、表格、矩阵、图表、图片及其他对象的工作表，以最高精度进行复制。

{{% /alert %}}

## **使用Microsoft Excel移动或复制工作表**

以下是在Microsoft Excel中在工作簿内部或不同工作簿之间复制和移动工作表所涉及的步骤。

1. 要将工作表移动或复制到另一个工作簿中，请打开将要接收工作表的工作簿。
1. 切换到包含您想要移动或复制的工作表的工作簿，然后选择这些工作表。
1. 在“编辑”菜单上，单击“移动或复制工作表”
1. 在“选择工作簿”对话框中，单击要接收工作表的工作簿。
1. 要将所选工作表移动或复制到新工作簿中，请单击“新建工作簿”
1. 在“工作表之前”框中，单击要在其之前插入移动或复制的工作表。
1. 要复制工作表而不是移动它们，请选择“创建副本”复选框。

### **使用 Aspose.Cells for JavaScript 通过 C++ 在工作簿内复制工作表**

Aspose.Cells提供了一个重载方法，[**Aspose.Cells.WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#addCopy-number-)，用于将工作表添加到集合并从现有工作表复制数据。该方法的一个版本将源工作表的索引作为参数。另一个版本将源工作表的名称作为参数。

以下示例显示了如何在工作簿内复制现有工作表。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Sheet Within Workbook</title>
    </head>
    <body>
        <h1>Copy Sheet Within Workbook Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open an existing Excel file.
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheets object with reference to the sheets of the Workbook.
            const sheets = wb.worksheets;

            // Copy data to a new sheet from an existing sheet within the Workbook.
            sheets.addCopy("Sheet1");

            // Save the Excel file.
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyWithinWorkbook_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Sheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **在工作簿之间复制工作表**

Aspose.Cells提供一种方法[**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#copy-worksheet-)，用于复制数据和格式，从源工作表到另一个工作表，支持在或跨工作簿中操作。该方法需要源工作表对象作为参数。

以下示例显示了如何将一个工作表从一个工作簿复制到另一个工作簿。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Copy Worksheets Between Workbooks</title>
    </head>
    <body>
        <h1>Copy Worksheets Between Workbooks</h1>
        <p>Select the source Excel file (book1.xls) to copy its first worksheet into a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (book1.xls).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create a Workbook from the uploaded file (source workbook)
            const excelWorkbook0 = new Workbook(new Uint8Array(arrayBuffer));

            // Create another Workbook (destination workbook)
            const excelWorkbook1 = new Workbook();

            // Copy the first sheet of the first book into second book.
            excelWorkbook1.worksheets.get(0).copy(excelWorkbook0.worksheets.get(0));

            // Save the file as Excel 97-2003 (.xls)
            const outputData = excelWorkbook1.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyWorksheetsBetweenWorkbooks_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Copied Workbook';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

以下示例显示了如何将一个工作表从一个工作簿复制到另一个。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Copy Worksheet Between Workbooks Example</h1>
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
            // Create a new Workbook.
            const excelWorkbook0 = new Workbook();

            // Get the first worksheet in the book.
            const ws0 = excelWorkbook0.worksheets.get(0);

            // Put some data into header rows (A1:A4)
            for (let i = 0; i < 5; i++) {
                ws0.cells.get(i, 0).value = `Header Row ${i}`;
            }

            // Put some detail data (A5:A999)
            for (let i = 5; i < 1000; i++) {
                ws0.cells.get(i, 0).value = `Detail Row ${i}`;
            }

            // Define a pagesetup object based on the first worksheet.
            const pagesetup = ws0.pageSetup;

            // The first five rows are repeated in each page...
            // It can be seen in print preview.
            pagesetup.printTitleRows = "$1:$5";

            // Create another Workbook.
            const excelWorkbook1 = new Workbook();

            // Get the first worksheet in the book.
            const ws1 = excelWorkbook1.worksheets.get(0);

            // Name the worksheet.
            ws1.name = "MySheet";

            // Copy data from the first worksheet of the first workbook into the
            // first worksheet of the second workbook.
            ws1.copy(ws0);

            // Saving the modified Excel file
            const outputData = excelWorkbook1.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyWorksheetFromWorkbookToOther_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and worksheet copied successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **在工作簿内部移动工作表**

Aspose.Cells提供一种方法[**Aspose.Cells.Worksheet.moveTo()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#moveto-number-)，用于将工作表移动到同一工作簿的另一个位置。该方法接受目标工作表索引作为参数。

以下示例显示了如何将工作表移动到工作簿内的另一个位置。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Move Worksheet Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access worksheets collection
            const sheets = wb.worksheets;

            // Get the first worksheet
            const worksheet = sheets.get(0);

            // Move the first sheet to the third position (index 2)
            worksheet.moveTo(2);

            // Save the modified workbook in Excel97-2003 format
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'MoveWorksheet_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet moved successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
