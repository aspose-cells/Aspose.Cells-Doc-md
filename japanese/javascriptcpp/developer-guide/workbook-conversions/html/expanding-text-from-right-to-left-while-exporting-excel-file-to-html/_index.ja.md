---
title: ExcelファイルをHTMLにエクスポートする際に右から左へのテキスト展開を行います（JavaScript経由のC++）。
linktitle: Excel ファイルを HTML にエクスポートする際にテキストを右から左に展開
type: docs
weight: 60
url: /ja/javascript-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/
---

{{% alert color="primary" %}}

Aspose.Cells は、Excel ファイルを HTML にエクスポートする際にテキストを右から左に展開する機能を v8.9.0.0 以降でサポートしています。元の Excel ファイルに右から左に展開するテキストが含まれている場合、Aspose.Cells はそれを適切に HTML にエクスポートします。

{{% /alert %}}
## **Excel ファイルを HTML にエクスポートする際にテキストを右から左に展開**
[サンプルexcelファイル](5115502.xlsx)をHTMLに変換するサンプルコードは次のとおりです。このスクリーンショットは、サンプルExcelがMicrosoft Excel 2013でどのように表示されるかを示しています。

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

このスクリーンショットは、古いバージョンで生成された[output HTML](5115509)を示しています。

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

このスクリーンショットは、新しいバージョンで生成された[output HTML](5115508)を示しています。

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

スクリーンショットに示されるように、新しいバージョンでは右寄せされたテキストを Microsoft Excel と同様に適切に左に展開します。


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Expand Text From Right To Left Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

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

            // Load source excel file inside the workbook object
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Get CellsHelper version (converted from getVersion())
            const version = CellsHelper.version;

            // Save workbook in html format
            const outputData = wb.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `ExpandTextFromRightToLeft_out_${version}.html`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook converted to HTML successfully. Click the download link to get the result.</p>';
        });
    </script>
</html>
```
