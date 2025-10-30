---
title: スプレッドシートをCSVフォーマットにエクスポートする際、空白行のセパレータを保持する
linktitle: スプレッドシートをCSV形式にエクスポートする際に、空行のセパレーターを保持します
type: docs
weight: 160
url: /ja/javascript-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **CSV形式へのスプレッドシートのエクスポート時に空行の区切り記号を保持する**  

Aspose.Cells は、スプレッドシートを CSV 形式に変換する際に行の区切りを保持する機能を提供します。これには [**TxtSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/) の [**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--) プロパティを使用します。[**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--) はブール型のプロパティです。Excel ファイルを CSV に変換する際に空白行の区切りを保持したい場合は、[**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--) プロパティを **true** に設定します。  

以下のサンプルコードは、[ソースExcelファイル](84378743.xlsx)を読み込み、[**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--)プロパティを**true**に設定し、[出力.csv](84378744.csv)として保存します。スクリーンショットは、ソースExcelファイル、CSV変換時に生成されたデフォルト出力、そして[**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--)を**true**に設定した場合の出力の比較を示しています。  

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)  

## **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TxtSaveOptions Example</title>
    </head>
    <body>
        <h1>TxtSaveOptions to CSV Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to CSV</button>
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

            // Create a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate TxtSaveOptions
            const options = new TxtSaveOptions();

            // Set KeepSeparatorsForBlankRow to true to show separators in blank rows
            options.keepSeparatorsForBlankRow = true;

            // Save the workbook to CSV using the options
            const outputData = workbook.save(SaveFormat.CSV, options);

            const blob = new Blob([outputData], { type: 'text/csv' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.csv';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CSV File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the CSV file.</p>';
        });
    </script>
</html>
```
