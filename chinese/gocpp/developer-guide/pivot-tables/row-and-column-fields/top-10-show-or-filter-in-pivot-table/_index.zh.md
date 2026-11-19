---
title: 数据透视表中的前10显示或筛选
linktitle: 数据透视表中的前10显示或筛选
description: 了解如何在 Aspose.Cells for Go via C++ 中仅显示数据透视表字段的前/后排名项，本文介绍 Excel 97-2003 的 Top10AutoShow 方法、使用 Top10AutoShowSettings 读取选项以及 Excel 2007-365 通过 FilterTop10 的前10筛选。
keywords: Aspose.Cells, Go via C++, 数据透视表, 前10名, 自动显示, Top10AutoShow, GetTop10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, Go
type: docs
weight: 20
url: /zh/go-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
当行字段包含数十个成员时，数据透视表列出该字段的每个项目会导致难以阅读。前10报告仅保留最高或最低排名的项目，这正是排名报表所需的——例如“按收入排名前5的产品”或“按销售数量排名后3的地区”。Aspose.Cells 提供两种实现机制，它们对应 Microsoft Excel 的两个版本。
- **Excel 97-2003 AutoShow** — `PivotField.Top10AutoShow()` 方法。这是直接存储在数据透视字段上的经典“显示前/后 N 项”设置。它在所有 Excel 版本（旧版和新版）中均可使用，因为它属于原始数据透视表格式的一部分。
- **Excel 2007-365 Top 10 Filter** — `PivotField.FilterTop10()` 方法。这是位于字段菜单“值筛选”下的现代前10值筛选。它以附加在字段上的 `PivotFilter` 对象存储，并提供基于项目数量或百分比的排名。

## **Excel 97-2003 中的前10显示（Top10AutoShow）**
经典的自动显示通过一次调用 `PivotField.Top10AutoShow(isAutoShow bool, isTop bool, count int32, rankBy int32)` 来配置：
- `isAutoShow` — 启用或禁用字段上的自动显示设置。
- `isTop` — `true` 保留最高排名的项目（前），`false` 保留最低排名的项目（后）。
- `count` — 要保留的项目数量，例如经典的前10报告使用 10。
- `rankBy` — 用于对项目进行排名的 **数据字段** 的零基索引。传入 -1 表示按字段自身进行排名。
排名可以由数值字段或字段本身驱动。下面展示了两个常见变体。

### **按数值字段排名**
通过普通数值字段（例如“销售总额”）对行字段的项目进行排名。下面示例构建了一个包含行字段 (`Sport`) 和数据字段 (`Sales`) 的数据透视表，然后显示销售额最高的前 2 项运动。`rankBy` 为 0，因为 “销售总额” 是索引为 0 的数据字段。

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

### **按字段本身排名**
字段也可以按自身进行排名——将 `rankBy` 设为 -1。此变体不需要额外的数据字段；字段只需位于行（或列）区域。下面示例显示按字段自身排名的后 3 项运动。当此设置保存时，`rankBy` 属性会从数据透视表 XML 中省略，因为 -1 是该格式的默认值，`GetRankBy()` 会读取到 -1。

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

## **读取当前的自动显示选项**
`PivotField.GetTop10AutoShowSettings()` 方法返回一个 `PivotFieldTop10AutoShowSettings` 对象，公开字段当前存储的自动显示选项。可使用它检查现有工作簿或刚配置的数据透视表如何展示其项目——包括从文件加载的工作簿。

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

这些设置对应写入数据透视表 XML 的经典自动显示属性（`autoShow`、`topAutoShow`、`itemPageCount`、`rankBy`），因此读取回来的值是所有 Excel 版本都会遵循的值。

## **注意**

{{% alert color="primary" %}}
- 调用 `Top10AutoShow()` 后，再次调用 `PivotTable.CalculateData()` — 设置仅在下一次重新计算后于渲染布局中生效。
- 自动显示设置适用于行和列字段。仅位于页面（筛选）区域的字段无法通过此方式排名，因为其项目未在数据透视表主体中布局。
{{% /alert %}}

## **Excel 2007-365：前10筛选（FilterTop10）**
现代 Excel 版本在字段菜单的值筛选（Value Filters）中将前10作为一种数值筛选暴露。Aspose.Cells 使用 `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)` 方法对其建模，该方法返回创建的 `PivotFilter`：
- `valueFieldIndex` — 用于对项目进行排名的聚合值所在数据字段的零基索引。
- `type` — `itemCount` 的含义。`PivotFilterType.Count` 保留固定数量的项目（对话框的 Items 选项）。`PivotFilterType.Percent` 按百分比保留项目，因此 `itemCount` 本身就是百分比——30 表示保留前 30%。`PivotFilterType.Sum` 按累计值覆盖率排名。
- `isTop` — `true` 表示前（Top），`false` 表示后（Bottom）。
- `itemCount` — 前 N 中的 N；其单位取决于 `type`。

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
自动显示设置和 `FilterTop10` 是两个独立的功能。自动显示会在数据透视字段上写入经典的 `autoShow` 属性，并被所有自 Excel 97 起的 Excel 版本支持。`FilterTop10` 则写入现代的 `PivotFilter` 条目，需 Excel 2007 或更高版本才能使用。当工作簿在旧版 Excel 中打开时，使用现代筛选的数据透视表将回退为显示所有项目。对于必须在旧版工具之间往返的文档，建议使用 `Top10AutoShow`；对于现代工作簿，建议使用 `FilterTop10`，因为它能够与其他值筛选组合使用。
{{% /alert %}}

## **相关文档**
- [在数据透视表中分组透视字段](/cells/zh/go-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="go" >}}