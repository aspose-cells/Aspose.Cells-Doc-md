---
title: ピボットテーブルに条件付き書式を追加する
linktitle: ピボットテーブルに条件付き書式を追加する
description: Aspose.Cells for Go を C++ 経由で使用してピボットテーブルに条件付き書式を追加します。ApplyTo と PivotConditionFormatScopeType スコープを使用してデータ領域にルールをアンカーするか、AddCellArea と PivotAreas で対象を定義し、FormatConditions.AddCondition を介してルールとスタイルを付けます。
keywords: Aspose.Cells, ピボットテーブル, 条件付き書式, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C++
type: docs
weight: 30
url: /ja/go-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる使用シナリオ**
親ページおよび兄弟ページで説明されているスタイルは静的です。`PivotArea` または `CellArea` 領域は一度塗りつぶされ、値が何であってもその書式が保持されます。条件付き書式はルール駆動の対応物であり、200 を超える金額をハイライトしたり、中央の 50% をシェードしたり、下位ランクの項目にフラグを付けたりします。ハイライトはピボットテーブルが再計算またはリフレッシュされるたびに値に合わせて更新されます。  
Aspose.Cells では、ピボットテーブルの条件付き書式は `PivotTable.ConditionalFormats` コレクションに格納されます。各エントリは `PivotConditionalFormat` で、次の 2 つの質問に独立して答えます。
- **ルールはどこに適用されますか？** 対象領域は `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)` で定義でき、これは Excel の UI のスコープ選択と同等です。または `AddCellArea(CellArea)` と `PivotAreas` コレクションを使用して領域を明示的に指定します。  
- **ルールは何をテストしますか？** `FormatConditions` に対して `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` で 1 つ以上の条件を追加し、各条件は独自の `Style` を持ちます。

{{% alert color="primary" %}}
`FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` または `FormatConditionCollection.AddArea(CellArea)` をピボット条件付き書式の `FormatConditions` オブジェクトで呼び出さないでください。これら 2 つのオーバーロードは通常のワークシート条件付き書式 API から継承されたもので、ピボットテーブルでは機能しません。セル領域がピボット領域に変換されないため、リクエストは黙って無視されます。必ず `PivotConditionalFormat` 自体（`ApplyTo`、`AddCellArea`、または `PivotAreas`）で領域を定義し、`AddCondition` のいずれかのオーバーロードでルールを追加してください。
{{% /alert %}}

## **スコープを使用してルールを適用する（Excel UI の方法）**
最初の方法は、Excel のユーザーインターフェイスと同じようにルールを配置します。ピボットテーブルのセルはゼロベースのワークシート座標で名前付けされ、`PivotConditionFormatScopeType` スコープがそのセルからルールがどれだけ広がるかを指示します。
- `PivotConditionFormatScopeType.Data` – ピボットテーブルが生成するすべての値セル（総計を含む）。  
- `PivotConditionFormatScopeType.Field` – セルが示すフィールドに属する値セル（総計を除く）。セルは行フィールドのラベルなど、フィールドセルである必要があります。値セルを渡すと例外がスローされます。  
- `PivotConditionFormatScopeType.Selection` – セルが選択する交差点の値セルのみで、通常は単一の値セルです。
以下の例では、左上隅が E3 にあるフルーツ売上ピボットテーブルを作成し、`Data` スコープでセル F4（行 3、列 5）に条件付き書式をアンカーし、200 を超える金額を赤背景に白文字で太字にハイライトします。Apple が 220、Banana が 330、Cherry が 200、合計が 750 の場合、ルールは F4、F5、F7 を塗りつぶします — 解決された領域はデータ列全体の F4:F7 で、条件を満たすセルだけがハイライトされます。

