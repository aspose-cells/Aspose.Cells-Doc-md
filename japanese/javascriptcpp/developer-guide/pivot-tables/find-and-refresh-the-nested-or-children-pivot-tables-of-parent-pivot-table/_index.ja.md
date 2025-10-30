---
title: 親ピボットテーブルのネストされたピボットテーブルや子ピボットテーブルを見つけて更新する
type: docs
weight: 60
url: /ja/javascript-cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: 親ピボットテーブルのネストされたピボットテーブルや子ピボットテーブルをAspose.Cells for JavaScriptを使用して見つけて更新する方法。
keywords: C++のExcel、Excel JavaScriptライブラリを使用した、親ピボットテーブルのネストされたピボットテーブルを見つけて更新するAspose.Cells for JavaScriptの使用例。
---

## **可能な使用シナリオ**

親ピボットテーブルが別のピボットテーブルをデータソースとして使用する場合、それを子ピボットテーブルやネストされたピボットテーブルと呼びます。[**PivotTable.children**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#children--)を使用して親ピボットテーブルの子ピボットテーブルを見つけることができます。

## **親ピボットテーブルのネストされたまたは子供のピボットテーブルを検出および更新する方法**

次のサンプルコードでは、3つのピボットテーブルを含む[サンプルExcelファイル](61767747.xlsx)をロードし、その下の2つのピボットテーブルが、このスクリーンショットに示すように、上記のピボットテーブルの子であることを示しています。コードは、[**PivotTable.children**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#children--)を使用して子ピボットテーブルを見つけ、それぞれを更新します。

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Refresh Nested/Children Pivot Tables Example</h1>
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

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access third pivot table (index 2)
            const ptParent = ws.pivotTables.get(2);

            // Access the children of the parent pivot table
            const ptChildren = ptParent.children;

            // Refresh all the children pivot table
            for (let pivot of ptChildren) {
                pivot.refreshData();
                pivot.calculateData();
            }

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.sampleFindAndRefreshNestedOrChildrenPivotTables.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot tables refreshed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
