---
title: C++経由のJavaScriptを使用したMicrosoft Excelファイルのワークシート管理
linktitle: ワークシート
type: docs
weight: 90
url: /ja/javascript-cpp/manage-worksheets/
description: C++経由のAspose.Cells for JavaScriptを使用して、ワークシートの追加、削除、およびアクティベートを行います。
---

{{% alert color="primary" %}}
Aspose.Cellsの柔軟なAPIを使用して、Microsoft Excelファイルでワークシートを簡単に作成、管理できます。このトピックでは、Microsoft Excelファイルにワークシートを追加および削除する方法について説明します。
{{% /alert %}}

Aspose.Cellsは、Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスは、ワークシートの管理のためのさまざまなプロパティとメソッドを提供します。

## **新しいExcelファイルにワークシートを追加する**

プログラムで新しいExcelファイルを作成するには：

1. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスのオブジェクトを作成します。  
2. [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection)クラスの[**WorksheetCollection.add(SheetType)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#add-sheettype-)メソッドを呼び出します。 空のワークシートが自動的にExcelファイルに追加されます。 新しいワークシートのシートインデックスを[**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションに渡すことで参照できます。  
3. ワークシート参照を取得します。  
4. ワークシート上で作業を行います。  
5. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスの[**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-)メソッドを呼び出して新しいワークシートを含むExcelファイルを保存します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Add Worksheet Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Get current worksheet count (converted from getWorksheets().getCount())
            const i = workbook.worksheets.count;

            // Add a new worksheet (converted from getWorksheets().add())
            workbook.worksheets.add();

            // Obtain the newly added worksheet by index (converted from getWorksheets().get(i))
            const worksheet = workbook.worksheets.get(i);

            // Set the name of the newly added worksheet (converted from setName)
            worksheet.name = "My Worksheet";

            // Save the workbook to XLS format and prepare download
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **デザイナースプレッドシートにワークシートを追加する**

デザイナスプレッドシートにワークシートを追加する操作は、新しいワークシートの追加と同じですが、既存のExcelファイルを開く必要があります。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスを使用してデザイナスプレッドシートを開くことができます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Worksheet</title>
    </head>
    <body>
        <h1>Add Worksheet Example</h1>
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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding a new worksheet to the Workbook object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Setting the name of the newly added worksheet
            worksheet.name = "My Worksheet";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **シート名を使用してワークシートにアクセスする**

名前またはインデックスを指定して任意のワークシートにアクセスできます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example: Read Cell Value</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing a worksheet using its sheet name
            const worksheet = workbook.worksheets.get("Sheet1");
            const cell = worksheet.cells.get("A1");

            console.log(cell.value);
            document.getElementById('result').innerHTML = `<p>Cell A1 value: ${cell.value}</p>`;
        });
    </script>
</html>
```

## **シート名を使用してワークシートを削除する**

ファイルからワークシートを削除するには、[**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection)クラスの[**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#removeAt-string-)メソッドを呼び出します。シート名を渡して特定のワークシートを削除できます。

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

            // Removing a worksheet using its sheet name
            workbook.worksheets.removeAt("Sheet1");

            // Save workbook
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Sheet Indexを使用してワークシートを削除する**

名前でワークシートを削除するのは、ワークシートの名前がわかっている場合に効果的です。ワークシート名が不明な場合は、シート番号を指定するオーバーロードされた[**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#removeAt-string-)メソッドを使用してください。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Remove First Worksheet</h1>
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

            // Removing a worksheet using its sheet index
            workbook.worksheets.removeAt(0);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **シートのアクティブ化およびワークシート内のアクティブセルを作成します**

時には、Microsoft Excel ファイルを開いたときに特定のワークシートをアクティブにして表示させる必要があります。同様に、特定のセルをアクティブにしてスクロールバーをそのセルに合わせることもあります。Aspose.Cellsはこれらすべてのタスクを実行できます。

**アクティブなシート**とは、作業中のシートのことです。タブ上のアクティブなシートの名前は、デフォルトで太字になります。

**アクティブなセル**は選択されたセルであり、タイプを始めるとデータが入力されるセルです。1度に1つのセルがアクティブです。アクティブなセルは太い枠で強調表示されます。

### **シートのアクティブ化とセルをアクティブにする**

Aspose.Cellsはシートとセルをアクティブにするための特定のAPI呼び出しを提供します。例えば、[**WorksheetCollection.activeSheetIndex**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#activeSheetIndex--)プロパティはワークブック内のアクティブなシートを設定するのに役立ちます。同様に、[**Worksheet.activeCell**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#activeCell--)プロパティはワークシート内でアクティブなセルを設定および取得するために使用されます。

特定のデータを表示させるために水平または垂直スクロールバーを目的の行と列のインデックス位置に合わせるには、[**Worksheet.firstVisibleRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#firstVisibleRow--)と[**Worksheet.firstVisibleColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#firstVisibleColumn--)プロパティを使用します。

次の例は、ワークシートをアクティブ化し、その中のアクティブなセルにします。生成された出力では、スクロールバーは、2行と2列を最初に表示されるようにスクロールします。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Create Workbook Example</h1>
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
            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Add a worksheet if collection is empty
            const worksheets = workbook.worksheets;
            if (worksheets.count === 0) {
                worksheets.add();
            }

            // Get the first worksheet in the workbook.
            const worksheet1 = worksheets.get(0);

            // Get the cells in the worksheet.
            const cells = worksheet1.cells;

            // Input data into B2 cell.
            const cell = cells.get(1, 1);
            cell.value = "Hello World!";

            // Set the first sheet as an active sheet.
            worksheets.activeSheetIndex = 0;

            // Set B2 cell as an active cell in the worksheet.
            worksheet1.activeCell = "B2";

            // Set the B column as the first visible column in the worksheet.
            worksheet1.firstVisibleColumn = 1;

            // Set the 2nd row as the first visible row in the worksheet.
            worksheet1.firstVisibleRow = 1;

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **高度なトピック**
- [ワークシートのコピーおよび移動](/cells/ja/javascript-cpp/copying-and-moving-worksheets/)  
- [ワークシート内のセル数を数える](/cells/ja/javascript-cpp/count-number-of-cells-in-the-worksheet/)  
- [空のワークシートを検出する](/cells/ja/javascript-cpp/detecting-empty-worksheets/)  
- [ワークシートがダイアログシートであるかを検索する](/cells/ja/javascript-cpp/find-if-the-worksheet-is-dialog-sheet/)  
- [ワークシートの一意のIDを取得](/cells/ja/javascript-cpp/get-worksheet-unique-id/)  
- [シナリオを作成、操作、またはワークシートから削除する](/cells/ja/javascript-cpp/create-manipulate-or-remove-scenarios-from-worksheets/)  
- [ページ区切りの管理](/cells/ja/javascript-cpp/managing-page-breaks/)  
- [ページ設定機能](/cells/ja/javascript-cpp/page-setup-features/)  
- [Aspose.Cellsを使用したOpenXmlのSheet.SheetIdプロパティを利用する](/cells/ja/javascript-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)  
- [ワークシートビュー](/cells/ja/javascript-cpp/worksheet-views/)
