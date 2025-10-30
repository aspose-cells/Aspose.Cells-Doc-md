---
title: ピボットテーブルでのデータフィールドの表示形式を操作する
type: docs
weight: 140
url: /ja/javascript-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScriptはDataFieldのすべての表示形式をサポートしています。

{{% /alert %}}

## **「最小から最大への順位付け」と「最大から最小への順位付け」表示形式オプション**

ASpose.Cellsは、ピボットフィールドの表示形式オプションを設定する機能を提供しています。このためのAPIは[**PivotShowValuesSetting.calculationType**](https://reference.aspose.com/cells/javascript-cpp/pivotshowvaluessetting/#calculationType-pivotfielddatadisplayformat-)プロパティを提供しています。最大から最小への順位付けを行うには、[**PivotShowValuesSetting.calculationType**](https://reference.aspose.com/cells/javascript-cpp/pivotshowvaluessetting/#calculationType-pivotfielddatadisplayformat-)プロパティを[**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/javascript-cpp/pivotfielddatadisplayformat/)に設定できます。次のコードスニペットは、表示形式オプションの設定方法を示しています。

サンプルソースと出力ファイルは、テスト用のサンプルコードをダウンロードできます:

[ソースExcelファイル](101089332.xlsx)

[出力Excelファイル](101089333.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PivotTable Data Display Format</title>
    </head>
    <body>
        <h1>PivotTable Data Display Format Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils, PivotFieldDataDisplayFormat } = AsposeCells;

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

            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const pivotIndex = 0;

            // Accessing the PivotTable
            const pivotTable = worksheet.pivotTables.get(pivotIndex);

            // Accessing the data fields.
            const pivotFields = pivotTable.dataFields;

            // Accessing the first data field in the data fields.
            const pivotField = pivotFields.get(0);

            // Setting data display format (convert getters/setters to properties)
            pivotField.showValuesSetting.calculationType = PivotFieldDataDisplayFormat.RankLargestToSmallest;

            pivotTable.calculateData();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PivotTableDataDisplayFormatRanking_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
