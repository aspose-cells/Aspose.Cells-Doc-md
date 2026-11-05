---
title: 向数据透视表添加条件格式
linktitle: 向数据透视表添加条件格式
description: 通过 C++ 在 Aspose.Cells for Go 中向数据透视表添加条件格式——使用 ApplyTo 和 PivotConditionFormatScopeType 范围将规则锚定到数据区域，或使用 AddCellArea 和 PivotAreas 定义目标，然后通过 FormatConditions.AddCondition 附加规则和样式。
keywords: Aspose.Cells, 数据透视表, 条件格式, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C++
type: docs
weight: 30
url: /zh/go-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
在父页面和兄弟页面中描述的样式是静态的——`PivotArea` 或 `CellArea` 区域只会被绘制一次，无论数值如何都会保持其样式。条件格式是规则驱动的对应方式——突出显示所有大于 200 的金额、为中间 50% 的值着色，或标记排名最底的项——并且当数据透视表重新计算或刷新时，突出显示会随数值变化而更新。  
在 Aspose.Cells 中，数据透视表的条件格式位于 `PivotTable.ConditionalFormats` 集合中。每个条目都是一个 `PivotConditionalFormat`，它独立回答两个问题：
- **规则适用于哪个区域？** 目标区域可以通过 `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)` 定义，这与 Excel 用户界面的范围选择器相吻合；也可以通过 `AddCellArea(CellArea)` 与 `PivotAreas` 集合显式指定区域。
- **规则检测什么条件？** 使用 `FormatConditions` 的 `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` 添加一个或多个条件，每个条件携带自己的 `Style`。

{{% alert color="primary" %}}
请勿在数据透视表条件格式的 `FormatConditions` 对象上调用 `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` 或 `FormatConditionCollection.AddArea(CellArea)`。这两个重载继承自普通工作表的条件格式 API，无法用于数据透视表——单元格区域永远不会被转换为透视区域，因此请求会被静默忽略。请始终在 `PivotConditionalFormat` 本身上定义区域（`ApplyTo`、`AddCellArea` 或 `PivotAreas`），并使用 `AddCondition` 系列重载之一添加规则。
{{% /alert %}}

## **使用范围应用规则（Excel UI 方式）**
第一种方式遵循 Excel 用户界面的操作方式。数据透视表的单元格使用零基工作表坐标命名，`PivotConditionFormatScopeType` 范围告诉 Aspose.Cells 规则应从该单元格向外扩展到多远：
- `PivotConditionFormatScopeType.Data` - 透视表生成的所有数值单元格，包括总计。
- `PivotConditionFormatScopeType.Field` - 属于该单元格所标识字段的数值单元格，排除总计。该单元格必须是字段单元格，例如行字段标签；若传入数值单元格会抛出异常。
- `PivotConditionFormatScopeType.Selection` - 仅在该单元格选中的交叉点处的数值单元格，通常为单个数值单元格。
下面的示例创建了一个水果销售数据透视表，左上角位于 E3，将条件格式锚定在单元格 F4（第 3 行，第 5 列），使用 `Data` 范围，并将所有大于 200 的金额以红底白字加粗显示。给定 Apple 220、Banana 330、Cherry 200 以及总计 750，规则将覆盖 F4、F5、F7——解析后的区域为整列数据 F4:F7，仅有满足条件的单元格会被高亮。

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

将相同规则锚定在行字段标签 E4（第 3 行，第 4 列）并使用 `Field` 范围时，解析区域变为 F4:F6——同一数据列但不包括总计行，因为此时范围描述的是 `Fruit` 字段而非整个数值区域。使用 `Selection` 范围锚定在 F4 时，仅解析为 F4 单元格。

## **手动定义区域**
第二种方式跳过范围选择器，直接在 `PivotConditionalFormat` 上显式命名区域。

### **使用 AddCellArea 定义工作表矩形**
`AddCellArea(CellArea)` 将给定的矩形记录为规则的目标。坐标采用零基工作表坐标，区域恰好等于提供的矩形——不会自动扩展到数据列，也不会包含总计逻辑。适用于感兴趣的单元格已知为当前透视布局中的固定矩形的场景。

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

### **使用 PivotAreas 定义语义透视区域**
`PivotAreas` 与兄弟页面用于静态样式的语义区域模型相同。创建 `PivotArea`，使用 `Select` 或 `SelectField` 选择字段或区域，然后通过 `PivotAreas.AddPivotArea(PivotArea)` 添加。语义区域会绑定到其对应字段，因此条件格式在透视表刷新、布局变化时会随字段移动。`PivotAreas.Add(PivotArea)` 重载仍可编译，但已标记为过时——请优先使用 `AddPivotArea`。

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

## **规则的存储位置及其在重新加载时的持久化**
每次调用 `ConditionalFormats.Add()` 都会向数据透视表追加一个 `PivotConditionalFormat`。条件、公式以及样式会随工作簿一起保存——在下面的示例中重新打开文件时，仍能看到同样的规则及其类型、运算符和公式完整无缺，`GetCellAreas()` 也会报告相同的区域。未添加任何条件的条目在工作簿保存时会被删除，这与 Excel 会丢弃没有规则的条件格式的行为一致。

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

## **相关文档**
- [格式化数据透视表的部分](/cells/zh/go-cpp/format-part-of-pivot-table/)
- [数据透视表的前10项显示或筛选](/cells/zh/go-cpp/top-10-show-or-filter-in-pivot-table/)

{{< app/cells/assistant language="go" >}}