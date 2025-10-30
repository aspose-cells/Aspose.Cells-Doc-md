---
title: 統合機能
type: docs
weight: 20
url: /ja/javascript-cpp/consolidation-function/
description: C++を使用したAspose.Cells for JavaScriptでピボットテーブルの集計関数をデータフィールドに適用する方法。
keywords: C++を使用したAspose.Cells for JavaScriptでピボットテーブルのデータフィールドに集約機能を適用します。
---

## **統合機能**

C++のAspose.Cells for JavaScriptを使用してピボットテーブルのデータフィールド（または値フィールド）に集計関数を適用できます。Microsoft Excelでは、値フィールドを右クリックし、「値フィールド設定...」を選択し、「値の集計方法」タブからSum、Count、Average、Max、Min、Product、Distinct Countなど、任意の集約関数を選択できます。

C++を使用したAspose.Cells for JavaScriptは、以下の集約関数をサポートする[**ConsolidationFunction**](https://reference.aspose.com/cells/javascript-cpp/consolidationfunction/)列挙型を提供します。

- ConsolidationFunction.Average
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums
- ConsolidationFunction.DistinctCount
- ConsolidationFunction.Max
- ConsolidationFunction.Min
- ConsolidationFunction.Product
- ConsolidationFunction.StdDev
- ConsolidationFunction.StdDevp
- ConsolidationFunction.Sum
- ConsolidationFunction.Var
- ConsolidationFunction.Varp

## **C++を使用したAspose.Cells for JavaScriptでピボットテーブルのデータフィールドに集約関数を適用する方法。**

次のコードは、最初のデータフィールド（または値フィールド）に **平均** の統合機能を適用し、2番目のデータフィールド（または値フィールド）に **重複排除** の統合機能を適用します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PivotTable Consolidation Function</title>
    </head>
    <body>
        <h1>Apply Consolidation Function to PivotTable</h1>
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

            // Accessing the first worksheet of the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access the first pivot table of the worksheet
            const pivotTable = worksheet.pivotTables.get(0);

            // Apply Average consolidation function to first data field
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Average;

            // Apply DistinctCount consolidation function to second data field
            pivotTable.dataFields.get(1).function = AsposeCells.ConsolidationFunction.DistinctCount;

            // Calculate the data to make changes affect
            pivotTable.calculateData();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PivotTable consolidation functions applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

**DISTINCT_COUNT**集計関数は、Microsoft Excel 2013でのみサポートされています。

{{% /alert %}}
