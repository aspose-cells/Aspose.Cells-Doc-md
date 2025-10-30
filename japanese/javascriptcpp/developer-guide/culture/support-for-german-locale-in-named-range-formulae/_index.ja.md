---
title: JavaScriptをC++経由で、名前付き範囲のフォーミュラにドイツ語ロケールをサポートする方法
linktitle: 名前付き範囲式におけるドイツ語ロケールのサポート
type: docs
weight: 60
url: /ja/javascript-cpp/support-for-german-locale-in-named-range-formulae/
description: Aspose.Cells for JavaScriptを使用して、名前付き範囲のフォーミュラにドイツ語ロケールをサポートする方法を学びます。
---

英語の数式は名前付き領域に書き込まれます。このExcelファイルは、システムがドイツ語ロケールに設定されている環境で開くことができ、英語の数式はドイツ語に翻訳されます。以下の例はこの機能を示しています。ただし、Excelがドイツ語でインストールされている必要があり、システムロケールもドイツ語に設定されている必要があります。  

この機能のテスト用のサンプルファイルは、以下のリンクからダウンロードできます:  

[sampleNamedRangeTest.xlsm](73990165.xlsm)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Named Range Example</title>
    </head>
    <body>
        <h1>Named Range Example</h1>
        <p>Select an existing Excel macro-enabled workbook (.xlsm) to modify, or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
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
            if (!fileInput.files.length) {
                // No file selected - a new empty workbook will be created
            }

            const file = fileInput.files.length ? fileInput.files[0] : null;
            let workbook;
            if (file) {
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Define named range name and formula
            const name = "HasFormula";
            const value = '=GET.CELL(48, INDIRECT("ZS",FALSE))';

            // Access worksheets collection
            const wsCol = workbook.worksheets;

            // Add named range and set its reference
            const nameIndex = wsCol.names.add(name);
            const namedRange = wsCol.names.get(nameIndex);
            namedRange.refersTo = value;

            // Save the modified workbook as .xlsm and provide download link
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sampleOutputNamedRangeTest.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named range added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
