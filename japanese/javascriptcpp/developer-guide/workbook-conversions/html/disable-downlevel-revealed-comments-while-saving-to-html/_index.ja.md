---
title: Downlevel Revealed Commentsを無効にしてJavaScript経由のC++でHTMLに保存します。
linktitle: HTMLへの保存時にDownlevel表示されたコメントを無効にする
type: docs
weight: 20
url: /ja/javascript-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: ExcelファイルをHTMLに保存する際にdownlevel revealedコメントを無効にする方法をAspose.Cells for JavaScriptを使用して学びます（C++）。
---

## **可能な使用シナリオ**

ExcelファイルをHTMLに保存するとき、Aspose.CellsはDownlevel Conditional Commentsを表示します。これらの条件付きコメントは主に古いバージョンのInternet Explorerに関連しており、現代のWebブラウザには関係ありません。詳細は以下のリンクで確認できます。

- [条件付きコメント - Downlevel-revealed条件付きコメント](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells for JavaScriptを使用したC++でこれらのDownlevel Revealed Commentsを [**HtmlSaveOptions.disableDownlevelRevealedComments**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableDownlevelRevealedComments--) プロパティを **true** に設定することで削除できます。

## **HTML への保存時にダウンレベルの表示されたコメントを無効にする**

以下のサンプルコードは[**HtmlSaveOptions.disableDownlevelRevealedComments**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableDownlevelRevealedComments--)プロパティの使い方を示しており、設定されていない場合の効果もスクリーンショットで示しています。このコードで使用されるサンプルExcelファイル（50528257.xlsx）と、生成された出力HTML（50528258.zip）も参考としてダウンロードしてください。

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Disable Downlevel Revealed Comments Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;

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

            // Load sample workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Disable DisableDownlevelRevealedComments
            const opts = new HtmlSaveOptions();
            opts.disableDownlevelRevealedComments = true;

            // Save the workbook in html
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDisableDownlevelRevealedComments_true.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved as HTML with DisableDownlevelRevealedComments = true. Click the download link to get the result.</p>';
        });
    </script>
</html>
```
