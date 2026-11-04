---
title: 格式化数据透视表的部分
linktitle: 格式化数据透视表的部分
description: 在 Aspose.Cells for Java 中，通过 PivotTable.format 将样式应用于语义的 PivotArea 区域或 CellArea 矩形，以格式化数据透视表的部分；格式会存储在 PivotTable.getPivotFormats 中，并在数据透视表刷新时保持不变。
keywords: Aspose.Cells for Java, 数据透视表, 格式化, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Java
type: docs
weight: 20
url: /zh/java/format-part-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
`PivotTable.formatAll` 为整个数据透视表应用单一样式，相关内容已在父页面中说明。它不会区分标签、数值、合计或报告中的特定区域。  
在实际使用中，通常只需要突出显示数据透视表的某一部分。常见的目标包括属于某个行字段的标签、某个字段生成的数值单元格、总计行，或诸如前两行项目之类的任意矩形。  
直接对数据透视表所在工作表的单元格应用样式并非等价操作。Excel 将数据透视表的格式保存为语义的 `PivotArea` 区域，而不是普通的单元格样式记录。`PivotArea` 格式会附着在字段的标签或数据值等区域上，并在数据透视表重新计算、刷新或展开时重新解析。相反，直接写入单元格的样式仅属于该单元格位置，数据透视模型并不会追踪它。  
Aspose.Cells 提供完整的 `PivotTable.format` 重载族，使两种格式化方式均可使用：
- `format(PivotArea, Style)` 将样式锚定到使用 `PivotArea.select` 或 `PivotArea.selectField` 构建的语义区域。
- `format(CellArea, Style)` 将样式锚定到数据透视表内部的工作表矩形。
- `format(int row, int column, Style)` 目标为单个单元格。
- `formatAll(Style)` 为整个数据透视表格式化。

## **格式化 Pivot 区域**
当需要让高亮随字段或报告区域保持同步时，推荐使用语义区域工作流。
1. 使用 `new PivotArea(pivotTable)` 创建 `PivotArea`。该对象描述属于特定数据透视表的语义区域。  
2. 通过 `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)` 按零基位置在给定轴上选择字段。  
   - `PivotTableSelectionType.DATA_AND_LABEL` 选择字段的标签和数据。  
   - `PivotTableSelectionType.LABEL_ONLY` 仅选择字段的标签。  
   - `PivotTableSelectionType.DATA_ONLY` 仅选择字段的数据单元格。  
