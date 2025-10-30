---
title: JavaScriptを介したC++で行や列、スクロールバーの表示・非表示を行います
linktitle: 行、列、およびスクロールバーを表示して非表示にする
type: docs
weight: 20
url: /ja/javascript-cpp/show-and-hide-rows-columns-and-scroll-bars/
description: この記事は、JavaScriptを介してC++を使い、Excelワークシートの行や列、スクロールバーの表示と非表示をプログラムで実行する方法を示しています。スクロールバーの表示を制御し、複数の行や列を効率的に非表示にします。
---

{{% alert color="primary" %}}  
Aspose.Cellsはワークシートの行、列、およびスクロールバーの表示を制御する方法を提供しています。  
{{% /alert %}}  

## **行や列の表示と非表示**  

Aspose.Cells for JavaScriptをC++で提供するクラス、[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)はMicrosoft Excelファイルを表します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスは、そのワークシート内のすべてのセルを表す[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)コレクションを提供します。[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)コレクションは、ワークシート内の行または列を管理するための複数のメソッドを提供します。詳細は以下に述べます。  

### **行と列を表示**  

開発者は、[**unhideRow(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideRow-number-number-)と[**unhideColumn(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideColumn-number-number-)のメソッドを呼び出すことで、非表示になっている行や列を表示させることができます。どちらのメソッドも、2つのパラメータを取ります：  

- **行または列のインデックス** - 特定の行または列を表示するために使用される行または列のインデックス。  
- **行の高さまたは列の幅** - 非表示にする行または列に割り当てられた行の高さまたは列の幅。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Unhide Row and Column Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.unhideRow(2, 13.5);
            worksheet.cells.unhideColumn(1, 8.5);

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
隠された列を表示する場合、以前に割り当てられた幅や元の幅に復元したい場合は、負の幅で列を非表示解除してください。例：worksheet.Cells.unhideColumn(5, -1)  
{{% /alert %}}  

### **行と列を非表示**  

開発者は、[**hideRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideRow-number-)と[**hideColumn(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideColumn-number-)のメソッドを呼び出すことで、行や列を非表示にできます。どちらのメソッドも、特定の行や列のインデックスをパラメータとして受け取り、その行または列を非表示にします。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Hide Row/Column Example</h1>
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Hide the 3rd row (index 2) and 2nd column (index 1)
            worksheet.cells.hideRow(2);
            worksheet.cells.hideColumn(1);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row and column hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
また、行または列を非表示にすることもできます。その際は、行の高さまたは列の幅をそれぞれ0に設定することができます。  
{{% /alert %}}  

### **複数の行と列を非表示**  

開発者は、[**hideRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideRows-number-number-)と[**hideColumns(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideColumns-number-number-)のメソッドを呼び出し、複数の行や列を一度に非表示にできます。これらの両方のメソッドは、開始行または列のインデックスと隠す行または列の数をパラメータとして受け取ります。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Hide Rows and Columns</title>
    </head>
    <body>
        <h1>Hide Rows and Columns Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding 3, 4 and 5 rows in the worksheet (rows are zero-based index)
            worksheet.cells.hideRows(2, 3);

            // Hiding 2 and 3 columns in the worksheet (columns are zero-based index)
            worksheet.cells.hideColumns(1, 2);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **スクロールバーの表示と非表示**  

スクロールバーは、どのファイルの内容をナビゲートするために使用されます。通常、2種類のスクロールバーがあります。  

- 垂直スクロールバー  
- 水平スクロールバー  

Microsoft Excelは、ユーザーがワークシートの内容をスクロールできるように、水平および垂直のスクロールバーを提供しています。Aspose.Cellsを使用すると、Excelファイルの両方のタイプのスクロールバーの表示/非表示を制御することができます。  

### **スクロールバーの表示を制御する**  

Aspose.Cellsは、Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスは、Excelファイルの管理に役立つさまざまなプロパティとメソッドを備えています。スクロールバーの表示制御には、[**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--)と[**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--)プロパティを使用します。[**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--)と[**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--)はBoolean型のプロパティであり、これらは**true**または**false**のみを格納できます。  

#### **スクロールバーを表示する**  

スクロールバーを表示するには、[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスの[**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--)または[**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--)プロパティを**true**に設定します。  

#### **スクロールバーを非表示にする**  

スクロールバーを非表示にするには、[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスの[**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--)または[**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--)プロパティを**false**に設定します。  

**サンプルコード**  

以下は、Excelファイルであるbook1.xlsを開き、両方のスクロールバーを非表示にし、変更されたファイルをoutput.xlsとして保存する完全なコードです。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Hide Scrollbars Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Hiding the vertical scroll bar of the Excel file
            workbook.settings.isVScrollBarVisible = false;

            // Hiding the horizontal scroll bar of the Excel file
            workbook.settings.isHScrollBarVisible = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Scrollbars hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
