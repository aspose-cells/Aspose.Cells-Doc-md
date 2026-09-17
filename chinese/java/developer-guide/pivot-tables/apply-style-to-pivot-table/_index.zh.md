---
title: 在 Aspose.Cells for Java 中为数据透视表应用样式
linktitle: 在 Aspose.Cells for Java 中为数据透视表应用样式
description: 学习如何在 Aspose.Cells for Java 中为数据透视表应用内置和自定义样式，包括传统 XLS 自动格式、现代 Excel 2007+ 命名样式、自定义数据透视表样式以及 FormatAll 快捷方式。
keywords: Aspose.Cells Java 数据透视表样式, PivotTableStyleType, AutoFormatType, FormatAll, 自定义样式, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /zh/java/apply-style-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持同时应用传统的数据透视表自动格式（适用于 `.xls` 文件）和现代命名或自定义数据透视表样式（适用于 `.xlsx`、`.xlsm` 和 `.xlsb` 文件）。您应该调用的 API 取决于工作簿保存到的文件格式，而不是读取的格式。
{{% /alert %}}

## **简介**
Aspose.Cells 为数据透视表提供了两个并行的样式 API。它们之间的选择取决于工作簿保存到的文件格式，而不是读取的格式。从 `.xls` 文件加载的工作簿可以重新保存为 `.xlsx`，在这种情况下应用的是现代样式 API，而不是传统样式 API。
- `PivotTable.PivotTableStyleType` 从内置命名样式中选择一种（明色和暗色主题，包括 Excel 2017 中新增的样式）。这些预设是只读的。
- `PivotTable.PivotTableStyleName` 选择您通过 `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(...)` 自行定义的自定义样式。当您希望修改预设无法提供的颜色、边框或字体时，必须使用自定义样式。
此外，`PivotTable.formatAll(Style)` 是一个快捷方式，可将单个 `Style` 对象应用于数据透视表的每一个单元格，覆盖通过上述任一样式名称 API 设置的内容。当需要统一外观而不受底层主题影响时，此方法非常有用。

## **应用传统 XLS 预设自动格式**
`PivotTable.AutoFormatType` 接受来自 `com.aspose.cells.PivotTableAutoFormatType` 枚举的值。可用值为 `REPORT_1` 至 `REPORT_10`、`CLASSIC` 和 `TABLE_1` 至 `TABLE_10`。
下面的示例加载一个新工作簿，填充 Fruit/Year/Amount 示例数据，添加一个数据透视表，应用 `PivotTableAutoFormatType.REPORT_5`，并将结果保存为 `.xls`。

