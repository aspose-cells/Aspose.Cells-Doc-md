---
title: ピボットテーブルでの値の表示方法
linktitle: ピボットテーブルでの値の表示方法
description: Aspose.Cells for JavaScript via C++ を使用して、ピボットテーブルのデータ フィールドの値を合計に対する割合、ベース項目との差、累積合計、順位などとして表示します。
keywords: Aspose.Cells, JavaScript via C++, ピボットテーブル, 値の表示, データ表示形式, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /ja/javascript-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **使用シナリオ**
ピボットテーブルは通常、`Sum` や `Count` などの集計関数で各データ フィールドを集計します。Excel の **Show Values As** 機能は、集計結果を二次計算で置き換え、たとえば全体合計に対する割合、累積合計、選択したベース項目との差、順位などを表示できるようにします。これにより、補助的な数式や計算列を使用せずに比較分析が可能になります。  
一般的な利用例としては、行・列・全体合計に対する割合によるシェア分析、期間フィールドでの累積レポート、ベンチマーク項目に対する差分またはパーセンテージ差分によるばらつき分析、最小から最大（またはその逆）への順位付けなどがあります。  
Aspose.Cells for JavaScript via C++ では、`PivotFieldDataDisplayFormat` が二次計算を選択します。読み取り専用プロパティ `PivotField.showValuesSetting` は `PivotShowValuesSetting` オブジェクトを返し、書き込み可能な `calculationType`、`baseFieldIndex`、`baseItemPositionType`、`baseItemIndex` プロパティで動作を設定できます。便利メソッド `PivotField.showValuesAs(...)` は、これら 4 つの設定を 1 回の呼び出しで適用します。設定は `PivotTable.dataFields` から取得したデータまたは値フィールドに対して適用します。

## **PivotFieldDataDisplayFormat 列挙体のメンバー**
データ フィールドは集計関数（Sum や Count など）を保持したまま、Show Values As は集計値の表示方法だけを変換します。  
`PivotShowValuesSetting` プロパティを直接設定する方法（最終セクション参照）に加えて、1 回の呼び出しで同じ構成を適用する便利メソッドがあります。

```html
dataField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
```

| パラメータ | 意味 | 必要な場合 |
| --- | --- | --- |
| `displayFormat` | 適用する `PivotFieldDataDisplayFormat` 二次計算。 | 常に必須。 |
| `baseField` | ピボットテーブルのベースフィールドのゼロベースインデックス（例: ベース項目が属する行フィールドのインデックス）。 | 以下の 6 つの基準関連フォーマット（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`、`RunningTotalIn`、`PercentageOfRunningTotalIn`、`PercentageOfParentTotal`）のみで使用され、その他のフォーマットでは無視されます。 |
| `baseItemPositionType` | 現在の項目に対するベース項目の選択方法：`PivotItemPositionType.Previous`、`.Next`、または `.Custom`。 | 3 つの基準項目フォーマット（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`）のみで使用され、その他のフォーマットでは無視されます。 |
| `baseItem` | ベース項目のゼロベースインデックス。 | `baseItemPositionType` が `Custom` の場合にのみ使用（正確なベース項目を指定）。`Previous` / `Next` およびベース項目を使用しない形式では `0` を指定してください。 |

| 計算タイプ | 動作 | ベース項目パラメータ |
| --- | --- | --- |
| `Normal` | 二次計算は行われず、集計された値がそのまま表示されます（既定）。 | — |
| `DifferenceFrom` | ベースフィールド内のベース項目の値との差として表示します。 | `baseField` + `Previous`/`Next`/`Custom`（`Custom` の場合は `baseItem`） |
| `PercentageOf` | ベースフィールド内のベース項目の値に対するパーセンテージとして表示します。 | `baseField` + `Previous`/`Next`/`Custom`（`Custom` の場合は `baseItem`） |
| `PercentageDifferenceFrom` | ベースフィールド内のベース項目の値からのパーセンテージ差として表示します。 | `baseField` + `Previous`/`Next`/`Custom`（`Custom` の場合は `baseItem`） |
| `RunningTotalIn` | ベースフィールドの項目順に従って累積合計として表示します。 | `baseField`（累積を駆動するフィールド） |
| `PercentageOfRow` | 行合計に対するパーセンテージとして表示します。 | — |
| `PercentageOfColumn` | 列合計に対するパーセンテージとして表示します。 | — |
| `PercentageOfTotal` | 全体合計に対するパーセンテージとして表示します。 | — |
| `Index` | Excel のインデックス数式 ((value * grand total) / (row total * column total)) を使用して表示します。 | — |
| `PercentageOfParentRowTotal` | ネストされた行フィールドの場合、親行合計に対するパーセンテージとして表示します。 | — |
| `PercentageOfParentColumnTotal` | ネストされた列フィールドの場合、親列合計に対するパーセンテージとして表示します。 | — |
| `PercentageOfParentTotal` | 親合計に対するパーセンテージとして表示します。 | `baseField`（基準となる親フィールド） |
| `PercentageOfRunningTotalIn` | ベースフィールド内の累積合計に対するパーセンテージとして表示します。 | `baseField`（累積フィールド） |
| `RankSmallestToLargest` | 最小（1）から最大へ順位付けします。 | — |
| `RankLargestToSmallest` | 最大（1）から最小へ順位付けします。 | — |

