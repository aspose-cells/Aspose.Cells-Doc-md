---
title: JavaScriptによるExcelファイルの数式管理（C++対応）
linktitle: 数式
type: docs
weight: 122
url: /ja/javascript-cpp/using-formulas-or-functions-to-process-data/
description: Aspose.Cells for JavaScriptを使ったExcelファイルの数式管理方法を学ぶ。Aspose.CellsはExcelの数式の取得、設定、および計算をシンプルに行えます。
keywords: C++でのJavaScriptによる数式の計算方法、JavaScriptを使った関数と数式の管理、ビルトイン関数の使用方法、アドイン関数の使用法、配列数式の使用方法（via JavaScript）、JavaScriptでのR1C1数式の使用方法（C++対応）。
---

## **紹介**

Microsoft Excelの魅力的な機能の一つは、数式や関数を使ったデータ処理能力です。Excelは多くの組み込み関数と数式を提供し、複雑な計算を迅速に行えます。Aspose.Cellsもまた、値の計算を支援する多くの組み込み関数と数式を提供し、アドイン関数もサポートしています。さらに、配列やR1C1数式もサポートしています。

## **数式と関数の使用方法**

Aspose.Cells は、Microsoft Excel ファイルを表す [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) クラスには、Excel ファイル内の各ワークシートにアクセスするための [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) コレクションが含まれています。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) クラスは [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) コレクションを提供します。Cells コレクション内の各アイテムは、[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) クラスのオブジェクトを表します。

詳細については、[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) クラスが提供するプロパティとメソッドを使用してセルに数式を適用することが可能です。

- 組み込み関数の使用。
- アドイン関数の使用。
- 配列式の操作。
- R1C1 数式の作成。

## **組み込み関数の使用方法**

組み込みの関数または数式は、開発者の労力と時間を節約するための既製の関数として提供されています。Aspose.Cellsがサポートする[組み込み関数一覧](/cells/ja/javascript-cpp/supported-formula-functions/)を参照してください。関数はアルファベット順にリストされています。今後も機能が追加される予定です。

Aspose.Cellsは、Microsoft Excelが提供するほとんどの数式や関数をサポートしています。これらの関数はAPIまたは[デザイナースプレッドシート](/cells/ja/javascript-cpp/what-is-a-designer-spreadsheet/)を通じて使用可能です。Aspose.Cellsは数学、文字列、論理演算、日付/時間、統計、データベース、検索、参照の多くの数式をサポートしています。

セルに数式を追加するためには、[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) クラスの [**formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--) プロパティを使用します。例えば **複雑な数式** など

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

、Aspose.Cellsでは複雑な数式もサポートされています。セルに数式を適用する際は、常に文字列を等号（=）で始めてマイクロソフトExcelで数式を作成するときと同様に関数パラメータを区切るためにコンマ（,）を使用してください。

以下の例では、ワークシートの [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) コレクションの最初のセルに複雑な数式が適用されています。この数式は、Aspose.Cells が提供する組み込みの **IF** 関数を使用しています。

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a value to "A1" cell
            worksheet.cells.get("A1").putValue(1);

            // Adding a value to "A2" cell
            worksheet.cells.get("A2").putValue(2);

            // Adding a value to "A3" cell
            worksheet.cells.get("A3").putValue(3);

            // Adding a SUM formula to "A4" cell
            worksheet.cells.get("A4").formula = "=SUM(A1:A3)";

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A4").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated A4 value: ${value}. Click the download link to get the generated file.</p>`;
        });
    </script>
