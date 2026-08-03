---
title: 在 Aspose.Cells for Python via Java 中应用数据透视表样式
linktitle: 应用数据透视表样式
description: 了解如何在 Aspose.Cells for Python via Java 中将内置和自定义样式应用于数据透视表，涵盖旧版 XLS 自动格式、现代 Excel 2007+ 命名样式、自定义数据透视表样式以及 FormatAll 快捷方式。
keywords: Aspose.Cells Python via Java 数据透视表样式, PivotTableStyleType, AutoFormatType, FormatAll, 自定义样式, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /zh/python-java/apply-style-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持应用旧版数据透视表自动格式（适用于 `.xls` 文件）以及现代命名或自定义的数据透视表样式（适用于 `.xlsx`、`.xlsm` 和 `.xlsb` 文件）。您应调用的 API 取决于工作簿保存到的文件格式，而不是加载时的格式。

{{% /alert %}}

## **简介**

Aspose.Cells 为数据透视表提供了两套并行的样式 API。它们之间的选择取决于工作簿保存到的文件格式，而不是读取时的格式。从 `.xls` 文件加载的工作簿可以重新保存为 `.xlsx`，在这种情况下应使用现代样式 API 而非旧版 API。

对于旧版 `.xls` 输出，请使用 `pivotTable.setAutoFormatType(int)` 方法以及 `com.aspose.cells.pivot.PivotTableAutoFormatType` 枚举。此 API 对应于经典 Excel 为数据透视表提供的自动格式选择器。

对于现代 `.xlsx`、`.xlsm` 和 `.xlsb` 输出，可使用两种样式 API：

- `pivotTable.setPivotTableStyleType(int)` 选择某个内置命名样式（浅色和深色主题，包括 Excel 2017 中新增的样式）。这些预设是只读的。
- `pivotTable.setPivotTableStyleName(String)` 选择您通过 `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String)` 自行定义的自定义样式。当您需要修改预设所能提供的颜色、边框或字体时，必须使用自定义样式。

此外，`pivotTable.formatAll(Style)` 是一个快捷方式，它会将单个 `Style` 对象应用于数据透视表的每个单元格，覆盖通过上述任意样式名称 API 设置的内容。当需要无论底层主题如何都呈现统一外观时，此方法非常有用。

## **应用旧版 XLS 预设自动格式**

数据透视表上的 `setAutoFormatType` 方法接受来自 `com.aspose.cells.pivot.PivotTableAutoFormatType` 枚举的值。可用值包括 `REPORT_1` 至 `REPORT_10`、`CLASSIC` 以及 `TABLE_1` 至 `TABLE_10`。

{{% alert color="primary" %}}

`setAutoFormatType` 仅在工作簿保存为 `.xls` 时才有效。当同一工作簿保存为 `.xlsx`、`.xlsm` 或 `.xlsb` 时，Excel 会忽略此设置并回退到 `setPivotTableStyleType` 和 `setPivotTableStyleName` 设置。

{{% /alert %}}

以下示例加载一个新的工作簿，填充 Fruit/Year/Amount 示例数据，添加一个数据透视表，应用 `PivotTableAutoFormatType.REPORT_5`，并将结果保存为 `.xls`。

{{% alert color="primary" %}}

**为什么没有列字段？** Report 系列自动格式（`Report1` 到 `Report10`、`Table1` 到 `Table10`）是在经典 Excel 中为**单维度数据透视表**设计的——只有行字段和值，没有为列字段标题提供内置样式。如果透视表需要列字段，请改用下方场景 2 中的现代 `PivotTableStyleType` 预设样式，它们专为现代 Excel 的二维布局而设计。

