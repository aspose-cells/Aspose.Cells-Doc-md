---
title: ピボットテーブルで「値の表示方法」
linktitle: ピボットテーブルで「値の表示方法」
description: Aspose.Cells for JavaScript via C++ を使用して、ピボットテーブルのデータフィールドの値を総計の割合、基準項目との差、累積合計、順位などとして表示します。
keywords: Aspose.Cells, JavaScript via C++, ピボットテーブル, 値の表示方法, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /ja/javascript-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **使用シナリオ**
ピボットテーブルは通常、`Sum` や `Count` といった集計関数で各データフィールドを集計します。Excel の **Show Values As** 機能は、その集計結果に対して二次計算を行い、たとえば総計のパーセンテージや累積合計、基準項目との差、順位などに置き換えて表示します。これにより、ヘルパー数式や計算列を使用せずに比較分析が可能になります。  
典型的な利用例としては、行・列・総計に対するシェア分析、期間フィールドでの累積レポート、基準項目に対する差分またはパーセンテージ差分によるベンチマーク分析、最小から最大または最大から最小への順位付けなどがあります。  
Aspose.Cells for JavaScript via C++ では、`PivotShowValuesAsType` 列挙体で二次計算を選択します。読み取り専用の `PivotField.showValuesSetting` プロパティは `PivotShowValuesSetting` オブジェクトを返し、書き込み可能な `showValuesAs`、`baseFieldIndex`、`baseItemIndex` プロパティで動作を構成できます。便利メソッド `PivotField.showValuesAs(...)` を使用すると、同じ設定を一度の呼び出しで適用できます。これらの設定は `PivotTable.dataFields` から取得したデータまたは値フィールドに適用します。

## **PivotShowValuesAsType 列挙体メンバー**
データフィールドは集計関数（Sum や Count など）を保持したまま、Show Values As によって集計値の表示方法だけが変換されます。  
`PivotShowValuesSetting` プロパティを直接設定する方法（最終セクション参照）に加えて、同等の設定を一度の呼び出しで適用できる便利メソッドがあります。2 つの形式が用意されており、1 つはインデックスで基礎フィールドと基礎項目を指定し、もう 1 つは名前で指定します。

```html
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PercentageOf, "Fruit", "Apple"
```

