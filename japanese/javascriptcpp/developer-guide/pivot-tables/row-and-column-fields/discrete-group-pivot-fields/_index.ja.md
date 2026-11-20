---
title: ピボットフィールド項目の離散グループ化
linktitle: 離散グループ化
description: DiscreteGroupItem と `PivotFieldGroupOptions.discreteGroupItems` を使用して、`Aspose.Cells for JavaScript via C++` でピボットフィールド項目を果物や野菜など、任意の名前を設定したカスタムグループにグループ化する方法を学びます。
keywords: Aspose.Cells, ピボットテーブル, 離散グループ化, DiscreteGroupItem, PivotFieldGroupOptions, ピボット項目のグループ化, カスタムグループ, PivotField.group, Aspose.Cells for JavaScript via C++, Excel ピボットテーブル
type: docs
weight: 90
url: /ja/javascript-cpp/discrete-group-pivot-fields/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **使用可能なシナリオ**
- 自動グループ化では、データ型に基づいて項目をまとめます。たとえば、日付を月や四半期単位にまとめ、数値を範囲別にまとめます。離散グループ化では逆に、特定で無関係な項目を、任意の名前を設定したカスタムグループにまとめます。たとえば、商品を果物と野菜に、店舗を地域に、アカウントをゾーンにグループ化します。Aspose.Cells は `DiscreteGroupItem` クラスと `PivotFieldGroupOptions.discreteGroupItems` プロパティを通じて離散グループ化を提供します。
- `DiscreteGroupItem` は、グループ名と、それに属する項目で構成されます。項目は、名前（`new DiscreteGroupItem("fruit", ["grape", "cherry"])`）またはソースデータ内の 0 始まりの位置（`new DiscreteGroupItem("fruit", [0, 3])`）で識別できます。どちらの形式でも同じ結果になります。
- 離散グループ化は、`PivotField.group(PivotFieldGroupOptions)` にオプションを渡すことで、ピボットテーブルの行領域または列領域にあるフィールドに適用できます。