{{% alert color="primary" %}}
**为什么没有列字段？** Report 系列自动格式（`Report1` 至 `Report10`、`Table1` 至 `Table10`）是在经典 Excel 中为**单维数据透视表**（仅包含行字段和值）设计的，它们没有针对列字段标题的内置样式。如果您的数据透视表需要列字段，请改用[场景 2](#apply-a-modern-named-preset-pivot-table-style) 中的现代 `PivotTableStyleType` 预设，这些预设为现代 Excel 使用的二维布局而设计。
{{% /alert %}}

```java
import com.aspose.cells.*;
// 场景 1：应用旧版 XLS 预设自动格式
// 使用的 API：PivotTable.AutoFormatType
// 目标文件格式：.xls（旧版）
// 如需完整的示例和数据文件，请访问 https://github.com/aspose-cells/Aspose.Cells-for-.NET
// 创建新工作簿
Workbook workbook = new Workbook();
// 获取第一个工作表
Worksheet sheet = workbook.getWorksheets().get(0);
// 使用表头行（Fruit、Year、Amount）填充源数据
// 以及 9 行数据，涵盖 2020 年和 2021 年的葡萄、蓝莓、猕猴桃和樱桃
sheet.getCells().get(0, 0).putValue("Fruit");
sheet.getCells().get(0, 1).putValue("Year");
sheet.getCells().get(0, 2).putValue("Amount");
sheet.getCells().get(1, 0).putValue("grape");
sheet.getCells().get(1, 1).putValue(2020);
sheet.getCells().get(1, 2).putValue(50);
sheet.getCells().get(2, 0).putValue("blueberry");
sheet.getCells().get(2, 1).putValue(2020);
sheet.getCells().get(2, 2).putValue(30);
sheet.getCells().get(3, 0).putValue("kiwi");
sheet.getCells().get(3, 1).putValue(2020);
sheet.getCells().get(3, 2).putValue(25);
sheet.getCells().get(4, 0).putValue("cherry");
sheet.getCells().get(4, 1).putValue(2020);
sheet.getCells().get(4, 2).putValue(40);
sheet.getCells().get(5, 0).putValue("grape");
sheet.getCells().get(5, 1).putValue(2021);
sheet.getCells().get(5, 2).putValue(60);
sheet.getCells().get(6, 0).putValue("blueberry");
sheet.getCells().get(6, 1).putValue(2021);
sheet.getCells().get(6, 2).putValue(35);
sheet.getCells().get(7, 0).putValue("kiwi");
sheet.getCells().get(7, 1).putValue(2021);
sheet.getCells().get(7, 2).putValue(28);
sheet.getCells().get(8, 0).putValue("cherry");
sheet.getCells().get(8, 1).putValue(2021);
sheet.getCells().get(8, 2).putValue(45);
sheet.getCells().get(9, 0).putValue("grape");
sheet.getCells().get(9, 1).putValue(2020);
sheet.getCells().get(9, 2).putValue(45);
// 在目标单元格 E3 添加一个名为 "Pivot1" 的数据透视表，使用源数据区域 A1:C10
int pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);
// 分配字段：Fruit -> 行，Amount -> 数据
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// 应用旧版 XLS 预设自动格式 "Report5"
// 注意：此属性仅在另存为 .xls 时有效。
// 当另存为 .xlsx/.xlsm/.xlsb 时，Excel 会忽略 AutoFormatType
// 并使用 PivotTableStyleType / PivotTableStyleName 所指定的样式。
pivotTable.setAutoFormatType(PivotTableAutoFormatType.REPORT_5);
// 将工作簿保存为旧版 .xls 格式
workbook.save("output.xls");
```

## **应用现代命名预设数据透视表样式**

## **定义并应用自定义数据透视表样式**
无法修改内置预设。当您需要覆盖颜色、边框或字体时，必须定义自定义数据透视样式。工作流包含三个步骤：
1. 通过 `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)` 向工作簿的 `TableStyles` 集合添加自定义样式。这将返回新创建样式的索引。
2. 通过 `TableStyle.getTableStyleElements().add(TableStyleElementType)` 添加元素（例如 `WholeTable` 或 `GrandTotalRow`）来配置样式，然后通过 `TableStyleElement.setElementStyle(Style)` 为每个元素分配一个 `Style`。
3. 通过将 `PivotTable.PivotTableStyleName` 设置为样式名称，将自定义样式应用于数据透视表。此处不要使用 `PivotTableStyleType`，因为该属性用于选择内置预设。

{{% alert color="primary" %}}
`PivotTableStyleName` 和 `PivotTableStyleType` 不能互换使用。使用 `PivotTableStyleType` 选择内置预设，使用 `PivotTableStyleName` 选择通过 `addPivotTableStyle` 定义的自定义样式。同时设置两者不会产生错误，但只有与预期来源匹配的那一个会被渲染。
{{% /alert %}}

可用的 `TableStyleElementType` 值包括 `WHOLE_TABLE`、`FIRST_ROW`、`LAST_ROW`、`FIRST_COLUMN`、`LAST_COLUMN`、`GRAND_TOTAL_ROW`、`GRAND_TOTAL_COLUMN`、`PAGE_FIELD_LABELS` 和 `PAGE_FIELD_VALUES`。
下面的示例定义了一个自定义数据透视样式，其中 `WholeTable` 带有细黑色边框，`GrandTotalRow` 带有粗体红色字体，然后通过 `PivotTableStyleName` 应用它并保存为 `.xlsx`。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// 填充源数据：表头行 + 9 行数据（A1:C10）
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);
// 添加数据源为 A1:C10 的数据透视表，锚定在 E3，命名为 "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// 步骤 1：注册一个新的自定义数据透视表样式并获取其索引
int styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// 步骤 2：添加 WholeTable 元素并在四边应用细的黑色边框
int wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE);
TableStyleElement wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
Style wholeTableStyle = workbook.createStyle();
BorderCollection borders = wholeTableStyle.getBorders();
Border borderTop = borders.getByBorderType(BorderType.TOP_BORDER);
borderTop.setLineStyle(CellBorderType.THIN);
borderTop.setColor(Color.getBlack());
Border borderBottom = borders.getByBorderType(BorderType.BOTTOM_BORDER);
borderBottom.setLineStyle(CellBorderType.THIN);
borderBottom.setColor(Color.getBlack());
Border borderLeft = borders.getByBorderType(BorderType.LEFT_BORDER);
borderLeft.setLineStyle(CellBorderType.THIN);
borderLeft.setColor(Color.getBlack());
Border borderRight = borders.getByBorderType(BorderType.RIGHT_BORDER);
borderRight.setLineStyle(CellBorderType.THIN);
borderRight.setColor(Color.getBlack());
wholeTableElement.setElementStyle(wholeTableStyle);
// 步骤 3：添加 GrandTotalRow 元素并应用粗体红色字体
int grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW);
TableStyleElement grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
Style grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(Color.getRed());
grandTotalElement.setElementStyle(grandTotalStyle);
// 步骤 4：通过名称应用自定义样式（不要使用 PivotTableStyleType，它用于内置预设样式）
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **使用 FormatAll 将单个样式应用于数据透视表的每个单元格**
`PivotTable.formatAll(Style)` 是一个快捷方式，可将单个 `Style` 对象应用于数据透视表的每一个单元格，包括数据区域、行和列标题以及总计。通过 `PivotTableStyleType` 或 `PivotTableStyleName` 之前设置的任何内容都会被覆盖。

