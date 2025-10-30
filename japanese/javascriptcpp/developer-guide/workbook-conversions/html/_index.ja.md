---
title: HTMLをJavaScript経由でC++
linktitle: HTML
type: docs
weight: 230
url: /ja/javascript-cpp/convert-excel-to-html/
---

## **ExcelワークブックをHTMLに変換する**
Aspose.Cells APIは、スプレッドシートをHTML形式にエクスポートする機能をサポートしています。これには、出力HTMLの複数の側面を制御する柔軟性を提供する [**HtmlSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions) クラスを使用します。

 以下のコード例は、JavaScript経由でC++を使用してワークブックをHTMLファイルとして保存する方法を示しています：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Excel to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to HTML</button>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook to HTML format
            const outputData = workbook.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```


## **ExcelワークブックをMHTMLファイルに変換する**
MHTMLは、通常のHTMLに外部リソース（画像やアニメーション、音声など）を結合し、一つのファイルにまとめたものです。.mht拡張子のメールに使用されます。Aspose.Cellsは、MHTMLファイルの読み書きをサポートしています。

 以下のコード例は、JavaScriptを経由してC++を使用してワークブックをMHTMLファイルとして保存する方法を示しています：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Save as MHT</title>
    </head>
    <body>
        <h1>Save Excel as MHT Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your source workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save file to MHT format
            const outputData = workbook.save(SaveFormat.MHtml);
            const blob = new Blob([outputData], { type: 'application/octet-stream' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.mht';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download MHT File';

            resultDiv.innerHTML = '<p style="color: green;">File converted to MHT successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```

## **高度なトピック**
- [ワークブックにHTMLをロードする際の列と行を自動調整する](/cells/ja/javascript-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [HTMLからの大きな数値の指数表記を回避する](/cells/ja/javascript-cpp/avoid-exponential-notation-of-large-numbers-while-importing/)
- [HTMLリンクのターゲットタイプを変更する](/cells/ja/javascript-cpp/change-the-html-link-target-type/)
- [ツールチップ付きでExcelをHTMLに変換する](/cells/ja/javascript-cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/ja/javascript-cpp/create-transparent-image-of-excel-worksheet/)
- [HTMLのインポート時に改行後の余分なスペースを削除する](/cells/ja/javascript-cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [HTML への保存時にダウンレベルの表示されたコメントを無効にする](/cells/ja/javascript-cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [フレームスクリプトとドキュメントプロパティのエクスポートを無効にする](/cells/ja/javascript-cpp/disable-exporting-frame-scripts-and-document-properties/)
- [ExcelをHTMLに変換する際にPresentationPreferenceオプションを使用してレイアウトを向上させる](/cells/ja/javascript-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [ExcelからHTMLへの変換時に未使用のスタイルを除外](/cells/ja/javascript-cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Excel ファイルを HTML にエクスポートする際にテキストを右から左に展開](/cells/ja/javascript-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Excel を HTML に変換する際の DataBar、ColorScale、および IconSet 条件付き書式をエクスポート](/cells/ja/javascript-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [ExcelファイルをHTMLに保存する際にコメントをエクスポート](/cells/ja/javascript-cpp/export-comments-while-saving-excel-file-to/)
- [Excel を HTML に変換する際に文書のワークブックとワークシートのプロパティをエクスポート](/cells/ja/javascript-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [グリッドライン付きでExcelをHTMLにエクスポートする](/cells/ja/javascript-cpp/export-excel-to-html-with-gridlines/)
- [印刷範囲を HTML にエクスポート](/cells/ja/javascript-cpp/export-print-area-range-to/)
- [Webブラウザでサポートされていない場合の類似の境界線スタイルをHTMLにエクスポートする](/cells/ja/javascript-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [出力HTMLでワークシートのCSSを別々にエクスポートする](/cells/ja/javascript-cpp/export-worksheet-css-separately-in-output/)
- [HTMLに保存する際のボーダースタイルがWebブラウザでサポートされていない場合に似たボーダースタイルをエクスポートする](/cells/ja/javascript-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [HtmlSaveOptions.TableCssIdプロパティの使用方法についてのサンプルコードを以下に説明します。参照のために、コードによって生成された[output HTML](60489791.zip)を確認してください。](/cells/ja/javascript-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [HTMLに保存する際に非表示のワークシートコンテンツをエクスポートしない](/cells/ja/javascript-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [IFilePathProviderインターフェースを介してエクスポートされたワークシートのhtmlファイルパスを提供](/cells/ja/javascript-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)
- [自己終了タグを認識](/cells/ja/javascript-cpp/recognise-self-closing-tags/)
- [スプレッドシートをHTMLに変換する際にWordArtのグラデーション塗りをレンダリング](/cells/ja/javascript-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [列の幅をemやpercentなどのスケーラブルな単位に設定します](/cells/ja/javascript-cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [スプレッドシートをHTMLにレンダリングする際のデフォルトフォントを設定する](/cells/ja/javascript-cpp/set-default-font-while-rendering-spreadsheet-to/)
- [出力HTML内の文字列をHtmlCrossTypeを使用してクロスする方法を指定](/cells/ja/javascript-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [HTMLをエクセルブックにロードする際にDIVタグのレイアウトをサポート](/cells/ja/javascript-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)

- [次のサンプルコードは、{0} 属性の使用例を示しています。このプロパティがTrueに設定されていない場合の効果もスクリーンショットで示しています。[サンプルExcelファイル](50528260.xlsx)と生成された[出力HTML](50528261.zip)をダウンロードして参照してください。](/cells/ja/javascript-cpp/enable-css-custom-properties-while-saving-to-html/)
