---
title: Excelシートのゼロ値の表示をJavaScriptを使って隠す方法
linktitle: ワークシートでゼロ値を非表示にする
type: docs
weight: 50
url: /ja/javascript-cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: この資料では、C++を使ったJavaScriptライブラリを使用してExcelスプレッドシート内のゼロ値をプログラム的に隠すサンプルコードを示します。
keywords: Excelワークシートのゼロ値をJavaScriptを使用して隠す
---

{{% alert color="primary" %}} 

時折、スプレッドシートでゼロ値を非表示にする必要があります。これは個人の好みである場合もありますし、書式設定の基準である場合もあります。

{{% /alert %}} 

Microsoft Excel でワークシートでゼロ値を非表示にするには:

1. **ツール** メニューから **オプション** を選択し、次に **表示** タブを選択します。
1. **ゼロ値** オプションを選択解除します。
1. **OK** をクリックします。

以下のサンプルコードは、C++でAspose.Cells for JavaScriptを使用してゼロを隠す方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide Zero Values Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Get First worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Hide the zero values in the sheet
            sheet.displayZeros = false;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputfile.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
