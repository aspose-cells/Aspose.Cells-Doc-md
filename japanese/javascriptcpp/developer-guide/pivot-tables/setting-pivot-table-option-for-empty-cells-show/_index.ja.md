---
title: ピボットテーブルオプションの設定  空白セルに表示する内容を設定する
type: docs
weight: 40
url: /ja/javascript-cpp/setting-pivot-table-option-for-empty-cells-show/
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScriptはC++を使用して、さまざまなピボットテーブルオプションを設定することができます。その一つが"空のセルには表示"です。このオプションを設定すると、ピボットテーブル内のすべての空のセルが指定された文字列として表示されます。

{{% /alert %}}

## **Microsoft Excelでのピボットテーブルオプションの設定**

Microsoft Excelでこのオプションを見つけて設定するには:

1. ピボットテーブルを選択し、右クリックします。
1. **ピボットテーブルオプション**を選択します。
1. **レイアウトと書式**タブを選択します。
1. **空白のセルに表示する内容**オプションを選択し、文字列を指定します。

## **Aspose.Cells for JavaScriptを使用したピボットテーブルオプションの設定例**

Aspose.Cells for JavaScriptはC++を使用して、"空のセルには表示"オプションの設定に[**PivotTable.displayNullString**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#displayNullString-boolean-)と[**PivotTable.nullString**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#nullString-string-)プロパティを提供しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PivotTable Update Example</title>
    </head>
    <body>
        <h1>Update PivotTable Null Display Example</h1>
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

            await AsposeCells.onReady();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and its first pivot table
            const worksheet = workbook.worksheets.get(0);
            const pt = worksheet.pivotTables.get(0);

            // Indicating if or not display the empty cell value
            pt.displayNullString = true;
            // Indicating the null string
            pt.nullString = "null";

            // Recalculate pivot table data
            pt.calculateData();

            // Do not refresh data on opening file
            pt.refreshDataOnOpeningFile = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Pivot table updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## 関連記事

- [ピボットテーブルの書式設定](/cells/ja/javascript-cpp/formatting-pivot-table/)