{{% alert color="primary" %}}
`FormatAll` 会覆盖 `PivotTableStyleType` 和 `PivotTableStyleName`。仅当需要在整个数据透视表中使用统一的、与主题无关的外观时才使用它。
{{% /alert %}}

下面的示例创建了一个具有黄色实心填充、粗体深蓝色字体以及所有边上细黑色边框的 `Style`，然后使用 `formatAll` 应用它并保存为 `.xlsx`。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// 填充源数据：表头行（第 1 行）+ 9 行数据（第 2-10 行）
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(5000);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(3000);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(4000);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(2000);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(6000);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(3500);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(4500);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(2500);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(5500);
// 添加数据透视表：源数据范围 A1:C10，目标单元格 E3，名称 "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// 分配透视字段：Fruit -> 行区域，Year -> 列区域，Amount -> 数据区域
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// 创建一个将强制应用于透视表每个单元格的样式
Style style = workbook.createStyle();
style.setForegroundColor(Color.getYellow());
style.setPattern(BackgroundType.SOLID);
style.getFont().setBold(true);
style.getFont().setColor(Color.getDarkBlue());
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack());
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack());
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack());
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack());
// 应用 FormatAll：将此单一样式强制应用于透视表的每个单元格，
// 覆盖先前设置的任何 PivotTableStyleType / PivotTableStyleName
pivotTable.formatAll(style);
// 以现代 .xlsx 格式保存工作簿
workbook.save("output.xlsx");
```

## **我应该使用哪个样式 API？**
样式 API 的选择取决于您要保存到的文件格式。请参考下表快速查询。
| 目标文件格式 | 要使用的 API | 备注 |
|---|---|---|
| `.xls`（传统） | `PivotTable.AutoFormatType` | 取值来自 `com.aspose.cells.PivotTableAutoFormatType`（例如 `REPORT_1`–`REPORT_10`、`CLASSIC`、`TABLE_1`–`TABLE_10`）。保存为现代格式时将被忽略。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代，内置样式） | `PivotTable.PivotTableStyleType` | 取值来自 `com.aspose.cells.PivotTableStyleType`（明色/暗色主题，包括 Excel 2017 新增内容）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代，自定义样式） | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.addPivotTableStyle(...)` | 当内置预设不够用时使用。通过 `TableStyleElement.setElementStyle(...)` 进行配置。 |
| 任何格式（统一覆盖） | `PivotTable.formatAll(Style)` | 快捷方式，覆盖整个数据透视表上的所有其他样式设置。 |
如有疑问，请保存为 `.xlsx` 并使用 `PivotTableStyleType` 选择内置主题，或使用 `PivotTableStyleName` 选择自定义主题。

{{< app/cells/assistant language="java" >}}