---
title: JavaScriptを介したC++によるExcelファイルに保存する有効桁数の指定
linktitle: Excelファイルに保存する有効桁数を指定する
type: docs
weight: 30
url: /ja/javascript-cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: C++を使用してAspose.Cells for JavaScriptでExcelファイルに保存する有効桁数の指定方法を学びます。
---

## **可能な使用シナリオ**  

デフォルトでは、Aspose.Cells for JavaScriptはC++を介してExcelファイル内に17桁の有効数字の倍精度浮動小数点値を格納します。これは、MS-Excelが15桁の有効数字のみを格納するのとは異なります。Aspose.Cellsのデフォルト動作を17桁から15桁に変更するには、[**CellsHelper.significantDigits**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#significantDigits--) プロパティを使用します。  

## **Excelファイルに保存する有効桁数を指定**  

以下のサンプルコードは、4835値をExcelファイルに保存する際にAspose.Cellsに15桁の有効数字を強制的に使用させるものです。出力されるExcelファイル（22774105.xlsx）を確認してください。拡張子を.zipに変更して解凍すると、15桁のみが保存されているのがわかります。以下のスクリーンショットは [**CellsHelper.significantDigits**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#significantDigits--) プロパティが出力Excelファイルに与える影響を示しています。  

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)  

## **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Significant Digits</title>
    </head>
    <body>
        <h1>Significant Digits Example</h1>
        <p>This example sets CellsHelper.significantDigits to 15 and writes a double to cell A1.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

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

            // If a file is provided, open it; otherwise create a new workbook (matches original Node behavior)
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // By default, Aspose.Cells stores 17 significant digits unlike MS-Excel which stores only 15 significant digits
            CellsHelper.significantDigits = 15;

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const c = worksheet.cells.get("A1");

            // Put double value, only 15 significant digits as specified by CellsHelper.significantDigits above will be stored
            c.value = 1234567890.123451711;

            // Saving the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_SignificantDigits.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
