---
title: 格式化数据透视表的部分
description: 在 Aspose.Cells for Node.js via C++ 中，通过 PivotTable.format 将样式应用于语义 PivotArea 区域或 CellArea 矩形，以格式化数据透视表的部分，格式存储在 PivotTable.getPivotFormats() 中，并在数据透视表刷新时保存。
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells, Node.js via C++, 数据透视表, 格式化, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, selectField, formatAll
type: docs
weight: 20
url: /zh/nodejs-cpp/format-part-of-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
`PivotTable.formatAll` 为整个数据透视表应用单一样式，相关内容已在父页面说明。它不会区分标签、数值、合计或报表的特定区域。
实际上，通常只需突出显示数据透视表的一部分。常见的目标包括属于某行字段的标签、某字段生成的数值单元格、总计行，或任意矩形区域（例如前两行项目）。
直接对数据透视表工作表单元格应用样式并不等同。Excel 将数据透视表的格式存储为语义 `PivotArea` 区域，而不是普通的单元格样式记录。`PivotArea` 格式会绑定到字段的标签或数据值等区域，并在数据透视表重新计算、刷新或展开时重新解析。相反，直接写入单元格的样式仅属于该单元格位置，数据透视表模型不会跟踪它。
Aspose.Cells 提供完整的 `PivotTable.format` 重载系列，使两种格式化方式均可使用：
- `format(PivotArea, Style)` 将样式锚定到通过 `PivotArea.select` 或 `PivotArea.selectField` 构建的语义区域。
- `format(CellArea, Style)` 将样式锚定到数据透视表内部的工作表矩形。
- `format(number row, number column, Style)` 目标为单个单元格。
- `formatAll(Style)` 为整个数据透视表设置格式。

## **格式化 Pivot 区域**
当需要使突出显示随字段或报表区域保持关联时，推荐使用语义区域工作流。
1. 使用 `new PivotArea(pivotTable)` 创建 `PivotArea`。该对象描述属于特定数据透视表的语义区域。  
2. 使用 `PivotArea.select(PivotFieldType axisType, number fieldPosition, PivotTableSelectionType selectionType)` 按给定轴上的零基位置选择字段。  
   - `PivotTableSelectionType.DataAndLabel` 同时选择字段的标签和数据。  
   - `PivotTableSelectionType.LabelOnly` 仅选择字段的标签。  
   - `PivotTableSelectionType.DataOnly` 仅选择字段的数据单元格。  
