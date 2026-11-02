---
title: Aspose.Cells for JavaScript via C++ でピボットテーブルに行フィールドと列フィールドを追加
linktitle: Aspose.Cells for JavaScript via C++ でピボットテーブルに行フィールドと列フィールドを追加
description: Aspose.Cells for JavaScript via C++ で、ピボットテーブルに行フィールドと列フィールドを追加し、PivotField.SetSubtotals と PivotFieldSubtotalType を使用してピボットフィールドの小計を制御する方法を学びます。
keywords: Aspose.Cells, JavaScript via C++, ピボットテーブル, 行フィールド, 列フィールド, PivotField, setSubtotals, PivotFieldSubtotalType, 小計, JavaScript, Excel ピボットテーブル
type: docs
weight: 220
url: /ja/javascript-cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **行領域または列領域にフィールドを追加する**
`pivotTable.addFieldToArea(fieldType, fieldName)` メソッドは、ベースフィールドをソースデータから 4 つのピボット領域のいずれかに移動します。`fieldType` 引数には、次の `PivotFieldType` 値のいずれかを指定できます。
- `Row` — 左側に縦方向に配置されるフィールド
- `Column` — 上部に横方向に配置されるフィールド
- `Data` — 値が集計されるフィールド
- `Page` — レポートフィルターとして使用されるフィールド
フィールドのネスト順序は重要です。`Category` を最初に行領域に追加し、その後 `Item` を追加すると、外側のグループが `Category`、内側のグループが `Item` になります。順序を逆にすると、階層も逆になります。

## **ピボットフィールドの小計**
`pivotField.setSubtotals(subtotalType, shown)` メソッドは、ピボットフィールドに表示される小計行を制御します。各呼び出しでは、1 種類の小計を個別に有効または無効にします。`shown = true` を渡すと小計行が表示され、`shown = false` を渡すと非表示になります。各呼び出しが 1 種類の小計にのみ影響するため、異なる `subtotalType` 値を指定してこのメソッドを複数回呼び出すと、必要な小計のサブセットを構成できます。
`PivotFieldSubtotalType` 列挙型は、利用可能な小計の種類を定義します。
- `Automatic` — Aspose.Cells が既定の選択を決定します（数値フィールドでは通常 `Sum`）
- `None` — すべての小計行を非表示にします
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
小計は、行領域（または列領域）に 2 つ以上のピボットフィールドがある場合にのみ表示されます。フィールドが 1 つだけの場合は、小計対象となるグループ間のデータがないため、`setSubtotals` を呼び出しても表示上の影響はありません。そのため、この記事では、すべての例に行フィールドを 2 つ（外側は `Category`、内側は `Item`）設定し、各 `Category` グループにおける小計の境界が明確になるようにしています。
{{% /alert %}}