{{% alert color="primary" %}}
`showValuesAs(...)` は `PivotShowValuesSetting` の 4 つのプロパティ（`calculationType`、`baseFieldIndex`、`baseItemPositionType`、`baseItemIndex`）を設定します。メソッドとプロパティ オブジェクトは同じ状態を構成する 2 つの手段であり、Excel の Show Values As ダイアログにあるベースフィールドおよびベース項目選択と同等です。
{{% /alert %}}

## **合計に対するパーセンテージとしての表示**
`PivotField.showValuesAs` メソッドに `PivotFieldDataDisplayFormat.PercentageOfTotal` を指定して呼び出すと、すべてのデータ フィールド セル（全体合計を含む）が全体合計に対するシェアに変換されます。その結果、表示される数値は全体結果セットの比率として解釈されます。この形式は全体合計に対してのみ測定するため、ベースフィールドやベース項目は不要です。末尾の引数（`0`、`PivotItemPositionType.Previous`、`0`）はフォーマットが無視するプレースホルダーであることは、上記のパラメータ表でも説明しています。

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
                // base arguments (0, Previous, 0) are placeholders the format ignores
                const dataField = pivotTable.dataFields.get(0);
                dataField.showValuesAs(
                    AsposeCells.PivotFieldDataDisplayFormat.PercentageOfTotal,
                    0,
                    AsposeCells.PivotItemPositionType.Previous,
                    0
                );
                pivotTable.calculateData();
                // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
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
`PivotField.showValuesSetting`（読み取り専用）を使用して現在の構成を取得します。このプロパティはフィールドの `PivotShowValuesSetting` オブジェクトを返し、4 つのプロパティがアクティブな「値の表示」計算を表します。構成を変更するには `PivotField.showValuesAs` メソッドを呼び出します。これにより 4 つの設定が一度に書き込まれるため、個別にプロパティを代入する必要はありません。  
`PivotShowValuesSetting` オブジェクトが公開する 4 つのプロパティは次のとおりです。
- `calculationType`：二次計算として使用する `PivotFieldDataDisplayFormat` を選択します。
- `baseFieldIndex`：ピボット フィールド内のベースフィールドのゼロベースインデックスを指定します。基準関連フォーマットで使用されます。
- `baseItemPositionType`：ベース項目の位置決め方法を決定し、`PivotItemPositionType.Next`、`PivotItemPositionType.Previous`、または `PivotItemPositionType.Custom` を受け入れます。
- `baseItemIndex`：ゼロベースのベース項目インデックスを指定し、`baseItemPositionType` が `Custom` の場合に使用されます。  
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
                    `CalculationType: ${settings.calculationType}`,
                    `BaseFieldIndex: ${settings.baseFieldIndex}`,
                    `BaseItemPositionType: ${settings.baseItemPositionType}`,
                    `BaseItemIndex: ${settings.baseItemIndex}`
                ];
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                // Switch to a base-item calculation with the one-call method: difference
                // from the value of the previous item in the row field
                dataField.showValuesAs(
                    AsposeCells.PivotFieldDataDisplayFormat.DifferenceFrom,
                    pivotTable.rowFields.get(0).baseIndex,
                    AsposeCells.PivotItemPositionType.Previous,
                    0
                );
                pivotTable.calculateData();
                // Note: the percentage number format saved by the previous example still
                // clings to the data field cells; the underlying values are now differences
                // Re-read the applied configuration
                messages.push(`CalculationType now: ${dataField.showValuesSetting.calculationType}`);
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

## **関連記事**
- [ピボットテーブルの値フィールドの管理](/cells/ja/javascript-cpp/manage-value-fields/)
- [ピボットテーブルの更新](/cells/ja/javascript-cpp/refresh-pivot-table/)
- [ピボットテーブルへのスタイルの適用](/cells/ja/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}