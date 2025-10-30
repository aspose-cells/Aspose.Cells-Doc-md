---
title: HtmlSaveOptions.tableCssIdプロパティを使ってテーブル要素のスタイルにプレフィックスをつけます（JavaScript経由のC++）
linktitle: HtmlSaveOptions.tableCssIdプロパティを使ってテーブル要素のスタイルにプレフィックスをつけます
type: docs
weight: 110
url: /ja/javascript-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: HTMLでテーブル要素のスタイルに接頭辞を付ける方法をAspose.Cells for JavaScriptを使用してC++で学習します。
---

## **可能な使用シナリオ**

Aspose.Cellsは、[**HtmlSaveOptions.tableCssId**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#tableCssId--)プロパティを使用してテーブル要素のスタイルにプレフィックスを付けることを可能にします。例えば、このプロパティに**MyTest_TableCssId**などの値を設定すると、次のようなテーブル要素のスタイルが表示されます：

{{< highlight javascript >}}
 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
{{< /highlight >}}

以下のスクリーンショットは、[**HtmlSaveOptions.tableCssId**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#tableCssId--)プロパティを使用した結果のHTMLの効果を示しています。

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **HtmlSaveOptions.tableCssIdプロパティを使用してテーブル要素のスタイルにプレフィックスを付ける**

次のサンプルコードは、[**HtmlSaveOptions.tableCssId**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#tableCssId--)プロパティの使い方を示しています。参考のために、コードによって生成された[出力HTML](60489790.zip)を確認してください。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Set Cell Style and Save as HTML with Table CSS ID</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Color } = AsposeCells;

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
            if (fileInput.files.length === 0) {
                // No file selected - create a new workbook as in original JavaScript sample
                const wb = new Workbook();

                // Access first worksheet
                const ws = wb.worksheets.get(0);

                // Access cell B5 and put value inside it
                const cell = ws.cells.get("B5");
                cell.value = "This is some text.";

                // Set the style of the cell - font color is Red
                const st = cell.style;
                st.font.color = Color.Red;
                cell.style = st;

                // Specify html save options - specify table css id
                const opts = new HtmlSaveOptions();
                opts.tableCssId = "MyTest_TableCssId";

                // Save the workbook in html
                const outputData = wb.save(SaveFormat.Html, opts);
                const blob = new Blob([outputData], { type: 'text/html' });
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'outputTableCssId.html';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download HTML File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the HTML file.</p>';
                return;
            }

            // If a file is provided, open it and apply the same changes
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell B5 and put value inside it
            const cell = ws.cells.get("B5");
            cell.value = "This is some text.";

            // Set the style of the cell - font color is Red
            const st = cell.style;
            st.font.color = Color.Red;
            cell.style = st;

            // Specify html save options - specify table css id
            const opts = new HtmlSaveOptions();
            opts.tableCssId = "MyTest_TableCssId";

            // Save the workbook in html
            const outputData = wb.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputTableCssId.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