## **シナリオ 1 — 自動（既定）の小計**
`setSubtotals` を一度も呼び出さない場合、Aspose.Cells は数値フィールドに `Automatic` の選択を適用します。次の例では、外側の `Category` 行フィールドに対して `setSubtotals(PivotFieldSubtotalType.Automatic, true)` を呼び出すことで、この動作を明示的に確認しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const cells = worksheet.cells;
            cells.get(0, 0).value = "Category";
            cells.get(0, 1).value = "Item";
            cells.get(0, 2).value = "Year";
            cells.get(0, 3).value = "Amount";
            cells.get(1, 0).value = "Fruit";
            cells.get(1, 1).value = "Apple";
            cells.get(1, 2).value = 2020;
            cells.get(1, 3).value = 100;
            cells.get(2, 0).value = "Fruit";
            cells.get(2, 1).value = "Apple";
            cells.get(2, 2).value = 2021;
            cells.get(2, 3).value = 150;
            cells.get(3, 0).value = "Fruit";
            cells.get(3, 1).value = "Banana";
            cells.get(3, 2).value = 2020;
            cells.get(3, 3).value = 80;
            cells.get(4, 0).value = "Fruit";
            cells.get(4, 1).value = "Banana";
            cells.get(4, 2).value = 2021;
            cells.get(4, 3).value = 90;
            cells.get(5, 0).value = "Vegetable";
            cells.get(5, 1).value = "Carrot";
            cells.get(5, 2).value = 2020;
            cells.get(5, 3).value = 50;
            cells.get(6, 0).value = "Vegetable";
            cells.get(6, 1).value = "Carrot";
            cells.get(6, 2).value = 2021;
            cells.get(6, 3).value = 60;
            cells.get(7, 0).value = "Vegetable";
            cells.get(7, 1).value = "Daikon";
            cells.get(7, 2).value = 2020;
            cells.get(7, 3).value = 40;
            cells.get(8, 0).value = "Vegetable";
            cells.get(8, 1).value = "Daikon";
            cells.get(8, 2).value = 2021;
            cells.get(8, 3).value = 45;
            const pivotTableIndex = worksheet.pivotTables.add("=A1:D9", "F3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);
            pivotTable.calculateData();
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_automatic.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **シナリオ 2 — すべての小計を非表示にする（None）**
`setSubtotals(PivotFieldSubtotalType.None, true)` を呼び出すと、ピボットテーブルからすべての小計行が削除され、フィールド行と下部のグランド totaledだけが残ります。集計行を含まない元のグループ化データを表示したい場合に便利です。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const headers = ["Category", "Item", "Year", "Amount"];
            for (let j = 0; j < headers.length; j++) {
                worksheet.cells.get(0, j).value = headers[j];
            }
            const data = [
                ["Fruit", "Apple", 2020, 100],
                ["Fruit", "Apple", 2021, 150],
                ["Fruit", "Banana", 2020, 80],
                ["Fruit", "Banana", 2021, 90],
                ["Vegetable", "Carrot", 2020, 50],
                ["Vegetable", "Carrot", 2021, 60],
                ["Vegetable", "Daikon", 2020, 40],
                ["Vegetable", "Daikon", 2021, 45]
            ];
            for (let i = 0; i < data.length; i++) {
                for (let j = 0; j < data[i].length; j++) {
                    worksheet.cells.get(i + 1, j).value = data[i][j];
                }
            }
            const pivotTableIndex = worksheet.pivotTables.add("=A1:D9", "F3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_none.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **シナリオ 3 — カスタム小計のサブセット（Sum + Average）**
小計タイプは 1 種類に限定されません。各 `setSubtotals` 呼び出しは 1 種類の小計に対して独立して作用するため、メソッドを 2 回（1 回目は `Sum`、2 回目は `Average`）呼び出すと、各 `Category` グループに 2 種類からなる小計行のカスタムサブセットが表示されます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const cells = worksheet.cells;
            cells.get("A1").value = "Category";
            cells.get("B1").value = "Item";
            cells.get("C1").value = "Year";
            cells.get("D1").value = "Amount";
            cells.get(1, 0).value = "Fruit";
            cells.get(1, 1).value = "Apple";
            cells.get(1, 2).value = 2020;
            cells.get(1, 3).value = 100;
            cells.get(2, 0).value = "Fruit";
            cells.get(2, 1).value = "Apple";
            cells.get(2, 2).value = 2021;
            cells.get(2, 3).value = 150;
            cells.get(3, 0).value = "Fruit";
            cells.get(3, 1).value = "Banana";
            cells.get(3, 2).value = 2020;
            cells.get(3, 3).value = 80;
            cells.get(4, 0).value = "Fruit";
            cells.get(4, 1).value = "Banana";
            cells.get(4, 2).value = 2021;
            cells.get(4, 3).value = 90;
            cells.get(5, 0).value = "Vegetable";
            cells.get(5, 1).value = "Carrot";
            cells.get(5, 2).value = 2020;
            cells.get(5, 3).value = 50;
            cells.get(6, 0).value = "Vegetable";
            cells.get(6, 1).value = "Carrot";
            cells.get(6, 2).value = 2021;
            cells.get(6, 3).value = 60;
            cells.get(7, 0).value = "Vegetable";
            cells.get(7, 1).value = "Daikon";
            cells.get(7, 2).value = 2020;
            cells.get(7, 3).value = 40;
            cells.get(8, 0).value = "Vegetable";
            cells.get(8, 1).value = "Daikon";
            cells.get(8, 2).value = 2021;
            cells.get(8, 3).value = 45;
            const pivotTables = worksheet.pivotTables;
            const i = pivotTables.add("=A1:D9", "F3", "PivotTable1");
            const pivotTable = pivotTables.get(i);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Sum, true);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Average, true);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_custom.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **まとめ**
3 つのシナリオで異なるのは、`setSubtotals` の呼び出しだけです。データセット、フィールド、および各フィールドが割り当てられる領域はすべて同一です。そのため、各レイアウトを直接比較できます。
- **フィールドの配置。** `pivotTable.addFieldToArea(PivotFieldType.Row, fieldName)` は、ソース列をあるピボット領域に移動します。同じ領域内では呼び出し順が表示順になるため、最初に呼び出したフィールドが最も外側のグループになります。小計には、同じ領域内に 2 つ以上のフィールドが必要です。フィールドが 1 つの場合、グループ間には小計対象となる内容がありません。
- **シナリオ 1 — 自動小計。** `setSubtotals` を呼び出さないままにすると、選択は Excel に委ねられ、Excel は数値フィールドに独自の既定の小計を適用します。`PivotFieldSubtotalType.Automatic` を指定して `setSubtotals` を呼び出すと、選択が暗黙的になるのではなく、明示的に記録されます。
- **シナリオ 2 — 小計なし。** `PivotFieldSubtotalType.None` を指定した `setSubtotals` は既定の小計を無効にするため、ピボットテーブルはフィールド行とグランド totaledを保持しますが、Excel が通常その間に挿入する小計行は削除されます。
- **シナリオ 3 — 選択したサブセット。** 各呼び出しは正確に 1 種類の小計を切り替え、呼び出しは互いにリセットするのではなく累積されます。したがって、`PivotFieldSubtotalType.Sum` で 1 回、`PivotFieldSubtotalType.Average` で 1 回呼び出すと、両方が有効になり、ピボットテーブルには Sum の小計、Average の小計、およびグランド totaledが表示されます。

{{% alert color="primary" %}}
小計の動作は行領域に固有のものではありません。`pivotTable.getColumnFields()` から取得したフィールドに対して同じ `setSubtotals` 呼び出しを行っても、列軸に同じ 3 つのレイアウトが得られます。これは、この設定がピボットフィールドに属し、配置されている軸の属性ではないためです。
{{% /alert %}}

## **関連記事**
- [ピボットテーブルのページフィールド](/cells/ja/javascript-cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for JavaScript via C++ でピボットテーブルを更新する](/cells/ja/javascript-cpp/refresh-pivot-table/)
- [ピボットテーブルにスタイルを適用する](/cells/ja/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}