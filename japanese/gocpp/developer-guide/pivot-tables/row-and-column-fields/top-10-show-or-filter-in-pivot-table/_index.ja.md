---
title: ピボットテーブルでの上位10件の表示またはフィルター
linktitle: ピボットテーブルでの上位10件の表示またはフィルター
description: Aspose.Cells for Go via C++ で、ピボットフィールドの上位または下位の項目のみを表示する方法を学びます。このiraràiでは、Excel 97-2003 の AutoShow 設定（SetIsAutoShow など）、設定値の読み取り、および FilterTop10 を使用した Excel 2007-365 の上位10件フィルターについて説明します。
keywords: Aspose.Cells, Go via C++, ピボットテーブル, 上位10件, AutoShow, SetIsAutoShow, SetIsAscendShow, SetAutoShowCount, SetAutoShowField, FilterTop10, PivotFilterType, PivotField, Go
type: docs
weight: 20
url: /ja/go-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる利用シーン**
行フィールドのすべての項目を一覧表示するピボットテーブルは、そのフィールドに数十のメンバーがある場合に読みにくくなることがあります。上位10件のレポートは、ランキング上位または下位の項目だけを残します。これは「売上上位5商品」や「販売件数下位3地域」などのランキングレポートにまさに必要な機能です。`Aspose.Cells` はこの用途に2つのメカニズムをサポートしており、それぞれ Microsoft Excel の2つの世代に対応しています。
- **Excel 97-2003 AutoShow** — `PivotField` の4つのセッター `SetIsAutoShow`、`SetIsAscendShow`、`SetAutoShowCount`、`SetAutoShowField` です。これは、ピボットフィールドに直接保存されるクラシックな「上位/下位N件の項目を表示」設定です。オリジナルのピボットテーブル形式の一部であるため、旧バージョンを含むすべての Excel バージョンで動作します。
- **Excel 2007-365 上位10件フィルター** — `PivotField.FilterTop10()` メソッドです。これは、フィールドメニューの「値フィルター」にある新しい上位10件値フィルターです。フィールドに紐づけられた `PivotFilter` オブジェクトとして保存され、項目数と割合に基づく順位付けを提供します。

## **Excel 97-2003 における上位10件の表示（AutoShow）**
クラシックな AutoShow は、`PivotField` に対する4つのセッター呼び出しで設定します。
- `SetIsAutoShow(bool)` — フィールドの AutoShow 設定を有効または無効にします。
- `SetIsAscendShow(bool)` — `false` の場合は上位の項目を保持し、`true` の場合は下位の項目を保持します。
- `SetAutoShowCount(int32)` — 保持する項目数を指定します。たとえば、クラシックな上位10件レポートでは10を指定します。
- `SetAutoShowField(int32)` — 項目の順位付けに使用する値を持つ**データフィールド**の0始まりインデックスを指定します。フィールド自体で項目を順位付けする場合は、-1を指定します。
順位付けは値フィールドまたはフィールド自体に基づいて実行できます。以下に、2つの代表的なパターンを示します。

### **値フィールドによる順位付け**
行フィールドの項目を、`Sales` の合計のような標準的な値フィールドで順位付けします。次の例では、行フィールド (`Sport`) が1つ、データフィールド (`Sales`) が1つあるピボットテーブルを作成し、`Sales` に基づいて上位2件のスポーツを表示します。`rankBy` が0なのは、`"Sum of Sales"` がインデックス0にあるデータフィールドだからです。

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
	// 「販売額合計」に基づいて上位2項目を表示する（データフィールドのインデックスは0）
	sportField.SetIsAutoShow(true)
	sportField.SetIsAscendShow(false)
	sportField.SetAutoShowCount(int32(2))
	sportField.SetAutoShowField(int32(0))
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-value-field.xlsx")
}
```

### **フィールド自体による順位付け**
フィールドをそれ自体で順位付けすることもできます。`SetAutoShowField` に-1を指定してください。このバリエーションには追加のデータフィールドは不要であり、フィールドが行（または列）領域に配置されている必要があります。次の例では、フィールド自体に基づいて順位付けした下位3件のスポーツを表示します。この設定では、-1がピボットテーブル形式の既定値であるため、`rankBy` 属性はピボットテーブル XML から省略されます。また、`GetAutoShowField()` は-1を読み戻します。

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
	// フィールド自体で順位付けされた下位3項目を表示する (rankBy = -1)
	sportField.SetIsAutoShow(true)
	sportField.SetIsAscendShow(true)
	sportField.SetAutoShowCount(3)
	sportField.SetAutoShowField(-1)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-field-itself.xlsx")
}
```

