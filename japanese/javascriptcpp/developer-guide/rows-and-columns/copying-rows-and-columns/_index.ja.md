---
title: 行と列のコピー（C++経由）
linktitle: 行と列のコピー
type: docs
weight: 40
url: /ja/javascript-cpp/copying-rows-and-columns/
description: この記事は、Aspose.Cells for JavaScriptを通じてC++ APIで行や列をコピーする方法を示しています。
keywords: JavaScriptをC++経由で、行と列のコピー方法、JavaScriptで行をコピー、JavaScriptを使った列のコピー、C++経由のAspose.Cells for JavaScriptを使用した行や列の貼り付け、複数行や列の貼り付け、単一の行や列のコピーと貼り付け。
---

## **紹介**  

時には、ワークシート全体をコピーせずに行や列をコピーする必要があります。Aspose.Cellsを使用すると、ワークブック内またはワークブック間で行や列をコピーすることができます。  
行（または列）をコピーすると、それに含まれるデータ（更新された参照を含む数式、値、コメント、書式設定、非表示セル、画像、その他の図形オブジェクトなど）がコピーされます。  

## **Microsoft Excelで行や列をコピーする方法**  

1. コピーしたい行または列を選択します。  
1. 行または列をコピーする場合は、**標準**ツールバーの**コピー**をクリックするか、**CTRL**+**C**を押します。  
1. コピーする選択範囲の下または右側に行または列を選択します。  
1. 行または列をコピーする際に、**挿入**メニューで**コピーしたセル**をクリックします。  

{{% alert color="primary" %}}  
**標準**ツールバーの**貼り付け**をクリックするか、**Insert**メニューのコマンドをクリックする代わりに**CTRL**+**V**を押すと、宛先セルの内容が置き換えられます。  
{{% /alert %}}  

## **Microsoft Excelを使用した貼り付けオプションを使用した行や列の貼り付け方法**  

1. コピーしたいデータやその他の属性を含むセルを選択します。  
1. **コピー**をクリックしてHomeタブを選択します。  
1. **貼り付け**したいエリア内で最初のセルをクリックします。  
1. Homeタブで、**貼り付け**の横にある矢印をクリックし、**貼り付け**を選択します。  
1. 希望する**オプション**を選択します。  

## **C++を使ったAspose.Cells for JavaScriptで行と列をコピーする方法**  

## **単一の行をコピーする方法**  

Aspose.Cells は [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) クラスの [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) メソッドを提供します。このメソッドは、数式、値、コメント、セル書式、非表示セル、画像、その他の描画オブジェクトを含むすべてのタイプのデータをソース行から宛先行にコピーします。  

[**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) メソッドは次のパラメータを受け取ります：  

- ソースの [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) オブジェクト、  
- ソースの行インデックス、および  
- 宛先の行インデックス。  

このメソッドを使用して、シート内または別のシートに行をコピーします。[**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) メソッドはMicrosoft Excelと似た動作をします。例えば、宛先行の高さを明示的に設定する必要はなく、その値もコピーされます。  

次の例は、ワークシートで行をコピーする方法を示しています。テンプレートとなるMicrosoft Excelファイルを使用し、2行目（データ、書式、コメント、画像などを含む）をコピーし、それを同じワークシートの12行目に貼り付けます。  

