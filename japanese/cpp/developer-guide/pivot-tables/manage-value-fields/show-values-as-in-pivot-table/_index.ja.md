---
title: Aspose.Cells for C++ でピボットテーブルの値表示方法を使用
linktitle: Aspose.Cells for C++ でピボットテーブルの値表示方法を使用
description: Aspose.Cells for C++ を使用すると、ピボットテーブルのデータフィールド値を全体合計に対する割合、基準項目との差、累計、順位などの方法で表示できます。
keywords: Aspose.Cells, C++, ピボットテーブル, 値表示方法, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, ShowValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /ja/cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる利用シナリオ**
ピボットテーブルでは通常、`Sum` や `Count` などの集計関数を使用して各データフィールドを集計します。Excel の **「値表示方法」** 機能では、表示される各結果を、その集計値から導出した二次計算に置き換えます。例えば、全体合計に対する割合、累計、選択した基準項目との差、順位などを使用できるため、ヘルパー数式や計算列を使用せずに比較分析を実行できます。
典型的な用途には、全体合計に占める割合の分析（行・列・全体合計のいずれかを基準とする百分率を含む）、期間フィールドの累計を使用した累積レポート、基準項目との差または基準項目との差の割合を使用したベンチマーク項目に対する差異分析、および値の順位付け（最小値から最大値、または最大値から最小値）が含まれます。
Aspose.Cells for C++ では、`PivotShowValuesAsType` 列挙型を使用して二次計算を選択します。`PivotField.GetShowValuesSetting()` アクセサーは `PivotShowValuesSetting` オブジェクトを返します。その `SetShowValuesAs`、`SetBaseFieldIndex`、`SetBaseItemIndex` メソッドで動作を構成できます。より簡便な `PivotField.ShowValuesAs(...)` メソッドでは、同じ設定を 1 回の呼び出しで適用できます。これらの設定は、`PivotTable.GetDataFields()` から取得したデータフィールドまたは値フィールドに適用します。

## **PivotShowValuesAsType 列挙型のメンバー**
データフィールドは、`Sum` や `Count` などの集計関数を保持したまま、「値表示方法」によって集計値の表示方法のみが変わります。
`PivotShowValuesSetting` の値を直接設定する方法に加え（最後のセクションを参照）、1 回の呼び出しで同じ構成を適用できる簡便なメソッドがあります。このメソッドには、基準フィールドと基準項目をインデックスで指定する形式と、名前で指定する形式の 2 種類があります。

```cpp
void ShowValuesAs(PivotShowValuesAsType showValuesAsType, int32_t baseField, int32_t baseItem);
void ShowValuesAs(PivotShowValuesAsType showValuesAsType, const U16String& baseField, const U16String& baseItem);
// index form: PivotShowValuesAsType::PercentageOfTotal, 0, 0
// name form:  PivotShowValuesAsType::PercentageOf, u"Fruit", u"Apple"
```

| パラメーター | 意味 | 必須となる場合 |
| --- | --- | --- |
| `showValuesAsType` | 適用する `PivotShowValuesAsType` の二次計算。 | 常に必要です。 |
| `baseField` | ピボットテーブルで基準フィールドの候補となるフィールドの 0 始まりのインデックス（例: 基準項目が属する行フィールドのインデックス）。名前指定形式では、基準フィールド名を指定します。 | 次の 8 つの形式（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`、`RunningTotalIn`、`PercentageOfParentTotal`、`PercentageOfRunningTotalIn`、`RankSmallestToLargest`、`RankLargestToSmallest`）では必要です。それ以外の形式では `0`（名前指定形式では空の `U16String`）を指定します。 |
| `baseItem` | 基準項目の 0 始まりのインデックス。2 つの番兵値があり、`-1` は前の項目、`-2` は次の項目を選択します。C++ API には番兵値用の名前付き定数が定義されていないため、リテラル値を指定します。名前指定形式では基準項目のキャプションを指定し、選択した形式が基準項目を必要としない場合は空の `U16String` を指定します。 | 基準項目を評価する 3 つの形式（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`）でのみ基準項目を評価します。基準項目を無視する 5 つの形式（`RunningTotalIn`、`PercentageOfParentTotal`、`PercentageOfRunningTotalIn`、および 2 つのランク形式）では、`0` または空の `U16String` を指定します。 |

