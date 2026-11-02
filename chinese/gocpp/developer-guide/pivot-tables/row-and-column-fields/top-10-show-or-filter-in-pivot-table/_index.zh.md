---
title: 数据透视表中的前 10 项显示或筛选
linktitle: 数据透视表中的前 10 项显示或筛选
description: 了解如何在 Aspose.Cells for Go via C++ 中仅显示数据透视字段中排名最高或最低的项目。本文介绍 Excel 97-2003 AutoShow 设置（SetIsAutoShow 等）、如何读回这些选项，以及如何通过 FilterTop10 实现 Excel 2007-365 前 10 项筛选。
keywords: Aspose.Cells, Go via C++, 数据透视表, 前 10 项, 自动显示, SetIsAutoShow, SetIsAscendShow, SetAutoShowCount, SetAutoShowField, FilterTop10, PivotFilterType, PivotField, Go
type: docs
weight: 20
url: /zh/go-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
如果行字段包含数十个成员，列出所有项目的数据透视表可能难以阅读。前 10 项报表仅保留排名最高或最低的项目，恰好满足排名报表的需要，例如“按收入排名前 5 的产品”或“按销售量排名后 3 的地区”。Aspose.Cells 支持两种机制，分别对应 Microsoft Excel 的两代版本。
- **Excel 97-2003 AutoShow** — `PivotField` 的四个设置方法 `SetIsAutoShow`、`SetIsAscendShow`、`SetAutoShowCount` 和 `SetAutoShowField`。这是在数据透视字段上直接存储的经典“显示前/后 N 项”设置。由于它是原始数据透视表格式的一部分，因此所有新旧 Excel 版本均支持此设置。
- **Excel 2007-365 前 10 项筛选** — `PivotField.FilterTop10()` 方法。这是字段菜单的“值筛选”下提供的现代前 10 项值筛选。它以附加到字段上的 `PivotFilter` 对象形式存储，并支持按项目数或百分比进行排名。

## **Excel 97-2003 中的前 10 项显示（AutoShow）**
经典 AutoShow 通过在 `PivotField` 上调用四个设置方法进行配置：
- `SetIsAutoShow(bool)` — 启用或禁用字段上的 AutoShow 设置。
- `SetIsAscendShow(bool)` — `false` 保留排名最高的项目（Top），`true` 保留排名最低的项目（Bottom）。
- `SetAutoShowCount(int32)` — 要保留的项目数量，例如经典前 10 项报表中可设为 10。
- `SetAutoShowField(int32)` — **数据字段**的从零开始索引，该字段的值用于对项目进行排名。传入 -1 时，按字段自身对项目进行排名。
排名既可由值字段驱动，也可由字段自身驱动。下面介绍两种常见变体。

### **按值字段排名**
可使用普通值字段（例如“求和项:Sales”）对行字段中的项目进行排名。以下示例创建一个数据透视表，其中包含一个行字段（`Sport`）和一个数据字段（`Sales`），然后显示按销售额排名前 2 的运动项目。`rankBy` 为 0，因为“求和项:Sales”是索引为 0 的数据字段。

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
	idx, _ := pivotTables.Add_String_String_String_Bool_Bool("A1:C16", "F3", "PivotTable1", true, false)
	pivotTable, _ := pivotTables.Get_Int(idx)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// 按“销售额汇总”显示排名前 2 的项目（数据字段索引为 0）
	sportField.SetIsAutoShow(true)
	sportField.SetIsAscendShow(false)
	sportField.SetAutoShowCount(int32(2))
	sportField.SetAutoShowField(int32(0))
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-value-field.xlsx")
}
```

### **按字段自身排名**
字段也可以按自身进行排名——只需向 `SetAutoShowField` 传入 -1。此变体无需额外的数据字段；该字段只需位于行（或列）区域。以下示例显示按字段自身进行排名后排名靠后的 3 个运动项目。保存此设置时，数据透视表 XML 中会省略 `rankBy` 属性，因为 -1 是该格式的默认值，而 `GetAutoShowField()` 会读回 -1。

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
	idx, _ := pivotTables.Add_String_String_String_Bool_Bool("A1:C16", "F3", "PivotTable1", true, false)
	pivotTable, _ := pivotTables.Get_Int(idx)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// 显示按字段本身排名靠后的 3 个项目（rankBy = -1）
	sportField.SetIsAutoShow(true)
	sportField.SetIsAscendShow(true)
	sportField.SetAutoShowCount(3)
	sportField.SetAutoShowField(-1)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-field-itself.xlsx")
}
```

