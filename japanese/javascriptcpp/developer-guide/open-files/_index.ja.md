---
title: Excel、OpenOffice、Json、Csv、Htmlファイルの読み込みと管理
linktitle: ファイルを開く
type: docs
weight: 20
url: /ja/javascript-cpp/loading-saving-and-managing/
description: Aspose.Cellsを使えば、JavaScript経由でExcel、CSV、TSV、ODS、HTML、Numbers、Json、XML、Pdf、Jpg、Tiff、画像、Mht、XPSファイルの作成、開封、管理が簡単にできます。
---

{{% alert color="primary" %}}

Aspose.Cellsを使えば、Excelファイルを作成、開き、データの取得やデザイナーテンプレートを使った開発速度向上などが容易に行えます。

{{% /alert %}}

## **新しいワークブックの作成**
次の例は、ゼロから新しいワークブックを作成します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Set Cell Value</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/Aspose.Cells.lic",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Instantiate a Workbook object (new blank workbook)
            const wb = new Workbook();

            // Access the first worksheet in the workbook
            const sheet = wb.worksheets.get(0);

            // Access the "A1" cell in the sheet
            const cell = sheet.cells.get("A1");

            // Input the "Hello World!" text into the "A1" cell
            cell.value = "Hello World!";

            // Save the Excel file and prepare download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'MyBook_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and cell updated. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **ファイルを開くと保存する**
Aspose.Cellsを使えば、Excelファイルを開き、保存し、管理するのは簡単です。

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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Creating a Workbook object and opening an Excel file using its file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding new sheet
            const sheetIndex = workbook.worksheets.add("MySheet");
            const sheet = workbook.worksheets.get(sheetIndex);

            // Setting active sheet
            workbook.worksheets.activeSheetIndex = 1;

            // Setting values.
            const cells = sheet.cells;

            // Setting text
            cells.get("A1").putValue("Hello!");

            // Setting number
            cells.get("A2").putValue(1000);

            // Setting Date Time
            const cell = cells.get("A3");
            cell.putValue(new Date());
            const style = cell.style;
            style.number = 14;
            cell.style = style;

            // Setting formula
            cells.get("A4").formula = "=SUM(A1:A3)";

            // Saving the workbook and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'dest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **上級トピック**
- [ファイルを開く異なる方法](/cells/ja/javascript-cpp/different-ways-to-open-files/)
- [ワークブックを読み込む際に定義名をフィルタリングする](/cells/ja/javascript-cpp/filter-defined-names-while-loading-workbook/)
- [ワークブックまたはワークシートをロードする際にオブジェクトをフィルタする](/cells/ja/javascript-cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [テンプレートファイルからワークブックをロードする際にデータの種類をフィルタする](/cells/ja/javascript-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Excelファイルの読み込み中に警告を受け取る](/cells/ja/javascript-cpp/get-warnings-while-loading-excel-file/)
- [チャートを含まないソースExcelファイルをロードする](/cells/ja/javascript-cpp/load-source-excel-file-without-charts/)
- [ワークブック内の特定のワークシートをロードする](/cells/ja/javascript-cpp/load-specific-worksheets-in-a-workbook/)
- [指定されたプリンタ用紙サイズでワークブックを読み込む](/cells/ja/javascript-cpp/load-workbook-with-specified-printer-paper-size/)
- [異なるMicrosoft Excelバージョンのファイルを開く](/cells/ja/javascript-cpp/opening-different-microsoft-excel-versions-files/)
- [異なるフォーマットのファイルを開く](/cells/ja/javascript-cpp/opening-files-with-different-formats/)
- [大規模なデータセットを持つ大きなファイルで作業する際のメモリ使用量を最適化する](/cells/ja/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Aspose.Cellsを使用してApple Inc.が開発したNumbersスプレッドシートを読む](/cells/ja/javascript-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [時間がかかりすぎる場合はInterruptMonitorを使用して変換または読み込みを停止してください](/cells/ja/javascript-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [LightCells APIの使用](/cells/ja/javascript-cpp/using-lightcells-api/)
- [CSVをJSONに変換](/cells/ja/javascript-cpp/convert-csv-to-json/)
- [ExcelをJSONに変換](/cells/ja/javascript-cpp/convert-excel-to-json/)
- [JSONをCSVに変換](/cells/ja/javascript-cpp/convert-json-to-csv/)
- [JSONをExcelに変換](/cells/ja/javascript-cpp/convert-json-to-excel/)
- [ExcelをHtmlに変換](/cells/ja/javascript-cpp/convert-excel-to-html/)
