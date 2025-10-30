---
title: フォーム付きCSVファイルを読み込むまたはインポートする via JavaScript
linktitle: 数式を持つCSVファイルを読み込むまたはインポートする
type: docs
weight: 350
url: /ja/javascript-cpp/load-or-import-csv-file-with-formulas/
description: フォーム付きCSVファイルの読み込みとインポート方法をAspose.Cells for JavaScriptを使って学びます。
---

{{% alert color="primary" %}}

CSVファイルは大部分がテキストデータであり、数式を含まないことが多いですが、まれに数式を含むCSVファイルもあります。そのようなCSVファイルは、[TxtLoadOptions.hasFormula](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#hasFormula--)を**true**に設定して読み込む必要があります。このプロパティを**true**に設定すると、Aspose.Cellsは数式を単なるテキストとして扱わず、通常の数式として処理します。Aspose.Cellsの数式計算エンジンがこれを処理します。

{{% /alert %}}

以下のコードは、数式を含む CSV ファイルのロードとインポートの例です。任意の CSV ファイルを使用できます。例として、[シンプルな CSV ファイル](5115034.csv) を使い、データを示します。ご覧の通り、数式を含んでいます。

{{< highlight javascript >}}
<!DOCTYPE html>
<html>
    <head>
        <title>Load CSV with Formulas and Save as XLSX</title>
    </head>
    <body>
        <h1>Load CSV with Formulas and Save as XLSX</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="convertToXlsx">Convert to XLSX</button>
        <a id="downloadLink" style="display: none;">Download XLSX</a>
        <div id="result"></div>

        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, TxtLoadOptions, SaveFormat } = AsposeCells;

            AsposeCells.onReady().then(() => {
                console.log("Aspose.Cells initialized");
            });

            document.getElementById('convertToXlsx').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                const loadOptions = new TxtLoadOptions();
                loadOptions.hasFormula = true;

                const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = file.name.replace(/\.csv$/i, '.xlsx');
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download XLSX File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed! Click the download link to get the XLSX file.</p>';
            });
        </script>
    </body>
</html>
{{< /highlight >}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells CSV Load Example</title>
    </head>
    <body>
        <h1>Load CSV with Formulas and Save as XLSX</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtLoadOptions, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const bytes = new Uint8Array(arrayBuffer);

            // TxtLoadOptions configuration
            const opts = new TxtLoadOptions();
            opts.separator = ',';
            opts.hasFormula = true;

            // Load your CSV file with formulas in a Workbook object
            const workbook = new Workbook(bytes, opts);

            // You can also import your CSV file like this
            // The code below is importing CSV file starting from cell D4 (rowIndex=3, colIndex=3)
            const worksheet = workbook.worksheets.get(0);
            worksheet.cells.importCSV(bytes, opts, 3, 3);

            // Save your workbook in Xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the converted file.</p>';
        });
    </script>
</html>
```

まずCSVファイルを読み込み、その後セルD4に再度インポートします。最後に、ワークブックオブジェクトをXLSX形式で保存します。[出力されるXLSXファイル](5115052.xlsx)はこのようになります。ご覧のとおり、セルC3とF4に数式が含まれており、その結果は800です。

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|  
| :- |
