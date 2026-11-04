---
title: ピボットテーブルの一部をフォーマットする
linktitle: ピボットテーブルの一部をフォーマットする
description: Aspose.Cells for Go via C++ で PivotTable.Format を使用して、意味的な PivotArea 領域または CellArea 矩形にスタイルを適用し、フォーマットを PivotTable.PivotFormats に保存して、ピボットテーブルがリフレッシュされた際にも保持されるように、ピボットテーブルの一部をフォーマットします。
keywords: Aspose.Cells for Go via C++, ピボットテーブル, フォーマット, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, Go via C++
type: docs
weight: 20
url: /ja/go-cpp/format-part-of-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる使用シナリオ**
`PivotTable.FormatAll` はピボットテーブル全体に単一のスタイルを適用し、親ページで説明されています。ラベル、値、合計、またはレポートの特定領域を区別しません。  
実務では、ピボットテーブルのごく一部だけを目立たせたいことが多くあります。一般的な対象としては、特定の行フィールドに属するラベル、あるフィールドによって生成された値セル、総計行、または最初の 2 行のような任意の矩形があります。  
ピボットテーブルのワークシート上のセルに直接スタイルを適用しても同等ではありません。Excel はピボットテーブルの書式設定を普通のセルスタイルレコードではなく、意味的な `PivotArea` 領域として保存します。`PivotArea` の書式はフィールドのラベルやデータ値といった領域に結び付けられ、ピボットテーブルが再計算、リフレッシュ、または拡張されると再解決されます。一方、セルに直接書き込まれたスタイルはそのセル位置に属し、ピボットモデルによって追跡されません。  
Aspose.Cells は完全な `PivotTable.Format` オーバーロード ファミリーを提供しており、両方の書式設定方法が利用可能です：
- `Format(PivotArea, Style)` は `PivotArea.Select` または `PivotArea.SelectField` で構築された意味領域にスタイルを固定します。
- `Format(CellArea, Style)` はピボットテーブル内のワークシート矩形にスタイルを固定します。
- `Format(int row, int column, Style)` は単一セルを対象とします。
- `FormatAll(Style)` はピボットテーブル全体をフォーマットします。

## **ピボット領域をフォーマットする**
レポートのフィールドや領域にハイライトを付け続ける必要がある場合は、意味領域のワークフローが推奨されます。
1. `NewPivotArea(pivotTable)` で `PivotArea` を作成します。このオブジェクトは対象のピボットテーブルに属する意味領域を表します。
2. `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)` を使用して、指定軸上のゼロベース位置でフィールドを選択します。  
   - `PivotTableSelectionType.DataAndLabel` はラベルとデータの両方を選択します。  
   - `PivotTableSelectionType.LabelOnly` はフィールドのラベルのみを選択します。  
   - `PivotTableSelectionType.DataOnly` はフィールドのデータセルのみを選択します。
3. `PivotArea.SelectField(PivotFieldType axisType, string fieldName)` で名前によりフィールドを選択します。行フィールドを名前で選択した場合、領域はそのフィールドのアイテムが生成する値セルに解決されます。
4. `Workbook.CreateStyle()` で `Style` を作成し、フォント、前景色、単色背景パターンを設定し、`PivotTable.Format(area, style)` に渡します。
5. `PivotArea` のオーバーロードを呼び出すたびに、`PivotTable.PivotFormats` に `PivotTableFormat` エントリが 1 件追加されます。
6. フィールドに固定された書式はピボットデータが計算される際に描画されます。したがって、書式を適用した後に `PivotTable.CalculateData()` を呼び出してスタイルを表示させます。  
以下の例は、フルーツ販売の小規模ピボットテーブルを作成し、`Fruit` 行ラベルを `PivotArea.Select` と `PivotTableSelectionType.LabelOnly` でスタイル設定し、同じ行フィールドが生成する値セルを `PivotArea.SelectField` でスタイル設定し、最後にピボットテーブルを再計算して両方のスタイルを描画します。

