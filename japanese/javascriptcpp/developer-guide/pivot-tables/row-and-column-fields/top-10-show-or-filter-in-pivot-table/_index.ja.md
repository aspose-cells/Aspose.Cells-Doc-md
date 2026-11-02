---
title: ピボットテーブルで上位10件を表示またはフィルター
linktitle: ピボットテーブルで上位10件を表示またはフィルター
description: Aspose.Cells for JavaScript via C++ で、ピボットフィールドで上位または下位と判定された項目だけを表示する方法を学びます。この Pooleでは、Excel 97-2003 の AutoShow プロパティ（isAutoShow など）、オプションの読み戻し、および filterTop10 による Excel 2007-365 の上位10件フィルターについて説明します。
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, ピボットテーブル, 上位10件, 自動表示, isAutoShow, isAscendShow, autoShowCount, autoShowField, filterTop10, PivotFilterType, PivotField, JavaScript
type: docs
weight: 20
url: /ja/javascript-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **使用例**
行フィールドのすべての項目を一覧表示するピボットテーブルは、そのフィールドに数十のメンバーがある場合に読みにくくなることがあります。上位10件のレポートは、順位が最も高い項目または最も低い項目だけを保持するため、ランキングレポート（「売上順の上位5商品」や「販売件数順の下位3地域」など）の要件にまさに応えます。Aspose.Cells はこのための2つのメカニズムをサポートしており、それぞれ Microsoft Excel の2つの世代に対応します。
- **Excel 97-2003 の AutoShow** — `PivotField` の4つのプロパティ `isAutoShow`、`isAscendShow`、`autoShowCount` および `autoShowField` です。これは、ピボットフィールドに直接保存される従来の「上位/下位 N 件の表示」設定です。元のピボットテーブル形式の一部であるため、新旧すべての Excel バージョンで動作します。
- **Excel 2007-365 の上位10件フィルター** — `PivotField.filterTop10()` メソッドです。これは、フィールドメニューの「値フィルター」で利用できる新しい上位10件の値フィルターです。フィールドに添付される `PivotFilter` オブジェクトとして保存され、項目数と割合に基づくランキングを提供します。

## **Excel 97-2003 での上位10件の表示（AutoShow）**
従来の AutoShow は、`PivotField` の4つのプロパティに値を代入して設定します。
- `isAutoShow` — フィールドの AutoShow 設定を有効または無効にします。
- `isAscendShow` — `false` の場合は順位が最も高い項目（上位）を保持し、`true` の場合は順位が最も低い項目（下位）を保持します。
- `autoShowCount` — 保持する項目数を指定します。例として、従来の上位10件レポートでは 10 などを指定します。
- `autoShowField` — 項目をランク付けする基準となる値を持つ**データフィールド**のゼロベースインデックスです。フィールド自体を基準に項目をランク付けする場合は -1 を指定します。
値フィールドまたはフィールド自体を基準に項目をランク付けできます。以下に、代表的な2つの例を示します。

### **値フィールドによるランク付け**
行フィールドの項目を、"Sum of Sales" のような通常の値フィールドでランク付けします。次の例では、1つの行フィールド（`Sport`）と1つのデータフィールド（`Sales`）を持つピボットテーブルを作成し、その後、売上上位2つのスポーツを表示します。`rankBy` は 0 です。これは、"Sum of Sales" がインデックス 0 のデータフィールドだからです。

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            for (const sport of sports) {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            }
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C16", "F3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // 「Sum of Sales」（データフィールドのインデックス 0）に基づいて上位 2 項目を表示する
            sportField.isAutoShow = true;
            sportField.isAscendShow = false;
            sportField.autoShowCount = 2;
            sportField.autoShowField = 0;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-by-value-field.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **フィールド自体によるランク付け**
