---
title: JavaScriptを通じてC++で共有式を設定する方法
linktitle: 共有式数式の設定
type: docs
weight: 10
url: /ja/javascript-cpp/setting-shared-formula/
---

{{% alert color="primary" %}}

ワークシートに計算を行う関数を追加したい場合は、この記事でC++を通じてAspose.Cells for JavaScriptを使用した方法を説明します。

{{% /alert %}}

## C++を通じてAspose.Cells for JavaScriptで共有式を設定する

次のサンプルワークシートのようなデータで満たされたワークシートがあるとします。

|**入力ファイル（1列のデータ）**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

B2に関数を追加し、最初のデータ行の売上税を計算したいとします。税金は9%です。売上税を計算する式は次のとおりです:"=A2*0.09"。この記事では、Aspose.Cellsでこの式を適用する方法について説明します。

Aspose.Cellsを使用すると、[**Cell.formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--) プロパティを使用して式を指定できます。その他のセル（B3、B4、B5など）に式を追加するためには、2つのオプションがあります。

最初のセルのように操作し、各セルに対して数式を設定し、セル参照を更新します（A3*0.09、A4*0.09、A5*0.09など）。これには各行のセル参照を更新する必要があります。また、Aspose.Cellsは各数式を個別に解析しなければならず、大きなスプレッドシートや複雑な数式の場合は時間がかかることがあります。さらに、ループで多少簡略化できますが、追加のコード行が必要です。

もう1つの方法は、**共有式**を使用することです。共有式を使用すると、式は各行のセル参照に自動的に更新されるため、税金が正しく計算されます。[**Cell.sharedFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#sharedFormula-string-number-number-) メソッドは、最初の方法よりも効率的です。

次の例では、その使用方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Apply Shared Formula</title>
    </head>
    <body>
        <h1>Apply Shared Formula Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the cells collection in the first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Apply the shared formula in the range i.e., B2:B14
            const cell = cells.get("B2");
            // Converted setSharedFormula(...) to property assignment per universal rule.
            cell.sharedFormula = { formula: "=A2*0.09", rowCount: 13, columnCount: 1 };

            // Save the excel file and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shared formula applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
