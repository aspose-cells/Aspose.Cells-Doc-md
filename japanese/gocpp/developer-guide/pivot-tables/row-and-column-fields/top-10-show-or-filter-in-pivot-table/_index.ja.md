---
title: ピボットテーブルで上位10件を表示またはフィルター
linktitle: ピボットテーブルで上位10件を表示またはフィルター
description: Aspose.Cells for Go via C++ で、ピボットフィールドの上位または下位の項目のみを表示する方法を学びます。この{div}-contrast{contrast-string="..."}記事{/div-contrast}では、Excel 97-2003 の Top10AutoShow メソッド、Top10AutoShowSettings による設定の読み取り、および FilterTop10 による Excel 2007-365 の上位10件フィルターについて説明します。
keywords: Aspose.Cells, Go via C++, ピボットテーブル, 上位10件, 自動表示, Top10AutoShow, GetTop10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, Go
type: docs
weight: 20
url: /ja/go-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる使用シナリオ**
行フィールドのすべての項目を一覧表示するピボットテーブルは、そのフィールドに数十個のメンバーがある場合は読み取りにくくなります。上位10件のレポートは、順位付けされた項目の上位または下位のみを保持します。これは「売上上位5商品」や「販売数下位3地域」のような順位レポートにまさに必要な機能です。Aspose.Cells はこのための2つのメカニズムをサポートしており、それぞれ Microsoft Excel の2つの世代に対応します。
- **Excel 97-2003 自動表示** — `PivotField.Top10AutoShow()` メソッドです。これは、ピボットフィールドに直接保存される従来の「上位/下位N項目を表示」設定です。元のピボットテーブル形式の一部であるため、新旧を問わずすべての Excel バージョンで機能します。
- **Excel 2007-365 上位10件フィルター** — `PivotField.FilterTop10()` メソッドです。これは、フィールドメニューの値フィルターにある「上位10件」フィルターです。フィールドに添付される `PivotFilter` オブジェクトとして保存され、項目数または割合に基づくランキングを提供します。

## **Excel 97-2003 での上位10件の表示（Top10AutoShow）**
従来の自動表示は、`PivotField.Top10AutoShow(isAutoShow bool, isTop bool, count int32, rankBy int32)` を1回呼び出すことで設定します。
- `isAutoShow` — フィールドの自動表示設定を有効または無効にします。
- `isTop` — `true` の場合は上位項目（Top）を保持し、`false` の場合は下位項目（Bottom）を保持します。
- `count` — 保持する項目数です。例として、従来の上位10件レポートでは 10 を指定します。
- `rankBy` — 項目を順位付けするための値を保持する**データフィールド**のゼロベースインデックスです。フィールド自体を基準に項目を順位付けするには -1 を渡します。

順位付けの基準には、値フィールドまたはフィールド自体を使用できます。以下に、2つの代表的な例を示します。

### **値フィールドによる順位付け**
行フィールドの項目を、「Sales の合計」のような標準的な値フィールドで順位付けします。次の例では、1つの行フィールド (`Sport`) と1つのデータフィールド (`Sales`) からなるピボットテーブルを作成し、その後、売上が上位2つのスポーツを表示します。「Sales の合計」はインデックス 0 のデータフィールドであるため、`rankBy` は 0 です。

```go
package main
import (
	"strconv"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	cells, _ := worksheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Sport")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Quarter")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Sales")
	sports := []string{"Golf", "Tennis", "Rugby", "Cricket", "Boxing"}
	row := int32(2)
	for _, sport := range sports {
		for quarter := int32(1); quarter <= 3; quarter++ {
			cell, _ = cells.Get_Int_Int(row, 0)
			cell.PutValue_String(sport)
			cell, _ = cells.Get_Int_Int(row, 1)
			cell.PutValue_String("Qtr" + strconv.Itoa(int(quarter)))
			cell, _ = cells.Get_Int_Int(row, 2)
			cell.PutValue_Int(1000 + 777*row)
			row++
		}
	}
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("A1:C16", 2, 5)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
	sportField.Top10AutoShow(true, true, 2, 0)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-value-field.xlsx")
}
```

