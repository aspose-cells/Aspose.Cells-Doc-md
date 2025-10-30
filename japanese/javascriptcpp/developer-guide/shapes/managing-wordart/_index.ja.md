---
title: ワークシートにWordArtウォーターマークを追加する方法（C++を使用したJavaScript）
linktitle: ワードアートの管理
type: docs
weight: 180
url: /ja/javascript-cpp/add-wordart-watermark-to-worksheet/
description: C++を使用したAspose.Cells for JavaScriptでワークシートにWordArtを背景ウォーターマークとして追加する方法を学びます。
---

{{% alert color="primary" %}} 

WordArtを使用してスプレッドシートに特殊なテキスト効果を追加できます。たとえば、タイトルをファイルの上に広げたり、テキストを装飾したり、テキストをプリセットの形状に合わせたり、Excelシートにテキストを背景ウォーターマークとして適用したりできます。WordArtは、スプレッドシートに追加するための移動や配置が可能なオブジェクトになります。

{{% /alert %}} 

次の例では、ワークシートの背景ウォーターマークとしてワードアート形状を追加する方法を示します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Watermark Example</h1>
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

            // If a file is provided, open it. Otherwise create a new workbook.
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first default sheet
            const sheet = workbook.worksheets.get(0);

            // Add Watermark
            const wordart = sheet.shapes.addTextEffect(AsposeCells.MsoPresetTextEffect.TextEffect1,
                "CONFIDENTIAL", "Arial Black", 50, false, true, 18, 8, 1, 1, 130, 800);

            // Get the fill format of the word art
            const wordArtFormat = wordart.fill;            

            // Set the transparency
            wordArtFormat.transparency = 0.9;

            // Make the line invisible
            const lineFormat = wordart.line;
            lineFormat.visible = false;

            // Saving the modified Excel file (Excel97-2003 format .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Watermark_Test.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File with Watermark';

            document.getElementById('result').innerHTML = '<p style="color: green;">Watermark added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **高度なトピック**
- [組み込みスタイルを持つ WordArt テキストを追加する](/cells/ja/javascript-cpp/add-word-art-text-with-built-in-styles/)
- [WordArtウォーターマークをロックする](/cells/ja/javascript-cpp/locking-wordart-watermark/)
- [テキストのシェイプに組み込みのWordArtスタイルを設定する](/cells/ja/javascript-cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
