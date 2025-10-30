---
title: JavaScriptを通じてスタイル付きの範囲をコピー
linktitle: スタイル付きの範囲のデータをコピーします。
type: docs
weight: 610
url: /ja/javascript-cpp/copy-range-data-with-style/
description: フォーマット付きのセル範囲をコピーする方法をAspose.Cells for JavaScriptを使って学びます。
---

{{% alert color="primary" %}}

[範囲のデータだけをコピー](/cells/ja/javascript-cpp/copy-range-data-only/)は、セル範囲から別の範囲へデータをコピーする方法について説明しています。特に、コピーしたセルに新しいスタイルのセットを適用します。Aspose.Cellsはフォーマットを含む範囲を丸ごとコピーすることも可能です。この説明をします。

{{% /alert %}}

Aspose.Cellsは、範囲の操作に関するさまざまなクラスとメソッドを提供します。例：[**createRange(string, string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-)、[**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag/)、[**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/cells/#applyStyle-style-styleflag-)。

この例:

1. ワークブックを作成します。  
2. 最初のシートの複数のセルにデータを入力します。  
3. [**Range**](https://reference.aspose.com/cells/javascript-cpp/range/)を作成します。  
4. 指定された書式属性を持つ[**Style**](https://reference.aspose.com/cells/javascript-cpp/style/)オブジェクトを作成します。  
5. データ範囲にスタイルを適用します。  
6. 2つ目のセル範囲を作成します。  
7. 最初の範囲から2番目の範囲にデータと書式設定をコピーします。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Copy Range Example</h1>
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
            if (fileInput.files.length && fileInput.files[0]) {
                // If a file is provided, open it and modify
            } else {
                // No file provided, will create a new workbook
            }

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first Worksheet Cells.
            const cells = workbook.worksheets.get(0).cells;

            // Fill some sample data into the cells.
            for (let i = 0; i < 50; i++) {
                for (let j = 0; j < 10; j++) {
                    cells.get(i, j).value = `${i},${j}`;
                }
            }

            // Create a range (A1:D3).
            const range = cells.createRange("A1", "D3");

            // Create a style object.
            let style = workbook.createStyle();
            // Specify the font attribute.
            style.font.name = "Calibri";
            // Specify the shading color.
            style.foregroundColor = AsposeCells.Color.Yellow;
            style.pattern = AsposeCells.BackgroundType.Solid;
            // Specify the border attributes.
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Blue;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Blue;
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Blue;
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Blue;

            // Create the styleflag object.
            const flag1 = new AsposeCells.StyleFlag();
            // Implement font attribute
            flag1.fontName = true;
            // Implement the shading / fill color.
            flag1.cellShading = true;
            // Implement border attributes.
            flag1.borders = true;
            // Set the Range style.
            range.applyStyle(style, flag1);

            // Create a second range (C10:F12).
            const range2 = cells.createRange("C10", "F12");

            // Copy the range data with formatting.
            range2.copy(range);

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyRange.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
