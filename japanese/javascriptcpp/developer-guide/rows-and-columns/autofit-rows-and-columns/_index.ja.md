---
title: JavaScriptを使った行と列の自動調整（C++経由）
linktitle: 行と列の自動調整
type: docs
weight: 20
url: /ja/javascript-cpp/autofit-rows-and-columns/
description: この記事では、C++を使ったAspose.Cells for JavaScriptで範囲内のセルの行、列、結合セルの行の自動調整方法を説明します。
keywords: 行の自動調整（JavaScript+C++）、列の自動調整（JavaScript+C++）、範囲内セルの行の自動調整（JavaScript+C++）、結合セルの行の自動調整（JavaScript+C++）
---

{{% alert color="primary" %}}  
Microsoft Excelでは、セルの内容に応じてセルの幅と高さを自動調整できます。この機能は、C++を使用したAspose.Cells for JavaScriptでも利用可能で、開発者はランタイム中にセルの寸法を自動調整できます。  
{{% /alert %}}  

## **自動調整**  

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスには、Excelファイルの各シートにアクセスできる[**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションが含まれています。シートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスはシート管理のための多くのプロパティとメソッドを提供します。この記事では、[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスを使用した行や列の自動調整について説明します。  

### **行の自動調整 - シンプル**  

行の幅と高さを自動調整する最も簡単な方法は、[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスの[**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-)メソッドを呼び出すことです。[**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-)メソッドは調整対象の行のインデックスをパラメータとして受け取ります。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - AutoFit Row</title>
    </head>
    <body>
        <h1>AutoFit Row Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Auto-fitting the 3rd row of the worksheet (row index 1 is the 2nd row; original code used 1)
            worksheet.autoFitRow(1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row auto-fitted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **セル範囲内の行を自動調整する方法**  

行は多くの列で構成されます。Aspose.Cellsでは、行内のセル範囲の内容に基づいて行を自動調整できるように、[**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-number-number-)メソッドのオーバーロード版を呼び出すことが可能です。引数は次の通りです。  

- **行インデックス**：自動調整される行のインデックス。  
- **最初の列インデックス**：行の最初の列のインデックス。  
- **最後の列インデックス**：行の最後の列のインデックス。  

[**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-number-number-)メソッドは、行内のすべての列の内容をチェックし、その後行を自動調整します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - AutoFit Row</title>
    </head>
    <body>
        <h1>Auto-Fit Row Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Auto-fitting the 3rd row of the worksheet (row index 1, startColumn 0, endColumn 5)
            worksheet.autoFitRow(1, 0, 5);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row auto-fitted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **セル範囲内の列を自動調整する方法**  

列は多くの行から構成されます。列内のセル範囲の内容に基づいて列を自動調整するには、次のパラメータを受け取る[**autoFitColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumn-number-)メソッドのオーバーロード版を呼び出します。  

- **列インデックス**：自動調整される列のインデックス。  
- **最初の行インデックス**：列の最初の行のインデックス。  
- **最後の行インデックス**：列の最後の行のインデックス。  

[**autoFitColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumn-number-)メソッドは、列内のすべての行の内容をチェックし、その後列を自動調整します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells AutoFit Column Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Auto-fitting the Column of the worksheet (column index 4)
            worksheet.autoFitColumn(4);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column auto-fitted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **結合セルの行を自動調整する方法**  

Aspose.Cellsを使用すれば、[**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) APIを用いて結合セルを含むセルの行も自動調整可能です。[**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions)クラスは、結合セル用に行自動調整に使える[**AutoFitterOptions.autoFitMergedCellsType()**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#autoFitMergedCellsType--)プロパティを提供しています。[**AutoFitterOptions.autoFitMergedCellsType()**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#autoFitMergedCellsType--)は、[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/javascript-cpp/autofitmergedcellstype)列挙可能な値と次のメンバーを受け入れます。  

- なし: 結合セルを無視します。  
- 最初の行のみ: 最初の行の高さのみ拡張します。  
- 最終行のみ: 最後の行の高さのみ拡張します。  
- 各行: 各行の高さのみ拡張します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Autofit Rows for Merged Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoFitterOptions, AutoFitMergedCellsType } = AsposeCells;

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
            let wb;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                wb = new Workbook();
            }

            // Get the first (default) worksheet
            const worksheet = wb.worksheets.get(0);

            // Create a range A1:B1
            const range = worksheet.cells.createRange(0, 0, 1, 2);

            // Merge the cells
            range.merge();

            // Insert value to the merged cell A1
            const cell = worksheet.cells.get(0, 0);
            cell.value = "A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end";

            // Create a style object
            const style = cell.style;

            // Set wrapping text on
            style.isTextWrapped = true;

            // Apply the style to the cell
            cell.style = style;

            // Create an object for AutoFitterOptions
            const options = new AutoFitterOptions();

            // Set auto-fit for merged cells
            options.autoFitMergedCellsType = AutoFitMergedCellsType.EachLine;

            // Autofit rows in the sheet (including the merged cells)
            worksheet.autoFitRows(options);

            // Save the Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AutofitRowsforMergedCells.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
また、[**autoFitRows**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRows-number-number-AutoFitterOptions-)や[**autoFitColumns**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumns-number-number-AutoFitterOptions-)のオーバーロード版を使用して、行や列の範囲と[**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions)のインスタンスを渡し、選択した行や列の高さや幅を desired [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) に自動調整することも可能です。  

上記メソッドのシグニチャは次の通りです：  

1. autoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) options)  
1. autoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) options)  
{{% /alert %}}  

## **重要なこと**  

{{% alert color="primary" %}}  
セルが結合されている場合、autoFitメソッドは適用されません。これはMicrosoft Excelと同じ動作です。これを回避するには autofilter API を使用してください。さらに、セル内のテキストが折り返されている場合も、[**autoFitColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumn-number-)メソッドは適用されません。autoFitメソッドは時間がかかるため、アプリケーションの効率性を保つためにこれらの呼び出しはできるだけ少なくしてください。  
{{% /alert %}}  

## **高度なトピック**  
- [結合されたセルの行のAutoFit](/cells/ja/javascript-cpp/autofit-rows-for-merged-cells/)
