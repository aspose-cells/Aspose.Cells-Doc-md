---
title: JavaScript経由のC++で1904日付システムを実装
description: Aspose.Cellsは、スプレッドシートファイルを操作するためのJavaScriptライブラリです。これにより、1904年の日付システムを実装でき、ユーザーは1904年の基準日から計算やフォーマットを行うことができます。この記事では、Aspose.Cellsライブラリを使用した1904日付システムの実装方法について説明します。
keywords: Aspose.Cells、1904日付システム、スプレッドシート、計算、フォーマット、JavaScriptをC++経由
type: docs
weight: 7000
url: /ja/javascript-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}} 

 Microsoft Excel は、2つの日付システムをサポートしています。1900日付システム（Windows用Excelに標準搭載）と1904日付システムです。1904日付システムは、Macintosh Excelファイルとの互換性を提供するために通常使用され、Mac版Excelを使用している場合はデフォルトのシステムです。これらは、Aspose.Cells for JavaScriptをC++経由で使用してExcelファイルの1904日付システムを設定できます。 

{{% /alert %}} 

Microsoft Excelで1904日付システムを実装する方法（例：Microsoft Excel 2003）：

1. **ツール**メニューから**オプション**を選択し、**計算**タブを選択します。
1. **1904年日付システム**オプションを選択します。
1. **OK** をクリックします。

|**Microsoft Excelで1904年日付システムを選択**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|

Aspose.CellsのAPIを使用してこの機能を実現するサンプルコードを以下に示します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Enable 1904 Date System</h1>
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Implement 1904 date system
            workbook.settings.date1904 = true;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Mybook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">1904 date system enabled. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