## **現在の AutoShow オプションの読み取り**
`PivotField` の読み取り用メソッド `IsAutoShow()`、`IsAscendShow()`、`GetAutoShowCount()`、`GetAutoShowField()` は、フィールドに現在保存されている AutoShow オプションを取得します。これらのメソッドを使用すると、既存のワークブックや、設定した直後のピボットテーブルで項目がどのように表示されるかを確認できます。ファイルから読み込んだワークブックについても同様です。

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
	isAutoShow, _ := sportField.IsAutoShow()
	isAscendShow, _ := sportField.IsAscendShow()
	autoShowCount, _ := sportField.GetAutoShowCount()
	autoShowField, _ := sportField.GetAutoShowField()
	direction := "Bottom"
	if !isAscendShow {
		direction = "Top"
	}
	fmt.Println("AutoShow enabled:", isAutoShow)
	fmt.Println("Direction:", direction)
	fmt.Println("Item count:", autoShowCount)
	fmt.Println("Ranking data field index:", autoShowField)
}
```

これら4つのプロパティは、ピボットテーブル XML に書き込まれるクラシックな AutoShow 属性 (`autoShow`、`topAutoShow`、`itemPageCount`、`rankBy`) に対応しています。そのため、読み戻される値は、すべての Excel バージョンで適用される値です。

## **注意**

{{% alert color="primary" %}}
- AutoShow のいずれかのセッターを変更したら、`PivotTable.CalculateData()` を再度呼び出してください。設定は、次回の再計算で生成されるレイアウトにのみ反映されます。
- AutoShow 設定は行フィールドと列フィールドで使用できます。ページ（フィルター）領域にのみ置かれているフィールドは、項目がピボットテーブルの本体領域に配置されていないため、この方法では順位付けできません。
{{% /alert %}}

## **Excel 2007-365: 上位10件フィルター（FilterTop10）**
新しい Excel バージョンでは、フィールドメニューの「値フィルター」にある「上位10件...」から、上位10件を値フィルターとして利用できます。`Aspose.Cells` は `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)` メソッドでこの機能を表し、作成された `PivotFilter` を返します。
- `valueFieldIndex` — 集計値に基づいて項目を順位付けするデータフィールドの0始まりインデックスです。
- `type` — `itemCount` の意味を決定します。`PivotFilterType.Count` は固定個数の項目を保持します（ダイアログの「項目数」オプション）。`PivotFilterType.Percent` は項目の一定割合を保持するため、`itemCount` は割合自体になります。つまり、30を指定すると上位30%を保持します。`PivotFilterType.Sum` は累積値のカバー率に基づいて順位付けします。
- `isTop` — 上位の場合は `true`、下位の場合は `false` です。
- `itemCount` — 「上位N件」の N を指定します。単位は `type` によって決まります。

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
	// トップ10フィルター — 「Sales の合計」に基づいて上位2項目を保持（データフィールドのインデックスは0）
	sportField.FilterTop10(0, PivotFilterType_Count, true, 2)
	// パーセンベースのフィルターを使用する場合は、項目の上位30%を保持します：
	// sportField.FilterTop10(0, PivotFilterType_Percent, true, 30)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-filter.xlsx")
}
```

{{% alert color="primary" %}}
AutoShow 設定と `FilterTop10` は別々の機能です。AutoShow はピボットフィールドに設定されたクラシックな `autoShow` 属性群を書き出し、Excel 97以降のすべての Excel バージョンで適用されます。`FilterTop10` は新しい `PivotFilter` エントリを書き出すため、Excel 2007以降が必要です。ワークブックを旧バージョンの Excel で開いた場合、新しいフィルターを使用するピボットテーブルは、フォールバックしてすべての項目を表示します。レガシーツールとの往復処理が必要なドキュメントでは、AutoShow のセッターを使用してください。新しいワークブックでは、他の値フィルターと組み合わせることができる `FilterTop10` の使用を推奨します。
{{% /alert %}}

## **関連記事**
- [ピボットテーブル内のピボットフィールドのグループ化](/cells/ja/go-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="go" >}}