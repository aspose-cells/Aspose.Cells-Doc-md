---
title: ピボットテーブルリボンの無効化
type: docs
weight: 90
url: /ja/javascript-cpp/disable-pivot-table-ribbons/
description: C++を使用したAspose.Cells for JavaScriptによるピボットテーブルリボンの無効化方法。
keywords: C++のExcel、C++ライブラリを使用したExcel JavaScript、Aspose.Cells for JavaScriptによるピボットテーブルリボンの無効化。
---

{{% alert color="primary" %}}

 ピボットテーブルに基づくレポートは便利ですが、対象ユーザーがExcelの詳細な知識を持っていない場合はエラーが発生しやすくなります。このような場合、組織はユーザーがピボットテーブルベースのレポートを変更できないよう制限したいと考えます。追加のフィルター、スライサー、フィールドを追加したり、レポート内の特定の項目の順序を変更したりするなどの一般的なピボットテーブル機能は、ほとんどのユーザーに推奨されません。一方、これらのユーザーは、レポートを更新したり、既存のフィルターやスライサーを使用したりすることも可能です。Aspose.Cells for JavaScriptは、レポート作成時にこれらの変更を制限する機能を提供しています。これには、ピボットテーブルのリボンを無効にする機能も含まれ、開発者はこれを無効にすることができます。

{{% /alert %}}

## ** C++を使用したAspose.Cells for JavaScriptによるピボットテーブルリボンの無効化方法**

次のコードは、シートからピボットテーブルを取得し、[**enableWizard**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#enableWizard-boolean-)を**false**に設定することでこの機能を示しています。サンプルのピボットテーブルファイルは、この[リンク](pivot_table_test.xlsx)からダウンロードできます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Pivot Table Wizard Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the pivot table in the first sheet
            const pt = workbook.worksheets.get(0).pivotTables.get(0);

            // Disable ribbon for this pivot table
            pt.enableWizard = false;

            // Save output file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table wizard disabled successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