3. 使用 `PivotArea.selectField(PivotFieldType axisType, String fieldName)` 按名称选择字段。当按名称选择行字段时，区域会解析为该字段项生成的数值单元格。  
4. 通过 `Workbook.createStyle()` 创建 `Style`，配置字体、前景色以及实线填充模式，然后将该样式传递给 `PivotTable.format(area, style)`。  
5. 每次调用 `PivotArea` 重载都会向 `PivotTable.getPivotFormats()` 添加一个 `PivotTableFormat` 条目。  
6. 字段锚定的格式会在数据透视计算时绘制。因此，在应用格式后需调用 `PivotTable.calculateData()`，使样式可见。  
以下示例构建了一个小型水果销售数据透视表，使用 `PivotArea.select` 与 `PivotTableSelectionType.LABEL_ONLY` 为 `Fruit` 行标签着色，使用 `PivotArea.selectField` 为同一行字段生成的数值单元格着色，随后重新计算数据透视表，使两种样式都被绘制。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Fruit sales data
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
Style labelStyle = workbook.createStyle();
labelStyle.getFont().setBold(true);
labelStyle.setForegroundColor(Color.getYellow());
labelStyle.setPattern(BackgroundType.SOLID);
PivotArea labelArea = new PivotArea(pivotTable);
labelArea.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
Style valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(Color.getLightGreen());
valueStyle.setPattern(BackgroundType.SOLID);
PivotArea valueArea = new PivotArea(pivotTable);
valueArea.selectField(PivotFieldType.ROW, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **格式化数据透视表的 Cell 区域**
当感兴趣的区域是普通工作表矩形而非语义的透视区域时，可使用 `PivotTable.format(CellArea, Style)`。  
`CellArea` 由 `getStartRow()`、`getStartColumn()`、`getEndRow()`、`getEndColumn()` 属性描述。属性值为零基工作表坐标，结束坐标指示矩形中包含的最后一行和最后一列，因此该区域覆盖从起始位置到结束位置（含）的所有单元格。  
与字段锚定的格式不同，`CellArea` 格式会立即作用于单元格，无需再次调用 `calculateData()`。  
`CellArea` 矩形可以同时包含标签单元格和数值单元格。下一节将说明 Aspose.Cells 与 Excel 如何在内部表示该矩形。  
以下示例将数据透视表的矩形 `E4:F5` 使用斜体、浅蓝样式进行格式化，并在不再重新计算的情况下保存工作簿。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
Style highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(BackgroundType.SOLID);
CellArea rectangle = new CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Pivot 区域与 Cell 区域的映射方式**
Excel 将数据透视表的格式存储为 `pivotArea` 记录，而非普通工作表单元格样式记录。Aspose.Cells 使用相同的模型，因此格式请求在记录时会被转换为透视区域。  
用户提供的 `CellArea` 与内部存储的 Pivot 区域之间是多对多的关系：
- 一个 `CellArea` 可能生成多个 Pivot 区域。如果矩形同时包含标签单元格和数值单元格，它会被拆分为独立的标签规则和数据规则，因为透视模型对标签格式和数据格式是独立处理的。  
- 一个 Pivot 区域可能对应多个不相连的 `CellArea` 实例。比如总计行或项不连续的字段，会覆盖多个矩形。这也是 `PivotArea.getCellAreas()` 返回集合而非单个矩形的原因。  
通过 `PivotTable.format` 执行的每一次格式化操作都会记录在 `PivotTable.getPivotFormats()` 中。每个 `PivotTableFormat` 条目公开其关联的 `PivotArea` 与所应用的 `Style`。`PivotArea` 重载每次调用只会添加一条记录，而包含不同语义区域的 `CellArea` 可能会添加多条记录。  
为区分已存储的区域，每个 `PivotArea` 暴露 `getOnlyLabel()` 与 `getOnlyData()` 标志。下面的示例对同时覆盖标签和数值的单个矩形进行格式化，检查 `PivotTable.getPivotFormats()`，并打印每个存储的 Pivot 区域所解析的 `CellArea` 坐标。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
Style highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(BackgroundType.SOLID);
// ONE rectangle in...
CellArea rectangle = new CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
System.out.println("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (int i = 0; i < pivotTable.getPivotFormats().getCount(); i++)
{
    PivotArea storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    System.out.println("Format " + i + ": OnlyLabel=" + storedArea.getOnlyLabel()
            + ", OnlyData=" + storedArea.getOnlyData());
    for (CellArea resolved : storedArea.getCellAreas())
    {
        System.out.println("    rows " + (resolved.StartRow + 1) + "-" + (resolved.EndRow + 1)
                + ", columns " + (resolved.StartColumn + 1) + "-" + (resolved.EndColumn + 1));
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
由于格式以 Pivot 区域而非普通单元格样式的形式存储，它们能够在重新计算和刷新后仍然保持。当使用 `PivotTable.refreshData` 刷新数据透视表、通过 `calculateData` 重新计算，或保存后重新加载时，每个存储的 Pivot 区域都会重新解析到当前所在位置，并重新应用其样式。
{{% /alert %}}

在需要让高亮随字段或语义区域在刷新后保持的情况下，使用 `select` 或 `selectField` 构建的 `PivotArea`；在仅需对当前布局中的固定矩形进行格式化时，使用 `CellArea`。`format(int row, int column, Style)` 重载针对单个单元格。若需一次性重新样式化整个数据透视表，请使用父页面中介绍的 `formatAll`。

## **相关文章**
- [将样式应用到数据透视表](/cells/zh/java/apply-style-to-pivot-table/)
- [添加数据透视表的行和列字段](/cells/zh/java/pivot-table-add-row-and-column-fields/)
- [管理数据透视表中的值字段](/cells/zh/java/manage-value-fields/)
- [刷新数据透视表](/cells/zh/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}