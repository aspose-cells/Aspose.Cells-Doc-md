---
title: ピボットテーブルでの「値の表示」方法
linktitle: ピボットテーブルでの「値の表示」方法
description: Aspose.Cells for Go via C++ を使用して、ピボットテーブルのデータ フィールドの値を合計に対するパーセンテージ、ベース項目との差、累積合計、ランキングなどとして表示します。
keywords: Aspose.Cells for Go via C++, ピボットテーブル, 値の表示形式, データ表示形式, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, C++
type: docs
weight: 145
url: /ja/go-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **利用シナリオ**
ピボットテーブルは通常、`Sum` や `Count` といった集計関数で各データ フィールドを集計します。Excel の **Show Values As** 機能は、集計結果を二次計算で置き換え、たとえば合計に対するパーセンテージ、累積合計、ベース項目との差、ランクなどを表示できるようにします。これにより、ヘルパー式や計算列を使用せずに比較分析が可能になります。  
一般的な使用例としては、行・列・合計のパーセンテージによる全体シェア分析、期間フィールドでの累積レポート、ベース項目との差またはパーセンテージ差によるベンチマーク分析、最小から最大または最大から最小へのランキングなどがあります。  
Aspose.Cells for Go via C++ では、`PivotFieldDataDisplayFormat` が二次計算を選択します。`PivotField.GetShowValuesSetting()` アクセサは `PivotShowValuesSetting` オブジェクトを返し、`SetCalculationType`、`SetBaseFieldIndex`、`SetBaseItemPositionType`、`SetBaseItemIndex` の各メソッドで動作を構成します。便利メソッド `PivotField.ShowValuesAs(...)` は、同じ 4 つの設定を 1 回の呼び出しで適用します。これらの設定は、`PivotTable.GetDataFields()` で取得したデータ フィールドまたは値フィールドに適用します。

## **PivotFieldDataDisplayFormat 列挙体メンバー**
データ フィールドは集計関数（Sum や Count など）を保持しますが、Show Values As は集計値の表示方法のみを変換します。  
`PivotShowValuesSetting` の値を直接記述する方法（最終セクション参照）に加えて、1 回の呼び出しで同じ構成を適用できる便利メソッドがあります。

```go
func (pivotField *PivotField) ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(displayFormat PivotFieldDataDisplayFormat, baseField int32, baseItemPositionType PivotItemPositionType, baseItem int32)
```

| パラメーター | 意味 | 必要な場合 |
| --- | --- | --- |
| `displayFormat` | 適用する `PivotFieldDataDisplayFormat` の二次計算。 | 常に。 |
| `baseField` | ピボットテーブルのベースフィールドのゼロベースインデックス（例: ベース項目が属する行フィールドのインデックス）。 | 以下の 6 つの基準関連フォーマット（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`、`RunningTotalIn`、`PercentageOfRunningTotalIn`、`PercentageOfParentTotal`）のみで使用され、その他のフォーマットでは無視されます。 |
| `baseItemPositionType` | 現在の項目に対してベース項目を選択する方法：`PivotItemPositionType.Previous`、`.Next`、または `.Custom`。 | 3 つの基準項目フォーマット（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`）のみで使用され、その他のフォーマットでは無視されます。 |
| `baseItem` | ベース項目のゼロベースインデックス。 | `baseItemPositionType` が `Custom` の場合にのみ使用（正確なベース項目を指定）。`Previous` / `Next` およびベース項目形式でない場合は `0` を渡してください。 |

| 計算タイプ | 動作 | ベース項目パラメーター |
| --- | --- | --- |
| `Normal` | 二次計算なし; 集計値がそのまま表示される（デフォルト）。 | — |
| `DifferenceFrom` | ベースフィールドのベース項目の値との差として表示。 | `baseField` + `Previous`/`Next`/`Custom`（`Custom` のみ `baseItem`） |
| `PercentageOf` | ベースフィールドのベース項目の値に対するパーセンテージとして表示。 | `baseField` + `Previous`/`Next`/`Custom`（`Custom` のみ `baseItem`） |
| `PercentageDifferenceFrom` | ベースフィールドのベース項目の値に対するパーセンテージ差として表示。 | `baseField` + `Previous`/`Next`/`Custom`（`Custom` のみ `baseItem`） |
| `RunningTotalIn` | ベースフィールドの連続項目に対して累積合計として表示。 | `baseField`（累積を駆動するフィールド） |
| `PercentageOfRow` | 行合計に対するパーセンテージとして表示。 | — |
| `PercentageOfColumn` | 列合計に対するパーセンテージとして表示。 | — |
| `PercentageOfTotal` | 合計に対するパーセンテージとして表示。 | — |
| `Index` | Excel の INDEX 形式（(value * grand total) / (row total * column total)）で表示。 | — |
| `PercentageOfParentRowTotal` | ネストした行フィールドの場合、親行合計に対するパーセンテージとして表示。 | — |
| `PercentageOfParentColumnTotal` | ネストした列フィールドの場合、親列合計に対するパーセンテージとして表示。 | — |
| `PercentageOfParentTotal` | 親合計に対するパーセンテージとして表示。 | `baseField`（基準となる親フィールド） |
| `PercentageOfRunningTotalIn` | ベースフィールドの累積合計に対するパーセンテージとして表示。 | `baseField`（累積フィールド） |
| `RankSmallestToLargest` | 最小 (1) から最大へランク付け。 | — |
| `RankLargestToSmallest` | 最大 (1) から最小へランク付け。 | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` は、4 つの `PivotShowValuesSetting` 値（`CalculationType`、`BaseFieldIndex`、`BaseItemPositionType`、`BaseItemIndex`）を設定します。メソッドと設定オブジェクトは同一の状態を構成する 2 つの手段であり、Excel の Show Values As ダイアログにあるベースフィールドおよびベース項目ピッカーを反映しています。
{{% /alert %}}

## **合計に対するパーセンテージとして値を表示**
`PivotField.ShowValuesAs` メソッドに `PivotFieldDataDisplayFormat.PercentageOfTotal` を指定して呼び出すと、すべてのデータ フィールド セル（合計も含む）が合計に対するシェアとして変換されます。表示される数値は全体結果セットの割合として解釈されます。この形式は合計に対してのみ測定するため、ベースフィールドやベース項目は不要です。フォーマットが無視する末尾の引数（`0`、`PivotItemPositionType.Previous`、`0`）はプレースホルダーです。

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load or create a workbook with source data
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	dataSheet, _ := worksheets.Get_Int(0)
	cells, _ := dataSheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Fruit")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Amount")
	fruits := []string{"Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"}
	amounts := []int{10, 20, 30, 40, 50, 60}
	for i := range fruits {
		fruitCell, _ := cells.Get_Int_Int(int32(i+1), int32(0))
		fruitCell.PutValue_String(fruits[i])
		amountCell, _ := cells.Get_Int_Int(int32(i+1), int32(1))
		amountCell.PutValue_Int(int32(amounts[i]))
	}
	// Add a pivot table on a new worksheet
	pivotSheetIndex, _ := worksheets.Add()
	pivotSheet, _ := worksheets.Get_Int(pivotSheetIndex)
	pivotTables, _ := pivotSheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=Sheet1!A1:B7", 2, 2)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Show the Amount data field as a percentage of the grand total with the
	// one-call method; PercentageOfTotal takes no base item, so the trailing
	// base arguments (0, Previous, 0) are placeholders the format ignores
	dataFields, _ := pivotTable.GetDataFields()
	dataField, _ := dataFields.Get_Int(0)
	dataField.ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(
		PivotFieldDataDisplayFormat_PercentageOfTotal,
		int32(0),
		PivotItemPositionType_Previous,
		int32(0),
	)
	pivotTable.CalculateData()
	// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
	workbook.Save_String("ShowValuesAsPercentageOfTotal.xlsx")
}
```