[**Cells.rowHeight(number, boolean, CellsUnitType)**](https://reference.aspose.com/cells/javascript-cpp/cells/#rowHeight-number-boolean-cellsunittype-) メソッドを使用すれば、ソース行の高さを取得するステップをスキップし、宛先行の高さを設定することも可能です。[**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) メソッドは自動的に行の高さを調整します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Row</title>
    </head>
    <body>
        <h1>Copy Row Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the workbook.
            const wsTemplate = workbook.worksheets.get(0);

            // Copy the second row (index 1) with data, formatting, images and drawing objects
            // To the 16th row (index 15) in the worksheet.
            wsTemplate.cells.copyRow(wsTemplate.cells, 1, 15);

            // Save the excel file in Excel97To2003 format (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
行をコピーする際は、関連する画像、グラフ、またはその他の描画オブジェクトに注目することが重要です。これはMicrosoft Excelと同じです。  

1. もしソース行インデックスが5であれば、画像、グラフなどはその3行に含まれている場合にコピーされます（開始行インデックスが4で終了行インデックスが6の場合）。  
1. 宛先行にある既存の画像やグラフなどは削除されません。  
{{% /alert %}}  

## **複数の行をコピーする方法**  

また、[**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-) メソッドを使用して複数の行をコピーし、その際に追加の整数型のパラメータでコピーするソース行の数を指定することもできます。  

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
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiate workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the cells collection of first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Copy the first 3 rows to 7th row (indexes are zero-based)
            cells.copyRows(cells, 0, 6, 3);

            // Save the result and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **列をコピーする方法**  

Aspose.Cellsは [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumn-cells-number-number-) クラスの [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) メソッドを提供します。このメソッドは、数式（更新された参照付き）を含むすべてのタイプのデータ、値、コメント、セル書式、非表示セル、画像、およびその他の描画オブジェクトをソース列から宛先列にコピーします。  

[**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumn-cells-number-number-) メソッドは次のパラメータを受け取ります：  

- ソースの [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) オブジェクト、  
- ソースの列インデックス、および  
- 宛先の列インデックス。  

この [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumn-cells-number-number-) メソッドを使用して、シート内または別のシートに列をコピーします。  

この例では、ワークシートから列をコピーして別のブック内のワークシートに貼り付けます。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Copy Column Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object using the uploaded file
            const excelWorkbook1 = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the book.
            const ws1 = excelWorkbook1.worksheets.get(0);

            // Copy the first column from the first worksheet into the third column of the same worksheet.
            const cells = ws1.cells;
            cells.copyColumn(cells, cells.columns.get(0).index, cells.columns.get(2).index);

            // Autofit the column.
            ws1.autoFitColumn(2);

            // Save the excel file (Excel97To2003 format for .xls)
            const outputData = excelWorkbook1.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **複数の列をコピーする方法**  

[**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-) メソッドに似ており、Aspose.Cells APIは複数のソース列を新しい場所にコピーするために [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-) メソッドも提供しています。  

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
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Create an instance of Workbook class by loading the existing spreadsheet
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet's cells collection
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Copy the first 3 columns to the 7th column
            cells.copyColumns(cells, 0, 6, 3);

            // Save the result and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **貼り付けオプションを使用して行と列を貼り付ける方法**  

Aspose.Cellsは現在、関数[**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-)および[**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-)を使用して[**PasteOptions**](https://reference.aspose.com/cells/javascript-cpp/pasteoptions/)を提供しています。これにより、Excelと同様の適切な貼り付けオプションを設定することができます。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Change Chart Data Source</title>
    </head>
    <body>
        <h1>Change Chart Data Source Example</h1>
        <p>Select an Excel file (sampleChangeChartDataSource.xlsx) from your local machine.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PasteType, CopyOptions, PasteOptions } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first sheet which contains chart
            const source = workbook.worksheets.get(0);

            // Add another sheet named DestSheet
            const destination = workbook.worksheets.add("DestSheet");

            // Set CopyOptions.ReferToDestinationSheet to true
            const options = new CopyOptions();
            options.referToDestinationSheet = true;

            // Set PasteOptions
            const pasteOptions = new PasteOptions();
            pasteOptions.pasteType = PasteType.Values;
            pasteOptions.onlyVisibleCells = true;

            // Copy all the rows of source worksheet to destination worksheet which includes chart as well
            // The chart data source will now refer to DestSheet
            destination.cells.copyRows(source.cells, 0, 0, source.cells.maxDisplayRange.rowCount, options, pasteOptions);

            // Save workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeChartDataSource.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