```go
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	cells, _ := sheet.GetCells()
	a1, _ := cells.Get_String("A1")
	a1.PutValue_String("Fruit")
	b1, _ := cells.Get_String("B1")
	b1.PutValue_String("Year")
	c1, _ := cells.Get_String("C1")
	c1.PutValue_String("Amount")
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
	for i := range fruits {
		fruitCell, _ := cells.Get_Int_Int(int32(i+1), int32(0))
		fruitCell.PutValue_String(fruits[i])
		yearCell, _ := cells.Get_Int_Int(int32(i+1), int32(1))
		yearCell.PutValue_Int(years[i])
		amountCell, _ := cells.Get_Int_Int(int32(i+1), int32(2))
		amountCell.PutValue_Int(amounts[i])
	}
	// Pivot table with its top-left corner at E3
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", int32(2), int32(4))
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Anchor the conditional format at F4 (row 3, column 5) with the Data scope
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	index, _ := conditionalFormats.Add()
	format, _ := conditionalFormats.Get(index)
	format.ApplyTo(int32(3), int32(5), PivotConditionFormatScopeType_Data)
	// Rule - highlight amounts greater than 200
	formatConditions, _ := format.GetFormatConditions()
	conditionIndex, _ := formatConditions.AddCondition_FormatConditionType_OperatorType_String_String(
		FormatConditionType_CellValue,
		OperatorType_GreaterThan,
		"200",
		"",
	)
	style, _ := workbook.CreateStyle()
	font, _ := style.GetFont()
	font.SetIsBold(true)
	white, _ := Color_FromArgb(int32(-1))
	red, _ := Color_FromArgb(int32(-65536))
	font.SetColor(white)
	style.SetForegroundColor(red)
	style.SetPattern(BackgroundType_Solid)
	condition, _ := formatConditions.Get(conditionIndex)
	condition.SetStyle(style)
	workbook.Save_String("PivotConditionalFormatData.xlsx")
}
```

同じルールを行フィールドラベル E4（行 3、列 4）に `Field` スコープでアンカーすると、解決される領域は F4:F6 になります — 総計行を除いた同じデータ列です。これはスコープが `Fruit` フィールドを表すためです。`Selection` スコープを F4 に設定すると、解決領域は F4 のみになります。

## **領域を手動で定義する**
2 番目の方法は、スコープ選択を省略し、`PivotConditionalFormat` で領域を明示的に指定します。

### **AddCellArea を使用したワークシートの矩形**
`AddCellArea(CellArea)` は、与えられた矩形をルールの対象として記録します。座標はゼロベースのワークシート座標で、領域は提供された矩形そのものです — データ列への拡張や総計ロジックはありません。現在のピボットレイアウトで対象セルが既知の固定矩形である場合に使用します。

```go
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	cells, _ := sheet.GetCells()
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Fruit")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Year")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Amount")
	for i := range fruits {
		cell, _ = cells.Get_Int_Int(int32(i+1), int32(0))
		cell.PutValue_String(fruits[i])
		cell, _ = cells.Get_Int_Int(int32(i+1), int32(1))
		cell.PutValue_Int(years[i])
		cell, _ = cells.Get_Int_Int(int32(i+1), int32(2))
		cell.PutValue_Int(amounts[i])
	}
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", 2, 4)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Target the rectangle F4:F6 (the value cells without the grand total)
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	index, _ := conditionalFormats.Add()
	format, _ := conditionalFormats.Get(index)
	area, _ := NewCellArea()
	area.Set_StartRow(3)
	area.Set_EndRow(5)
	area.Set_StartColumn(5)
	area.Set_EndColumn(5)
	format.AddCellArea(area)
	// Rule - italic on light yellow for amounts between 150 and 300
	formatConditions, _ := format.GetFormatConditions()
	conditionIndex, _ := formatConditions.AddCondition_FormatConditionType_OperatorType_String_String(
		FormatConditionType_CellValue,
		OperatorType_Between,
		"150",
		"300",
	)
	style, _ := workbook.CreateStyle()
	font, _ := style.GetFont()
	font.SetIsItalic(true)
	lightYellow, _ := Color_FromArgb(int32(0xFFFFE0))
	style.SetForegroundColor(lightYellow)
	style.SetPattern(BackgroundType_Solid)
	condition, _ := formatConditions.Get(conditionIndex)
	condition.SetStyle(style)
	workbook.Save_String("PivotConditionalFormatCellArea.xlsx")
}
```

### **PivotAreas を使用した意味的ピボット領域**
`PivotAreas` は兄弟ページで静的スタイルに使用されているのと同じ意味的領域モデルです。`PivotArea` を作成し、`Select` または `SelectField` でフィールドや領域を選択し、`PivotAreas.AddPivotArea(PivotArea)` で追加します。意味的領域はそのフィールドに結び付けられるため、ピボットテーブルがリフレッシュされレイアウトが変わっても条件付き書式はフィールドに追従します。`PivotAreas.Add(PivotArea)` オーバーロードもコンパイルは通りますが、廃止予定としてマークされているため、`AddPivotArea` を使用してください。

