---
title: 見出しと本文のテーマフォント
linktitle: 見出しと本文のテーマフォント
description: Aspose.Cellsは、スプレッドシートファイルを操作するためのC++経由のJavaScriptライブラリです。Excelドキュメントの見出しと本文のテーマフォント設定をサポートし、ユーザーがドキュメントの外観やスタイルをカスタマイズできるようにします。この記事では、Aspose.Cellsライブラリを使用してExcelドキュメントの見出しと本文のテーマフォントを操作する方法を紹介します。
keywords: Aspose.Cells、Excelドキュメント、見出し、本文、テーマフォント、外観、スタイル、JavaScript via C++
type: docs
weight: 120
url: /ja/javascript-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

リージョン設定が変更されると、既定のフォントは自動的に変更されます。

デフォルトフォントが変更されると、行の高さや列の幅も変更され、ページレイアウトが乱れることさえあります。

デフォルトフォントの変更の原因は何ですか？

Excelのテーマフォントが設定されている場合、Excelは現在の言語環境に応じて自動的に異なるフォントに切り替えます。

{{% /alert %}}

## **Excelでの見出しと本文のテーマフォント**

Excelで、ホームタブを選択し、フォントのドロップダウンボックスをクリックすると、「テーマフォント」が表示され、上部に英語のリージョン設定でCalibri Light（見出し）とCalibri（本文）の2つのテーマフォントがあります。

**![テーマフォント](Theme-Fonts.png)**

テーマフォントを選択すると、フォント名は異なるリージョンで異なる表示になります。リージョンに応じて自動的にフォントが変わるのを避けたい場合は、2つのテーマフォントを選択しないでください。

## **ヘッダーと本文のフォントをプログラムで変更**
C++経由のAspose.Cells for JavaScriptを使用して、デフォルトのフォントがテーマフォントかどうかを確認したり、[**Font.schemeType**](https://reference.aspose.com/cells/javascript-cpp/font/#schemeType-fontschemetype-)メソッドを使用してテーマフォントを設定したりできます。

次のサンプルコードは、テーマフォントを操作する方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Theme Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FontSchemeType, Utils } = AsposeCells;

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

            // Accessing and modifying the default style and its font scheme
            let defaultStyle = workbook.defaultStyle;
            let font = defaultStyle.font;
            let schemeType = font.schemeType;

            if (schemeType === FontSchemeType.Major || schemeType === FontSchemeType.Minor) {
                console.log("It's theme font");
            }

            // Change theme font to normal font
            font.schemeType = FontSchemeType.None;

            // Assign the modified default style back to the workbook
            workbook.defaultStyle = defaultStyle;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.modified.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Theme font changed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



## **動的にローカルテーマフォントをプログラム的に取得**
時々、サーバーとユーザーのマシンが同じ地域にないことがあります。ユーザーがファイル処理に望むフォントをどのように取得すればよいでしょうか？

ファイルを読み込む前に、[**LoadOptions.region**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#region-countrycode-)メソッドを使用してシステムのリージョン設定を設定する必要があります。

以下のサンプルコードは、ローカルのテーマフォントを取得する方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Default Style Local Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new LoadOptions.
            const options = new AsposeCells.LoadOptions();
            // Sets the customer's region
            options.region = AsposeCells.CountryCode.Japan;

            // Instantiate a new Workbook using the uploaded file and load options.
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Get the default style
            const defaultStyle = workbook.defaultStyle;

            // Gets customer's local font.
            const localFontName = defaultStyle.font.name;

            resultDiv.innerHTML = `<p style="color: green;">Local font name: ${localFontName}</p>`;
        });
    </script>
</html>
```
