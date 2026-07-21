---
title: 将样式应用于数据透视表
linktitle: 将样式应用于数据透视表
description: 学习如何在 Aspose.Cells for Java 中对数据透视表应用内置和自定义样式，涵盖旧版 XLS 自动格式、现代 Excel 2007+ 命名样式、自定义数据透视表样式以及 FormatAll 快捷方式。
keywords: Aspose.Cells Java 数据透视表样式, PivotTableStyleType, AutoFormatType, FormatAll, 自定义样式, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /zh/java/apply-style-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持对旧版数据透视表自动格式（适用于 `.xls` 文件）和现代命名或自定义数据透视表样式（适用于 `.xlsx`、`.xlsm` 和 `.xlsb` 文件）进行应用。应调用的 API 取决于工作簿**保存到的**文件格式，而不是**读取自的**文件格式。

{{% /alert %}}

## **简介**

Aspose.Cells 为数据透视表提供了两套并行的样式 API。它们之间的选择由工作簿保存到的文件格式决定，而不是由读取的文件格式决定。从 `.xls` 文件加载的工作簿可以重新保存为 `.xlsx`，在这种情况下，应使用现代样式 API，而不是旧版 API。

对于旧版 `.xls` 输出，请使用 `PivotTable.AutoFormatType` 属性以及 `com.aspose.cells.PivotTableAutoFormatType` 枚举。此 API 对应于经典 Excel 为数据透视表提供的自动格式选择器。

对于现代 `.xlsx`、`.xlsm` 和 `.xlsb` 输出，提供两种风格的样式 API：

- `PivotTable.PivotTableStyleType` 用于选择内置命名样式之一（浅色和深色主题，包括 Excel 2017 中新增的样式）。这些预设是只读的。
- `PivotTable.PivotTableStyleName` 用于选择您通过 `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(...)` 自行定义的自定义样式。当您希望修改预设提供的颜色、边框或字体时，必须使用自定义样式。

此外，`PivotTable.formatAll(Style)` 是一个快捷方式，它将单个 `Style` 对象应用于数据透视表的每个单元格，覆盖通过上述任一样式名称 API 设置的内容。当需要统一外观而不考虑底层主题时，这非常有用。

## **应用旧版 XLS 预设自动格式**

`PivotTable.AutoFormatType` 接受来自 `com.aspose.cells.PivotTableAutoFormatType` 枚举的值。可用值为 `REPORT_1` 到 `REPORT_10`、`CLASSIC` 以及 `TABLE_1` 到 `TABLE_10`。

{{% alert color="primary" %}}

`AutoFormatType` 仅在工作簿保存为 `.xls` 时生效。当同一工作簿保存为 `.xlsx`、`.xlsm` 或 `.xlsb` 时，Excel 会忽略此属性并回退到 `PivotTableStyleType` 和 `PivotTableStyleName` 设置。

{{% /alert %}}

下面的示例加载一个新工作簿，填充 Fruit/Year/Amount 示例数据，添加一个数据透视表，应用 `PivotTableAutoFormatType.REPORT_5`，并将结果保存为 `.xls`。

```java
import com.aspose.cells.*;

// 场景 1：应用旧版 XLS 预设自动格式
// 使用的 API：PivotTable.AutoFormatType
// 目标文件格式：.xls（旧版）
// 有关完整示例和数据文件，请访问 https://github.com/aspose-cells/Aspose.Cells-for-.NET

// 创建新的工作簿
Workbook workbook = new Workbook();

// 获取第一个工作表
Worksheet sheet = workbook.getWorksheets().get(0);

// 使用表头行（Fruit、Year、Amount）填充源数据
// 以及 9 行覆盖 2020 和 2021 年葡萄、蓝莓、猕猴桃、樱桃的数据
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

// 在目标单元格 E3 处添加数据透视表，名称为 "Pivot1"，使用源范围 A1:C10
int pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);

// 分配字段：Fruit -> 行，Year -> 列，Amount -> 数据
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// 应用旧版 XLS 预设自动格式 "Report5"
// 注意：此属性仅在另存为 .xls 时有效。
// 当另存为 .xlsx/.xlsm/.xlsb 时，Excel 将忽略 AutoFormatType
// 并使用 PivotTableStyleType / PivotTableStyleName 所指定的样式。
pivotTable.setAutoFormatType(PivotTableAutoFormatType.REPORT_5);

// 将工作簿另存为旧版 .xls 格式
workbook.save("output.xls");
```

## **应用现代命名预设数据透视表样式**

`PivotTable.PivotTableStyleType` 接受来自 `com.aspose.cells.PivotTableStyleType` 枚举的值。该枚举涵盖浅色主题 `PIVOT_TABLE_STYLE_LIGHT_1` 到 `PIVOT_TABLE_STYLE_LIGHT_28` 和深色主题 `PIVOT_TABLE_STYLE_DARK_1` 到 `PIVOT_TABLE_STYLE_DARK_28`。Excel 2017 中新增的样式（浅色和深色主题的第二波）可以通过同一枚举访问。

对于任何现代文件格式，推荐使用此 API。与旧版自动格式不同，此处选择的样式可由 Excel 忠实地呈现，并在通过其他 Office 工具往返转换后保持不变。

下面的示例使用相同的 Fruit/Year/Amount 数据，创建相同的数据透视表，应用 `PIVOT_TABLE_STYLE_DARK_1`，并将工作簿保存为 `.xlsx`。

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// 表头行：水果 / 年份 / 金额
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9 行数据，包含水果 / 年份 / 金额
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(150);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(180);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(120);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(170);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(210);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(190);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(130);