フィールドは、それ自体を基準としてランク付けすることもできます。その場合は `autoShowField` に -1 を指定します。この方法では追加のデータフィールドは不要です。フィールドを行（または列）領域に配置するだけです。以下の例では、フィールド自体を基準にランク付けした下位3つのスポーツを表示します。この設定を保存すると、-1 がこの形式のデフォルト値であるため、ピボットテーブルの XML から `rankBy` 属性が省略されます。さらに、`autoShowField` を読み戻すと -1 になります。

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            for (const sport of sports) {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            }
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C16", "F3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // フィールド自体を基準に順位付けされた下位3項目を表示する (rankBy = -1)
            sportField.isAutoShow = true;
            sportField.isAscendShow = true;
            sportField.autoShowCount = 3;
            sportField.autoShowField = -1;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-by-field-itself.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **現在の AutoShow オプションの読み取り**
`PivotField` の `isAutoShow`、`isAscendShow`、`autoShowCount` および `autoShowField` プロパティで、フィールドに現在保存されている AutoShow オプションを確認できます。これらを使用すると、既存のワークブック、または直前に設定したピボットテーブルで項目がどのように表示されるかを調査できます。ファイルから読み込んだワークブックも対象です。

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const pivotTable = worksheet.pivotTables.get(0);
                const sportField = pivotTable.rowFields.get(0);
                const autoShowEnabled = sportField.isAutoShow;
                const direction = sportField.isAscendShow ? "Bottom" : "Top";
                const itemCount = sportField.autoShowCount;
                const rankingDataFieldIndex = sportField.autoShowField;
                result.innerHTML =
                    '<p>AutoShow enabled: ' + autoShowEnabled + '</p>' +
                    '<p>Direction: ' + direction + '</p>' +
                    '<p>Item count: ' + itemCount + '</p>' +
                    '<p>Ranking data field index: ' + rankingDataFieldIndex + '</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

4つのプロパティは、ピボットテーブルの XML に書き込まれる従来の AutoShow 属性（`autoShow`、`topAutoShow`、`itemPageCount`、`rankBy`）に対応しています。そのため、読み戻される値は、すべての Excel バージョンが適用する値になります。

## **注意**

{{% alert color="primary" %}}
- AutoShow プロパティを変更したら、`pivotTable.calculateData()` をもう一度呼び出してください。設定は、次回の再計算時にレンダリングされるレイアウトでのみ有効になります。
- AutoShow 設定は行フィールドと列フィールドで機能します。ページ（フィルター）領域にのみ配置されているフィールドは、項目がピボットテーブルの本体に配置されないため、この方法ではランク付けできません。
{{% /alert %}}

## **Excel 2007-365：上位10件フィルター（filterTop10）**
新しい Excel バージョンでは、フィールドメニューの「値フィルター」→「上位10件...」から上位10件を値フィルターとして利用できます。Aspose.Cells はこの機能に `PivotField.filterTop10(number valueFieldIndex, PivotFilterType type, boolean isTop, number itemCount)` メソッドで対応し、作成された `PivotFilter` を返します。
- `valueFieldIndex` — 集計値に基づいて項目をランク付けするデータフィールドのゼロベースインデックスです。
- `type` — `itemCount` の意味を指定します。`PivotFilterType.Count` は固定数の項目を保持します（ダイアログの「項目数」オプション）。`PivotFilterType.Percent` は項目の割合を保持するため、`itemCount` はその割合そのものになります。30 を指定すると上位30%を保持します。`PivotFilterType.Sum` は累積値のカバレッジに基づいて項目をランク付けします。
- `isTop` — 上位の場合は `true`、下位の場合は `false` です。
- `itemCount` — 上位 N 件の N を指定します。単位は `type` によって異なります。

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            sports.forEach(sport => {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
        });
    </script>
</html>
```

{{% alert color="primary" %}}
AutoShow プロパティと `filterTop10` は別々の機能です。AutoShow はピボットフィールドに従来の `autoShow` 属性を書き込み、Excel 97 以降のすべての Excel バージョンで適用されます。`filterTop10` は新しい `PivotFilter` エントリを書き込み、Excel 2007 以降が必要です。古い Excel バージョンでワークブックを開くと、新しいフィルターを使用するピボットテーブルは、すべての項目を表示するようにフォールバックします。旧バージョンのツールとの往復処理が必要なドキュメントでは AutoShow プロパティを、新しいワークブックでは他の値フィルターと組み合わせられる `filterTop10` を使用してください。
{{% /alert %}}

## **関連記事**
- [ピボットテーブルでピボットフィールドをグループ化](/cells/ja/javascript-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}