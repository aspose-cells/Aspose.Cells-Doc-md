---
title: CSSのカスタムプロパティを有効にしてJavaScript経由のC++でHTMLに保存します。
linktitle: HTML保存時にCSSカスタムプロパティを有効にする方法を学びます。
type: docs
weight: 320
url: /ja/javascript-cpp/enable-css-custom-properties-while-saving-to-html/
description: ExcelファイルをHTMLに保存する際にCSSカスタムプロパティを有効にする方法をAspose.Cells for JavaScriptを使用して学びます（C++）。 
---

## **可能な使用シナリオ**

ExcelファイルをHTMLに保存するとき、特定のBase64画像について複数の出現箇所がある場合に、カスタムプロパティを使用して画像データを一度だけ保存し、結果のHTMLのパフォーマンスを向上させることができます。[**HtmlSaveOptions.enableCssCustomProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#enableCssCustomProperties--)プロパティを使用し、**true**に設定して保存してください。
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## **次のサンプルコードは、{0} 属性の使用例を示しています。このプロパティがTrueに設定されていない場合の効果もスクリーンショットで示しています。[サンプルExcelファイル](50528260.xlsx)と生成された[出力HTML](50528261.zip)をダウンロードして参照してください。**

以下のサンプルコードは[**HtmlSaveOptions.enableCssCustomProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#enableCssCustomProperties--)プロパティの使い方を示しており、設定されていない場合の効果もスクリーンショットで表示しています。このコードで使用されるサンプルExcelファイル（50528260.xlsx）と、生成された出力HTML（50528261.zip）も参考としてダウンロードしてください。



## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Enable CSS Custom Properties Example</title>
    </head>
    <body>
        <h1>Enable CSS Custom Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HtmlSaveOptions and set properties (converted from setters to property assignments)
            const opts = new AsposeCells.HtmlSaveOptions();
            opts.exportImagesAsBase64 = true;
            opts.enableCssCustomProperties = true;

            // Save the workbook to HTML using SaveFormat.Html and provided options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputEnableCssCustomProperties.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML saved successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
