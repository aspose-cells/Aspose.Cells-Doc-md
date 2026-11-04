---
title: 格式化数据透视表的部分
linktitle: 格式化数据透视表的部分
description: 通过 PivotTable.Format 将样式应用于语义 PivotArea 区域或 CellArea 矩形，以在 Aspose.Cells for Go via C++ 中格式化数据透视表的一部分，格式存储在 PivotTable.PivotFormats 中，并在刷新数据透视表时保留。
keywords: Aspose.Cells for Go via C++, 数据透视表, 格式化, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, Go via C++
type: docs
weight: 20
url: /zh/go-cpp/format-part-of-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
`PivotTable.FormatAll` 为整个数据透视表应用单一样式，相关内容已在父页面中说明。它不会区分标签、数值、合计或报表的特定区域。  
在实际操作中，通常只需要突出显示数据透视表的某一部分。常见的目标包括属于某一行字段的标签、某字段产生的数值单元格、总计行，或像前两行项目这样的任意矩形。  
直接对数据透视表所在工作表的单元格应用样式并不等同。Excel 将数据透视表的格式存储为语义 `PivotArea` 区域，而不是普通的单元格样式记录。`PivotArea` 格式会附着在字段的标签或数据值等区域，并在数据透视表重新计算、刷新或展开时重新解析。而直接写入单元格的样式则只属于该单元格位置，未被数据透视表模型跟踪。  
Aspose.Cells 提供完整的 `PivotTable.Format` 重载族，使两种格式化方式均可使用：
- `Format(PivotArea, Style)` 将样式锚定到通过 `PivotArea.Select` 或 `PivotArea.SelectField` 构建的语义区域。
- `Format(CellArea, Style)` 将样式锚定到数据透视表内部的工作表矩形。
- `Format(int row, int column, Style)` 用于定位单元格。
- `FormatAll(Style)` 格式化整张数据透视表。

## **格式化 Pivot 区域**
当需要让高亮随字段或报表区域保持关联时，推荐使用语义区域工作流。
1. 使用 `NewPivotArea(pivotTable)` 创建 `PivotArea`。该对象描述了属于该数据透视表的语义区域。  
2. 使用 `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)` 按给定轴的零基位置选择字段。  
   - `PivotTableSelectionType.DataAndLabel` 选择字段的标签和数据。  
   - `PivotTableSelectionType.LabelOnly` 仅选择字段的标签。  
   - `PivotTableSelectionType.DataOnly` 仅选择字段的数据单元格。  
3. 使用 `PivotArea.SelectField(PivotFieldType axisType, string fieldName)` 按名称选择字段。当按名称选择行字段时，区域解析为该字段项产生的数值单元格。  
4. 使用 `Workbook.CreateStyle()` 创建 `Style`，配置其字体、前景色和实线填充模式，然后将该样式传递给 `PivotTable.Format(area, style)`。  
5. 每次调用 `PivotArea` 重载都会向 `PivotTable.PivotFormats` 添加一个 `PivotTableFormat` 条目。  
6. 字段锚定的格式在计算数据透视表时绘制。因此，在应用格式后调用 `PivotTable.CalculateData()` 以使样式可见。  
下面的示例构建了一个小型水果销售数据透视表，使用 `PivotArea.Select` 和 `PivotTableSelectionType.LabelOnly` 为 `Fruit` 行标签设置样式，使用 `PivotArea.SelectField` 为同一行字段产生的数值单元格设置样式，然后重新计算数据透视表，以便两种样式均被绘制。

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

## **格式化数据透视表的单元格区域**
当感兴趣的区域是普通工作表矩形而非语义数据透视区域时，使用 `PivotTable.Format(CellArea, Style)`。  
`CellArea` 通过其 `StartRow`、`EndRow`、`StartColumn`、`EndColumn` 值描述，可通过相应的 `Set_StartRow` 系列访问器设置。这些值是零基工作表坐标，结束坐标标识矩形中最后包含的行和列，因此该区域覆盖从起始位置到结束位置（含结束位置）的所有单元格。  
不同于字段锚定的格式，`CellArea` 格式会立即应用于单元格，无需再次调用 `CalculateData()` 即可看到样式。  
`CellArea` 矩形可以同时包含标签单元格和数值单元格。下一节将说明 Aspose.Cells 与 Excel 在内部如何表示该矩形。  
下面的示例将数据透视表的矩形 `E4:F5` 使用斜体、淡蓝色样式进行格式化，并在无需进一步重新计算的情况下保存工作簿。

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

## **Pivot 区域和单元格区域的映射方式**
Excel 将数据透视表的格式存储为 `pivotArea` 记录，而非普通工作表单元格样式记录。Aspose.Cells 使用相同的模型，因此格式化请求会在记录时转换为 Pivot 区域。  
用户提供的 `CellArea` 与内部存储的 Pivot 区域之间的对应关系是多对多的：  
- 一个 `CellArea` 可能产生多个 Pivot 区域。如果矩形跨越标签单元格和数值单元格，它会被拆分为单独的标签规则和数据规则，因为数据透视模型将标签格式化和数据格式化视为独立。  
- 一个 Pivot 区域可能解析为多个不相连的 `CellArea` 实例。诸如总计行、或项目不连续的字段等语义区域可以覆盖多个矩形，这也是 `PivotArea.GetCellAreas()` 返回集合而非单一矩形的原因。  
通过 `PivotTable.Format` 执行的每一次格式操作都会记录在 `PivotTable.PivotFormats` 中。每个 `PivotTableFormat` 条目公开关联的 `PivotArea` 与应用于该区域的 `Style`。`PivotArea` 重载每次调用仅添加一个条目，而包含不同语义区域的 `CellArea` 则可能添加多个条目。  
为区分存储的区域，每个 `PivotArea` 公开 `OnlyLabel` 和 `OnlyData` 标记。下面的示例对同时覆盖标签和数值的单一矩形进行格式化，检查 `PivotTable.PivotFormats`，并打印每个存储的 Pivot 区域解析后的 `CellArea` 坐标。

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
由于格式以 Pivot 区域而非普通单元格样式存储，它们在重新计算和刷新后仍会保留。无论是使用 `PivotTable.RefreshData` 刷新数据透视表、使用 `CalculateData` 重新计算，还是保存后重新加载，所有存储的 Pivot 区域都会重新解析到其当前所在位置并重新应用样式。
{{% /alert %}}

在需要让高亮随字段或语义区域在刷新后保持关联时，请使用通过 `Select` 或 `SelectField` 构建的 `PivotArea`；在仅需在当前数据透视表布局中格式化固定矩形时，可使用 `CellArea`。单元格重载 `Format(int row, int column, Style)` 用于定位单个单元格。若需一次性重新样式化整张数据透视表，请使用父页面中介绍的 `FormatAll`。

{{< app/cells/assistant language="go" >}}