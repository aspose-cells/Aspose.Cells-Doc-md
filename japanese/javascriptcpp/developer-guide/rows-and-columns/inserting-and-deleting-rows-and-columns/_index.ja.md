---
title: Excelファイルの行と列の挿入と削除
linktitle: Excelファイルの行と列の挿入と削除
type: docs
weight: 70
url: /ja/javascript-cpp/inserting-and-deleting-rows-and-columns/
description: この資料は、Aspose.Cells for JavaScriptをC++ APIで使用し、行と列の挿入および削除方法を示しています。
keywords: Aspose.Cells JavaScriptをC++経由で、行と列の管理、行と列の挿入と削除
---

## **紹介**

ワークシートをゼロから作成するか、既存のワークシートで作業する場合、さらなるデータを収容するために追加の行や列を必要とする場合があります。逆に、ワークシート内の特定の位置から行や列を削除する必要がある場合もあります。 
これらの要件を満たすために、Aspose.Cells for JavaScriptをC++経由で提供される非常にシンプルなクラスとメソッドセットについて以下に説明します。

### **行と列の管理**

C++を通じてAspose.Cells for JavaScriptはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスにはExcelファイルの各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスはワークシート内のすべてのセルを表す[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)コレクションを提供します。

[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)コレクションは、ワークシート内の行と列を管理するためのいくつかのメソッドを提供します。いくつかの例を以下に示します。

{{% alert color="primary" %}}

行や列を追加すると、ワークシート内の内容が下または右にシフトされ、削除すると上または左にシフトされます。

{{% /alert %}}


## **行と列の挿入**

### **行の挿入方法**

任意の位置に行を挿入するには、[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)コレクションの[**insertRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRow-number-)メソッドを呼び出します。[**insertRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRow-number-)メソッドは、新しい行を挿入する位置のインデックスを取ります。

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

### **複数の行を挿入する方法**

ワークシートに複数の行を挿入するには、[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)コレクションの[**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-)メソッドを呼び出します。[**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-)メソッドは2つのパラメータを取ります：

- 行インデックス、新しい行が挿入される行のインデックス。
- 行数、挿入する必要がある行の合計数。

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

### **書式付きで行を挿入する方法**

書式設定オプション付きの行を挿入するには、引数に[**InsertOptions**](https://reference.aspose.com/cells/javascript-cpp/insertoptions)を取る[**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-)のオーバーロードを使用します。[**InsertOptions**](https://reference.aspose.com/cells/javascript-cpp/insertoptions)クラスの[**CopyFormatType**](https://reference.aspose.com/cells/javascript-cpp/copyformattype/)プロパティを[**CopyFormatType**](https://reference.aspose.com/cells/javascript-cpp/copyformattype/)列挙型で設定します。[**CopyFormatType**](https://reference.aspose.com/cells/javascript-cpp/copyformattype/)列挙型には以下の3つのメンバーがあります。

- SameAsAbove: 上の行と同じフォーマット。
- SameAsBelow: 下の行と同じように行をフォーマットします。
- Clear: 書式をクリアします。

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

### **列の挿入方法**

開発者は、任意の場所に列を挿入することもできます。[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)コレクションの[**insertColumn(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertColumn-number-boolean-)メソッドを呼び出します。[**insertColumn(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertColumn-number-boolean-)メソッドは、挿入する列のインデックスを受け取ります。

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

## **行と列の削除**

### **複数の行を削除する方法**

複数行を削除するには、[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)コレクションの[**deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-)メソッドを呼び出します。[**deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-)メソッドは2つのパラメータを取ります：

- 行インデックス、削除される行のインデックス。
- 行数、削除する必要がある行の合計数。

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


### **列を削除する方法**

任意の場所で列を削除するには、[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)コレクションの[**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteColumn-number-boolean-)メソッドを呼び出します。[**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteColumn-number-boolean-)メソッドは削除する列のインデックスを受け取ります。

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
