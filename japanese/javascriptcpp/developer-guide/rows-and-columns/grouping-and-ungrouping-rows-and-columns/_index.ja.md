---
title: JavaScriptをC++経由で行と列のグループ化およびグループ解除
linktitle: 行と列のグループ化および展開
type: docs
weight: 50
url: /ja/javascript-cpp/grouping-and-ungrouping-rows-and-columns/
description: C++を使用したAspose.Cells for JavaScriptを使った行と列のグループ化と解除方法を紹介します。
---

## **紹介**

Microsoft Excelファイルでは、データの概要を作成して、1回のマウスクリックで詳細のレベルを表示したり非表示にしたりできます。

**アウトライン記号**の1、2、3、+、および-をクリックして、ワークシートのセクションの要約または見出しを迅速に表示したり、個々の要約または見出しの詳細を表示する際に使用できます。下の図で示されているように、個々の要約または見出しの詳細を表示するためにシンボルを使用できます。

|**行と列のグループ化**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **行と列のグループ管理**

Aspose.Cellsは、Microsoft Excelファイルを表す [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) クラスにはExcelファイル内の各ワークシートにアクセスできる [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) が含まれます。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) クラスは、そのワークシート内のすべてのセルを表す [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) コレクションを提供します。

[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) コレクションは、ワークシート内の行または列を管理するためのいくつかのメソッドを提供し、その中のいくつかを詳細に説明します。

### **行と列のグループ化**

[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) コレクションの [**groupRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#groupRows-number-number-boolean-) および [**groupColumns(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#groupColumns-number-number-) メソッドを呼び出すことで、行や列をグループ化できます。両方のメソッドは次のパラメータを取ります：

- 最初の行/列インデックス、グループ内の最初の行または列
 - グループ内の最後の行/列のインデックス、最後の行または列。
- 非表示かどうか、グループ化後に行または列を非表示にするかどうかを指定するブールパラメータ。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group Rows and Columns Example</title>
    </head>
    <body>
        <h1>Group Rows and Columns Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.groupRows(0, 5, true);
            worksheet.cells.groupColumns(0, 2, true);

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows and columns grouped successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **グループ設定**

Microsoft Excelでは、以下を表示するためのグループ設定を構成できます:

- 詳細の下の要約行。
- 詳細の右側の要約列。

これらのグループ設定は、[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) クラスの [**outline**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#outline--) プロパティを使用して構成できます。

### **詳細の下にサマリー行**

詳細の下にサマリ行を表示するかどうかを制御するには、[**Outline**](https://reference.aspose.com/cells/javascript-cpp/outline) クラスの [**summaryRowBelow**](https://reference.aspose.com/cells/javascript-cpp/outline/#summaryRowBelow--) プロパティを **true** か **false** に設定します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Example - Group Rows/Columns and Set Outline</h1>
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

            // Grouping first six rows and first three columns
            worksheet.cells.groupRows(0, 5, true);
            worksheet.cells.groupColumns(0, 2, true);

            // Setting SummaryRowBelow property to false
            worksheet.outline.summaryRowBelow = false;

            // Saving the modified Excel file (Excel97To2003 -> .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
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

### **詳細の右側にサマリー列**

詳細の右側にサマリ列を表示するかどうかも、[**Outline**](https://reference.aspose.com/cells/javascript-cpp/outline) クラスの [**summaryColumnRight**](https://reference.aspose.com/cells/javascript-cpp/outline/#summaryColumnRight--) プロパティを **true** か **false** に設定することで制御できます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Group Rows and Columns Example</h1>
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

            // Grouping first six rows and first three columns
            worksheet.cells.groupRows(0, 5, true);
            worksheet.cells.groupColumns(0, 2, true);

            // Set summary column to right
            worksheet.outline.summaryColumnRight = true;

            // Saving the modified Excel file (Excel 97-2003 format)
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

## **行と列のグループ解除**

グループ化された行や列を解除するには、[**ungroupColumns(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#ungroupColumns-number-number-) コレクションの [**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#ungroupRows-number-number-boolean-) および [**ungroupColumns(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#ungroupColumns-number-number-) メソッドを呼び出します。両方のメソッドには2つのパラメータが必要です：

- 最初の行または列のインデックス、グループ化を解除する最初の行/列。
- 最後の行または列のインデックス、グループ化を解除する最後の行/列。

[**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#ungroupRows-number-number-boolean-) には、Booleanの第3パラメータを取るオーバーロードがあります。それを **true** に設定すると、すべてのグループ情報が削除されます。そうでなければ、外側のグループ情報だけが削除されます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Ungroup Rows and Columns Example</h1>
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

            // Instantiating a Workbook object with file content
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Ungrouping first six rows (from 0 to 5)
            worksheet.cells.ungroupRows(0, 5);

            // Ungrouping first three columns (from 0 to 2)
            worksheet.cells.ungroupColumns(0, 2);

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
