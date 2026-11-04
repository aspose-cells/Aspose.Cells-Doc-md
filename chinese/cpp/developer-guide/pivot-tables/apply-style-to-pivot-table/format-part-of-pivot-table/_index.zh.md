---
title: 格式化数据透视表的部分
linktitle: 格式化数据透视表的部分
description: 通过使用 PivotTable.Format 将样式应用于语义 PivotArea 区域或 CellArea 矩形来格式化 Aspose.Cells for C++ 中的数据透视表的部分，格式存储在 PivotTable.GetPivotFormats 中，并在数据透视表刷新时保留。
keywords: Aspose.Cells, 数据透视表, 格式, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C++
type: docs
weight: 20
url: /zh/cpp/format-part-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
`PivotTable.FormatAll` 为整个数据透视表应用单一样式，相关内容已在父页面中说明。它不会区分标签、数值、合计或报告的特定区域。
实际工作中，通常只需要突出显示数据透视表的某一部分。常见的目标包括某个行字段的标签、某个字段产生的数值单元格、总计行，或任意矩形（如前两行项目）。
直接对数据透视表所在工作表的单元格应用样式并不等价。Excel 将数据透视表的格式存储为语义 `PivotArea` 区域，而不是普通的单元格样式记录。`PivotArea` 格式会绑定到诸如字段标签或数据值等区域，并在数据透视表重新计算、刷新或展开时重新解析。相反，直接写入单元格的样式属于该单元格位置，数据透视表模型不会跟踪它。
Aspose.Cells 暴露了完整的 `PivotTable.Format` 重载系列，提供两种格式化方式：
- `Format(const PivotArea&, const Style&)` 将样式锚定到使用 `PivotArea.Select` 或 `PivotArea.SelectField` 构建的语义区域。
- `Format(const CellArea&, const Style&)` 将样式锚定到数据透视表内部的工作表矩形。
- `Format(int32_t row, int32_t column, const Style&)` 作用于单个单元格。
- `FormatAll(const Style&)` 为整个数据透视表设定格式。

## **格式化 Pivot 区域**
当需要使高亮随字段或报告区域保持一致时，推荐使用语义区域工作流。
1. 使用 `PivotArea pivotArea(pivotTable);` 创建 `PivotArea`。该对象描述属于特定数据透视表的语义区域。  
2. 使用 `PivotArea.Select(PivotFieldType axisType, int32_t fieldPosition, PivotTableSelectionType selectionType)` 按零基位置在指定轴上选择字段。  
   - `PivotTableSelectionType::DataAndLabel` 同时选择字段的标签和数据。  
   - `PivotTableSelectionType::LabelOnly` 只选择字段的标签。  
   - `PivotTableSelectionType::DataOnly` 只选择字段的数据单元格。  
