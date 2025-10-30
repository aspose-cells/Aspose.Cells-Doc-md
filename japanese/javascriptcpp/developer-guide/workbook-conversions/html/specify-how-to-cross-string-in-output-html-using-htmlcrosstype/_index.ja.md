---
title: JavaScriptを使用してC++で出力HTML内の文字列を交差させる方法を指定します（HtmlCrossTypeを使用）
linktitle: 出力HTML内の文字列をHtmlCrossTypeを使用してクロスする方法を指定
type: docs
weight: 140
url: /ja/javascript-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Aspose.Cells for JavaScriptを使用してC++でHTMLの出力における文字列のオーバーフローを制御する方法を学習します。
---

## **可能な使用シナリオ**

セルにテキストまたは文字列が含まれている場合でも、その幅を超えると次の列のセルがnullまたは空の場合に文字列がはみ出します。ExcelファイルをHTMLに保存するとき、[**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype)列挙型を使用してこのはみ出しを制御できます。主な値は以下の通りです：

- **HtmlCrossType.Default**: MS Excelのように表示; 次のセルに依存します。次のセルがnullの場合、文字列は跨るか切り捨てられます。

- **HtmlCrossType.MSExport**: 文字列はMS ExcelでHTMLをエクスポートしたように表示されます。

- **HtmlCrossType.Cross**: HTMLのクロス文字列を表示; 大きなHTMLファイルの作成パフォーマンスは、DefaultやFitToCell設定の十倍以上高速です。

- **HtmlCrossType.FitToCell**: 文字列をセル内の幅に合わせて表示します。

## **出力HTML内の文字列をHtmlCrossTypeを使用してクロスする方法を指定**

以下のサンプルコードは、[サンプルExcelファイル](51740732.xlsx)を読み込み、異なる [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) を指定してHTML形式に保存します。このコードで生成された[出力HTML](51740734.zip)をダウンロードしてください。サンプルExcelファイルには、赤色の枠線で囲まれた画像が含まれています。このスクリーンショットは、[**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) の値が出力HTMLに与える影響を示しています。

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export HTML Cross String Type Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, HtmlCrossType, Utils } = AsposeCells;

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

            // Specify HTML Cross Type via HtmlSaveOptions
            const opts = new HtmlSaveOptions();
            // Applying the sequence of assignments as in the original JavaScript code
            opts.htmlCrossStringType = HtmlCrossType.Default;
            opts.htmlCrossStringType = HtmlCrossType.MSExport;
            opts.htmlCrossStringType = HtmlCrossType.Cross;
            opts.htmlCrossStringType = HtmlCrossType.FitToCell;

            // Save workbook to HTML using the specified options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: "text/html" });
            const downloadLink = document.getElementById('downloadLink');
            const fileName = 'out' + opts.htmlCrossStringType + '.htm';
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = fileName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML exported successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