</html>
```

## **アドイン関数の使用方法**

ユーザー定義の数式を作成し、Excelのアドインとして追加できます。セルの.formula関数に組み込み関数を設定するだけでなく、カスタム関数や数式をアドイン関数を使用して設定する必要があります。

Aspose.Cellsは、[**Worksheets.registerAddInFunction(string, string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#registerAddInFunction-string-string-boolean-)を使用してアドイン関数を登録する機能を提供します。その後、cell.formulaに任意のアドイン関数を設定すると、出力されるExcelファイルにはアドイン関数からの計算結果が含まれます。

以下のサンプルコードの中でアドイン関数を登録するために XLAM ファイルをダウンロードできます。同様に、出力ファイル "test_udf.xlsx" もダウンロードして出力を確認することができます。

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Register Add-In Function Example</title>
    </head>
    <body>
        <h1>Register Add-In Function Example</h1>
        <p>Select the add-in file (.xlam/.xla) that contains the UDFs to register:</p>
        <input type="file" id="addInInput" accept=".xlam,.xla" />
        <button id="runExample">Register Add-In & Create Workbook</button>
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
            const fileInput = document.getElementById('addInInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an add-in file (.xlam/.xla).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const addinData = new Uint8Array(arrayBuffer);

            // Create empty workbook
            const workbook = new Workbook();

            // Register macro enabled add-in along with the function name
            const id = workbook.worksheets.registerAddInFunction(addinData, "TEST_UDF", false);

            // Register more functions in the file (if any)
            workbook.worksheets.registerAddInFunction(id, "TEST_UDF1");

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first cell
            const cell = worksheet.cells.get("A1");

            // Set formula name present in the add-in
            cell.formula = "=TEST_UDF()";

            // Save workbook to output XLSX format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'test_udf.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Add-in registered and formula set successfully! Click the download link to get the workbook.</p>';
        });
    </script>
</html>
```

## **配列式の使用方法**

配列式は、数式を構成する関数に個々の数値ではなく配列を引数として取る数式です。配列式が表示されると、括弧({})で囲まれています。

いくつかのMicrosoft Excel関数は値の配列を返します。配列数式を使用して複数の結果を計算するには、配列を配列引数と同じ行数および列数のセル範囲に入力してください。

配列式をセルに適用するには、[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) クラスの [**arrayFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#arrayFormula-string-number-number-) メソッドを呼び出します。[**arrayFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#arrayFormula-string-number-number-) メソッドは以下のパラメータを取ります:

- **配列数式**、配列数式。
- **行数**、配列数式の結果を設定する行数。
- **列数**, 配列式の結果を入力する列数。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells LINEST Example</h1>
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
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding values to cells
            worksheet.cells.get("A1").value = 1;
            worksheet.cells.get("A2").value = 2;
            worksheet.cells.get("A3").value = 3;

            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 5;
            worksheet.cells.get("B3").value = 6;

            worksheet.cells.get("C1").value = 7;
            worksheet.cells.get("C2").value = 8;
            worksheet.cells.get("C3").value = 9;

            // Adding a SUM/LINEST array formula to "A6" cell
            worksheet.cells.get("A6").arrayFormula = { formula: "=LINEST(A1:A3,B1:C3,TRUE,TRUE)", rows: 5, cols: 3 };

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A6").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated value: ${value}</p>`;
        });
    </script>
</html>
```

## **R1C1 数式の使用方法**

セルに **R1C1** 参照スタイルの数式を [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) クラスの [**r1C1Formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#r1C1Formula--) プロパティを使用して追加します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set R1C1 Formula Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting an R1C1 formula on the "A11" cell,
            // Row and Column indices are relative to destination index
            const cell = worksheet.cells.get("A11");
            cell.r1C1Formula = "=SUM(R[-10]C[0]:R[-7]C[0])";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">R1C1 formula set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **高度なトピック**
- [先行および後行](/cells/ja/javascript-cpp/precedents-and-dependents/)
- [数式で外部リンクを設定する](/cells/ja/javascript-cpp/set-external-links-in-formulas/)
- [新しい行にデータを入力する際に、表やリストオブジェクトの式を自動的に伝播させる](/cells/ja/javascript-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [名前付き範囲の式の設定](/cells/ja/javascript-cpp/setting-formula-for-named-range/)
- [数式の設定 - 英語以外のユーザーへの通知](/cells/ja/javascript-cpp/setting-formulas-notice-for-non-english-users/)
- [共有数式の設定](/cells/ja/javascript-cpp/setting-shared-formula/)
- [共有式の最大行数を指定](/cells/ja/javascript-cpp/specify-maximum-rows-of-shared-formula/)
- [サポートされているExcel関数](/cells/ja/javascript-cpp/supported-formula-functions/)
