---
title: JavaScriptとC++を利用した数式の計算
linktitle: 数式の計算
description: この記事では、Aspose.Cellsライブラリを使用して、C++経由のJavaScriptを用いてMicrosoft Excelの数式を計算する方法を紹介します。既存のExcelファイルを読み込むか新たに作成し、Aspose.Cellsのメソッドを利用して数式を計算し、結果を取得します。最後に、修正したExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、数式、計算、数式の直接計算、繰り返し数式の計算、JavaScriptをC++経由で追加
type: docs
weight: 125
url: /ja/javascript-cpp/calculate-formulas/
---

## **数式の追加と結果の計算**

Aspose.Cellsには組み込みの式計算エンジンがあります。これにより、デザイナーテンプレートからインポートした式の再計算だけでなく、ランタイムで追加された式の結果の計算もサポートしています。

Aspose.Cellsは、Microsoft Excelのほとんどの数式や関数をサポートしています（[サポートされている関数のリスト](/cells/ja/javascript-cpp/supported-formula-functions/)を参照）。これらの関数はAPIまたはデザイナースプレッドシートを通じて使用可能です。Aspose.Cellsは、多数の数学、文字列、論理演算、日時、統計、データベース、ルックアップ、参照の数式をサポートしています。

セルに式を追加するには、[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)クラスの[**formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--)プロパティまたは[**formula(string, object)**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula-string-object-)メソッドを使用します。式を適用する際は、Microsoft Excelでの作成と同じく文字列の先頭に等号（=）を付け、関数パラメータをカンマ（,）で区切ります。

式の結果を計算するには、ユーザーは[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスの[**calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)メソッドを呼び出してExcelファイル内のすべての式を処理させるか、[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスの[**calculateFormula(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-)メソッドを呼び出してシート内のすべての式を処理させるか、または、[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)クラスの[**calculate(CalculationOptions)**](https://reference.aspose.com/cells/javascript-cpp/cell/#calculate-calculationoptions-)メソッドを呼び出して特定のセルの式を処理させることができます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Add a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a value to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = 1;

            // Adding a value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 2;

            // Adding a value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.value = 3;

            // Adding a SUM formula to "A4" cell
            const cellA4 = worksheet.cells.get("A4");
            cellA4.formula = "=SUM(A1:A3)";

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A4").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated value in A4: ${value}. Click the download link to get the file.</p>`;
        });
    </script>
</html>
```

### **数式に関する重要な点**

{{% alert color="primary" %}}

[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)クラスの**Formula**プロパティと**formula(...)**メソッドは、[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)、[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)、[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)クラスの**calculate**メソッドと異なり、単にセルに数式を追加するだけで、実行時に結果を計算しません。数式の結果を取得するには、**calculate**メソッドを呼び出してください。

{{% /alert %}}

## **数式の直接計算**

Aspose.Cellsには、埋め込みファイルからインポートされた数式を計算するだけでなく、直接数式の結果を計算する機能があります。

ときには、シートに追加せずに式の結果を直接計算する必要があります。式に使用されるセルの値はすでにシートに存在し、それらの値の結果をMicrosoft Excelの式に基づいて見つけたい場合です。

Aspose.Cellsの式計算エンジンAPIを使用して、[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)から[**calculateFormula(string, FormulaParseOptions, CalculationOptions, number, number, CalculationData)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-formulaparseoptions-calculationoptions-number-number-calculationdata-)までの式の結果をシートに追加せずに計算できます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Calculate Sum</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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

            // Create or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put 20 in cell A1
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = 20;

            // Put 30 in cell A2
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 30;

            // Calculate the Sum of A1 and A2
            const results = worksheet.calculateFormula("=Sum(A1:A2)");

            // Prepare output text
            const outputHtml = [
                `<p>Value of A1: ${cellA1.stringValue}</p>`,
                `<p>Value of A2: ${cellA2.stringValue}</p>`,
                `<p>Result of Sum(A1:A2): ${results.toString()}</p>`
            ].join("");

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<div style="color: green;">Operation completed successfully!</div>${outputHtml}`;
        });
    </script>
    </body>
</html>
```

上記のコードは次の出力を生成します：
{{< highlight nodejs >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **数式を繰り返し計算する方法**

ワークブックに多くの式があり、少しの変更を加えながら繰り返し計算する必要がある場合、パフォーマンス向上のために式の計算チェーンを有効にすることが役立ちます：[**formulaSettings.enableCalculationChain**](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#enableCalculationChain--)。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Calculate Formulas</title>
    </head>
    <body>
        <h1>Calculate Formulas Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Print the time before formula calculation
            console.log(new Date());

            // Set the CreateCalcChain as true
            workbook.settings.formulaSettings.enableCalculationChain = true;

            // Calculate the workbook formulas
            workbook.calculateFormula();

            // Print the time after formula calculation
            console.log(new Date());

            // Change the value of one cell (A1 in first worksheet)
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");
            cell.value = "newvalue";

            // Re-calculate those formulas which depend on cell A1
            workbook.calculateFormula();

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Formulas calculated and cell updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **重要なこと**

{{% alert color="primary" %}}

デフォルトでは、計算チェーンは無効です。チェーンの作成には追加の時間がかかるため、最初の式計算（[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)）は、チェーンを作成しない場合に比べて、より多くのCPU処理時間とメモリを消費することがあります。繰り返し式を計算しない場合は、標準的な動作（式を直接計算する）を選んだ方が良いでしょう。

{{% /alert %}}

## **高度なトピック**
- [Microsoft Excelフォーミュラ計算エンジンのAspose.Cells](/cells/ja/javascript-cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cellsを使用してIFNA関数を計算する](/cells/ja/javascript-cpp/calculating-ifna-function-using-aspose-cells/)
- [データテーブルの配列式の計算](/cells/ja/javascript-cpp/calculation-of-array-formula-of-data-tables/)
- [Excel 2016のMINIFSおよびMAXIFS関数の計算](/cells/ja/javascript-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [セルの計算時間を短縮する方法](/cells/ja/javascript-cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [循環参照の検出](/cells/ja/javascript-cpp/detecting-circular-reference/)
- [ワークシートに書き込まずにカスタム機能を直接計算する](/cells/ja/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Aspose.Cellsのデフォルトの計算エンジンを拡張するためにカスタム計算エンジンを実装する](/cells/ja/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [ワークブックの数式計算を中断またはキャンセルする](/cells/ja/javascript-cpp/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [AbstarctCalculationEngineを使用して値の範囲を返す](/cells/ja/javascript-cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [ブックの数式計算モードの設定](/cells/ja/javascript-cpp/setting-formula-calculation-mode-of-workbook/)
- [Aspose.CellsでのFormulaText関数の使用](/cells/ja/javascript-cpp/using-formulatext-function-in-aspose-cells/)
