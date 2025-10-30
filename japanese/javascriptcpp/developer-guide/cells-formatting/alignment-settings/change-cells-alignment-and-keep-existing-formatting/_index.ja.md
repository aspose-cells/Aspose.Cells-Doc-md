---
title: セルの配置を変更し、既存の書式を保持する
linktitle: セルの配置を変更し、既存の書式を保持する
description: Aspose.Cellsライブラリを使ってJavaScriptを通じてセルの配置を変更し、既存の書式設定を維持します。
keywords: Aspose.Cells、JavaScript経由C++、セルの整列、既存の書式設定の維持
type: docs
weight: 340
url: /ja/javascript-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **可能な使用シナリオ**

時には、複数のセルの整列を変更したいが、既存の書式設定も維持したい場合があります。Aspose.Cells for JavaScriptをC++で使うと、[**StyleFlag.alignments(boolean)**](https://reference.aspose.com/cells/javascript-cpp/styleflag/#alignments-boolean-)メソッドを使ってこれを実現できます。もし**true**に設定すれば整列の変更が適用されますが、そうでなければ適用されません。なお、[**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag)オブジェクトをパラメータとして[**Range.applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/range/#applyStyle-style-styleflag-)メソッドに渡すと、実際に範囲内のセルに書式設定を適用します。

## **セルの配置を変更し、既存の書式を保持する**

次のサンプルコードは、[サンプルExcelファイル](67338585.xlsx)を読み込み、範囲を作成し、セルの内容を水平および垂直に中央揃えにし、既存の書式をそのまま維持します。次のスクリーンショットは、サンプルExcelファイルと[出力されたExcelファイル](67338586.xlsx)を比較し、セルの既存の書式が変わらず、ただしセルの中央揃えが水平および垂直に行われたことが示されています。

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Cells Alignment and Keep Existing Formatting</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, TextAlignmentType, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create cells range
            const range = worksheet.cells.createRange("B2:D7");

            // Create style object
            const style = workbook.createStyle();

            // Set the horizontal and vertical alignment to center using property assignments
            style.horizontalAlignment = TextAlignmentType.Center;
            style.verticalAlignment = TextAlignmentType.Center;

            // Create style flag object
            const flag = new StyleFlag();
            flag.alignments = true; // Set style flag alignments true

            // Apply style to range of cells
            range.applyStyle(style, flag);

            // Save the workbook in XLSX format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeCellsAlignmentAndKeepExistingFormatting.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
