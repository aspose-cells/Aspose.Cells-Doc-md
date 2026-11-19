---
title: 使用 Golang 通过 C++ 对数据透视表中的透视字段进行分组
linktitle: 使用 Golang 通过 C++ 对数据透视表中的透视字段进行分组
description: 了解如何使用 Aspose.Cells for Go via C++ 中的 PivotField.Group 和 PivotFieldGroupOptions，将数据透视表中的行透视字段和列透视字段按月份和季度等日期周期以及数值范围进行分组。
keywords: Aspose.Cells, Aspose.Cells for Go via C++, 数据透视表, 透视字段, 对透视字段进行分组, Group, Group_PivotFieldGroupOptions, PivotFieldGroupOptions, 日期分组, 数值范围, Go
type: docs
weight: 80
url: /zh/go-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
- 当数据透视表中的行字段或列字段包含大量不同的项目时，对透视字段进行分组非常有用，例如包含数百个日期的日期字段或包含许多离散值的数值字段。分组会将这些项目归并为有意义的层级：日期按月、季度和年分组，数值按 0-1、2-3、4-5 等范围分组。这可以使大型数据透视表更紧凑、更易于分析。Aspose.Cells 通过 `PivotField.Group()` 方法（根据数据类型自动分组）和 `PivotField.Group(PivotFieldGroupOptions)` 重载（自定义分组选项）提供此功能。
- 日期分组将各个日期归并为更大的周期，例如日、月、季度和年，并构建时间层次结构（例如年、季度、月）。这样可以直观地显示随时间变化的趋势，而且每个周期级别都会在数据透视表的行区域或列区域中成为一个独立的透视字段。
- 仅可以对放置在数据透视表行区域或列区域中的字段进行分组。数据（值）字段无法直接分组。若要对此类字段进行分组，必须先将其添加到数据透视表的行区域或列区域。

## **自动对透视字段进行分组**
无参数的 `PivotField.Group()` 重载会检查字段的数据类型并自动进行分组。仅包含日期（和空白值）的字段会按月分组。仅包含数值（和空白值）的字段会使用自动间隔划分为数值范围。

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// Group the first row field automatically by its data type
	rowFields, _ := pivotTable.GetRowFields()
	field, _ := rowFields.Get_Int(0)
	field.Group()
	pivotTable.CalculateData()
	workbook.Save_String("outputAutoGroupPivotField.xlsx")
}
```

## **使用自定义选项对透视字段进行分组**
`PivotFieldGroupOptions` 类提供自定义分组配置。对于日期字段，请设置 `StartDate`、`EndDate` 和 `GroupTypes`（日期以 Go `time.Time` 值的形式传入）。对于数值字段，请设置 `StartNumber`、`EndNumber` 和 `Interval`。`newPivotField` 选项控制分组时是否会在保留原字段的同时创建新的透视字段（请参阅本文末尾的“注意”部分）。

### **按月份和季度对日期字段进行分组**
以下示例将示例数据透视表中的日期行字段按月份和季度分组，并设置开始日期和结束日期。代码加载[示例 Excel 文件](sampleGroupPivotFieldsInPivotTable.xlsx)，执行分组，计算数据透视表数据，然后保存分组结果。截图展示了分组后的效果：日期行字段现已按季度和月份分组。
请注意，`GroupTypes` 中值的顺序会被忽略。无论分组类型以何种顺序列出，分组后的字段始终从最大周期到最小周期显示：年、季度、月、日、时、分、秒。在本例中，`GroupTypes` 中先列出月份，后列出季度，但显示时季度为外层级别，月份为内层级别。

```go
package main
import (
	"time"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// Group the date row field by months and quarters between the given dates
	options, _ := NewPivotFieldGroupOptions()
	options.SetStartDate(time.Date(2008, 1, 1, 0, 0, 0, 0, time.UTC))
	options.SetEndDate(time.Date(2008, 9, 5, 0, 0, 0, 0, time.UTC))
	options.SetGroupTypes([]PivotGroupByType{PivotGroupByType_Months, PivotGroupByType_Quarters})
	rowFields, _ := pivotTable.GetRowFields()
	dateField, _ := rowFields.Get_Int(0)
	dateField.Group_PivotFieldGroupOptions(options)
	pivotTable.CalculateData()
	workbook.Save_String("outputGroupPivotFieldsInPivotTable.xlsx")
}
```

![按月份和季度分组的数据透视表](group-pivot-fields-in-the-pivot-table_1.png)

### **将数值字段分组为数值范围**
`FieldTwo` 最初是示例数据透视表中的数据（值）字段。由于仅行字段或列字段可以分组，代码先调用 `PivotTable.AddFieldToArea(PivotFieldType_Row, "FieldTwo")` 将 `FieldTwo` 移至行区域，刷新数据透视表，然后使用 `StartNumber = 0`、`EndNumber = 5` 和 `Interval = 2` 将数值字段划分为以下范围：0-1、2-3 和 4-5。

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// FieldTwo is a data field: move it to the row area first,
	// because only row/column fields can be grouped
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "FieldTwo")
	pivotTable.CalculateData()
	// Group the numeric field into the ranges 0-1, 2-3, 4-5
	options, _ := NewPivotFieldGroupOptions()
	options.SetStartNumber(0)
	options.SetEndNumber(5)
	options.SetInterval(2)
	rowFields, _ := pivotTable.GetRowFields()
	numericField, _ := rowFields.Get_Int(1)
	numericField.Group_PivotFieldGroupOptions(options)
	pivotTable.CalculateData()
	workbook.Save_String("outputNumberGroupPivotField.xlsx")
}
```

## **注意**

{{% alert color="primary" %}}
- `PivotField.GroupBy()` 方法的重载已弃用，并已从 API 中移除。`PivotField.Group()` 和 `PivotField.Group(PivotFieldGroupOptions)` 是相应的替代方法。
- 在 Microsoft Excel 中，对数值字段进行分组会使用分组后的范围替换原透视字段，而对日期字段进行分组则会在原字段旁创建新的透视字段（每个分组级别一个，例如季度和月份）。从 Aspose.Cells 26.10 开始，`PivotField.Group()` 方法的行为与 Excel 相同。
- `PivotFieldGroupOptions.Interval` 属性仅对数值分组以及按天进行的日期分组（例如将日期划分为每 7 天一个周期）生效；按月、季度或年对日期进行分组时，该属性会被忽略。
{{% /alert %}}

## **相关文章**
- [在数据透视表中显示或筛选前 10 项](/cells/zh/go-cpp/top-10-show-or-filter-in-pivot-table/)
- [数据透视表中的值显示方式](/cells/zh/go-cpp/show-values-as-in-pivot-table/)
- [格式化数据透视表的一部分](/cells/zh/go-cpp/format-part-of-pivot-table/)
- [为数据透视表添加条件格式](/cells/zh/go-cpp/add-conditional-formatting-to-pivot-table/)

{{< app/cells/assistant language="go" >}}