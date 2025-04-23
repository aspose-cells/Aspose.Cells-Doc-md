---
title: 边框设置
description: 如何在 C# 中使用 Aspose.Cells 库设置单元格的边框样式和颜色。通过调整边框的宽度、样式和颜色，您可以更好地控制单元格的外观。
keywords: Aspose.Cells, 单元格边框设置, C#, 边框宽度, 边框样式, 边框颜色
type: docs
weight: 40
url: /zh/net/cells-border-settings/
---

## **向单元格添加边框**

Microsoft Excel 允许用户通过添加边框来格式化单元格。边框的类型取决于添加的位置。例如，顶部边框是添加到单元格顶部位置的边框。用户还可以修改边框的线条样式和颜色。

借助 Aspose.Cells，开发人员可以以与 Microsoft Excel 中相同的灵活方式添加边框并自定义其外观。

### **向单元格添加边框**

Aspose.Cells 提供了一个表示 Microsoft Excel 文件的 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类。 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) 集合，该集合允许访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类表示。 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类提供 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 集合。 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) 集合中的每个项表示 [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) 类的对象。

Aspose.Cells 在 [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) 类中提供了 [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) 方法。 [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) 方法用于设置单元格的格式样式。 [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) 类提供了用于向单元格添加边框的属性。

#### **向单元格添加边框**

开发人员可以通过使用 [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) 对象的 [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) 集合向单元格添加边框。边框类型作为索引传递给 [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) 集合。所有边框类型都在 [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) 枚举中预定义。

**边框枚举**

|**边框类型**|**描述**|
| :- | :- |
|BottomBorder| 底部边框线|
|DiagonalDown| 从左上到右下的对角线|
|DiagonalUp| 从左下到右上的对角线|
|LeftBorder|左边框线|
|RightBorder|右边框线|
|TopBorder|顶部边框线|

The [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection stores all borders. Each border in the [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection is represented by a [**Border**](https://reference.aspose.com/cells/net/aspose.cells/border) object which provides two properties, [**Color**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) and [**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) to set a border's line color and style respectively.

要设置边框线颜色，请使用.NET Framework的Color枚举（.NET Framework的一部分）选择颜色并将其分配给Border对象的Color属性。

通过从[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)枚举中选择线条样式来设置边框线样式。

**CellBorderType枚举**

|**线条样式**|**描述**|
| :- | :- |
|DashDot|细长虚点线|
|DashDotDot|细长虚点虚点线|
|Dashed|虚线|
|Dotted|点状线|
|Double|双线|
|Hair|细线|
|MediumDashDot|中等虚点线|
|MediumDashDotDot|中等虚点虚点线|
|MediumDashed|中等虚线|
|None|无线|
|Medium|中线|
|SlantedDashDot|倾斜中等虚点线|
|Thick|粗线|
|Thin|细线|
选择其中一种线条样式，然后将其分配给“[**Border**](https://reference.aspose.com/cells/net/aspose.cells/border)”对象的[**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)属性。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

您应同时设置线条样式和颜色。两条对角边框线的线条样式和颜色应相同。

{{% /alert %}}

#### **向单元格范围添加边框**

还可以为一系列的单元格添加边框，而不仅仅是单个单元格。要实现这一点，首先通过调用“[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)”集合的[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1)方法创建一系列单元格。它使用以下参数：

- 第一行，范围的第一行。
- 第一列，表示范围的第一列。
- 行数，范围中的行数。
- 列数，范围中的列数。

“[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1)”方法返回一个[**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)对象，它包含指定范围的单元格。[**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)对象提供一个[**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder)方法，使用以下参数为单元格范围添加边框：

- **边框类型**，从[**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)枚举中选择的边框类型。
- **线条样式**，从[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)枚举中选择的边框线条样式。
- **颜色**，线条颜色，从Color枚举中选择。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