| 計算タイプ | 動作 | 基準項目のパラメーター |
| --- | --- | --- |
| `Normal` | 二次計算は行いません。集計値がそのまま表示されます（デフォルト）。 | — |
| `DifferenceFrom` | 基準フィールドの基準項目の値との差として表示します。 | `baseField` + `baseItem`（インデックスまたはキャプション、または前/次の番兵値） |
| `PercentageOf` | 基準フィールドの基準項目の値に対する割合として表示します。 | `baseField` + `baseItem`（インデックスまたはキャプション、または前/次の番兵値） |
| `PercentageDifferenceFrom` | 基準フィールドの基準項目の値との差の割合として表示します。 | `baseField` + `baseItem`（インデックスまたはキャプション、または前/次の番兵値） |
| `RunningTotalIn` | 基準フィールドの連続する項目について、累計として表示します。 | `baseField`（項目の順序が累積を左右するフィールド） |
| `PercentageOfRow` | 行合計に対する割合として表示します。 | — |
| `PercentageOfColumn` | 列合計に対する割合として表示します。 | — |
| `PercentageOfTotal` | 全体合計に対する割合として表示します。 | — |
| `Index` | Excel のインデックス数式 ((value * grand total) / (row total * column total)) に基づいて値を表示します。 | — |
| `PercentageOfParentRowTotal` | 親行合計に対する割合として表示します（入れ子になった行フィールド用）。 | — |
| `PercentageOfParentColumnTotal` | 親列合計に対する割合として表示します（入れ子になった列フィールド用）。 | — |
| `PercentageOfParentTotal` | 親合計に対する割合として表示します。 | `baseField`（合計の基準となる親フィールド） |
| `PercentageOfRunningTotalIn` | 基準フィールドの累計に対する割合として表示します。 | `baseField`（累積フィールド） |
| `RankSmallestToLargest` | 値の順位を最小値（1）から最大値の順に表示します。 | `baseField`（順位付けの対象範囲を項目が定義するフィールド） |
| `RankLargestToSmallest` | 値の順位を最大値（1）から最小値の順に表示します。 | `baseField`（順位付けの対象範囲を項目が定義するフィールド） |

{{% alert color="primary" %}}
`ShowValuesAs(...)` は `PivotShowValuesSetting` の各値（`ShowValuesAs`、`BaseFieldIndex`、`BaseItemIndex`）を設定します。このメソッドと設定オブジェクトは、同じ状態を設定する 2 つの方法であり、Excel の「値表示方法」ダイアログにある基準フィールドおよび基準項目の選択欄と対応しています。
{{% /alert %}}

