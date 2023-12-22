---
title: 边框设置
description: 如何使用C#中的Aspose.Cells库设置单元格的边框样式和颜色。通过调整边框的宽度、样式和颜色，您可以更好地控制单元格的外观和显示方式。
keywords: Aspose.Cells, Cell Border Settings, C#, Border Width, Border Style, Border Color
type: docs
weight: 40
url: /zh/net/cells-border-settings/
---
##  **为 Cells 添加边框**

Microsoft Excel 允许用户通过添加边框来设置单元格格式。边框的类型取决于添加的位置。例如，顶部边框是添加到单元格顶部位置的边框。用户还可以修改边框的线条样式和颜色。

使用 Aspose.Cells，开发人员可以添加边框并以与 Microsoft Excel 中相同的灵活方式自定义边框的外观。

###  **为 Cells 添加边框**

Aspose.Cells提供一堂课，[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)代表 Microsoft Excel 文件。这[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中的每个工作表的集合。工作表由以下形式表示[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏。中的每一项[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合代表一个对象[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级。

 Aspose.Cells 提供[**获取样式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)方法中的[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级。这[**设置样式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)方法用于设置单元格的格式样式。这[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)类提供用于向单元格添加边框的属性。

####  **为 Cell 添加边框**

开发人员可以使用以下命令向单元格添加边框[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**边框**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)收藏。边框类型作为索引传递给[**边框**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)收藏。所有边框类型均在中预定义[**边框类型**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)枚举。

**边界枚举**

|**边框类型**|**描述**|
| :- | :- |
|下边框|底部边框线|
|对角向下|从左上角到右下角的对角线|
|对角向上|从左下角到右上角的对角线|
|左边框|左边界线|
|右边框|右边界线|
|上边框|顶部边框线|

这[**边框**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)集合存储所有边框。中的每个边界[**边框**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)集合由一个表示[**边界**](https://reference.aspose.com/cells/net/aspose.cells/border)提供两个属性的对象，[**颜色**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color)和[**线条样式**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)分别设置边框的线条颜色和样式。

要设置边框的线条颜色，请使用 Color 枚举（.NET 框架的一部分）选择一种颜色，并将其分配给 Border 对象的 Color 属性。

边框的线条样式是通过从以下选项中选择线条样式来设置的：[**单元格边框类型**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)枚举。

**CellBorderType 枚举**

|**线条样式**|**描述**|
| :- | :- |
|点划线|细点划线|
|点划点|细点划线|
|虚线|虚线|
|点状|虚线|
|双倍的|双线|
|头发|发际线|
|中点划线|中点划线|
|中点划点点|中点划线|
|中虚线|中虚线|
|没有任何|没有线路|
|中等的|中线|
|斜点划线|倾斜的中点划线|
|厚的|粗线|
|薄的|细线|
选择一种线条样式，然后将其指定给[**边界**](https://reference.aspose.com/cells/net/aspose.cells/border)对象的[**线条样式**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)财产。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

您应该同时设置线条样式和颜色。两条对角边框线应具有相同的线型和颜色。

{{% /alert %}}

####  **向 Cells 范围添加边框**

还可以向一系列单元格而不只是单个单元格添加边框。为此，首先，通过调用创建一个单元格范围[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏的[**创建范围**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1)方法。它需要以下参数：

- 第一行，范围的第一行。
- 第一列，表示范围的第一列。
- 行数，范围内的行数。
- 列数，范围内的列数。

这[**创建范围**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1)方法返回一个[**范围**](https://reference.aspose.com/cells/net/aspose.cells/range)对象，其中包含指定的单元格范围。这[**范围**](https://reference.aspose.com/cells/net/aspose.cells/range)对象提供了一个[**设置轮廓边框**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder)方法采用以下参数向单元格区域添加边框：

-  *边框类型**，边框类型，从[**边框类型**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)枚举。
- *Line Style**，边框线样式，从[**单元格边框类型**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)枚举。
- *颜色**，线条颜色，从 Color 枚举中选择。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}