| パラメーター | 意味 | 必要な場合 |
| --- | --- | --- |
| `showValuesAsType` | 適用する `PivotShowValuesAsType` の二次計算。 | 常に必須。 |
| `baseField` | ピボットテーブルの基礎フィールドのゼロベースインデックス（例: 基礎項目が属する行フィールドのインデックス）、または名前形式の場合は基礎フィールドの名前。 | 下記 8 つの基礎相対フォーマット（`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`）で使用。それ以外のフォーマットは `0`（名前形式では `null`）を指定。 |
| `baseItem` | 基礎項目のゼロベースインデックス。2 つのセンテネルがあり、-1 は前の項目、-2 は次の項目を示す（JavaScript via C++ バインディングは名前定数をエクスポートしないのでリテラル値を渡す）。名前形式では基礎項目のキャプションを指定し、フォーマットが基礎項目を必要としない場合は `null` を使用。 | `DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom` の 3 つの基礎項目フォーマットで評価され、それ以外の 5 つのフィールド相対フォーマット（`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, 両方の順位）では無視されるため `0` または `null` を指定。 |

| 計算タイプ | 動作 | 基礎項目パラメーター |
| --- | --- | --- |
| `Normal` | 二次計算は行われず、集計値がそのまま表示されます（デフォルト）。 | — |
| `DifferenceFrom` | 基礎フィールドの基礎項目の値との差として表示します。 | `baseField` + `baseItem`（インデックス、キャプション、または前後センテネル） |
| `PercentageOf` | 基礎フィールドの基礎項目の値に対するパーセンテージとして表示します。 | `baseField` + `baseItem`（インデックス、キャプション、または前後センテネル） |
| `PercentageDifferenceFrom` | 基礎フィールドの基礎項目の値に対するパーセンテージ差として表示します。 | `baseField` + `baseItem`（インデックス、キャプション、または前後センテネル） |
| `RunningTotalIn` | 基礎フィールドの項目順に従って累積合計として表示します。 | `baseField`（蓄積を司るフィールド） |
| `PercentageOfRow` | 行合計に対するパーセンテージとして表示します。 | — |
| `PercentageOfColumn` | 列合計に対するパーセンテージとして表示します。 | — |
| `PercentageOfTotal` | 総計に対するパーセンテージとして表示します。 | — |
| `Index` | Excel のインデックス数式 ((value * grand total) / (row total * column total)) を使用して表示します。 | — |
| `PercentageOfParentRowTotal` | ネストされた行フィールドの場合、親行合計に対するパーセンテージとして表示します。 | — |
| `PercentageOfParentColumnTotal` | ネストされた列フィールドの場合、親列合計に対するパーセンテージとして表示します。 | — |
| `PercentageOfParentTotal` | 親合計に対するパーセンテージとして表示します。 | `baseField`（参照対象となる親フィールド） |
| `PercentageOfRunningTotalIn` | 基礎フィールドの累積合計に対するパーセンテージとして表示します。 | `baseField`（蓄積フィールド） |
| `RankSmallestToLargest` | 最小 (1) から最大へ順位付けします。 | `baseField`（順位付けの範囲を決めるフィールド） |
| `RankLargestToSmallest` | 最大 (1) から最小へ順位付けします。 | `baseField`（順位付けの範囲を決めるフィールド） |

{{% alert color="primary" %}}
`showValuesAs(...)` は `PivotShowValuesSetting` のプロパティ（`showValuesAs`、`baseFieldIndex`、`baseItemIndex`）を書き込みます。メソッドとプロパティオブジェクトは同じ状態を設定する 2 つの方法であり、Excel の「値の表示方法」ダイアログの基礎フィールドおよび基礎項目ピッカーと同様です。
{{% /alert %}}

## **合計の割合として値を表示**
`PivotField.showValuesAs` メソッドに `PivotShowValuesAsType.PercentageOfTotal` を指定して呼び出すと、すべてのデータフィールドセル（総計を含む）が総計に対する割合に変換されます。表示される数値は全体の結果セットに対する比率として解釈されます。この形式は総計のみを基準に測定するため、基礎フィールドや基礎項目は不要です。パラメーター表に記載されているように、末尾の引数 (`0`, `0`) はフォーマットが無視するプレースホルダーです。

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat } = AsposeCells;
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {

                // Load or create a workbook with source data
                const workbook = new Workbook();
                const dataSheet = workbook.worksheets.get(0);
                const cells = dataSheet.cells;
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Amount";
                const fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"];
                const amounts = [10, 20, 30, 40, 50, 60];
                for (let i = 0; i < fruits.length; i++) {
                    cells.get(i + 1, 0).value = fruits[i];
                    cells.get(i + 1, 1).value = amounts[i];
                }
                // Add a pivot table on a new worksheet
                const pivotSheetIndex = workbook.worksheets.add();
                const pivotSheet = workbook.worksheets.get(pivotSheetIndex);
                const pivotTable = pivotSheet.pivotTables.add("=Sheet1!A1:B7", 2, 2);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.calculateData();
                // Show the Amount data field as a percentage of the grand total with the
                // one-call method; PercentageOfTotal takes no base item, so the trailing
                // base arguments (0, 0) are placeholders the format ignores
                const dataField = pivotTable.dataFields.get(0);
                dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0);
                pivotTable.calculateData();
                // Body now reads (underlying values are fractions, shown with the
                // percentage format): Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "ShowValuesAsPercentageOfTotal.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## **PivotField.showValuesSetting の取得と構成**
`PivotField.showValuesSetting` を使用して現在の構成を読み取ります。この読み取り専用プロパティはフィールドの `PivotShowValuesSetting` オブジェクトを返し、アクティブな「値の表示方法」計算を記述するプロパティを保持しています。構成を変更するには `PivotField.showValuesAs` メソッドを呼び出します。これによりすべての設定が一度に書き込まれ、個別にプロパティを割り当てる必要がなくなります。  
`PivotShowValuesSetting` オブジェクトが公開する状態は次のとおりです。  
- `showValuesAs` は適用する `PivotShowValuesAsType` の二次計算を選択します。  
- `baseFieldIndex` はピボットフィールド内の基礎フィールドのゼロベースインデックスを指定し、基礎相対フォーマットで使用されます。  
- `baseItemIndex` は基礎項目を指定します。具体的には特定のピボット項目のゼロベースインデックス、または 2 つのセンテネル値（前の項目は -1、次の項目は -2）で、基礎項目フォーマットで使用されます。  
- `baseFieldName` と `baseItemCaption` は読み取り専用ビューで、解決された基礎フィールド名と基礎項目キャプションを返します。たとえば前項目センテネルを選択した場合、`baseItemCaption` は `(previous)` を返します。  
`showValuesAs` を呼び出した後、`PivotTable.calculateData()` を再度実行してピボット本体を再計算し、更新された構成で再描画します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const ready = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                await ready;
                const file = document.getElementById('fileInput').files[0];
                if (!file) {
                    throw new Error("Please select ShowValuesAsPercentageOfTotal.xlsx.");
                }
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(1);
                const pivotTable = worksheet.pivotTables.get(0);
                const dataField = pivotTable.dataFields.get(0);
                // Read the current show-values settings
                const settings = dataField.showValuesSetting;
                const messages = [
                    `ShowValuesAs: ${settings.showValuesAs}`,
                    `BaseFieldIndex: ${settings.baseFieldIndex}`,
                    `BaseItemIndex: ${settings.baseItemIndex}`,
                    `BaseFieldName: ${settings.baseFieldName}`,
                    `BaseItemCaption: ${settings.baseItemCaption}`
                ];
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                // Switch to a base-item calculation with the one-call method: difference
                // from the value of the previous item in the row field
                // (-1 is the previous-item sentinel; the binding does not export the constant)
                dataField.showValuesAs(
                    AsposeCells.PivotShowValuesAsType.DifferenceFrom,
                    pivotTable.rowFields.get(0).baseIndex,
                    -1
                );
                pivotTable.calculateData();
                // Note: the percentage number format saved by the previous example still
                // clings to the data field cells; the underlying values are now differences
                // Re-read the applied configuration
                messages.push(`ShowValuesAs now: ${dataField.showValuesSetting.showValuesAs}`);
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "ShowValuesAsDifferenceFrom.xlsx";
                downloadLink.style.display = "block";
            } catch (error) {
                document.getElementById('result').innerHTML =
                    `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

## **関連項目**
- [ピボットテーブルでの値フィールドの管理](/cells/ja/javascript-cpp/manage-value-fields/)
- [ピボットテーブルの更新](/cells/ja/javascript-cpp/refresh-pivot-table/)
- [ピボットテーブルへのスタイル適用](/cells/ja/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}