## **读取当前 AutoShow 选项**
`PivotField` 的读取方法 `IsAutoShow()`、`IsAscendShow()`、`GetAutoShowCount()` 和 `GetAutoShowField()` 可用于获取当前存储在字段上的 AutoShow 选项。可使用这些方法检查现有工作簿或刚配置的数据透视表中字段的呈现方式，包括检查从文件加载的工作簿。

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

这四个选项对应于写入数据透视表 XML 的经典 AutoShow 属性（`autoShow`、`topAutoShow`、`itemPageCount`、`rankBy`），因此读回的值就是所有 Excel 版本都会采用的值。

## **注意**

{{% alert color="primary" %}}
- 更改任何 AutoShow 设置方法后，需再次调用 `PivotTable.CalculateData()`；这些设置仅会在下一次重新计算后应用到呈现的布局中。
- AutoShow 设置适用于行字段和列字段。仅位于页面（筛选）区域的字段无法通过此方式进行排名，因为其项目不会排列在数据透视表主体中。
{{% /alert %}}

## **Excel 2007-365：前 10 项筛选（FilterTop10）**
现代 Excel 版本在字段菜单中将前 10 项作为值筛选提供（“值筛选”、“前 10 项...”）。Aspose.Cells 使用 `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)` 方法表示此功能，该方法返回创建的 `PivotFilter`：
- `valueFieldIndex` — 数据字段的从零开始索引，该字段的汇总值用于对项目进行排名。
- `type` — `itemCount` 的含义。`PivotFilterType.Count` 保留固定数量的项目（对话框中的“项目数”选项）。`PivotFilterType.Percent` 保留项目的一定百分比，因此 `itemCount` 本身即为百分比；30 表示保留排名前 30% 的项目。`PivotFilterType.Sum` 根据累计值覆盖比例进行排名。
- `isTop` — `true` 表示保留排名靠前的项目，`false` 表示保留排名靠后的项目。
- `itemCount` — 前 N 项中的 N；其单位取决于 `type`。

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
	idx, _ := pivotTables.Add_String_String_String_Bool_Bool("A1:C16", "F3", "PivotTable1", true, false)
	pivotTable, _ := pivotTables.Get_Int(idx)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// 前 10 项筛选——按“Sales 汇总”保留前 2 个项目（数据字段索引 0）
	sportField.FilterTop10(0, PivotFilterType_Count, true, 2)
	// 若改用基于百分比的筛选，则保留前 30% 的项目：
	// sportField.FilterTop10(0, PivotFilterType_Percent, true, 30)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-filter.xlsx")
}
```

{{% alert color="primary" %}}
AutoShow 设置与 `FilterTop10` 是两个彼此独立的功能。AutoShow 会在数据透视字段上写入经典 `autoShow` 属性集，并受到从 Excel 97 到更高版本的所有 Excel 版本支持。`FilterTop10` 会写入现代 `PivotFilter` 条目，这要求使用 Excel 2007 或更高版本。在较旧 Excel 版本中打开工作簿时，使用现代筛选器的数据透视表会退回到显示所有项目。对于必须通过旧版工具链进行往返处理的文档，建议使用 AutoShow 设置方法；对于现代工作簿，建议使用 `FilterTop10`，因为它可与其他值筛选组合使用。
{{% /alert %}}

## **相关文章**
- [对数据透视表中的数据透视字段进行分组](/cells/zh/go-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="go" >}}