---
title: Copy and Move Worksheets Within and Between Workbooks with JavaScript via C++
linktitle: Copy and Move Worksheets Within and Between Workbooks
type: docs
weight: 80
url: /javascript-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Learn how to copy and move worksheets within and between workbooks using Aspose.Cells for JavaScript via C++. Efficiently manage your workbook structures.
---

{{% alert color="primary" %}}

Sometimes, you do need a number of worksheets with common formatting and data entry. For example, if you work with quarterly budgets, you might want to create a workbook with sheets that contain the same column headings, row headings, and formulas. There is a way to do this: by creating one sheet and then copying it three times.

Aspose.Cells for JavaScript via C++ supports copying or moving worksheets within or between workbooks. Worksheets including data, formatting, tables, matrices, charts, images, and other objects are copied with the highest degree of precision.

{{% /alert %}}

## **Copying and Moving Worksheets**

### **Copying a Worksheet within a Workbook**

The initial steps are the same for all examples.

1. Create two workbooks with some data in Microsoft Excel. For the purposes of this example, we created two new workbooks in Microsoft Excel and input some data into the worksheets.

- FirstWorkbook.xlsx (3 worksheets).
- SecondWorkbook.xlsx (1 worksheet).

1. Download and install Aspose.Cells:
   1. [Download Aspose.Cells for JavaScript via C++](https://downloads.aspose.com/cells/javascript-cpp).
   1. Install it on your development computer.
      All [Aspose](http://www.aspose.com/) components, when installed, work in evaluation mode. The evaluation mode has no time limit and it only injects watermarks into produced documents.
1. Create a project:
   1. Start your development environment.
   1. Create a new console application.
1. Add references:
   1. Add a reference to Aspose.Cells to the project.
      For example, add a reference to ...\Program Files\Aspose\Aspose.Cells\Bin\NodeJs\Aspose.Cells.dll
1. Copy the worksheet within a workbook
   The first example copies the first worksheet (Copy) within FirstWorkbook.xlsx.

When executing the code, the worksheet named Copy is copied within FirstWorkbook.xlsx with the name Last Sheet.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Copy Worksheet Example</title>
    </head>
    <body>
        <h1>Copy Worksheet Example</h1>
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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Copy the first sheet of the first book within the workbook
            workbook.worksheets.get(2).copy(workbook.worksheets.get("Copy"));

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FirstWorkbookCopied_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Moving a Worksheet within a Workbook**

The code below shows how to move a worksheet from one position in a workbook to another. Executing the code moves the worksheet called Move from index 1 to index 2 in FirstWorkbook.xlsx.

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Move the first sheet to index 1
            const worksheets = workbook.worksheets;
            const worksheet = worksheets.get(0);
            worksheet.moveTo(1);

            // Saving the modified Excel file and offering it for download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FirstWorkbookMoved_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet moved successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Copying a Worksheet between Workbooks**

Executing the code copies the worksheet named Copy into SecondWorkbook.xlsx with the name Sheet2.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Copy Worksheets Between Workbooks</h1>
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
            // Create two workbooks
            const excelWorkbook3 = new Workbook();
            const excelWorkbook4 = new Workbook();

            // Create source worksheet
            excelWorkbook3.worksheets.add("Copy");

            // Add new worksheet into second Workbook
            excelWorkbook4.worksheets.add();

            // Copy the first sheet of the first book into second book.
            excelWorkbook4.worksheets.get(1).copy(excelWorkbook3.worksheets.get("Copy"));

            // Save the file.
            const outputData = excelWorkbook4.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyWorksheetsBetweenWorkbooks_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheets copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Moving a Worksheet between Workbooks**

Executing the code moves the worksheet named Move from FirstWorkbook.xlsx to SecondWorkbook.xlsx with the name Sheet3.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Move Worksheets Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download First Workbook</a>
        <a id="downloadLink2" style="display: none;">Download Second Workbook</a>
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
            // Create new workbooks instead of opening existing files
            const excelWorkbook5 = new Workbook();
            const excelWorkbook6 = new Workbook();

            // Add New Worksheet
            excelWorkbook6.worksheets.add();

            // Copy the sheet from first book into second book.
            excelWorkbook6.worksheets.get(0).copy(excelWorkbook5.worksheets.get(0));

            // Remove the copied worksheet from first workbook
            excelWorkbook5.worksheets.removeAt(0);

            // Save the first workbook
            const outputData1 = excelWorkbook5.save(SaveFormat.Xlsx);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'FirstWorkbookWithMove_out.xlsx';
            downloadLink1.style.display = 'inline';
            downloadLink1.textContent = 'Download FirstWorkbookWithMove_out.xlsx';

            // Save the second workbook
            const outputData2 = excelWorkbook6.save(SaveFormat.Xlsx);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'SecondWorkbookWithMove_out.xlsx';
            downloadLink2.style.display = 'inline';
            downloadLink2.textContent = 'Download SecondWorkbookWithMove_out.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbooks processed successfully. Click the download links to retrieve the files.</p>';
        });
    </script>
</html>
```