## **PivotField.ShowValuesSetting の取得と構成**
`PivotField.GetShowValuesSetting()` で現在の構成を取得できます。このアクセサはフィールドの `PivotShowValuesSetting` オブジェクトを返し、4 つの取得メソッドで有効な Show Values As 計算を示します。構成を変更するには `PivotField.ShowValuesAs` メソッドを呼び出します。これにより 4 つの設定が一度に書き込まれるため、個別に設定する手間が省けます。  
`PivotShowValuesSetting` オブジェクトが公開する 4 つの値は次のとおりです。  
- `GetCalculationType()` / `SetCalculationType()` が `PivotFieldDataDisplayFormat` の二次計算を選択します。  
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` がベースフィールドのゼロベースインデックスを指定し、基準関連フォーマットで使用されます。  
- `GetBaseItemPositionType()` / `SetBaseItemPositionType()` がベース項目の位置取り方法を決定し、`PivotItemPositionType.Next`、`PivotItemPositionType.Previous`、`PivotItemPositionType.Custom` を受け取ります。  
- `GetBaseItemIndex()` / `SetBaseItemIndex()` がゼロベースのベース項目インデックスを指定し、位置取りタイプが `Custom` の場合に使用されます。  
`ShowValuesAs` を呼び出した後は、`PivotTable.CalculateData()` を再度実行してピボット本体を再計算し、更新された構成で再描画します。

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook_String("ShowValuesAsPercentageOfTotal.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	dataFields, _ := pivotTable.GetDataFields()
	dataField, _ := dataFields.Get_Int(0)
	// Read the current show-values settings
	settings, _ := dataField.GetShowValuesSetting()
	calculationType, _ := settings.GetCalculationType()
	baseFieldIndex, _ := settings.GetBaseFieldIndex()
	baseItemPositionType, _ := settings.GetBaseItemPositionType()
	baseItemIndex, _ := settings.GetBaseItemIndex()
	fmt.Println("CalculationType:", calculationType)
	fmt.Println("BaseFieldIndex:", baseFieldIndex)
	fmt.Println("BaseItemPositionType:", baseItemPositionType)
	fmt.Println("BaseItemIndex:", baseItemIndex)
	// Switch to a base-item calculation with the one-call method: difference
	// from the value of the previous item in the row field
	rowFields, _ := pivotTable.GetRowFields()
	rowField, _ := rowFields.Get_Int(0)
	baseIndex, _ := rowField.GetBaseIndex()
	dataField.ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(
		PivotFieldDataDisplayFormat_DifferenceFrom,
		baseIndex,
		PivotItemPositionType_Previous,
		0,
	)
	pivotTable.CalculateData()
	// Note: the percentage number format saved by the previous example still
	// clings to the data field cells; the underlying values are now differences
	// Re-read the applied configuration
	updatedSettings, _ := dataField.GetShowValuesSetting()
	updatedCalculationType, _ := updatedSettings.GetCalculationType()
	fmt.Println("CalculationType now:", updatedCalculationType)
	workbook.Save_String("ShowValuesAsDifferenceFrom.xlsx")
}
```

## **関連記事**
- [ピボットテーブルでピボットフィールドをグループ化](/cells/ja/go-cpp/group-pivot-fields-in-the-pivot-table/)
- [ピボットテーブルの上位10の表示またはフィルタ](/cells/ja/go-cpp/top-10-show-or-filter-in-pivot-table/)
- [スライサーの更新](/cells/ja/go-cpp/updating-slicer/)

{{< app/cells/assistant language="go" >}}