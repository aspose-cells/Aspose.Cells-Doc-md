---
title: 插入和删除Excel文件的行和列
linktitle: 插入和删除行和列
type: docs
weight: 70
url: /zh/javascript-cpp/inserting-and-deleting-rows-and-columns/
description: 本文介绍如何通过Aspose.Cells for JavaScript通过C++ API插入和删除行与列。
keywords: Aspose.Cells通过JavaScript用C++管理行和列，插入行和列，删除行和列
---

## **介绍**

无论是从头开始创建新工作表还是在现有工作表上操作，我们可能需要添加额外的行或列来容纳更多数据。反之，我们可能还需要从工作表中的指定位置删除行或列。 
为了满足这些需求，Aspose.Cells for JavaScript通过C++提供了一套非常简洁的类和方法，具体如下。

### **管理行和列**

Aspose.Cells for JavaScript通过C++提供一个类[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)，代表一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类提供一个[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)集合，表示工作表中的所有单元格。

[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) 集合提供了多种管理工作表中行和列的方法，下面将介绍一些。

{{% alert color="primary" %}}

当添加行或列时，工作表中的内容会向下或向右移动；删除行或列时，内容会向上或向左移动。

{{% /alert %}}


## **插入行和列**

### **如何插入行**

通过调用 [**insertRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRow-number-) 方法，您可以在任何位置插入一行到工作表中。[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) 方法接受将插入新行的行索引。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Insert Row Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Inserting a row into the worksheet at 3rd position (index 2)
            worksheet.cells.insertRow(2);

            // Saving the modified Excel file as Excel97To2003 (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **如何插入多行**

要在工作表中插入多行，请调用 [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) 方法。此方法需要两个参数：

- 行索引，新行将从该行插入。
- 行数，需要插入的总行数。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Rows Example</title>
    </head>
    <body>
        <h1>Insert Rows Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Inserting 10 rows into the worksheet starting at index 2
            worksheet.cells.insertRows(2, 10);

            // Saving the modified Excel file (Excel 97-2003 format)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **如何插入带有格式的行**

若要插入带有格式选项的行，请使用接受 [**InsertOptions**](https://reference.aspose.com/cells/javascript-cpp/insertoptions) 作为参数的 [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) 重载。将 [**CopyFormatType**](https://reference.aspose.com/cells/javascript-cpp/copyformattype/) 属性设置为 [**CopyFormatType**](https://reference.aspose.com/cells/javascript-cpp/copyformattype/) 枚举。[**InsertOptions**](https://reference.aspose.com/cells/javascript-cpp/insertoptions) 类的 [**CopyFormatType**](https://reference.aspose.com/cells/javascript-cpp/copyformattype/) 属性被赋予值。枚举 [**CopyFormatType**](https://reference.aspose.com/cells/javascript-cpp/copyformattype/) 中，包括以下三个成员：

开发者还可以调用 {0} 方法，插入列，参数为列索引。
- SameAsBelow：将行格式化为与下一行相同。
- Clear: 清除格式。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Inserting a Row With Formatting Example</title>
    </head>
    <body>
        <h1>Inserting a Row With Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, InsertOptions, CopyFormatType, Utils } = AsposeCells;

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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting Formatting options
            const insertOptions = new InsertOptions();
            insertOptions.copyFormatType = CopyFormatType.SameAsAbove;

            // Inserting a row into the worksheet at 3rd position
            worksheet.cells.insertRows(2, 1, insertOptions);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'InsertingARowWithFormatting.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **如何插入列**

用C++从工作表中删除列

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Insert Column Example</title>
    </head>
    <body>
        <h1>Insert Column Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Inserting a column into the worksheet at 2nd position
            worksheet.cells.insertColumn(1);

            // Saving the modified Excel file (Excel97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **删除行和列**

### **如何删除多行**

调用 [**deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-) 方法，从工作表中删除列，参数为列索引。

- 行索引，要删除行的索引。
- 行数，需要删除的总行数。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Delete Rows Example</title>
    </head>
    <body>
        <h1>Delete Rows Example</h1>
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

            // Instantiating a Workbook object with file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Deleting 10 rows from the worksheet starting from 3rd row (index 2)
            worksheet.cells.deleteRows(2, 10);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows deleted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


### **如何删除列**

用C++删除工作表中的重复行

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Delete Column Example</title>
    </head>
    <body>
        <h1>Delete Column Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Deleting a column from the worksheet at 5th position (zero-based index 4)
            worksheet.cells.deleteColumn(4);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column deleted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
