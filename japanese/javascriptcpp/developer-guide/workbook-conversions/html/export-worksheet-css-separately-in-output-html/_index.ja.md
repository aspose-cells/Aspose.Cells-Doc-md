---
title: 出力HTMLにワークシートのCSSを個別にエクスポート JavaScript via C++
linktitle: 出力HTMLでワークシートのCSSを別々にエクスポートする
type: docs
weight: 80
url: /ja/javascript-cpp/export-worksheet-css-separately-in-output/
description: ExcelをHTMLに変換する際に、ワークシートのCSSを個別にエクスポートする方法をAspose.Cells for JavaScript via C++で学びます。
---

## **可能な使用シナリオ**

Aspose.Cells for JavaScript via C++は、ExcelファイルをHTMLに変換する際にワークシートのCSSを個別にエクスポートする機能を提供します。この目的のために[**HtmlSaveOptions.exportWorksheetCSSSeparately**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorksheetCSSSeparately--)プロパティを使用し、ExcelファイルをHTMLに保存する際に**true**に設定してください。

## **出力HTMLでワークシートのCSSを別々にエクスポートする**

次のサンプルコードは、Excelファイルを作成し、セル**B5**に赤色のテキストを追加して保存します。[**HtmlSaveOptions.exportWorksheetCSSSeparately**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorksheetCSSSeparately--)プロパティを使ったHTML形式で保存し、参考として[出力HTML](60489766.zip)も確認できます。サンプルコードによって生成された状態では**stylesheet.css**も含まれています。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Worksheet CSS Separately Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Color, Utils } = AsposeCells;

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
            // Create a new workbook
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

            // Specify html save options - export worksheet css separately
            const opts = new HtmlSaveOptions();
            opts.exportWorksheetCSSSeparately = true;

            // Save the workbook in html 
            const outputData = wb.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportWorksheetCSSSeparately.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved as HTML. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **単一のシートのワークブックをHTMLにエクスポートする**

複数のシートを持つブックをAspose.Cells for JavaScript via C++を使ってHTMLに変換すると、HTMLファイルとともにCSSを含むフォルダや複数のHTMLファイルが作成されます。このHTMLファイルをブラウザで開くとタブが表示されます。単一ワークシートのブックの場合も同じ動作が必要ですが、以前は単一シートのワークブック用にフォルダは作成されず、HTMLファイルのみが作成されていました。そのため、そのHTMLファイルをブラウザで開くとタブは表示されませんでした。Microsoft Excelは単一シートのブック用にも正しいフォルダとHTMLを作成しますので、その動作をAspose.Cells APIで実現しています。以下のリンクからサンプルファイルをダウンロードし、下記のサンプルコードで使用できます。

[sampleSingleSheet.xlsx](79527937.xlsx)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Save Workbook as HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, EncodingType, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify HTML save options
            const options = new HtmlSaveOptions();

            // Set optional settings (converted from setters to properties)
            options.encoding = EncodingType.UTF8;
            options.exportImagesAsBase64 = true;
            options.exportGridLines = true;
            options.exportSimilarBorderStyle = true;
            options.exportBogusRowData = true;
            options.excludeUnusedStyles = true;
            options.exportHiddenWorksheet = true;

            // Save the workbook in HTML format with specified HtmlSaveOptions
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSampleSingleSheet.htm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook saved to HTML. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