```go
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	cells, _ := sheet.GetCells()
	// Fruit sales data
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
	a1Cell, _ := cells.Get_String("A1")
	a1Cell.PutValue_String("Fruit")
	b1Cell, _ := cells.Get_String("B1")
	b1Cell.PutValue_String("Year")
	c1Cell, _ := cells.Get_String("C1")
	c1Cell.PutValue_String("Amount")
	for i := 0; i < len(fruits); i++ {
		fruitCell, _ := cells.Get_Int_Int(int32(i+1), 0)
		fruitCell.PutValue_String(fruits[i])
		yearCell, _ := cells.Get_Int_Int(int32(i+1), 1)
		yearCell.PutValue_Int(years[i])
		amountCell, _ := cells.Get_Int_Int(int32(i+1), 2)
		amountCell.PutValue_Int(amounts[i])
	}
	// Pivot table with its top-left corner at E3 (row 2, column 4)
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", 2, 4)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Bold yellow fill on the row field's label cells
	labelStyle, _ := workbook.CreateStyle()
	labelFont, _ := labelStyle.GetFont()
	labelFont.SetIsBold(true)
	yellow, _ := Color_Yellow()
	labelStyle.SetForegroundColor(yellow)
	labelStyle.SetPattern(BackgroundType_Solid)
	labelArea, _ := NewPivotArea(pivotTable)
	labelArea.Select(PivotFieldType_Row, 0, PivotTableSelectionType_LabelOnly)
	pivotTable.Format_PivotArea_Style(labelArea, labelStyle)
	// Light green fill on the value cells the row field produces
	valueStyle, _ := workbook.CreateStyle()
	lightGreen, _ := Color_LightGreen()
	valueStyle.SetForegroundColor(lightGreen)
	valueStyle.SetPattern(BackgroundType_Solid)
	valueArea, _ := NewPivotArea(pivotTable)
	valueArea.SelectField_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.Format_PivotArea_Style(valueArea, valueStyle)
	// Field-anchored formats are painted when the data is calculated
	pivotTable.CalculateData()
	// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
	workbook.Save_String("FormatPivotArea.xlsx")
}
```

