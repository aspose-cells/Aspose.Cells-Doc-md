---
title: 格式化数据透视表的部分
description: 通过 PivotTable.format 将样式应用于语义 PivotArea 区域或 CellArea 矩形，以格式化 Aspose.Cells for Node.js via Java 中的数据透视表的部分，格式存储在 PivotTable.getPivotFormats() 中，并在数据透视表刷新时得以保留。
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells for Node.js via Java, 数据透视表, 格式化, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Node.js via Java
type: docs
weight: 20
url: /zh/nodejs-java/format-part-of-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
`PivotTable.formatAll` 为整个数据透视表应用单一样式，相关说明请参阅父页面。它不会区分标签、数值、合计或报表的特定区域。
在实际使用中，通常只需要突出显示数据透视表的某一部分。常见的目标包括某一行字段的标签、某一字段产生的数值单元格、总计行，或诸如前两行项目这样的任意矩形。
直接对数据透视表所在工作表的单元格应用样式并不等同。Excel 将数据透视表的格式存储为语义 `PivotArea` 区域，而不是普通的单元格样式记录。`PivotArea` 格式会附着在字段的标签或数据值等区域上，并在数据透视表重新计算、刷新或展开时重新解析。而直接写入单元格的样式则只属于该单元格位置，数据透视模型不会追踪它。
Aspose.Cells 提供完整的 `PivotTable.format` 重载族，支持两种格式化方式：
- `format(PivotArea, Style)` 将样式锚定到使用 `PivotArea.select` 或 `PivotArea.selectField` 构建的语义区域。
- `format(CellArea, Style)` 将样式锚定到数据透视表内部的工作表矩形。
- `format(int row, int column, Style)` 目标为单个单元格。
- `formatAll(Style)` 格式化整个数据透视表。

## **格式化 Pivot 区域**
当需要让高亮随字段或报表区域保持关联时，推荐使用语义区域工作流。
1. 使用 `new PivotArea(pivotTable)` 创建 `PivotArea`。该对象描述了属于该特定数据透视表的语义区域。
2. 使用 `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)` 按给定轴上字段的零基位置选择字段。
   - `PivotTableSelectionType.DATA_AND_LABEL` 同时选择该字段的标签和数据。
   - `PivotTableSelectionType.LABEL_ONLY` 仅选择字段的标签。
   - `PivotTableSelectionType.DATA_ONLY` 仅选择字段的数据单元格。
