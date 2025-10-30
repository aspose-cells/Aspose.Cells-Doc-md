---
title: JavaScriptをC++経由で行と列の非表示と表示
linktitle: 行と列の非表示および表示
type: docs
weight: 60
url: /ja/javascript-cpp/hiding-and-showing-rows-and-columns/
description: ワークシートの行と列を非表示および表示する方法をAspose.Cells for JavaScriptをC++経由で学びます。
---

{{% alert color="primary" %}}

時々、ワークシートに特定の行または列を非表示にして後で表示することが理にかなっています。Microsoft Excelはこの機能を提供し、Aspose.Cellsも同様です。

{{% /alert %}}

## **行と列の可視性の制御**

Aspose.Cells for JavaScriptをC++経由で、Microsoft Excelファイルを表すクラス、[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスにはExcelファイル内の各ワークシートにアクセスできる[**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection)が含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスはワークシート内のすべてのセルを表す[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションを提供します。[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションには、ワークシート内の行や列を管理するいくつかのメソッドがあります。以下に一部を説明します。

### **行と列の非表示**

開発者は、[**hideRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideRow-number-)と[**hideColumn(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideColumn-number-)のメソッドを呼び出すことで、行や列を非表示にできます。どちらのメソッドも、特定の行や列のインデックスをパラメータとして受け取り、その行または列を非表示にします。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide Row and Column Example</h1>
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

            // Instantiating a Workbook object with Uint8Array
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding the 3rd row of the worksheet
            worksheet.cells.hideRow(2);

            // Hiding the 2nd column of the worksheet
            worksheet.cells.hideColumn(1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row and column hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

また、行または列を非表示にすることもできます。その際は、行の高さまたは列の幅をそれぞれ0に設定することができます。

{{% /alert %}}

### **行と列の表示**

開発者は、[**unhideRow(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideRow-number-number-)と[**unhideColumn(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideColumn-number-number-)のメソッドを呼び出すことで、非表示になっている行や列を表示させることができます。どちらのメソッドも、2つのパラメータを取ります：

- **行または列のインデックス** - 特定の行または列を表示するために使用される行または列のインデックス。
- **行の高さまたは列の幅** - 非表示にする行または列に割り当てられた行の高さまたは列の幅。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Unhide Rows and Columns Example</title>
    </head>
    <body>
        <h1>Unhide Rows and Columns Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiating a Workbook object with file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Unhiding the 3rd row and setting its height to 13.5
            worksheet.cells.unhideRow(2, 13.5);

            // Unhiding the 2nd column and setting its width to 8.5
            worksheet.cells.unhideColumn(1, 8.5);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

隠された列を表示状態に戻す際に、以前設定した幅や元の幅に復元する必要がある場合は、負の幅を使用して列の非表示を解除してください。例：worksheet.cells.unhideColumn(5, -1)

{{% /alert %}}

### **複数の行および列の非表示**

開発者は、[**hideRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideRows-number-number-)と[**hideColumns(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideColumns-number-number-)のメソッドを呼び出し、複数の行や列を一度に非表示にできます。これらの両方のメソッドは、開始行または列のインデックスと隠す行または列の数をパラメータとして受け取ります。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Hide Rows and Columns</title>
    </head>
    <body>
        <h1>Hide Rows and Columns Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding 3, 4, and 5 rows in the worksheet (rows are zero-based index)
            worksheet.cells.hideRows(2, 3);

            // Hiding 2 and 3 columns in the worksheet (columns are zero-based index)
            worksheet.cells.hideColumns(1, 2);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: 'application/octet-stream' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Rows and columns hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

また、[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)クラスの[**unhideRows(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideRows-number-number-number-)と[**unhideColumns(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideColumns-number-number-number-)メソッドを使って複数の行や列を表示状態にすることも可能です。

{{% /alert %}}
