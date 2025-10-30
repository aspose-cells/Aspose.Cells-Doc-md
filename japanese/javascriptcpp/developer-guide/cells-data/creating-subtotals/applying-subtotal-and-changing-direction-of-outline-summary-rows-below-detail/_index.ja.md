---
title: 小計を適用し、詳細以下のアウトラインサマリー行を変更する
type: docs
weight: 100
url: /ja/javascript-cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: C++ APIを使用してAspose.Cells for JavaScriptを使い、合計行の適用とアウトラインサマリー行の方向変更方法について学びます。
keywords: サブトータルを適用し、サブトータルを追加し、詳細の下にアウトラインサマリー行の方向を変更し、詳細の右側にアウトラインサマリー列の方向を変更し、サブトータルを作成し、詳細の下にアウトラインサマリー行の方向を変更する
---

{{% alert color="primary" %}}

この記事では、データに小計を適用し、詳細の下にアウトラインサマリー行の方向を変更する方法について説明します。

データに小計を適用する方法を説明します。次のパラメータを取ります。

- **CellArea** - 小計を適用する範囲
- **GroupBy** - グループ化するフィールド（ゼロベースの整数オフセット）
- **Function** - 小計関数
- **TotalList** - 小計が追加されるゼロベースのフィールドオフセットの配列
- **Replace** - 現在の小計を置換するかどうかを示します
- **PageBreaks** - グループ間にページ区切りを追加するかどうかを示します
- **SummaryBelowData** - データの下に要約を追加するかどうかを示します

また、以下のスクリーンショットに示すように、Worksheet.Outline.SummaryRowBelowプロパティを使用してアウトラインの**詳細以下のサマリー行**の方向を制御できます。これを実行するには、Microsoft Excelで**データ > アウトライン > 設定**を開くことができます。

![todo:image_alt_text](1.png)

{{% /alert %}}

## ソースファイルと出力ファイルの画像

次のスクリーンショットは、以下のサンプルコードで使用されるソース Excel ファイルを示しており、列 A と列 B にいくつかのデータが含まれています。

![todo:image_alt_text](2.png)

サンプルコードによって生成されたExcelファイルの出力画面が以下に表示されています。範囲A2:B11に小計が適用されたことがわかります。また、アウトラインの方向は、詳細の下に集計行が表示されます。

![todo:image_alt_text](3.png)

## 送付の合計とアウトラインサマリー行の方向変更を適用するJavaScript



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Subtotal Example</title>
    </head>
    <body>
        <h1>Apply Subtotal Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ConsolidationFunction, Utils } = AsposeCells;

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

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the Cells collection in the first worksheet
            const cells = worksheet.cells;

            // Create a cellarea i.e., A2:B11
            const ca = CellArea.createCellArea("A2", "B11");

            // Apply subtotal, the consolidation function is Sum and it will applied to Second column (B) in the list
            cells.subtotal(ca, 0, ConsolidationFunction.Sum, [1], true, false, true);

            // Set the direction of outline summary
            worksheet.outline.summaryRowBelow = true;

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Subtotal applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