## **ピボットテーブルのセル領域をフォーマットする**
関心領域が意味的なピボット領域ではなく、単なるワークシート矩形である場合は `PivotTable.Format(CellArea, Style)` を使用します。  
`CellArea` は `StartRow`, `EndRow`, `StartColumn`, `EndColumn` の値で記述され、対応する `Set_StartRow` 系アクセサを通じて設定します。これらの値はゼロベースのワークシート座標であり、終了座標は矩形に含まれる最終行と最終列を示すため、開始位置から終了位置までのセルがすべて対象になります。  
フィールドに固定された書式とは異なり、`CellArea` の書式は即座にセルに適用されます。スタイルを表示させるために追加の `CalculateData()` 呼び出しは不要です。  
`CellArea` 矩形はラベルセルと値セルを同時に含むことができます。次のセクションでは、Aspose.Cells と Excel がその矩形を内部でどのように表現しているかを説明します。  
以下の例は、ピボットテーブルの矩形 `E4:F5` にイタリック体の薄青スタイルを適用し、再計算せずにワークブックを保存します。

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
	years := []int{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int{100, 150, 120, 180, 90, 110}
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
		cell.PutValue_Int(int32(years[i]))
		cell, _ = cells.Get_Int_Int(int32(i+1), int32(2))
		cell.PutValue_Int(int32(amounts[i]))
	}
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", 2, 4)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Highlight the first two fruit rows (the rectangle E4:F5)
	highlightStyle, _ := workbook.CreateStyle()
	font, _ := highlightStyle.GetFont()
	font.SetIsItalic(true)
	highlightColor, _ := Color_LightBlue()
	highlightStyle.SetForegroundColor(highlightColor)
	highlightStyle.SetPattern(BackgroundType_Solid)
	rectangle, _ := NewCellArea()
	rectangle.Set_StartRow(3)
	rectangle.Set_EndRow(4)
	rectangle.Set_StartColumn(4)
	rectangle.Set_EndColumn(5)
	pivotTable.Format_CellArea_Style(rectangle, highlightStyle)
	// E4:F5 is italic on light blue immediately, no recalculation needed
	workbook.Save_String("FormatPivotCellArea.xlsx")
}
```

## **Pivot領域とCell領域のマッピング**
Excel はピボットテーブルの書式設定を普通のワークシートセルスタイルレコードではなく `pivotArea` レコードとして保存します。このモデルは Aspose.Cells でも使用されており、書式設定要求は記録時にピボット領域に変換されます。  
ユーザーが提供した `CellArea` と内部に保持されるピボット領域との関係は、多対多の双方向です。  
- 1 つの `CellArea` は複数のピボット領域を生成することがあります。矩形がラベルセルと値セルの両方を跨ぐ場合、ラベル書式とデータ書式が別々のルールに分解されます。ピボットモデルはラベル書式とデータ書式を独立して扱うためです。  
- 1 つのピボット領域は複数の離散した `CellArea` インスタンスに解決されることがあります。総計行や、アイテムが連続していないフィールドなどの意味領域は複数の矩形をカバーする可能性があるためです。これが `PivotArea.GetCellAreas()` が単一の矩形ではなくコレクションを返す理由です。  
`PivotTable.Format` を通じて実行されたすべての書式操作は `PivotTable.PivotFormats` に記録されます。各 `PivotTableFormat` エントリは関連付けられた `PivotArea` と適用された `Style` を公開します。`PivotArea` のオーバーロードは呼び出しごとに正確に 1 件のエントリを追加しますが、異なる意味領域を含む `CellArea` は複数のエントリを追加することがあります。  
保存されている領域を区別するために、各 `PivotArea` は `OnlyLabel` と `OnlyData` フラグを提供します。以下の例は、ラベルと値の両方をカバーする単一矩形をフォーマットし、`PivotTable.PivotFormats` を調査して、各保存されたピボット領域が解決する `CellArea` 座標を出力します。

```go
import (
	"fmt"
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
		cell, _ = cells.Get_Int_Int(int32(i+1), 0)
		cell.PutValue_String(fruits[i])
		cell, _ = cells.Get_Int_Int(int32(i+1), 1)
		cell.PutValue_Int(years[i])
		cell, _ = cells.Get_Int_Int(int32(i+1), 2)
		cell.PutValue_Int(amounts[i])
	}
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", 2, 4)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	highlightStyle, _ := workbook.CreateStyle()
	font, _ := highlightStyle.GetFont()
	font.SetIsItalic(true)
	highlightColor, _ := Color_LightBlue()
	highlightStyle.SetForegroundColor(highlightColor)
	highlightStyle.SetPattern(BackgroundType_Solid)
	// ONE rectangle in...
	rectangle, _ := NewCellArea()
	rectangle.Set_StartRow(3)
	rectangle.Set_EndRow(4)
	rectangle.Set_StartColumn(4)
	rectangle.Set_EndColumn(5)
	pivotTable.Format_CellArea_Style(rectangle, highlightStyle)
	// ...TWO semantic pivot areas out: the label part and the data part are stored separately
	pivotFormats, _ := pivotTable.GetPivotFormats()
	formatCount, _ := pivotFormats.GetCount()
	fmt.Printf("Stored formats: %d\n", formatCount)
	for i := int32(0); i < int32(formatCount); i++ {
		pivotFormat, _ := pivotFormats.Get(i)
		storedArea, _ := pivotFormat.GetPivotArea()
		onlyLabel, _ := storedArea.GetOnlyLabel()
		onlyData, _ := storedArea.GetOnlyData()
		onlyLabelText := "False"
		if onlyLabel {
			onlyLabelText = "True"
		}
		onlyDataText := "False"
		if onlyData {
			onlyDataText = "True"
		}
		fmt.Printf("Format %d: OnlyLabel=%s, OnlyData=%s\n", i, onlyLabelText, onlyDataText)
		resolvedAreas, _ := storedArea.GetCellAreas()
		for _, resolved := range resolvedAreas {
			startRow, _ := resolved.Get_StartRow()
			endRow, _ := resolved.Get_EndRow()
			startColumn, _ := resolved.Get_StartColumn()
			endColumn, _ := resolved.Get_EndColumn()
			fmt.Printf(
				"    rows %d-%d, columns %d-%d\n",
				startRow+1,
				endRow+1,
				startColumn+1,
				endColumn+1,
			)
		}
	}
	// This prints:
	// Stored formats: 2
	// Format 0: OnlyLabel=True, OnlyData=False
	//     rows 4-5, columns 5-5        (E4:E5, the label part)
	// Format 1: OnlyLabel=False, OnlyData=True
	//     rows 4-5, columns 6-6        (F4:F5, the data part)
	workbook.Save_String("FormatPivotAreasMap.xlsx")
}
```

{{% alert color="primary" %}}
書式がピボット領域として保存され、通常のセルスタイルとしてではなくなるため、再計算やリフレッシュ後も保持されます。ピボットテーブルを `PivotTable.RefreshData` でリフレッシュしたり、`CalculateData` で再計算したり、保存後に再読み込みした場合でも、すべての保存されたピボット領域は現在の位置に再解決され、スタイルが再適用されます。
{{% /alert %}}

ハイライトをフィールドや意味的領域に付け続ける必要がある場合は `Select` または `SelectField` で構築した `PivotArea` を使用し、現在のレイアウト内の固定矩形をフォーマットするだけでよい場合は `CellArea` を使用してください。単一セルを対象とする `Format(int row, int column, Style)` オーバーロードは個別のセルに適用できます。ピボットテーブル全体を一度に再スタイル化したい場合は、親ページで説明されている `FormatAll` を使用します。

{{< app/cells/assistant language="go" >}}