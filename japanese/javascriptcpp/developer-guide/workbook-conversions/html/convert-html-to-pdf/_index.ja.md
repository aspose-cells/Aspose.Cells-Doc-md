---
title: JavaScriptを使用したHTMLをPDFに変換する方法
linktitle: HTMLをPDFに変換する方法
type: docs
weight: 80
url: /ja/javascript-cpp/convert-html-to-pdf/
description: このトピックでは、Aspose.Cells for JavaScriptを使用してHTMLおよびMHTMLをPDFに変換する方法を紹介します。
keywords: JavaScriptを使用してHTMLとMHTMLをPDFに変換 
---

## **概要**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>HTMLをPDFに変換する</b>. It covers the following topics.

<ul>
<li><a href="#js-convert-html-to-pdf">JavaScriptを使ったHTMLからPDFへの変換</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScriptを使ったHTMLをPDFに変換</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScriptでHTMLをPDFに変換する方法</a></li>
</ul>

## **JavaScriptによるHTMLからPDFへの変換**
HTMLをPDFに変換するには？ [Aspose.Cells for JavaScriptを使用したC++](https://releases.aspose.com/cells/javascript-cpp/)ライブラリを使用すれば、数行のコードでHTMLからPDFへ簡単にプログラム的に変換できます。Aspose.Cells for JavaScriptは、クロスプラットフォームアプリケーションの構築、Excelファイルの生成、変更、変換、レンダリング、および印刷が可能です。

## **JavaScriptを使ったHTMLをPDFに変換**
以下のJavaScriptコードサンプルは、[Aspose.Cells for JavaScriptを使用したHTMLからPDFへ変換](https://releases.aspose.com/cells/javascript-cpp/)方法を示しています。

1. [HtmlLoadOptions](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/)クラスのインスタンスを作成します。
[ワークブック](https://reference.aspose.com/cells/javascript-cpp/workbook/) オブジェクトを初期化します。
1. Workbook.save() メソッドを呼び出して、出力 PDF ドキュメントを保存します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells HTML to PDF Example</title>
    </head>
    <body>
        <h1>Convert HTML to PDF using Aspose.Cells</h1>
        <input type="file" id="fileInput" accept=".html,.htm" />
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an HTML file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const options = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **オンラインでHTMLをPDFに変換してみてください**

[Aspose.Cells for JavaScript via C++](https://releases.aspose.com/cells/javascript-cpp/) presents you online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">「HTMLをPDFに」</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
