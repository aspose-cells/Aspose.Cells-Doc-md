---
title: 边框设置
description: 在Python中如何使用 Aspose.Cells for Python via .NET 库设置单元格的边框样式和颜色。通过调整边框的宽度、样式和颜色，可以更好地控制单元格的外观和效果。
keywords: Aspose.Cells for Python via .NET，单元格边框设置，Python边框宽度，边框样式，边框颜色
type: docs
weight: 40
url: /zh/python-net/cells-border-settings/
---

## **向单元格添加边框**

Microsoft Excel 允许用户通过添加边框来格式化单元格。边框的类型取决于添加的位置。例如，顶部边框是添加到单元格顶部位置的边框。用户还可以修改边框的线条样式和颜色。

使用Aspose.Cells for Python via .NET，开发者可以像在Microsoft Excel中一样添加边框并自定义其外观。

### **向单元格添加边框**

Aspose.Cells for Python via .NET提供一个类 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)，代表一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类包含一个 [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) 集合，允许访问Excel文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类提供一个 [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合。[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合中的每个项目代表一个 [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) 类的对象。

Aspose.Cells for Python via .NET在 [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) 类中提供 [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) 方法。[**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) 方法用于设置单元格的格式样式。[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) 类提供添加边框到单元格的属性。

#### **向单元格添加边框**

开发人员可以通过使用 [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) 对象的 [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) 集合向单元格添加边框。边框类型作为索引传递给 [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) 集合。所有边框类型都在 [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype) 枚举中预定义。

**边框枚举**

|**边框类型**|**描述**|
| :- | :- |
|BOTTOM_BORDER|底部边框线|
|DIAGONAL_DOWN|从左上到右下的对角线|
|DIAGONAL_UP|从左下到右上的对角线|
|LEFT_BORDER|左边边框线|
|RIGHT_BORDER|右边边框线|
|TOP_BORDER|顶部边框线|

The [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection stores all borders. Each border in the [**Borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection is represented by a [**Border**](https://reference.aspose.com/cells/python-net/aspose.cells/border) object which provides two properties, [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/border/color) and [**line_style**](https://reference.aspose.com/cells/python-net/aspose.cells/border/line_style) to set a border's line color and style respectively.

要设置边框线颜色，请使用.NET Framework的Color枚举（.NET Framework的一部分）选择颜色并将其分配给Border对象的Color属性。

通过从[**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype)枚举中选择线条样式来设置边框线样式。

**CellBorderType枚举**

|**线条样式**|**描述**|
| :- | :- |
|DASH_DOT|细虚线|
|DASH_DOT_DOT|细点虚线|
|DASHED|虚线|
|DOTTED|点线|
|DOUBLE|双线|
|HAIR|细线|
|MEDIUM_DASH_DOT|中虚线|
|MEDIUM_DASH_DOT_DOT|中点虚线|
|MEDIUM_DASHED|中虚线|
|NONE|无线条|
|MEDIUM|中线|
|SLANTED_DASH_DOT|斜虚线|
|THICK|加粗线|
|THIN|细线|
选择其中一种线条样式，然后将其分配给“[**Border**](https://reference.aspose.com/cells/python-net/aspose.cells/border)”对象的[**line_style**](https://reference.aspose.com/cells/python-net/aspose.cells/border/line_style)属性。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Borders-AddingBordersToCells-1.py" >}}

{{% alert color="primary" %}}

您应同时设置线条样式和颜色。两条对角边框线的线条样式和颜色应相同。

{{% /alert %}}

#### **向单元格范围添加边框**

还可以为一系列的单元格添加边框，而不仅仅是单个单元格。要实现这一点，首先通过调用“[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)”集合的[**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range)方法创建一系列单元格。它使用以下参数：

- 第一行，范围的第一行。
- 第一列，表示范围的第一列。
- 行数，范围中的行数。
- 列数，范围中的列数。

“[**create_range**](hhttps://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str)”方法返回一个[**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)对象，它包含指定范围的单元格。[**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)对象提供一个[**set_outline_border**](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_outline_border)方法，使用以下参数为单元格范围添加边框：

- **边框类型**，从[**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype)枚举中选择的边框类型。
- **线条样式**，从[**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype)枚举中选择的边框线条样式。
- **颜色**，线条颜色，从Color枚举中选择。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Borders-AddingBorderstoRange-1.py" >}}

