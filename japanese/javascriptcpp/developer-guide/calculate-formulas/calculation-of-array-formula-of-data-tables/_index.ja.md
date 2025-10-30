---
title: JavaScriptを介したC++によるデータテーブルの配列式の計算
linktitle: データテーブルの配列式の計算
description: Aspose.Cellsライブラリを使用して、JavaScriptを介したC++でMicrosoft Excelのデータテーブルの配列式を計算する方法。Excelファイルを読み込むか作成し、配列式を計算して、変更されたファイルを保存します。
keywords: Aspose.Cells、Excel、データテーブル、配列式、計算、JavaScriptを介したC++
type: docs
weight: 70
url: /ja/javascript-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Microsoft ExcelでData > シナリオ分析 > データテーブル...を使用してデータテーブルを作成できます。Aspose.Cellsは現在、データテーブルの配列数式の計算を可能にしています。通常どおり[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)を使用してあらゆるタイプの数式を計算してください。

{{% /alert %}}

次のサンプルコードでは、[元のExcelファイル](5115535.xlsx) を使用しました。セルB1の値を100に変更すると、黄色で塗られたデータテーブルの値が120になる様子が次の画像で示されます。サンプルコードは、[出力PDF](5115538.pdf) を生成します。

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>DataTable Calculation Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Creating a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
            const cell = worksheet.cells.get("B1");
            cell.putValue(100);

            // Calculate formula, now it also calculates Data Table array formula
            workbook.calculateFormula();

            // Save the workbook in pdf format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
