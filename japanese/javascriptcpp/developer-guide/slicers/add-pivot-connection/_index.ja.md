---
title: JavaScriptをC++経由でピボット接続を追加
linktitle: ピボット接続を追加する
type: docs
weight: 30
url: /ja/javascript-cpp/add-pivot-connection/
description: Aspose.Cells for JavaScriptをC++経由で使用してピボット接続を追加する方法を学ぶ。
keywords: Office 2013, Office 2016, Office 2019, Office 365なしでピボット接続を追加するJavaScriptをC++経由で使用
---

## **可能な使用シナリオ**

Excelでスライサーとピボットテーブルを関連付ける場合は、スライサーを右クリックして「レポート接続...」を選択します。オプションリストのチェックボックスで操作できます。同様に、Aspose.Cells APIを使用してプログラム的にスライサーとピボットテーブルを関連付ける場合は、[**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/javascript-cpp/slicer/#addPivotConnection-PivotTable-)メソッドを使用してください。これによりスライサーとピボットテーブルの関連付けが行われます。

## **スライサーとピボットテーブルを関連付ける**

以下のサンプルコードは、既存のスライサーを含む[サンプルExcelファイル](add-pivot-connection.xlsx)をロードし、スライサーにアクセスしてスライサーとピボットテーブルの関連付けを行います。最後に、ワークブックを[出力Excelファイル](add-pivot-connection-out.xlsx)として保存します。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add Pivot Connection Example</title>
    </head>
    <body>
        <h1>Add Pivot Connection Example</h1>
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

            const pivotTable = worksheet.pivotTables.get(0);

            const slicer = worksheet.slicers.get(0);

            slicer.addPivotConnection(pivotTable);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'add-pivot-connection-out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot connection added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
