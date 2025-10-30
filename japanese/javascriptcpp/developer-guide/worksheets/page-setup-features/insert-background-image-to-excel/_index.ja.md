---
title: C++経由のJavaScriptを使ってExcelに背景画像を挿入
linktitle: Excelに背景画像を挿入する
type: docs
weight: 90
url: /ja/javascript-cpp/insert-background-image-to-excel/
description: "C++経由のAspose.Cells for JavaScriptを使用してExcelに背景画像を挿入する方法"
---

{{% alert color="primary" %}} 

特別な要素がシート上のデータを遮らずに背景のヒントを追加する特別な企業図形がある場合、これはワークシートをより魅力的にすることができます。Aspose.Cells APIを使用して、シートの背景画像を追加することができます。

{{% /alert %}} 

## **Microsoft Excelでのシートの背景の設定方法（例：Microsoft Excel 2019）：**

1. **ページレイアウト**メニューから**ページの設定**オプションを見つけ、**背景**オプションをクリックします。

1. **ページレイアウト**メニューから**ページ設定**オプションを見つけ、**背景**オプションをクリックします。
1. シートの背景画像を設定するために画像を選択します。

   シートの背景を設定する

![todo:image_alt_text](insert-background-to-excel.jpg)

## ** C++経由のAspose.Cells for JavaScriptを使ったシート背景設定**

以下のコードは、ストリームから画像を使用して背景画像を設定します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Worksheet Background Image</title>
    </head>
    <body>
        <h1>Set Worksheet Background Image Example</h1>
        <p>
            Select a background image to apply to a new workbook's first worksheet,
            then click "Apply Background & Save" to generate XLSX and HTML files.
        </p>
        <input type="file" id="bgInput" accept="image/*" />
        <button id="runExample">Apply Background & Save</button>
        <a id="downloadXlsx" style="display: none; margin-left: 10px;"></a>
        <a id="downloadHtml" style="display: none; margin-left: 10px;"></a>
        <div id="result" style="margin-top: 1em;"></div>
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
            const bgInput = document.getElementById('bgInput');
            const resultDiv = document.getElementById('result');

            if (!bgInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a background image file.</p>';
                return;
            }

            const bgFile = bgInput.files[0];
            const arrayBuffer = await bgFile.arrayBuffer();
            const imgBytes = new Uint8Array(arrayBuffer);

            // Create a new Workbook.
            const workbook = new Workbook();

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Set the background image for the worksheet.
            sheet.backgroundImage = imgBytes;

            // Save the Excel file (XLSX)
            const xlsxData = workbook.save(SaveFormat.Xlsx);
            const blobXlsx = new Blob([xlsxData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadXlsx = document.getElementById('downloadXlsx');
            downloadXlsx.href = URL.createObjectURL(blobXlsx);
            downloadXlsx.download = 'outputBackImageSheet.xlsx';
            downloadXlsx.style.display = 'inline';
            downloadXlsx.textContent = 'Download Excel File';

            // Save the HTML file
            const htmlData = workbook.save(SaveFormat.Html);
            const blobHtml = new Blob([htmlData], { type: 'text/html' });
            const downloadHtml = document.getElementById('downloadHtml');
            downloadHtml.href = URL.createObjectURL(blobHtml);
            downloadHtml.download = 'outputBackImageSheet.html';
            downloadHtml.style.display = 'inline';
            downloadHtml.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Background image applied. Download links are ready.</p>';
        });
    </script>
</html>
```

## 関連記事

- [ODSファイルで背景を操作する](/cells/ja/javascript-cpp/working-with-background-in-ods-files/)
