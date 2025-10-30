---
title: ピボットテーブルに計算フィールドを追加する
type: docs
weight: 130
url: /ja/javascript-cpp/add-calculated-field-in-pivot-table/
description: C++を使用したAspose.Cells for JavaScriptでピボットテーブルに計算フィールドを追加する方法
keywords: C++ライブラリを使用したAspose.Cells for JavaScriptでピボットテーブルに計算フィールドを追加する方法
---

## **可能な使用シナリオ**
既知のデータに基づいてピボットテーブルを作成すると、それに含まれるデータが望んでいるものではないことがあります。望んでいるデータは、これらの元のデータの組み合わせです。たとえば、データを望んだ形式にするために、元のデータを加算、減算、乗算、除算する必要があります。その場合、計算フィールドを構築し、計算用の対応する式を設定する必要があります。その後、計算フィールドで統計などの操作を行います。 

## **Excelでピボットテーブルに計算フィールドを追加する方法**
Excelのピボットテーブルに計算フィールドを挿入するには、以下の手順に従います:

1. 追加したいピボットテーブルを選択します。 
2. リボットテーブルツールの「分析」タブに移動します。
3. 「フィールド、アイテム、およびセット」をクリックし、その後、ドロップダウンメニューから「計算フィールド」を選択します。
4. 「名前」フィールドに、計算フィールドの名前を入力します。
5. 「式」フィールドに、適切なピボットテーブルのフィールド名と数学演算子を使用して実行する計算の式を入力します。 
<br>
<img src="1.png" width=80% />
6. 「OK」をクリックして計算フィールドを作成します。
7. 新しい計算フィールドは、値のセクションの下にあるピボットテーブルフィールドリストに表示されます。
8. 計算フィールドをピボットテーブルの値セクションにドラッグして、計算された値を表示します。
<br>
<img src="2.png" width=80% />

## **How to Add calculated field in Pivot Table Using Aspose.Cells for JavaScript via C++ Library**
C++を使用したAspose.Cells for JavaScriptでExcelファイルに計算フィールドを追加します。以下のサンプルコードを参照してください。例のコードを実行すると、計算フィールドを含むピボットテーブルがワークシートに追加されます。
1. 元のデータを設定し、ピボットテーブルを作成します。 
2. ピボットテーブル内の既存のPivotFieldに応じて計算フィールドを作成します。
3. 計算フィールドをデータ領域に追加します。 
4. 最後に、[output XLSX](out.xlsx)形式でブックを保存します。 

## **サンプルコード**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PivotFieldType, Utils } = AsposeCells;

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

            // Obtain the reference of the newly added worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells (converted putValue -> value)
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";
            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";
            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;
            cell = cells.get("C2");
            cell.value = 5;
            cell = cells.get("C3");
            cell.value = 20;
            cell = cells.get("C4");
            cell.value = 30;
            cell = cells.get("C5");
            cell.value = 60;

            // Adding a PivotTable to the worksheet (converted getPivotTables -> pivotTables)
            const i = ws.pivotTables.add("=A1:C5", "D10", "PivotTable1");
            // Accessing the instance of the newly added PivotTable
            const pivotTable = ws.pivotTables.get(i);
            pivotTable.addFieldToArea(PivotFieldType.Row, 0);
            // Adding a calculated field to PivotTable and drag it to data area.
            pivotTable.addCalculatedField("total", "=Count*Price", true);
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PivotTable created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