### **フィールド自体による順位付け**
フィールド自体を基準に順位付けすることもできます。この場合は `rankBy` に -1 を渡します。この例では追加のデータフィールドは不要であり、フィールドを行（または列）領域に配置するだけです。次の例では、フィールド自体を基準に順位付けした下位3つのスポーツを表示します。この設定を保存すると、-1 はこの形式の既定値であるため、`rankBy` 属性はピボットテーブル XML から省略されます。また、`GetRankBy()` は -1 を読み戻します。

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	cells, _ := worksheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Sport")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Quarter")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Sales")
	sports := []string{"Golf", "Tennis", "Rugby", "Cricket", "Boxing"}
	row := int32(2)
	for _, sport := range sports {
		for quarter := int32(1); quarter <= 3; quarter++ {
			cell, _ = cells.Get_Int_Int(row, 0)
			cell.PutValue_String(sport)
			cell, _ = cells.Get_Int_Int(row, 1)
			cell.PutValue_String(fmt.Sprintf("Qtr%d", quarter))
			cell, _ = cells.Get_Int_Int(row, 2)
			cell.PutValue_Int(1000 + 777*row)
			row++
		}
	}
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("A1:C16", 2, 5)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Show the bottom 3 items ranked by the field itself (rankBy = -1)
	sportField.Top10AutoShow(true, false, 3, -1)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-field-itself.xlsx")
}
```

## **現在の自動表示オプションの読み取り**
`PivotField.GetTop10AutoShowSettings()` メソッドは、フィールドに現在保存されている自動表示の設定を保持する `PivotFieldTop10AutoShowSettings` オブジェクトを返します。このメソッドを使用すると、既存のワークブックや、設定したばかりのピボットテーブルで項目がどのように表示されるかを確認できます。ファイルから読み込んだワークブックについても同様です。

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook_String("output-top10-by-value-field.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	settings, _ := sportField.GetTop10AutoShowSettings()
	isAutoShow, _ := settings.IsAutoShow()
	isTop, _ := settings.IsTop()
	autoShowCount, _ := settings.GetAutoShowCount()
	rankBy, _ := settings.GetRankBy()
	direction := "Bottom"
	if isTop {
		direction = "Top"
	}
	fmt.Println("AutoShow enabled:", isAutoShow)
	fmt.Println("Direction:", direction)
	fmt.Println("Item count:", autoShowCount)
	fmt.Println("Ranking data field index:", rankBy)
}
```

これらの設定は、ピボットテーブル XML に書き込まれる従来の自動表示属性 (`autoShow`、`topAutoShow`、`itemPageCount`、`rankBy`) に対応しています。したがって、読み戻される値は、すべての Excel バージョンで適用される値です。

## **注意**

{{% alert color="primary" %}}
- `Top10AutoShow()` を呼び出した後は、`PivotTable.CalculateData()` を再度呼び出してください。設定は、次の再計算でピボットレイアウトが再描画されたときにのみ反映されます。
- 自動表示の設定は行フィールドおよび列フィールドで使用できます。ページ（フィルター）領域にのみ配置されているフィールドは、項目がピボット本体の領域に配置されていないため、この方法では順位付けできません。
{{% /alert %}}

## **Excel 2007-365：上位10件フィルター（FilterTop10）**
Excel 2007-365 では、フィールドメニューの「値フィルター」にある「上位10件...」フィルターを利用できます。Aspose.Cells では、`PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)` メソッドでこの機能を利用できます。このメソッドは、作成された `PivotFilter` を返します。
- `valueFieldIndex` — 集計値に基づいて項目を順位付けするデータフィールドのゼロベースインデックスです。
- `type` — `itemCount` の意味を指定します。`PivotFilterType.Count` は固定数の項目を保持します（ダイアログの「項目数」オプション）。`PivotFilterType.Percent` は項目の指定割合を保持するため、`itemCount` 自体が割合になります。30 を指定すると上位30%を保持します。`PivotFilterType.Sum` は累積値でカバーされる範囲に基づいて順位付けします。
- `isTop` — 上位の場合は `true`、下位の場合は `false` です。
- `itemCount` — 上位N件における N を表します。単位は `type` によって異なります。

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	wss, _ := workbook.GetWorksheets()
	worksheet, _ := wss.Get_Int(0)
	cells, _ := worksheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Sport")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Quarter")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Sales")
	sports := []string{"Golf", "Tennis", "Rugby", "Cricket", "Boxing"}
	row := int32(2)
	for _, sport := range sports {
		for quarter := int32(1); quarter <= 3; quarter++ {
			cell, _ = cells.Get_Int_Int(row, 0)
			cell.PutValue_String(sport)
			cell, _ = cells.Get_Int_Int(row, 1)
			cell.PutValue_String(fmt.Sprintf("Qtr%d", quarter))
			cell, _ = cells.Get_Int_Int(row, 2)
			cell.PutValue_Int(1000 + 777*row)
			row++
		}
	}
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("A1:C16", 2, 5)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
	sportField.FilterTop10(0, PivotFilterType_Count, true, 2)
	// For a percentage-based filter instead, keep the top 30 percent of the items:
	// sportField.FilterTop10(0, PivotFilterType_Percent, true, 30)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-filter.xlsx")
}
```

{{% alert color="primary" %}}
自動表示の設定と `FilterTop10` は独立した機能です。自動表示は、ピボットフィールドに設定された従来の `autoShow` 属性を書き込み、Excel 97以降のすべての Excel バージョンで適用されます。`FilterTop10` は、新しい `PivotFilter` エントリを書き込むため、Excel 2007以降が必要です。古い Excel バージョンでワークブックを開くと、新しいフィルターを使用するピボットテーブルでは、すべての項目が表示されます。レガシーツールとの往復処理が必要なドキュメントでは `Top10AutoShow` を優先してください。新しいワークブックでは、他の値フィルターと組み合わせられる `FilterTop10` を優先してください。
{{% /alert %}}

## **関連記事**
- [ピボットテーブルでピボットフィールドをグループ化](/cells/ja/go-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="go" >}}