3. 使用 `PivotArea.SelectField(PivotFieldType axisType, const char16_t* fieldName)` 按名称选择字段。若按名称选择行字段，区域将解析为该字段项产生的数值单元格。  
4. 使用 `Workbook.CreateStyle()` 创建 `Style`，配置字体、前景色和实线填充模式，并将该样式传递给 `PivotTable.Format(pivotArea, style)`。  
5. 每次调用 `PivotArea` 重载都会向 `PivotTable.GetPivotFormats()` 添加一个 `PivotTableFormat` 条目。  
6. 字段锚定的格式在数据透视表计算完成后才会绘制。因此，在应用格式后请调用 `PivotTable.CalculateData()` 使样式可见。  
下面的示例构建了一个小型水果销售数据透视表，使用 `PivotArea.Select` 和 `PivotTableSelectionType::LabelOnly` 为 `Fruit` 行标签设定样式，使用 `PivotArea.SelectField` 为同一行字段产生的数值单元格设定样式，随后重新计算数据透视表，使两种样式都被绘制。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Fruit sales data
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    // Pivot table with its top-left corner at E3
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Bold yellow fill on the row field's label cells
    Style labelStyle = workbook.CreateStyle();
    labelStyle.GetFont().SetIsBold(true);
    labelStyle.SetForegroundColor(Color::Yellow());
    labelStyle.SetPattern(BackgroundType::Solid);
    PivotArea labelArea(pivotTable);
    labelArea.Select(PivotFieldType::Row, 0, PivotTableSelectionType::LabelOnly);
    pivotTable.Format(labelArea, labelStyle);
    // Light green fill on the value cells the row field produces
    Style valueStyle = workbook.CreateStyle();
    valueStyle.SetForegroundColor(Color::LightGreen());
    valueStyle.SetPattern(BackgroundType::Solid);
    PivotArea valueArea(pivotTable);
    valueArea.SelectField(PivotFieldType::Row, u"Fruit");
    pivotTable.Format(valueArea, valueStyle);
    // Field-anchored formats are painted when the data is calculated
    pivotTable.CalculateData();
    // Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
    workbook.Save(u"FormatPivotArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **格式化数据透视表的单元格区域**
当感兴趣的区域是普通的工作表矩形而非语义 Pivot 区域时，使用 `PivotTable.Format(const CellArea&, const Style&)`。
`CellArea` 由公共字段 `StartRow`、`StartColumn`、`EndRow`、`EndColumn` 描述。这些值为零基工作表坐标，结束坐标标识矩形中包含的最后一行和最后一列，因此该区域覆盖从起始位置到结束位置（含）的所有单元格。
与字段锚定的格式不同，`CellArea` 格式会立即应用到单元格，无需再次调用 `CalculateData()`。
`CellArea` 矩形可能同时包含标签单元格和数值单元格。下一节将说明 Aspose.Cells 与 Excel 在内部如何表示该矩形。
下面的示例将数据透视表中矩形 `E4:F5` 设为斜体、浅蓝色样式，并在不进行进一步重新计算的情况下保存工作簿。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Highlight the first two fruit rows (the rectangle E4:F5)
    Style highlightStyle = workbook.CreateStyle();
    highlightStyle.GetFont().SetIsItalic(true);
    highlightStyle.SetForegroundColor(Color{ 0xFF, 0x99, 0xCC, 0xFF });
    highlightStyle.SetPattern(BackgroundType::Solid);
    CellArea rectangle;
    rectangle.StartRow = 3;
    rectangle.StartColumn = 4;
    rectangle.EndRow = 4;
    rectangle.EndColumn = 5;
    pivotTable.Format(rectangle, highlightStyle);
    // E4:F5 is italic on light blue immediately, no recalculation needed
    workbook.Save(u"FormatPivotCellArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Pivot 区域和单元格区域的映射方式**
Excel 将数据透视表的格式存储为 `pivotArea` 记录，而非普通工作表单元格样式记录。Aspose.Cells 采用相同模型，因此格式请求会在记录时转换为 Pivot 区域。
用户提供的 `CellArea` 与内部存储的 Pivot 区域之间是多对多的关系：
- 一个 `CellArea` 可能生成多个 Pivot 区域。如果矩形同时包含标签单元格和数值单元格，系统会将其拆分为独立的标签规则和数据规则，因为 Pivot 模型分别处理标签格式和数据格式。  
- 一个 Pivot 区域可能映射到多个不相连的 `CellArea` 实例。诸如总计行或项不连续的字段等语义区域可以覆盖多个矩形，这也是 `PivotArea.GetCellAreas()` 返回 `Vector<CellArea>` 而非单一矩形的原因。  
通过 `PivotTable.Format` 执行的每一次格式操作都会记录在 `PivotTable.GetPivotFormats()` 中。每个 `PivotTableFormat` 条目公开关联的 `PivotArea` 与所应用的 `Style`。`PivotArea` 重载每次调用仅添加一个条目，而包含不同语义区域的 `CellArea` 可能会产生多个条目。
为区分已存储的区域，每个 `PivotArea` 提供 `GetOnlyLabel()` 和 `GetOnlyData()` 标志。下面的示例格式化了一个同时覆盖标签和数值的单一矩形，检查 `PivotTable.GetPivotFormats()`，并打印每个已存储的 Pivot 区域解析后的 `CellArea` 坐标。

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    Style highlightStyle = workbook.CreateStyle();
    highlightStyle.GetFont().SetIsItalic(true);
    highlightStyle.SetForegroundColor(Color{ 0xFF, 0x99, 0xCC, 0xFF });
    highlightStyle.SetPattern(BackgroundType::Solid);
    // ONE rectangle in...
    CellArea rectangle;
    rectangle.StartRow = 3;
    rectangle.StartColumn = 4;
    rectangle.EndRow = 4;
    rectangle.EndColumn = 5;
    pivotTable.Format(rectangle, highlightStyle);
    // ...TWO semantic pivot areas out: the label part and the data part are stored separately
    std::cout << "Stored formats: " << pivotTable.GetPivotFormats().GetCount() << std::endl;
    for (int i = 0; i < pivotTable.GetPivotFormats().GetCount(); i++)
    {
        PivotArea storedArea = pivotTable.GetPivotFormats().Get(i).GetPivotArea();
        std::cout << "Format " << i << ": OnlyLabel=" << (storedArea.GetOnlyLabel() ? "true" : "false")
                  << ", OnlyData=" << (storedArea.GetOnlyData() ? "true" : "false") << std::endl;
        Vector<CellArea> resolved = storedArea.GetCellAreas();
        for (int j = 0; j < resolved.GetLength(); j++)
        {
            std::cout << "    rows " << (resolved[j].StartRow + 1) << "-" << (resolved[j].EndRow + 1)
                      << ", columns " << (resolved[j].StartColumn + 1) << "-" << (resolved[j].EndColumn + 1) << std::endl;
        }
    }
    // This prints:
    // Stored formats: 2
    // Format 0: OnlyLabel=true, OnlyData=false
    //     rows 4-5, columns 5-5        (E4:E5, the label part)
    // Format 1: OnlyLabel=false, OnlyData=true
    //     rows 4-5, columns 6-6        (F4:F5, the data part)
    workbook.Save(u"FormatPivotAreasMap.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}
由于格式存储为 Pivot 区域而非普通单元格样式，它们能够在重新计算和刷新后仍然保留。无论是使用 `PivotTable.RefreshData` 刷新数据透视表、使用 `CalculateData` 重新计算，还是保存后重新加载，所有已存储的 Pivot 区域都会重新解析到其当前所在位置并重新应用样式。
{{% /alert %}}

在需要使高亮随字段或语义区域在刷新后保持关联时，使用 `Select` 或 `SelectField` 构建的 `PivotArea`；在仅需对当前数据透视表布局中的固定矩形进行格式化时，使用 `CellArea`。单元格级别的 `Format(int32_t row, int32_t column, const Style&)` 重载用于定位单个单元格。若希望一次性重新样式化整个数据透视表，请使用父页面中介绍的 `FormatAll`。

## **相关文章**
- [将样式应用于数据透视表](/cells/zh/cpp/apply-style-to-pivot-table/)
- [添加数据透视表的行列字段](/cells/zh/cpp/pivot-table-add-row-and-column-fields/)
- [管理数据透视表中的值字段](/cells/zh/cpp/manage-value-fields/)
- [刷新数据透视表](/cells/zh/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}