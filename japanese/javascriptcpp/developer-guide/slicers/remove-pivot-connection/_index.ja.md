---
title: JavaScriptを使用したピボット接続の削除（C++経由）
linktitle: ピボット接続を解除する
type: docs
weight: 30
url: /ja/javascript-cpp/remove-pivot-connection/
description: C++を使用してスクリプトAspose.Cells for Javaを使ったピボット接続の削除方法を学びます。
keywords: Office 2013、2016、2019、365を使用せず、JavaScriptとC++を使用してピボット接続を削除します。
---

## **可能な使用シナリオ**

Excelでスライサーとピボットテーブルの関連付けを解除したい場合は、スライサーを右クリックして「レポート接続...」を選択します。オプションリストでチェックボックスを操作できます。同様に、C++ APIのスクリプトAspose.Cells for Javaを使用してプログラム的にスライサーとピボットテーブルの関連付けを解除するには、[**Slicer.removePivotConnection(PivotTable)**](https://reference.aspose.com/cells/javascript-cpp/slicer/#removePivotConnection-pivottable-)メソッドを使用してください。これによりスライサーとピボットテーブルの関連付けが解除されます。

## **スライサーとピボットテーブルの非連携**

次のサンプルコードは、既存のスライサーを含む[サンプルExcelファイル](remove-pivot-connection.xlsx)をロードし、スライサーにアクセスしてピボットテーブルとの関連付けを解除します。最後に、ワークブックを[出力Excelファイル](remove-pivot-connection-out.xlsx)として保存します。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Pivot Connection</title>
    </head>
    <body>
        <h1>Remove Pivot Connection Example</h1>
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

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access the first PivotTable inside the PivotTable collection.
            const pivotTable = worksheet.pivotTables.get(0);

            // Access the first slicer inside the slicer collection.
            const slicer = worksheet.slicers.get(0);

            // Remove PivotTable connection.
            slicer.removePivotConnection(pivotTable);

            // Save the workbook in output XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'remove-pivot-connection-out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot connection removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