## **項目名でピボットフィールド項目をグループ化**
次の例では、製品、日付、金額からなる小さな販売データを作成し、そのデータからピボットテーブルを生成します。`product` を行領域、`date` を列領域、`amount` をデータ領域に配置してから、項目名に基づいて、`fruit`（`grape`、`cherry`）と `vegetables`（`carrot`、`potato`）の 2 つのカスタムグループを定義します。結果には 2 階層の行レイアウトが表示され、外側のレベルにはグループ名が、その下には元の項目がネストされます。これにより、カスタムグループごと、および項目ごとに傾向を読み取ることができます。

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
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            const { Workbook, DiscreteGroupItem, PivotFieldGroupOptions } = AsposeCells;
            document.getElementById('runExample').addEventListener('click', async () => {
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                cells.get(0, 0).value = "product";
                cells.get(1, 0).value = "grape";
                cells.get(2, 0).value = "carrot";
                cells.get(3, 0).value = "potato";
                cells.get(4, 0).value = "cherry";
                const dateStyle = workbook.createStyle();
                dateStyle.custom = "m/d/yyyy";
                cells.get(0, 1).value = "date";
                cells.get(1, 1).value = new Date(2021, 1, 5);
                cells.get(2, 1).value = new Date(2022, 2, 8);
                cells.get(3, 1).value = new Date(2023, 3, 10);
                cells.get(4, 1).value = new Date(2024, 4, 16);
                for (let r = 1; r <= 4; r++) {
                    cells.get(r, 1).style = dateStyle;
                }
                cells.get(0, 2).value = "amount";
                cells.get(1, 2).value = 50;
                cells.get(2, 2).value = 60;
                cells.get(3, 2).value = 70;
                cells.get(4, 2).value = 80;
                // Add a pivot table with the destination cell A12 (row 11, column 0)
                const pivotTable = sheet.pivotTables.add("=Sheet1!A1:C5", 11, 0);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
                pivotTable.pivotTableStyleType =
                    AsposeCells.PivotTableStyleType.PivotTableStyleMedium10;
                // Group specific items into custom groups by item names
                const fruit = new DiscreteGroupItem("fruit", ["grape", "cherry"]);
                const vegetable = new DiscreteGroupItem("vegetable", ["carrot", "potato"]);
                const groupOptions = new PivotFieldGroupOptions();
                groupOptions.discreteGroupItems = [fruit, vegetable];
                pivotTable.rowFields.get(0).group(groupOptions);
                pivotTable.calculateData();
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputDiscreteGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

`calculateData()` の実行後、ピボットテーブルの行領域には `fruit`（`grape` 50、`cherry` 80）と `vegetable`（`carrot` 60、`potato` 70）が表示され、総合計は 260 になります。列ラベルには、4 つの日付（`2/5/2021`、`3/8/2022`、`4/10/2023`、`5/16/2024`）が保持されます。

## **項目インデックスでピボットフィールド項目をグループ化**
項目名が長い場合やローカライズされている場合は、`DiscreteGroupItem` の 2 番目のコンストラクターで、インデックスによって項目を識別できます。インデックスは、項目がソースデータに現れる順序での 0 始まりの位置であり、アルファベット順ではありません。上記のサンプルデータでは、`grape` は項目 0、`carrot` は項目 1、`potato` は項目 2、`cherry` は項目 3 となるため、`fruit` は `{ 0, 3 }`、`vegetable` は `{ 1, 2 }` です。結果は、名前に基づいてグループ化した例と同じになります。

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
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            const {
                Workbook,
                SaveFormat,
                DiscreteGroupItem,
                PivotFieldGroupOptions
            } = AsposeCells;
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').addEventListener('click', async () => {
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                cells.get(0, 0).value = "product";
                cells.get(1, 0).value = "grape";
                cells.get(2, 0).value = "carrot";
                cells.get(3, 0).value = "potato";
                cells.get(4, 0).value = "cherry";
                const dateStyle = workbook.createStyle();
                dateStyle.custom = "m/d/yyyy";
                cells.get(0, 1).value = "date";
                cells.get(1, 1).value = new Date(2021, 1, 5);
                cells.get(2, 1).value = new Date(2022, 2, 8);
                cells.get(3, 1).value = new Date(2023, 3, 10);
                cells.get(4, 1).value = new Date(2024, 4, 16);
                for (let r = 1; r <= 4; r++) {
                    cells.get(r, 1).style = dateStyle;
                }
                cells.get(0, 2).value = "amount";
                cells.get(1, 2).value = 50;
                cells.get(2, 2).value = 60;
                cells.get(3, 2).value = 70;
                cells.get(4, 2).value = 80;
                // Add a pivot table with the destination cell A12 (row 11, column 0)
                const pivotTable = sheet.pivotTables.add("=Sheet1!A1:C5", 11, 0);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
                pivotTable.pivotTableStyleType = AsposeCells.PivotTableStyleType.PivotTableStyleMedium10;
                // grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
                // (zero-based positions in the order the items appear in the source data)
                const fruit = new DiscreteGroupItem("fruit", [0, 3]);
                const vegetable = new DiscreteGroupItem("vegetable", [1, 2]);
                const groupOptions = new PivotFieldGroupOptions();
                groupOptions.discreteGroupItems = [fruit, vegetable];
                pivotTable.rowFields.get(0).group(groupOptions);
                pivotTable.calculateData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputDiscreteGroupPivotFieldByIndex.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

## **注意**

{{% alert color="primary" %}}
- どのカスタムグループにも割り当てられていない項目が失われるわけではありません。それぞれの項目は、単独の項目エントリとして、カスタムグループと同じレベルにピボットテーブル内に残ります。上記の例では、`fruit` グループだけを定義すると、`carrot` と `potato` は、`fruit` グループの隣に行領域内で独立したエントリとして残ります。
- `PivotFieldGroupOptions.newPivotField` プロパティは、離散グループ化のレイアウトを制御します。デフォルト値は `true` で、グループ化されたフィールドを元のフィールドの隣に新しい外側フィールドとして追加し、上記の 2 階層のレイアウトを生成します（`rowFields` は 2 に増加します）。`false` に設定すると、元のフィールドが置き換えられ、行領域には、集計値を持つグループ名だけを含む単一階層が表示されます。`fruit` は 130（50 + 80）、`vegetable` は 130（60 + 70）です。
- `DiscreteGroupItem` の名前指定のコンストラクターとインデックス指定のコンストラクターは、同じ `discreteGroupItems` 配列内で併用できます。
{{% /alert %}}

## **関連記事**
- [ピボットテーブル内でピボットフィールドをグループ化](/cells/ja/javascript-cpp/group-pivot-fields-in-the-pivot-table/)
- [ピボットテーブルに行フィールドと列フィールドを追加](/cells/ja/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [ラベルまたは値によるピボットテーブルのフィルター](/cells/ja/javascript-cpp/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルにスタイルを適用](/cells/ja/javascript-cpp/apply-style-to-pivot-table/)
- [ピボットテーブルの更新](/cells/ja/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}