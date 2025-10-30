---
title: JavaScriptを介したC++でワークシートタグの色を設定します
linktitle: ワークシートタブの色を設定
type: docs
weight: 120
url: /ja/javascript-cpp/set-worksheet-tab-color/
description: この記事は、JavaScriptを介したC++を使用してExcelワークシートのタブの色をプログラムで設定するサンプルコードを示しています。
keywords: Excelタブの色をJavaScriptを介してC++で設定するコードについて説明します。
---

{{% alert color="primary" %}}

Aspose.Cells を使用すると、個々のワークシートタブの色を変更して目立たせることができます。たとえば、Expenses を赤、Sales を緑、Assets を青などにすることができます。

{{% /alert %}}
## **Microsoft Excel でワークシートのタブの色を設定する**
1. 現在のワークシートの下部にあるタブシートでタブを右クリックします。
1. **タブの色**を選択します。
1. パレットから色を選択します。
1. **OK** をクリックします。
## **Aspose.Cellsでワークシートのタブの色を設定する**
以下のサンプルコードは、Aspose.Cellsでタブの色を設定する方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Worksheet Tab Color Example</title>
    </head>
    <body>
        <h1>Set Worksheet Tab Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);
            worksheet.tabColor = AsposeCells.Color.Red;
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'worksheettabcolor.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet tab color set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
