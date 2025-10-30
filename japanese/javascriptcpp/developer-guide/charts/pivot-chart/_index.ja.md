---
title: C++ を使用した Aspose.Cells for JavaScript でピボットチャートを追加する方法
linktitle: ピボットチャート
type: docs
weight: 100
url: /ja/javascript-cpp/how-to-add-pivot-chart/
description: C++ を使用した Aspose.Cells for JavaScript でピボットチャートを追加する方法
keywords: C++ を使用した JavaScript のピボットチャート
---
## PivotChartとは

ピボットチャートは、ピボットテーブルのデータを視覚的に表現したものです。ピボットチャートは、要約の概要、分析、探索、および提示のための方法を提供します。主な特徴と側面は以下の通りです：

1. 動的データ表現：ピボットチャートは、ピボットテーブルの変更に応じて自動的に更新されます。フィールドの追加や削除により、ピボットチャートもそれに応じて更新されます。

1. インタラクティブ：ピボットチャートはインタラクティブで、フィルタリング、並べ替え、詳細表示が可能です。これにより、データセットのさまざまな側面を簡単に探索できます。

1. 柔軟なレイアウト：ユーザーはフィールドをドラッグアンドドロップしてピボットチャートのレイアウトを変更でき、データの視覚化に柔軟性を持たせることができます。

1. 様々なチャートタイプ：棒グラフ、折れ線グラフ、円グラフなど、さまざまなタイプのチャートで作成可能です。データの性質や洞察したい内容に応じて選択します。

1. 要約：ピボットチャートは大量のデータを要約し、合計値、平均値、カウント、その他の統計情報を表示できます。

1. フィルタリング：特定の条件を満たすデータのみを表示するフィルタリング機能もあります。

<br>
ピボットチャートは、ビジネスインテリジェンスやデータ分析によく使われ、複雑なデータセットの明確で簡潔なビジュアル概要を提供します。データ駆動の意思決定に強力なツールです。

## C++ を使用した Aspose.Cells for JavaScript でピボットチャートを追加する方法

### **ピボットテーブルの追加**

C++ を使用してピボットテーブルを作成する方法：

1. セルオブジェクトの`putValue`メソッドを使ってワークシートにデータを追加します。既にデータが入力されたテンプレートファイルを使用することも可能です。そのデータはピボットテーブルのデータソースとして利用されます。
1. `PivotTables`コレクションの`add`メソッドを呼び出してピボットテーブルをワークシートに追加します。
1. `PivotTables`コレクションからインデックスを渡して新しい`PivotTable`オブジェクトにアクセスします。`.PivotTable`オブジェクトにカプセル化されたピボットテーブルのいずれかを使用して管理します。

以下にコード例を示します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Populate Worksheet and Download</h1>
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
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Obtaining the reference of the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Name the sheet
            sheet.name = "Data";
            const cells = sheet.cells;

            // Setting the header values to the cells
            cells.get("A1").value = "Employee";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Product";
            cells.get("D1").value = "Continent";
            cells.get("E1").value = "Country";
            cells.get("F1").value = "Sale";

            const namesAndValues = [
                ["David", 1, "Maxilaku", "Asia", "China", 2000],
                ["David", 2, "Maxilaku", "Asia", "India", 500],
                ["David", 3, "Chai", "Asia", "Korea", 1200],
                ["David", 4, "Maxilaku", "Asia", "India", 1500],
                ["James", 1, "Chang", "Europe", "France", 500],
                ["James", 2, "Chang", "Europe", "France", 1500],
                ["James", 3, "Chang", "Europe", "Germany", 800],
                ["James", 4, "Chang", "Europe", "Italy", 900],
                ["James", 4, "Chang", "Europe", "France", 500],
                ["Miya", 1, "Geitost", "America", "U.S.", 1600],
                ["Miya", 2, "Chai", "America", "U.S.", 600],
                ["Miya", 3, "Geitost", "America", "Brazil", 2000],
                ["Miya", 2, "Geitost", "America", "U.S.", 500],
                ["Miya", 3, "Maxilaku", "America", "Canada", 900],
                ["Miya", 4, "Geitost", "America", "U.S.", 700],
                ["Miya", 5, "Geitost", "America", "U.S.", 1400],
                ["Miya", 6, "Ikuru", "Europe", "Italy", 1350],
                ["Miya", 7, "Ikuru", "Europe", "France", 300],
                ["Miya", 8, "Ikuru", "Europe", "Italy", 500],
                ["Miya", 9, "Ikuru", "America", "New Zealand", 1000],
                ["Miya", 10, "Ipoh Coffee", "Oceania", "Australia", 1500],
                ["Miya", 11, "Chocolade", "Oceania", "Australia", 500],
                ["Miya", 12, "Chocolade", "Oceania", "New Zealand", 1500],
                ["Miya", 13, "Chocolade", "Oceania", "S.Africa", 1600],
                ["Miya", 14, "Chocolade", "Africa", "Egypt", 1000],
                ["Miya", 15, "Chocolade", "Africa", "Egypt", 1200],
                ["Miya", 16, "Chocolade", "Africa", "Egypt", 1300],
            ];

            namesAndValues.forEach((item, index) => {
                const rowIndex = index + 2;
                cells.get(`A${rowIndex}`).value = item[0];
                cells.get(`B${rowIndex}`).value = item[1];
                cells.get(`C${rowIndex}`).value = item[2];
                cells.get(`D${rowIndex}`).value = item[3];
                cells.get(`E${rowIndex}`).value = item[4];
                cells.get(`F${rowIndex}`).value = item[5];
            });

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet populated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **ピボットチャートの追加**

C++ で Aspose.Cells for JavaScript を使ってピボットチャートを作成する方法：

1. チャートを追加します。
1. グラフの `PivotSource` を既存のピボットテーブルを指すように設定します。
1. 他の属性を設定します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Pivot Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding a new sheet of Chart type
            const sheetIndex = workbook.worksheets.add(AsposeCells.SheetType.Chart);
            const sheet3 = workbook.worksheets.get(sheetIndex);
            sheet3.name = "PivotChart";

            // Adding a column chart
            const index = sheet3.charts.add(AsposeCells.ChartType.Column, 0, 5, 28, 16);

            // Setting the pivot chart data source and hiding pivot field buttons
            const chart = sheet3.charts.get(index);
            chart.pivotSource = "PivotTable!PivotTable1";
            chart.hidePivotFieldButtons = false;

            // Saving the modified Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'pivotChart_test_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Pivot chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