## **全体合計に対する割合として値を表示する**
`PivotShowValuesAsType::PercentageOfTotal` を指定して `PivotField.ShowValuesAs` メソッドを呼び出すと、すべてのデータフィールドセル（全体合計を含む）を全体合計に占める割合として表示できます。したがって、表示される数値は結果全体に対する割合として示されます。この形式は各値を全体合計だけと比較するため、基準フィールドも基準項目も不要です。末尾の引数（`0`、`0`）は、この形式では無視されるプレースホルダーです。これは前述のパラメータ表のとおりです。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Load or create a workbook with source data
    Workbook workbook;
    Worksheet dataSheet = workbook.GetWorksheets().Get(0);
    Cells cells = dataSheet.GetCells();
    cells.Get(0, 0).PutValue(U16String("Fruit"));
    cells.Get(0, 1).PutValue(U16String("Amount"));
    const char* fruits[6] = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
    int32_t amounts[6] = { 10, 20, 30, 40, 50, 60 };
    for (int32_t i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(amounts[i]);
    }
    // Add a pivot table on a new worksheet
    int32_t pivotSheetIndex = workbook.GetWorksheets().Add();
    PivotTable pivotTable = workbook.GetWorksheets().Get(pivotSheetIndex).GetPivotTables().Add(u"=Sheet1!A1:B7", 2, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Show the Amount data field as a percentage of the grand total with the
    // one-call method; PercentageOfTotal takes no base item, so the trailing
    // base arguments (0, 0) are placeholders the format ignores
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    dataField.ShowValuesAs(PivotShowValuesAsType::PercentageOfTotal, 0, 0);
    pivotTable.CalculateData();
    // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
    workbook.Save(u"ShowValuesAsPercentageOfTotal.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **PivotField.ShowValuesSetting の取得と構成**
現在の構成は `PivotField.GetShowValuesSetting()` で取得できます。このアクセサーは、フィールドの `PivotShowValuesSetting` オブジェクトを返します。オブジェクトのゲッターメソッドから、使用中の「値表示方法」の計算内容を確認できます。構成を変更するには、`PivotField.ShowValuesAs` メソッドを呼び出します。このメソッドは、すべての設定を 1 回の呼び出しで書き込みます。そのため、各値を個別に設定する必要はありません。
`PivotShowValuesSetting` オブジェクトは、`ShowValuesAs` によって設定される次の状態を提供します。
- `GetShowValuesAs()` / `SetShowValuesAs()` は、使用する `PivotShowValuesAsType` の二次計算を選択します。
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` は、ピボットフィールド内の基準フィールドの 0 始まりのインデックスを指定します。この値は基準フィールドを必要とする形式で使用されます。
- `GetBaseItemIndex()` / `SetBaseItemIndex()` は、特定のピボット項目の 0 始まりのインデックス、または 2 つの番兵値（`-1` は前の項目、`-2` は次の項目）のいずれかを指定します。C++ API には番兵値用の名前付き定数が定義されていません。この値は基準項目を必要とする形式で使用されます。
- `GetBaseFieldName()` と `GetBaseItemCaption()` は、解決された基準フィールド名と基準項目キャプションを返す読み取り専用のアクセサです。例えば、前の項目を示す番兵値を選択すると、`GetBaseItemCaption()` は `(previous)` を返します。
`ShowValuesAs` の呼び出し後は、`PivotTable.CalculateData()` を再度呼び出してください。これにより、更新した構成でピボット本体が再計算され、再描画されます。

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"ShowValuesAsPercentageOfTotal.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(1).GetPivotTables().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    // Read the current show-values settings
    PivotShowValuesSetting settings = dataField.GetShowValuesSetting();
    std::cout << "ShowValuesAs: " << static_cast<int32_t>(settings.GetShowValuesAs()) << std::endl;
    std::cout << "BaseFieldIndex: " << settings.GetBaseFieldIndex() << std::endl;
    std::cout << "BaseItemIndex: " << settings.GetBaseItemIndex() << std::endl;
    std::cout << "BaseFieldName: " << settings.GetBaseFieldName().ToUtf8() << std::endl;
    std::cout << "BaseItemCaption: " << settings.GetBaseItemCaption().ToUtf8() << std::endl;
    // Switch to a base-item calculation with the one-call method: difference
    // from the value of the previous item in the row field
    // (-1 is the previous-item sentinel; no named constant exists in C++)
    dataField.ShowValuesAs(PivotShowValuesAsType::DifferenceFrom,
        pivotTable.GetRowFields().Get(0).GetBaseIndex(), -1);
    pivotTable.CalculateData();
    // Note: the percentage number format saved by the previous example still
    // clings to the data field cells; the underlying values are now differences
    // Re-read the applied configuration
    std::cout << "ShowValuesAs now: " << static_cast<int32_t>(dataField.GetShowValuesSetting().GetShowValuesAs()) << std::endl;
    std::cout << "BaseItemCaption now: " << dataField.GetShowValuesSetting().GetBaseItemCaption().ToUtf8() << std::endl;
    workbook.Save(u"ShowValuesAsDifferenceFrom.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **関連記事**
- [ピボットテーブルの値フィールドの管理](/cells/ja/cpp/manage-value-fields/)
- [ピボットテーブルの更新](/cells/ja/cpp/refresh-pivot-table/)
- [ピボットテーブルにスタイルを適用](/cells/ja/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}