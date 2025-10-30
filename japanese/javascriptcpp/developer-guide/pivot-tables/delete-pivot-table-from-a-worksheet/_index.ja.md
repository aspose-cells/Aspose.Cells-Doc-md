---
title: ワークシートからのピボットテーブルの削除
type: docs
weight: 60
url: /ja/javascript-cpp/delete-pivot-table-from-a-worksheet/
description: Excelワークシートのピボットテーブルを削除または除去するためのAspose.Cells for JavaScriptをC++コード
keywords: Aspose.Cells for JavaScriptをC++ Excel、Excel JavaScriptライブラリで使用し、ワークシートからピボットテーブルを削除、Excelからピボットテーブルを削除、Aspose.Cells for JavaScriptをC++でピボットテーブルを削除、削除：
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScriptをC++は、ピボットテーブルをワークシートから削除または除去する機能を提供します。ピボットテーブルオブジェクトまたはピボットテーブルの位置を使用して削除できます。ピボットテーブルオブジェクトを使用して削除する場合は[**Worksheet.pivotTables.remove(pivotTable)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#remove-pivottable-)メソッドを、位置を指定して削除する場合は[**Worksheet.pivotTables.removeAt(index, keepData)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#removeAt-number-boolean-)メソッドを使用してください。

{{% /alert %}}

## ** C++を使用したAspose.Cells for JavaScriptによるワークシートからのピボットテーブルの削除方法**

次のサンプルコードでは、ワークシートから2つのピボットテーブルを削除する方法が示されています。最初に[**Worksheet.pivotTables.remove(pivotTable)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#remove-pivottable-)メソッドを使用してピボットテーブルを削除し、次に[**Worksheet.pivotTables.removeAt(index, keepData)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#removeAt-number-boolean-)メソッドを使用してピボットテーブルを削除します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Pivot Table</title>
    </head>
    <body>
        <h1>Remove Pivot Table Example</h1>
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
            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first pivot table object
            const pivotTable = worksheet.pivotTables.get(0);

            // Remove pivot table using pivot table object
            worksheet.pivotTables.remove(pivotTable);
            // OR remove by index:
            // worksheet.pivotTables.removeAt(0);

            // Saving the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