```go
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Create a new workbook
	workbook, _ := NewWorkbook()
	// Get the first worksheet
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	// Get the cells collection
	cells, _ := sheet.GetCells()
	// Data arrays
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
	// Write headers
	cellA1, _ := cells.Get_String("A1")
	cellA1.PutValue_String("Fruit")
	cellB1, _ := cells.Get_String("B1")
	cellB1.PutValue_String("Year")
	cellC1, _ := cells.Get_String("C1")
	cellC1.PutValue_String("Amount")
	// Write data rows
	for i := 0; i < len(fruits); i++ {
		row := int32(i + 1)
		c0, _ := cells.Get_Int_Int(row, 0)
		c0.PutValue_String(fruits[i])
		c1, _ := cells.Get_Int_Int(row, 1)
		c1.PutValue_Int(years[i])
		c2, _ := cells.Get_Int_Int(row, 2)
		c2.PutValue_Int(amounts[i])
	}
	// Create pivot table
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", int32(2), int32(4))
	// Add fields to the pivot
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Attach conditional format to the Amount data field
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	cfIdx, _ := conditionalFormats.Add()
	condFormat, _ := conditionalFormats.Get(cfIdx)
	// Define the pivot area covering the Amount data field
	area, _ := NewPivotArea(pivotTable)
	area.SelectField_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotAreas, _ := condFormat.GetPivotAreas()
	pivotAreas.AddPivotArea(area)
	// Add a condition: grey text for amounts below 150
	formatConds, _ := condFormat.GetFormatConditions()
	condIdx, _ := formatConds.AddCondition_FormatConditionType_OperatorType_String_String(
		FormatConditionType_CellValue,
		OperatorType_LessThan,
		"150",
		"", // null second formula
	)
	// Create style with grey font color
	style, _ := workbook.CreateStyle()
	font, _ := style.GetFont()
	grayColor, _ := Color_Gray()
	font.SetColor(grayColor)
	// Apply style to the condition
	cond, _ := formatConds.Get(condIdx)
	cond.SetStyle(style)
	// Save the workbook
	_ = workbook.Save_String("PivotConditionalFormatPivotArea.xlsx")
	fmt.Println("Workbook saved.")
}
```

## **ルールの保存場所と再読込後の存続方法**
`ConditionalFormats.Add()` の呼び出しは、ピボットテーブルに `PivotConditionalFormat` を 1 つ追加します。条件、数式、およびスタイルはワークブックに保存され、下の例でファイルを再度開くと、同じルールがタイプ、演算子、数式がそのまま保持された状態で表示され、`GetCellAreas()` は同じ領域を報告します。条件がまったく設定されていないエントリは、ワークブックが保存される際に削除されます。これは Excel がルールのない条件付き書式を破棄するのと同じ動作です。

```go
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook_String("PivotConditionalFormatData.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	conditionalFormatCount, _ := conditionalFormats.GetCount()
	fmt.Printf("Conditional formats: %d\n", conditionalFormatCount)
	for i := int32(0); i < conditionalFormatCount; i++ {
		format, _ := conditionalFormats.Get(i)
		formatConditions, _ := format.GetFormatConditions()
		formatConditionCount, _ := formatConditions.GetCount()
		for j := int32(0); j < formatConditionCount; j++ {
			condition, _ := formatConditions.Get(j)
			conditionType, _ := condition.GetType()
			operatorType, _ := condition.GetOperator()
			formula1, _ := condition.GetFormula1()
			conditionTypeName := fmt.Sprintf("%v", conditionType)
			if int32(conditionType) == int32(FormatConditionType_CellValue) {
				conditionTypeName = "CellValue"
			}
			operatorTypeName := fmt.Sprintf("%v", operatorType)
			if int32(operatorType) == int32(OperatorType_GreaterThan) {
				operatorTypeName = "GreaterThan"
			}
			fmt.Printf("Format %d: %s %s formula1=%s\n",
				i, conditionTypeName, operatorTypeName, formula1)
		}
		areas, _ := format.GetCellAreas()
		for _, area := range areas {
			startRow, _ := area.Get_StartRow()
			endRow, _ := area.Get_EndRow()
			startColumn, _ := area.Get_StartColumn()
			endColumn, _ := area.Get_EndColumn()
			fmt.Printf("    rows %d-%d, columns %d-%d\n",
				startRow+1, endRow+1, startColumn+1, endColumn+1)
		}
	}
	// This prints:
	// Conditional formats: 1
	// Format 0: CellValue GreaterThan formula1==200
	//     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
}
```

## **関連記事**
- [ピボットテーブルの一部を書式設定する](/cells/ja/go-cpp/format-part-of-pivot-table/)
- [ピボットテーブルで上位10件の表示またはフィルター](/cells/ja/go-cpp/top-10-show-or-filter-in-pivot-table/)

{{< app/cells/assistant language="go" >}}