{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType, PivotTableAutoFormatType

# 场景 1:应用旧版 XLS 预设自动格式
# 使用的 API:PivotTable.AutoFormatType
# 目标文件格式:.xls(旧版)
# 完整示例和数据文件,请访问 https://github.com/aspose-cells/Aspose.Cells-for-.NET

# 创建一个新工作簿
workbook = Workbook()

# 获取第一个工作表
sheet = workbook.getWorksheets().get(0)

# 使用表头行(Fruit、Year、Amount)填充源数据
# 以及涵盖 2020 年和 2021 年葡萄、蓝莓、猕猴桃、樱桃的 9 行数据
sheet.getCells().get(0, 0).putValue("Fruit")
sheet.getCells().get(0, 1).putValue("Year")
sheet.getCells().get(0, 2).putValue("Amount")

sheet.getCells().get(1, 0).putValue("grape")
sheet.getCells().get(1, 1).putValue(2020)
sheet.getCells().get(1, 2).putValue(50)

sheet.getCells().get(2, 0).putValue("blueberry")
sheet.getCells().get(2, 1).putValue(2020)
sheet.getCells().get(2, 2).putValue(30)

sheet.getCells().get(3, 0).putValue("kiwi")
sheet.getCells().get(3, 1).putValue(2020)
sheet.getCells().get(3, 2).putValue(25)

sheet.getCells().get(4, 0).putValue("cherry")
sheet.getCells().get(4, 1).putValue(2020)
sheet.getCells().get(4, 2).putValue(40)

sheet.getCells().get(5, 0).putValue("grape")
sheet.getCells().get(5, 1).putValue(2021)
sheet.getCells().get(5, 2).putValue(60)

sheet.getCells().get(6, 0).putValue("blueberry")
sheet.getCells().get(6, 1).putValue(2021)
sheet.getCells().get(6, 2).putValue(35)

sheet.getCells().get(7, 0).putValue("kiwi")
sheet.getCells().get(7, 1).putValue(2021)
sheet.getCells().get(7, 2).putValue(28)

sheet.getCells().get(8, 0).putValue("cherry")
sheet.getCells().get(8, 1).putValue(2021)
sheet.getCells().get(8, 2).putValue(45)

sheet.getCells().get(9, 0).putValue("grape")
sheet.getCells().get(9, 1).putValue(2020)
sheet.getCells().get(9, 2).putValue(45)

# 在目标单元格 E3 处添加一个名为 "Pivot1" 的数据透视表,使用源区域 A1:C10
pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = sheet.getPivotTables().get(pivotIndex)

# 分配字段:Fruit -> 行,Year -> 列,Amount -> 数据
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# 应用旧版 XLS 预设自动格式 "Report5"
# 注意:此属性仅在保存为 .xls 时有效。
# 当保存为 .xlsx/.xlsm/.xlsb 时,Excel 会忽略 AutoFormatType
# 并使用 PivotTableStyleType / PivotTableStyleName 所指定的样式。
pivotTable.setAutoFormatType(PivotTableAutoFormatType.Report5)

# 将工作簿保存为旧版 .xls 格式
workbook.save("output.xls")

jpype.shutdownJVM()
```

## **应用现代命名预设数据透视表样式**

数据透视表上的 `setPivotTableStyleType` 方法接受来自 `com.aspose.cells.PivotTableStyleType` 枚举的值。该枚举涵盖浅色主题 `PIVOT_TABLE_STYLE_LIGHT_1` 至 `PIVOT_TABLE_STYLE_LIGHT_28` 以及深色主题 `PIVOT_TABLE_STYLE_DARK_1` 至 `PIVOT_TABLE_STYLE_DARK_28`。Excel 2017 中新增的样式（浅色和深色主题的第二波）也可通过同一枚举访问。

对于任何现代文件格式，这是推荐使用的 API。与旧版自动格式不同，此处选择的样式可被 Excel 准确呈现，并在通过其他 Office 工具进行往返转换时得以保留。

以下示例使用相同的 Fruit/Year/Amount 数据，创建一个相同的数据透视表，应用 `PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1`，并将工作簿保存为 `.xlsx`。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableStyleType, PivotFieldType

# 场景 2：使用 PivotTableStyleType 应用现代 Excel 2007+ 命名预设样式。
# 目标文件格式：.xlsx。PivotTableStyleType 枚举位于 Aspose.Cells 命名空间中
#（不在 Aspose.Cells.Pivot 中）—— 这就是为什么我们不需要任何额外的 using 引用。
# GitHub 参考：https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# 表头行：水果 / 年份 / 金额
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# 9 行水果 / 年份 / 金额数据
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(150)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(180)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(120)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(170)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(210)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(190)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(130)

# 在 E3 位置添加一个名为 "Pivot1" 的数据透视表，数据源为 A1:C10
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# 分配透视字段：水果 -> 行区域，年份 -> 列区域，金额 -> 数据区域
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# 应用现代 Excel 2007+ 命名预设透视表样式。
# PivotTableStyleType 是适用于 .xlsx / .xlsm / .xlsb 文件的正确 API；AutoFormatType
# 在这些格式中 Excel 会忽略 AutoFormatType。PivotTableStyleDark1 属于深色主题
# 系列（PivotTableStyleDark1..PivotTableStyleDark28），同一枚举还公开了
# 较新的 Excel 2017 浅色/深色主题（PivotTableStyleLight1..Light28 / Dark1..Dark28）。
pivotTable.setPivotTableStyleType(PivotTableStyleType.PivotTableStyleDark1)

# 保存为现代 .xlsx 格式——这是 PivotTableStyleType 有意义的格式。
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **定义并应用自定义数据透视表样式**

内置预设不可修改。当您需要覆盖颜色、边框或字体时，必须定义自定义数据透视表样式。工作流包含三个步骤：

1. 通过 `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)` 将自定义样式添加到工作簿的 `TableStyles` 集合中。这将返回新创建样式的索引。
2. 通过 `tableStyle.getTableStyleElements().add(TableStyleElementType)` 添加元素（例如 `WHOLE_TABLE` 或 `GRAND_TOTAL_ROW`）来配置样式，然后通过 `tableStyleElement.setElementStyle(Style)` 为每个元素分配 `Style`。
3. 通过使用样式的名称调用 `pivotTable.setPivotTableStyleName(String)` 将自定义样式应用于数据透视表。此处不要使用 `setPivotTableStyleType`，因为该方法选择的是内置预设。

{{% alert color="primary" %}}

`setPivotTableStyleName` 和 `setPivotTableStyleType` 不能互换使用。对内置预设使用 `setPivotTableStyleType`，对通过 `addPivotTableStyle` 定义的自定义样式使用 `setPivotTableStyleName`。同时设置两者没有副作用，但只有与预期来源匹配的那个才会被渲染。

{{% /alert %}}

可用的 `TableStyleElementType` 值包括 `WHOLE_TABLE`、`FIRST_ROW`、`LAST_ROW`、`FIRST_COLUMN`、`LAST_COLUMN`、`GRAND_TOTAL_ROW`、`GRAND_TOTAL_COLUMN`、`PAGE_FIELD_LABELS` 和 `PAGE_FIELD_VALUES`。

以下示例定义一个自定义数据透视表样式，在 `WHOLE_TABLE` 上使用细黑色边框，在 `GRAND_TOTAL_ROW` 上使用粗体红色字体，然后通过 `setPivotTableStyleName` 应用它并保存为 `.xlsx`。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import PivotFieldType, TableStyleElementType, BorderType, CellBorderType
from java.awt import Color

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# 填充源数据: 表头行 + 9 行数据 (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(900)

# 添加数据源为 A1:C10 的透视表,锚定在 E3,命名为 "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

# 步骤 1: 注册一个新的自定义透视表样式并获取其索引
styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle")
tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex)

# 步骤 2: 添加 WholeTable 元素并在四边应用细黑色边框
wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE)
wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex)
wholeTableStyle = workbook.createStyle()
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)
wholeTableElement.setElementStyle(wholeTableStyle)

# 步骤 3: 添加 GrandTotalRow 元素并应用粗体红色字体
grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW)
grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex)
grandTotalStyle = workbook.createStyle()
grandTotalStyle.getFont().setBold(True)
grandTotalStyle.getFont().setColor(Color.RED)
grandTotalElement.setElementStyle(grandTotalStyle)

# 步骤 4: 通过名称应用自定义样式(不是使用 PivotTableStyleType,该类型用于内置预设)
pivotTable.setPivotTableStyleName("CustomPivotStyle")

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **使用 FormatAll 将一个样式应用于所有数据透视表单元格**

`pivotTable.formatAll(Style)` 是一个快捷方式，它会将单个 `Style` 对象应用于数据透视表的每个单元格，包括数据区域、行和列标题以及总计。之前通过 `setPivotTableStyleType` 或 `setPivotTableStyleName` 设置的内容将被覆盖。

{{% alert color="primary" %}}

`formatAll` 会覆盖 `setPivotTableStyleType` 和 `setPivotTableStyleName`。仅当整个数据透视表需要呈现统一、与主题无关的外观时才使用它。

{{% /alert %}}

以下示例创建一个具有黄色纯色填充、粗体深蓝色字体以及四周细黑色边框的 `Style`，然后使用 `formatAll` 应用它并保存为 `.xlsx`。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style
from asposecells.api import Color
from asposecells.api import PivotTable, PivotFieldType
from asposecells.api import BorderType, CellBorderType, BackgroundType

# 场景 4：使用 FormatAll 将单个样式应用于每个数据透视表单元格
# 使用的 API：PivotTable.FormatAll(Style)
# 目标格式：.xlsx
# GitHub 参考：参见 Aspose.Cells-for-.NET 仓库 — 数据透视表样式示例

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# 填充源数据：标题行（第 1 行）+ 9 行数据（第 2-10 行）
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(5000)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(3000)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(4000)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(2000)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(6000)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(3500)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(4500)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(2500)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(5500)

# 添加数据透视表：源范围 A1:C10，目标单元格 E3，名称 "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# 分配透视字段：Fruit -> 行区域，Year -> 列区域，Amount -> 数据区域
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

# 构建一个将强制应用到数据透视表每个单元格的样式
style = workbook.createStyle()
style.setForegroundColor(Color.YELLOW)
style.setPattern(BackgroundType.SOLID)
style.getFont().setIsBold(True)
style.getFont().setColor(Color.DARK_BLUE)
style.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)

# 应用 FormatAll：强制将此单个样式应用到数据透视表的每个单元格，
# 覆盖之前设置的任何 PivotTableStyleType / PivotTableStyleName
pivotTable.formatAll(style)

# 以现代 .xlsx 格式保存工作簿
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **应该使用哪个样式 API？**

样式 API 的选择取决于您要保存到的文件格式。请使用下表作为快速参考。

| 目标文件格式 | 使用的 API | 备注 |
|---|---|---|
| `.xls`（旧版） | `pivotTable.setAutoFormatType(int)` | 值来自 `com.aspose.cells.pivot.PivotTableAutoFormatType`（例如 `REPORT_1`–`REPORT_10`、`CLASSIC`、`TABLE_1`–`TABLE_10`）。保存为现代格式时会被忽略。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代，内置样式） | `pivotTable.setPivotTableStyleType(int)` | 值来自 `com.aspose.cells.PivotTableStyleType`（浅色/深色主题，包括 Excel 2017 新增的样式）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代，自定义样式） | `pivotTable.setPivotTableStyleName(String)` + `tableStyles.addPivotTableStyle(String)` | 在内置预设不够时使用。通过 `tableStyleElement.setElementStyle(Style)` 进行配置。 |
| 任何格式（统一覆盖） | `pivotTable.formatAll(Style)` | 快捷方式，可覆盖整个数据透视表的所有其他样式设置。 |

如有疑问，请保存为 `.xlsx`，对内置主题使用 `setPivotTableStyleType`，对自定义主题使用 `setPivotTableStyleName`。

{{< app/cells/assistant language="python" >}}