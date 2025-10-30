---
title: セル内にHTMLリッチテキストを追加
linktitle: HTML文字列値
type: docs
weight: 50
url: /ja/javascript-cpp/adding-html-rich-text-inside-the-cell/
description: C++ APIによるAspose.Cells for JavaScriptを使用してセル内にHTMLリッチテキストを追加する方法を学習してください。
keywords: JavaScript経由のC++でセル内にHTMLリッチテキストを追加、設定、挿入する方法
---

{{% alert color="primary" %}}

Aspose.Cellsは、Microsoft Excel向けのHTMLをXLS/XLSXフォーマットに変換できることをサポートします。つまり、Microsoft Excelが生成したHTMLをAspose.Cellsを使ってXLS/XLSXに再変換できます。

同様に、いくつかのシンプルなHTMLがある場合、Aspose.CellsはそれをHTMLリッチテキストに変換できます。Aspose.Cellsは[**Cell.htmlString**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-string-)プロパティを提供しており、そのプロパティはこのようなシンプルなHTMLを受け取り、装飾されたセルテキストに変換できます。

{{% /alert %}}

以下のコードサンプルは、セル内に HTML リッチテキストを追加する方法を示しています。出力 Excel ファイルのスクリーンショットを参照してください。

![todo:image_alt_text](adding-html-rich-text-inside-the-cell_1)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells HTML String Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            let workbook;

            // If a file is provided, open it; otherwise create a new workbook
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set HTML formatted string to the cell (converted setter -> property)
            cell.htmlString = "<Font Style=\"FONT-WEIGHT: bold;FONT-STYLE: italic;TEXT-DECORATION: underline;FONT-FAMILY: Arial;FONT-SIZE: 11pt;COLOR: #ff0000;\">This is simple HTML formatted text.</Font>";

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML string written to A1. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## 関連記事

- [HTMLを設定して箇条書きを表示](/cells/ja/javascript-cpp/display-bullets-by-setting-cell-value-using/)
- [セルからHTML5文字列を取得](/cells/ja/javascript-cpp/get-html5-string-from-cell/)
