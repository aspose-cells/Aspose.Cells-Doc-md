---
title: JavaScriptを使用してHTMLリンクのターゲット種類を変更
linktitle: HTMLリンクのターゲットタイプを変更する
type: docs
weight: 320
url: /ja/javascript-cpp/change-the-html-link-target-type/
description: Aspose.Cells for JavaScriptを使用して、HTMLのリンクターゲットタイプを変更する方法を学びましょう。リンクのターゲット属性を制御します。
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、HTMLリンクのターゲットタイプを変更できます。HTMLリンクは以下のようになります。

{{< highlight javascript >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

上のHTMLリンクのターゲット属性は**_self**です。[**HtmlSaveOptions.linkTargetType**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#linkTargetType--)プロパティを使用してこのターゲット属性を制御できます。このプロパティは以下の値を持つ[**HtmlLinkTargetType**](https://reference.aspose.com/cells/javascript-cpp/htmllinktargettype)列挙型を受け取ります。

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

以下のコードは[**HtmlSaveOptions.linkTargetType**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#linkTargetType--)プロパティの使用例を示しています。リンクターゲットタイプを**blank**に変更します。デフォルトは**parent**です。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, HtmlLinkTargetType, Utils } = AsposeCells;

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

            // Create HTML save options and set link target type
            const opts = new HtmlSaveOptions();
            opts.linkTargetType = HtmlLinkTargetType.Self;

            // Save the workbook to HTML using the save options
            const outputData = workbook.save(SaveFormat.Html, opts);

            // Create a downloadable blob for the resulting HTML
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = `<p style="color: green;">File converted and ready for download: ${downloadLink.download}</p>`;
        });
    </script>
</html>
```
