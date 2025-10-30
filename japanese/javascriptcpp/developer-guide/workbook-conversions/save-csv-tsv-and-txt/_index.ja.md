---
title: JavaScriptを使用したExcelからCSV、TSV、TXTへの変換
linktitle: CSV、TSV、TXTとして保存
type: docs
weight: 40
url: /ja/javascript-cpp/convert-excel-to-csv-tsv-and-txt/
description: ExcelファイルをCSV、TSV、TXT形式に変換する方法をAspose.Cells for JavaScript via C++で学びましょう。
---

{{% alert color="primary" %}}

Aspose.Cellsは、Excel、ODS、JSONなどのさまざまなフォーマットのファイルをCSV、TSV、TXTに変換できます。

{{% /alert %}}

## **ワークブックをテキストまたはCSV形式で保存**

複数のワークシートを持つワークブックをテキスト形式に変換または保存したい場合があります。テキスト形式（例：TXT、TabDelim、CSVなど）の場合、デフォルトではMicrosoft ExcelとAspose.Cellsはアクティブなワークシートの内容のみを保存します。

以下のコード例では、ワークブック全体をテキスト形式で保存する方法を説明します。ソースワークブックを読み込み、任意のMicrosoft ExcelまたはOpenOfficeのスプレッドシートファイル（XLS、XLSX、XLSM、XLSB、ODSなど）に含まれる複数のワークシートを扱います。

コードを実行すると、ワークブックのすべてのシートのデータがTXT形式に変換されます。

同じ例を修正してファイルをCSV形式に保存することもできます。デフォルトでは、[**TxtSaveOptions.separator**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#separator--)はカンマなので、CSV形式で保存する場合はセパレータを指定しないでください。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Txt Save Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Txt Save Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtSaveOptions, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Text save options. You can use any type of separator
            const opts = new TxtSaveOptions();
            opts.separator = '\t';
            opts.exportAllSheets = true;

            // Save entire workbook data into file (as text)
            const outputData = workbook.save(SaveFormat.Txt, opts);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.txt';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Text File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved as text. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **カスタム区切り文字でテキストファイルを保存**

テキストファイルには書式がないスプレッドシートデータが含まれます。ファイルは、データ間にいくつかのカスタマイズされた区切り記号があるプレーンテキストファイルの種類です。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Workbook to TXT/CSV Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, TxtSaveOptions, SaveFormat } = AsposeCells;

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

            // Create a Workbook object from the uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate Text File's Save Options
            const options = new TxtSaveOptions();

            // Specify the separator
            options.separator = ";";

            // Optionally specify CSV save format if required by the API
            options.saveFormat = SaveFormat.CSV;

            // Save the workbook to CSV/TXT using the options
            const outputData = wb.save(SaveFormat.CSV, options);
            const blob = new Blob([outputData], { type: 'text/csv' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.csv';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CSV File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```


## **高度なトピック**
- [CSV形式へのスプレッドシートのエクスポート時に空行の区切り記号を保持する](/cells/ja/javascript-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [スプレッドシートをCSV形式にエクスポートする際に先行する空白行と列をトリミングします。](/cells/ja/javascript-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
