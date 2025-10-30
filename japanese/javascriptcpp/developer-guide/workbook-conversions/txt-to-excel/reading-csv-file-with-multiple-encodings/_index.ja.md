---
title: JavaScriptを介して複数エンコーディングのCSVファイルを読む
linktitle: 複数のエンコーディングでのCSVファイルの読み込み
type: docs
weight: 200
url: /ja/javascript-cpp/reading-csv-file-with-multiple-encodings/
description: 異なるエンコーディングを持つCSVファイルの読み取り方法をAspose.Cells for JavaScriptを使って学びます。
---

{{% alert color="primary" %}}

時には、CSV ファイルが複数のエンコーディング（Unicode、ANSI、UTF8、UTF7 など）を含む場合があります。Aspose.Cells を使えば、そのようなCSVファイルを正しく読み込み、他のフォーマット（PDFや XLSX など）に変換できます。

{{% /alert %}}

Aspose.Cellsは[**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--)プロパティを提供しており、これを**true**に設定する必要があります。そうすることで、複数エンコーディングのCSVファイルを正しく読み込むことができます。

以下のスクリーンショットは、2行を含むサンプルCSVファイルを示しています。1行目は**ANSI**エンコーディングで、2行目は**Unicode**エンコーディングです

|**入力ファイル**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

以下のスクリーンショットは、上記のCSVファイルから変換されたXLSXファイルを、[**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--)プロパティを**true**に設定しなかった場合を示しています。ご覧のとおり、Unicodeテキストは正しく変換されませんでした。

|**出力ファイル1: 複数のエンコーディングを考慮していない**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

以下のスクリーンショットは、[**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--) プロパティを **true** に設定した後、上記 CSV ファイルから変換された XLSX ファイルです。Unicode テキストは正しく変換されました。

|**出力ファイル2: IsMultiEncodedをtrueに設定**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

以下は、上記のCSVファイルを正しくXLSX形式に変換するサンプルコードです。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Multi-Encoded CSV to XLSX</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Convert to XLSX</button>
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

            // Create TxtLoadOptions and set isMultiEncoded property
            const options = new TxtLoadOptions();
            options.isMultiEncoded = true;

            // Load the CSV into a Workbook using the options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            const outName = file.name.replace(/(\.[^/.]+)$/, '$1.out.xlsx');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = outName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to save the XLSX file.</p>';
        });
    </script>
</html>
```

## 関連記事

- [CSV ファイルを開く](/cells/ja/javascript-cpp/opening-files-with-different-formats/#opening-csv-files)
