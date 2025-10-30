---
title: JavaScriptを通じてC++で共有式の最大行数を指定する
linktitle: 共有式の最大行数を指定
type: docs
weight: 40
url: /ja/javascript-cpp/specify-maximum-rows-of-shared-formula/
description: C++を通じてAspose.Cells for JavaScriptを使用して共有式の最大行数を指定する方法を学ぶ。
---

## **可能な使用シナリオ**  

 共有数式のデフォルト最大行数は64です。これを任意の数値（例：1000）に変更できます。共有数式の行数によってパフォーマンスが変動します。そのため、Aspose.Cellsは[**WorkbookSettings.maxRowsOfSharedFormula**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRowsOfSharedFormula--)プロパティを提供し、これを使って最大行数を設定できます。共有数式の総行数がこれを超えると、複数の共有数式に分割されます。以下のスクリーンショットは、その設定例を示しています。  

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)  

## **共有式の最大行数を指定**  

 [**WorkbookSettings.maxRowsOfSharedFormula**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRowsOfSharedFormula--)プロパティの使用例を示すサンプルコードです。最大行数を5に設定し、セルD1に100行分の共有数式を追加し、[出力Excelファイル](61767856.xlsx)に保存します。出力Excelの内容を展開し、*sheet1.xml*を確認すると、各5行ごとに分割された共有数式が見えます。  

## **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Specify Maximum Rows Of Shared Formula Example</title>
    </head>
    <body>
        <h1>Specify Maximum Rows Of Shared Formula Example</h1>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Set the max rows of shared formula to 5
            workbook.settings.maxRowsOfSharedFormula = 5;

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access cell D1
            const cell = ws.cells.get("D1");

            // Set the shared formula in 100 rows
            cell.sharedFormula = ["=Sum(A1:A2)", 100, 1];

            // Save the output Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyMaximumRowsOfSharedFormula.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