// 在 E3 位置添加一个名为 "Pivot1" 的数据透视表，数据源为 A1:C10
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// 指定透视字段：水果 -> 行区域，年份 -> 列区域，金额 -> 数据区域
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// 应用一个现代 Excel 2007+ 命名的预设透视样式。
// PivotTableStyleType 是适用于 .xlsx / .xlsb / .xlsb 文件的正确 API；AutoFormatType
// 在这些格式下会被 Excel 忽略。PivotTableStyleDark1 属于深色主题系列
// （PivotTableStyleDark1..PivotTableStyleDark28），同一枚举还公开了
// 较新的 Excel 2017 浅色/深色主题（PivotTableStyleLight1..Light28 / Dark1..Dark28）。
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);

// 保存为现代 .xlsx 格式 - 这是 PivotTableStyleType 有效的格式。
workbook.save("output.xlsx");
```

## **定义并应用自定义数据透视表样式**

内置预设无法修改。每当您需要覆盖颜色、边框或字体时，都必须定义自定义数据透视表样式。该工作流包含三个步骤：

1. 通过 `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)` 向工作簿的 `TableStyles` 集合添加自定义样式。这将返回新创建样式的索引。
2. 通过 `TableStyle.getTableStyleElements().add(TableStyleElementType)` 添加元素（例如 `WholeTable` 或 `GrandTotalRow`）来配置样式，然后通过 `TableStyleElement.setElementStyle(Style)` 为每个元素分配一个 `Style`。
3. 通过将 `PivotTable.PivotTableStyleName` 设置为样式名称，将自定义样式应用于数据透视表。此处不要使用 `PivotTableStyleType`，因为该属性用于选择内置预设。

{{% alert color="primary" %}}

`PivotTableStyleName` 和 `PivotTableStyleType` 不可互换。`PivotTableStyleType` 用于内置预设，`PivotTableStyleName` 用于您通过 `addPivotTableStyle` 定义的自定义样式。同时设置两者是无害的，但只有与预期来源匹配的设置才会被呈现。

{{% /alert %}}

可用的 `TableStyleElementType` 值包括 `WHOLE_TABLE`、`FIRST_ROW`、`LAST_ROW`、`FIRST_COLUMN`、`LAST_COLUMN`、`GRAND_TOTAL_ROW`、`GRAND_TOTAL_COLUMN`、`PAGE_FIELD_LABELS` 和 `PAGE_FIELD_VALUES`。

下面的示例定义了一个自定义数据透视表样式，其中 `WholeTable` 上有细黑色边框，`GrandTotalRow` 上有粗体红色字体，然后通过 `PivotTableStyleName` 应用该样式并保存为 `.xlsx`。

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

// 添加数据源为 A1:C10、锚定在 E3、名为 "Pivot1" 的数据透视表
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// 步骤 1：注册一个新的自定义数据透视表样式并获取其索引
int styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);

// 步骤 2：添加 WholeTable 元素，并在四边应用细黑色边框
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

// 步骤 3：添加 GrandTotalRow 元素，并应用粗体红色字体
int grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW);
TableStyleElement grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
Style grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(Color.getRed());
grandTotalElement.setElementStyle(grandTotalStyle);

// 步骤 4：按名称应用自定义样式（不要使用 PivotTableStyleType，那是用于内置预设样式的）
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **使用 FormatAll 将单一样式应用于每个数据透视表单元格**

`PivotTable.formatAll(Style)` 是一个快捷方式，它将单个 `Style` 对象应用于数据透视表的每个单元格，包括数据区域、行和列标题以及总计。通过 `PivotTableStyleType` 或 `PivotTableStyleName` 之前设置的任何内容都会被覆盖。

{{% alert color="primary" %}}

`FormatAll` 会覆盖 `PivotTableStyleType` 和 `PivotTableStyleName`。仅当整个数据透视表需要统一且独立于主题的外观时才使用它。

{{% /alert %}}

下面的示例创建了一个具有黄色实心填充、粗体深蓝色字体以及所有边细黑色边框的 `Style`，然后使用 `formatAll` 应用它并保存为 `.xlsx`。

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

// 添加数据透视表：源区域 A1:C10，目标单元格 E3，名称 "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// 分配透视字段：Fruit -> 行区域，Year -> 列区域，Amount -> 数据区域
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// 构建一个将强制应用于数据透视表每个单元格的样式
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

// 应用 FormatAll：强制将此单一样式应用到数据透视表的每个单元格，
// 覆盖之前设置的任何 PivotTableStyleType / PivotTableStyleName
pivotTable.formatAll(style);

// 以现代的 .xlsx 格式保存工作簿
workbook.save("output.xlsx");
```

## **我应该使用哪种样式 API？**

样式 API 的选择取决于您保存到的文件格式。请使用下表作为快速参考。

| 目标文件格式 | 使用的 API | 备注 |
|---|---|---|
| `.xls`（旧版） | `PivotTable.AutoFormatType` | 来自 `com.aspose.cells.PivotTableAutoFormatType` 的值（例如 `REPORT_1`–`REPORT_10`、`CLASSIC`、`TABLE_1`–`TABLE_10`）。保存为现代格式时会被忽略。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代，内置样式） | `PivotTable.PivotTableStyleType` | 来自 `com.aspose.cells.PivotTableStyleType` 的值（浅色/深色主题，包括 Excel 2017 新增的样式）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代，自定义样式） | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.addPivotTableStyle(...)` | 在内置预设不够用时使用。通过 `TableStyleElement.setElementStyle(...)` 进行配置。 |
| 任何格式（统一覆盖） | `PivotTable.formatAll(Style)` | 快捷方式，覆盖整个数据透视表上的所有其他样式设置。 |

如有疑问，请保存为 `.xlsx`，并对内置主题使用 `PivotTableStyleType`，或对自定义主题使用 `PivotTableStyleName`。

{{< app/cells/assistant language="java" >}}