---
title: 条件付き書式を使用して交互の行と列に網掛けを適用する
linktitle: 条件付き書式を使用して交互の行と列に網掛けを適用する
description: Aspose.Cellsライブラリを使ってJavaScript経由C++で交互の行と列のシャドウを持つ条件付き書式の適用方法。これらの基準を調整することで、セルの見た目をより詳細に制御できます。
keywords: Aspose.Cells、条件付き書式、JavaScript経由C++、交互の行、交互の列、シャドウ
type: docs
weight: 30
url: /ja/javascript-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells APIは、[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)オブジェクト用の条件付き書式ルールを追加・操作する手段を提供します。これらのルールは、条件やルールに基づいて望ましい書式を得るためにさまざまに調整できます。この記事では、条件付き書式ルールとExcelの組み込み関数を使って、交互の行と列にシェーディングを適用するためにAspose.Cells for JavaScriptをC++ APIを使って使用する方法を示します。

{{% /alert %}}

この記事では、Excelの組み込み関数であるROW、COLUMN、MODなどの詳細について説明します。これらの関数の詳細な内容を提供し、コードスニペットの理解を深めます。

- **ROW()**関数は、セル参照の行番号を返します。引数に参照を省略した場合は、そのセルアドレスに対して値を返します。
- **COLUMN()**関数は、セル参照の列番号を返します。引数に参照を省略した場合は、そのセルアドレスに対して値を返します。
- **MOD()** 関数は、数値が除算された後の余りを返します。関数の最初のパラメーターは、余りを求めたい数値で、2番目のパラメーターは、数値パラメーターで除算する数です。除数が0の場合、#DIV/0!エラーが返されます。

この目標を達成するために、Aspose.Cells for JavaScriptをC++ APIを使ってコードを書き始めましょう。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Conditional Formatting</title>
    </head>
    <body>
        <h1>Conditional Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, Utils } = AsposeCells;

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
            // Create an instance of Workbook
            const book = new Workbook();

            // Access the first worksheet
            const sheet = book.worksheets.get(0);

            // Add FormatConditions to the instance of Worksheet
            let idx = sheet.conditionalFormattings.add();

            // Access the newly added FormatConditions via its index
            const conditionCollection = sheet.conditionalFormattings.get(idx);

            // Define a CellsArea on which conditional formatting will be applicable (A1 to I20)
            const area = CellArea.createCellArea("A1", "I20");

            // Add area to the instance of FormatConditions
            conditionCollection.addArea(area);

            // Add a condition to the instance of FormatConditions (Expression type)
            idx = conditionCollection.addCondition(AsposeCells.FormatConditionType.Expression);

            // Access the newly added FormatCondition via its index
            const formatCondition = conditionCollection.get(idx);

            // Set the formula for the FormatCondition
            formatCondition.formula1 = "=MOD(ROW(),2)=0";

            // Set the background color and pattern for the FormatCondition's Style
            formatCondition.style.backgroundColor = AsposeCells.Color.Blue;
            formatCondition.style.pattern = AsposeCells.BackgroundType.Solid;

            // Save the result and provide a download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


次のスナップショットは、Excelアプリケーションで読み込まれた結果のスプレッドシートを示しています。

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

交互の列に網掛けを適用するためには、単に式を **=MOD(ROW(),2)=0** から **=MOD(COLUMN(),2)=0** に変更するだけで済みます。つまり、行索引を取得する代わりに、式を変更して列索引を取得します。  
この場合の結果のスプレッドシートは以下のようになります。

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