3. 使用 `PivotArea.selectField(PivotFieldType axisType, string fieldName)` 按名称选择字段。当按名称选择行字段时，区域解析为该字段项产生的数值单元格。
4. 使用 `Workbook.createStyle()` 创建 `Style`，配置其字体、前景色和实线填充模式，然后将该样式传递给 `PivotTable.format(area, style)`。
5. 每次调用 `PivotArea` 重载都会向 `PivotTable.getPivotFormats()` 添加一个 `PivotTableFormat` 条目。
6. 字段锚定的格式在计算数据时绘制。因此，在应用格式后调用 `PivotTable.calculateData()`，使样式可见。
以下示例创建一个小型水果销售数据透视表，使用 `PivotArea.select` 与 `PivotTableSelectionType.LABEL_ONLY` 为 `Fruit` 行标签设置样式，使用 `PivotArea.selectField` 为同一行字段产生的数值单元格设置样式，然后重新计算数据透视表，使两种样式均被绘制。

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
const labelStyle = workbook.createStyle();
labelStyle.getFont().setBold(true);
labelStyle.setForegroundColor(AsposeCells.Color.getYellow());
labelStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const labelArea = new AsposeCells.PivotArea(pivotTable);
labelArea.select(
    AsposeCells.PivotFieldType.ROW,
    0,
    AsposeCells.PivotTableSelectionType.LABEL_ONLY
);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
const valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(AsposeCells.Color.getLightGreen());
valueStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const valueArea = new AsposeCells.PivotArea(pivotTable);
valueArea.selectField(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **格式化数据透视表的单元格区域**
当感兴趣的区域是普通工作表矩形而非语义数据透视区域时，使用 `PivotTable.format(CellArea, Style)`。
`CellArea` 通过公共字段 `StartRow`、`StartColumn`、`EndRow`、`EndColumn` 描述。这些值为零基工作表坐标，结束坐标标识矩形中包含的最后一行和最后一列，因此该区域覆盖从起始位置到结束位置（含）的所有单元格。
不同于字段锚定的格式，`CellArea` 格式会立即应用到单元格，无需再次调用 `calculateData()`。
`CellArea` 矩形可以同时包含标签单元格和数值单元格。下一节将说明 Aspose.Cells 与 Excel 如何在内部表示该矩形。
以下示例使用斜体、浅蓝色样式格式化数据透视表的矩形 `E4:F5`，并在不进行进一步重新计算的情况下保存工作簿。

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(
    AsposeCells.Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF)
);
highlightStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const rectangle = new AsposeCells.CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Pivot 区域和单元格区域的映射方式**
Excel 将数据透视表的格式存储为 `pivotArea` 记录，而不是普通工作表单元格样式记录。Aspose.Cells 使用相同的模型，将格式请求转换为内部的 pivot 区域进行记录。
用户提供的 `CellArea` 与内部存储的 pivot 区域之间的对应关系是多对多的：
- 一个 `CellArea` 可能产生多个 pivot 区域。如果矩形同时跨越标签单元格和数值单元格，则会被拆分为单独的标签规则和数据规则，因为数据透视模型独立处理标签格式和数据格式。
- 一个 pivot 区域可能解析为多个不相连的 `CellArea` 实例。诸如总计行或项不连续的字段等语义区域可覆盖多个矩形，这也是 `PivotArea.getCellAreas()` 返回集合而非单一矩形的原因。
通过 `PivotTable.format` 执行的每一次格式操作都会记录在 `PivotTable.getPivotFormats()` 中。每个 `PivotTableFormat` 条目公开关联的 `PivotArea` 与被应用的 `Style`。`PivotArea` 重载每次调用只添加一个条目，而包含不同语义区域的 `CellArea` 可能添加多个条目。
为了区分已存储的区域，每个 `PivotArea` 提供 `getOnlyLabel()` 和 `getOnlyData()` 标志。下面的示例格式化了一个同时覆盖标签和数值的矩形，检查 `PivotTable.getPivotFormats()`，并打印每个存储的 pivot 区域解析得到的 `CellArea` 坐标。

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(AsposeCells.BackgroundType.SOLID);
// ONE rectangle in...
const rectangle = new AsposeCells.CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
console.log("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (let i = 0; i < pivotTable.getPivotFormats().getCount(); i++) {
    const storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    console.log(
        `Format ${i}: OnlyLabel=${storedArea.getOnlyLabel()}, OnlyData=${storedArea.getOnlyData()}`
    );
    const resolvedAreas = storedArea.getCellAreas();
    for (let j = 0; j < resolvedAreas.length; j++) {
        const resolved = resolvedAreas[j];
        console.log(
            `    rows ${resolved.StartRow + 1}-${resolved.EndRow + 1}, columns ${resolved.StartColumn + 1}-${resolved.EndColumn + 1}`
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
由于格式存储为 pivot 区域而非普通单元格样式，它们在重新计算和刷新后依然有效。当使用 `PivotTable.refreshData()` 刷新数据透视表，或使用 `calculateData()` 重新计算，亦或保存后重新加载时，所有存储的 pivot 区域都会重新解析到其当前所在位置并重新应用样式。
{{% /alert %}}

在需要使高亮随字段或语义区域跨刷新保持关联时，请使用通过 `select` 或 `selectField` 构建的 `PivotArea`；在仅需对当前数据透视表布局中的固定矩形进行格式化时，使用 `CellArea`。单元格重载 `format(int row, int column, Style)` 用于定位单个单元格。若需一次性重新样式化整个数据透视表，请使用在父页面介绍的 `formatAll`。

## **相关文档**
- [将样式应用于数据透视表](/cells/zh/nodejs-java/apply-style-to-pivot-table/)
- [添加数据透视表行和列字段](/cells/zh/nodejs-java/pivot-table-add-row-and-column-fields/)
- [管理数据透视表中的值字段](/cells/zh/nodejs-java/manage-value-fields/)
- [刷新数据透视表](/cells/zh/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}