3. 使用 `PivotArea.selectField(PivotFieldType axisType, string fieldName)` 按名称选择字段。若按名称选中行字段，区域将解析为该字段项目生成的值单元格。  
4. 使用 `workbook.createStyle()` 创建 `Style`，配置字体、前景色和纯色背景图案，然后将该样式传递给 `pivotTable.format(area, style)`。  
5. 每次调用 `PivotArea` 重载都会向 `pivotTable.getPivotFormats()` 添加一个 `PivotTableFormat` 条目。  
6. 字段锚定的格式在计算数据后才会绘制。因此，在应用格式后请调用 `pivotTable.calculateData()`，使样式可见。
以下示例构建一个小型水果销售数据透视表，使用 `PivotArea.select` 与 `PivotTableSelectionType.LabelOnly` 为 `Fruit` 行标签设置样式，使用 `PivotArea.selectField` 为同一行字段生成的值单元格设置样式，随后重新计算数据透视表，使两种样式均被绘制。

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
// Fruit sales data
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
const labelStyle = workbook.createStyle();
labelStyle.getFont().setIsBold(true);
labelStyle.setForegroundColor(AsposeCells.Color.Yellow);
labelStyle.setPattern(AsposeCells.BackgroundType.Solid);
const labelArea = new AsposeCells.PivotArea(pivotTable);
labelArea.select(
    AsposeCells.PivotFieldType.Row,
    0,
    AsposeCells.PivotTableSelectionType.LabelOnly
);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
const valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(AsposeCells.Color.LightGreen);
valueStyle.setPattern(AsposeCells.BackgroundType.Solid);
const valueArea = new AsposeCells.PivotArea(pivotTable);
valueArea.selectField(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **格式化数据透视表的单元格区域**
当感兴趣的区域是普通的工作表矩形而非语义的透视区域时，使用 `PivotTable.format(CellArea, Style)`。
`CellArea` 通过其 `startRow`、`startColumn`、`endRow`、`endColumn` 属性描述。属性值为零基工作表坐标，结束坐标标识矩形中包含的最后一行和最后一列，因此区域覆盖从起始位置到结束位置（含）的所有单元格。
与字段锚定的格式不同，`CellArea` 格式会立即应用于单元格，无需再次调用 `pivotTable.calculateData()`。
`CellArea` 矩形可以同时包含标签单元格和数值单元格。下一节将说明 Aspose.Cells 与 Excel 在内部如何表示该矩形。
以下示例为数据透视表的矩形 `E4:F5` 应用斜体、浅蓝色样式，并在无需进一步重新计算的情况下保存工作簿。

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setIsItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.LightBlue);
highlightStyle.setPattern(AsposeCells.BackgroundType.Solid);
const rectangle = new AsposeCells.CellArea();
rectangle.startRow = 3;
rectangle.startColumn = 4;
rectangle.endRow = 4;
rectangle.endColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Pivot 区域与 Cell 区域的映射关系**
Excel 将数据透视表格式存储为 `pivotArea` 记录，而非普通工作表单元格样式记录。Aspose.Cells 采用相同模型，因而格式化请求在记录时会转换为透视区域。
用户提供的 `CellArea` 与内部存储的透视区域之间是多对多的关系：
- 一个 `CellArea` 可能生成多个透视区域。如果矩形同时包含标签单元格和数值单元格，它会被分解为独立的标签规则和数据规则，因为透视模型会分别处理标签格式和数据格式。  
- 一个透视区域可能解析为多个不相连的 `CellArea` 实例。诸如总计行或项目不连续的字段等语义区域可能覆盖多个矩形。这就是 `PivotArea.getCellAreas()` 返回集合而非单一矩形的原因。
通过 `pivotTable.format()` 执行的每一次格式化操作都会记录在 `pivotTable.getPivotFormats()` 中。每个 `PivotTableFormat` 条目公开其关联的 `PivotArea` 与所应用的 `Style`。`PivotArea` 重载每次调用仅添加一个条目，而包含不同语义区域的 `CellArea` 可能会添加多个条目。
为区分存储的区域，每个 `PivotArea` 公开 `getOnlyLabel()` 与 `getOnlyData()` 标志。下面的示例格式化一个同时覆盖标签和数值的单一矩形，检查 `pivotTable.getPivotFormats()`，并打印每个存储的透视区域解析得到的 `CellArea` 坐标。

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setIsItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.LightBlue);
highlightStyle.setPattern(AsposeCells.BackgroundType.Solid);
// ONE rectangle in...
const rectangle = new AsposeCells.CellArea();
rectangle.startRow = 3;
rectangle.startColumn = 4;
rectangle.endRow = 4;
rectangle.endColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
console.log("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (let i = 0; i < pivotTable.getPivotFormats().getCount(); i++) {
    const storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    console.log(
        `Format ${i}: OnlyLabel=${storedArea.getOnlyLabel()}, OnlyData=${storedArea.getOnlyData()}`
    );
    const resolvedAreas = storedArea.getCellAreas();
    for (const resolved of resolvedAreas) {
        console.log(
            `    rows ${resolved.startRow + 1}-${resolved.endRow + 1}, ` +
            `columns ${resolved.startColumn + 1}-${resolved.endColumn + 1}`
        );
    }
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=true, OnlyData=false
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=false, OnlyData=true
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
由于格式以透视区域而非普通单元格样式存储，它们在重新计算和刷新后仍然有效。当使用 `pivotTable.refreshData()` 刷新数据透视表，或使用 `pivotTable.calculateData()` 重新计算，亦或保存后重新加载时，每个存储的透视区域都会重新解析到其当前所在位置并重新应用样式。
{{% /alert %}}

在需要使突出显示随字段或语义区域在刷新后保持关联时，请使用 `select` 或 `selectField` 构建的 `PivotArea`；在仅需对当前数据透视表布局中的固定矩形进行格式化时，请使用 `CellArea`。单元格重载 `format(number row, number column, Style)` 用于定位单个单元格。若需一次性重新设置整个数据透视表的样式，请使用父页面中介绍的 `formatAll`。

## **相关文档**
- [将样式应用于数据透视表](/cells/zh/nodejs-cpp/apply-style-to-pivot-table/)
- [添加数据透视表的行和列字段](/cells/zh/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [管理数据透视表中的数值字段](/cells/zh/nodejs-cpp/manage-value-fields/)
- [刷新数据透视表](/cells/zh/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}