---
title: JavaScriptを使用してC++のIFilePathProviderインターフェースを介してエクスポートされたワークシートのHTMLファイルのパスを提供します。
linktitle: IFilePathProviderインターフェースを介してエクスポートされたワークシートのHTMLファイルパスを提供する
type: docs
weight: 70
url: /ja/javascript-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **可能な使用シナリオ**
複数のシートを持つExcelファイルがあり、それぞれのシートを個別のHTMLファイルにエクスポートしたい場合、シートのリンクが切れる可能性があります。この問題を解決するために、Aspose.Cells for JavaScriptは、[IFilePathProvider](https://reference.aspose.com/cells/javascript-cpp/ifilepathprovider)インターフェースを提供し、実装してリンクの修正を行うことができます。

## **IFilePathProviderインターフェースを介してエクスポートされたワークシートのHTMLファイルパスを提供する**
次のコードで使用されるサンプルExcelファイル([sample excel file](5115213.zip))とエクスポートされたHTMLファイルをダウンロードしてください。これらのファイルはすべてTempディレクトリ内にあります。C:ドライブに解凍してください。その後、C:\Tempディレクトリになります。その後、ブラウザでSheet1.htmlファイルを開き、中のリンクを2つクリックします。これらのリンクは、C:\Temp\OtherSheetsディレクトリ内にあるこれらの2つのエクスポートされたHTMLワークシートを参照しています。

{{< highlight javascript >}}
 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1
{{< /highlight >}}

次のスクリーンショットは、C:\Temp\Sheet1.htmlおよびそのリンクの外観を示しています。

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

以下のスクリーンショットはHTMLソースを示しています。リンクは現在C:\Temp\OtherSheetsディレクトリを参照しています。これは[IFilePathProvider](https://reference.aspose.com/cells/javascript-cpp/ifilepathprovider)インターフェースを使用して実現されました。

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)

## **サンプルコード**
C:\Tempディレクトリはあくまで例示用です。好きなディレクトリを使用し、[サンプルExcelファイル](5115211.xlsx)をそこに配置して、提供されたサンプルコードを実行できます。すると、そのディレクトリ内にOtherSheetsサブディレクトリを作成し、その中に2番目と3番目のワークシートのHTMLをエクスポートします。コード内のdirPath変数を変更し、実行前に任意のディレクトリを指定してください。

{{% alert color="primary" %}} 

サンプルコードは、ライセンスが設定されている場合のみ動作します。ライセンスを設定せずにコードを実行すると、無限ループに入ります。そのため、ライセンスが設定されていない場合はメッセージを表示し、実行を停止するチェックを追加しています。ライセンスを購入するか、Aspose.Purchaseチームから30日間の一時ライセンスをリクエストしてください。

{{% /alert %}} 

これらの行をコード内でコメントアウトすると、Sheet1.htmlのリンクが壊れ、リンクをクリックしてもSheet2.htmlやSheet3.htmlが開きません。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Worksheet to HTML with FilePathProvider Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

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

        // Implementation of IFilePathProvider for browser
        class FilePathProvider extends AsposeCells.IFilePathProvider {
            constructor() {
                super();
            }

            // Converted method name from getFullName -> fullName per universal getter/setter conversion rule
            fullName(sheetName) {
                if (sheetName === "Sheet2") {
                    return "file:///OtherSheets/Sheet2.html";
                } else if (sheetName === "Sheet3") {
                    return "file:///OtherSheets/Sheet3.html";
                }
                return "";
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HtmlSaveOptions and assign FilePathProvider (converted setter to property assignment)
            const options = new HtmlSaveOptions();
            options.filePathProvider = new FilePathProvider();

            // Save workbook to HTML using options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">HTML exported successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - IFilePathProvider</title>
    </head>
    <body>
        <h1>Aspose.Cells IFilePathProvider Example (Browser)</h1>
        <p>Select the Sample_filepath.xlsx file to export worksheets to separate HTML files.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <div id="links"></div>
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

        // Implementation of IFilePathProvider interface for browser
        class FilePathProvider extends AsposeCells.IFilePathProvider {
            constructor() {
                super();
            }

            // Gets the full path of the file by worksheet name when exporting worksheet to html separately.
            // So the references among the worksheets could be exported correctly.
            getFullName(sheetName) {
                if (sheetName === "Sheet2") {
                    return "file:///OtherSheets/Sheet2.html";
                } else if (sheetName === "Sheet3") {
                    return "file:///OtherSheets/Sheet3.html";
                }
                return "";
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            const linksDiv = document.getElementById('links');
            linksDiv.innerHTML = '';
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select the Sample_filepath.xlsx file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Check license
            if (!workbook.isLicensed()) {
                resultDiv.innerHTML = '<p style="color: red;">You must set the license to execute this code successfully.</p>';
                return;
            }

            // Export each worksheet to separate HTML using HtmlSaveOptions and FilePathProvider
            const sheetCount = workbook.worksheets.count;

            for (let i = 0; i < sheetCount; i++) {
                // Set the active worksheet to current index
                workbook.worksheets.activeSheetIndex = i;

                // Create html save option
                const options = new HtmlSaveOptions();
                options.exportActiveWorksheetOnly = true;
                // Provide file path provider so hyperlinks among sheets are preserved correctly
                options.filePathProvider = new FilePathProvider();

                // Save the active worksheet to HTML (returns Uint8Array)
                const outputData = workbook.save(SaveFormat.Html, options);

                // Create downloadable blob for the HTML
                const blob = new Blob([outputData], { type: 'text/html' });

                // Determine filename similar to original logic
                const sheetIndex = i + 1;
                let filename = '';
                if (i === 0) {
                    filename = 'Sheet1.html';
                } else {
                    filename = `OtherSheets_Sheet${sheetIndex}_out.html`;
                }

                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = filename;
                link.textContent = 'Download ' + filename;
                link.style.display = 'block';
                linksDiv.appendChild(link);
            }

            resultDiv.innerHTML = '<p style="color: green;">Worksheets exported successfully! Use the links below to download each HTML file.</p>';
        });
    </script>
</html>
```
