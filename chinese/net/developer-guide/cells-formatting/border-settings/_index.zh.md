---
title: 边框设置
type: docs
weight: 40
url: /zh/net/cells-border-settings/
---
## **为 Cells 添加边框**

Microsoft Excel 允许用户通过添加边框来格式化单元格。边框的类型取决于添加的位置。例如，顶部边框是添加到单元格顶部位置的边框。用户还可以修改边框的线条样式和颜色。

使用 Aspose.Cells，开发人员可以像在 Microsoft Excel 中一样灵活地添加边框和自定义外观。

### **为 Cells 添加边框**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏。中的每一项[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合代表一个对象[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级。

Aspose.Cells 提供了[**获取样式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)中的方法[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级。这[**设置样式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)方法用于设置单元格的格式样式。这[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)类提供用于向单元格添加边框的属性。

#### **为 Cell 添加边框**

开发人员可以使用[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**边框**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)收藏。边框类型作为索引传递给[**边框**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)收藏。所有边框类型都预定义在[**边框类型**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)枚举。

**边界枚举**

|**边框类型**|**描述**|
|:- |:- |
|底部边框|底部边界线|
|对角向下|从左上角到右下角的对角线|
|对角向上|从左下角到右上角的对角线|
|左边框|一条左边界线|
|右边框|右边界线|
|顶部边框|顶部边界线|

这[**边框**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)集合存储所有边界。中的每个边框[**边框**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)集合由一个表示[**边界**](https://reference.aspose.com/cells/net/aspose.cells/border)提供两个属性的对象，[**颜色**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color)和[**线型**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)分别设置边框的线条颜色和样式。

要设置边框的线条颜色，请使用 Color 枚举（.NET Framework 的一部分）选择一种颜色，并将其分配给 Border 对象的 Color 属性。

边框的线条样式是通过从中选择一种线条样式来设置的[**单元格边框类型**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)枚举。

**CellBorderType 枚举**

|**线型**|**描述**|
|:- |:- |
|点划线|细点划线|
|点点滴滴|细点划线|
|虚线|虚线|
|点缀的|虚线|
|双倍的|双线|
|头发|发际线|
|MediumDashDot|中点划线|
|MediumDashDotDot 点|中点划线|
|中虚线|中虚线|
|没有任何|没有线|
|中等的|中线|
|斜划线点|倾斜的中点划线|
|厚的|粗线|
|薄的|细线|
选择一种线型，然后将其分配给[**边界**](https://reference.aspose.com/cells/net/aspose.cells/border)对象的[**线型**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)财产。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

您应该同时设置线型和颜色。两条对角边框线应具有相同的线型和颜色。

{{% /alert %}}

#### **为 Cells 范围添加边框**

也可以为一系列单元格添加边框，而不仅仅是单个单元格。为此，首先，通过调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏的[**创建范围**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1)方法。它采用以下参数：

- First Row，范围的第一行。
- 第一列，代表范围的第一列。
- Number of Rows，范围内的行数。
- Number of Columns，范围内的列数。

这[**创建范围**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1)方法返回一个[**范围**](https://reference.aspose.com/cells/net/aspose.cells/range)对象，其中包含指定范围的单元格。这[**范围**](https://reference.aspose.com/cells/net/aspose.cells/range)对象提供了一个[**设置轮廓边框**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder)采用以下参数为单元格区域添加边框的方法：

- **边框类型**，边框类型，从[**边框类型**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)枚举。
- **线型** 边框线条样式，选自[**单元格边框类型**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)枚举。
- **颜色**，线条颜色，从 Color 枚举中选择。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}

## **颜色和调色板**

调色板是可用于创建图像的颜色数量。在演示文稿中使用标准化调色板允许用户创建一致的外观。每个 Microsoft Excel (97-2003) 文件都有一个 56 种颜色的调色板，可应用于图表中的单元格、字体、网格线、图形对象、填充和线条。

使用 Aspose.Cells 不仅可以使用调色板的现有颜色，还可以使用自定义颜色。在使用自定义颜色之前，请先将其添加到调色板中。

本主题讨论如何将自定义颜色添加到调色板。

### **将自定义颜色添加到调色板**

Aspose.Cells 支持Microsoft Excel的56色调色板。要使用未在调色板中定义的自定义颜色，请将颜色添加到调色板。

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类提供了[**改变调色板**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette)采用以下参数添加自定义颜色以修改调色板的方法：

- Custom Color，要添加的自定义颜色。
- 索引，自定义颜色将替换的调色板中颜色的索引。应该在 0-55 之间。

下面的示例在将自定义颜色（兰花）应用于字体之前将其添加到调色板。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

调色板只有 56 种颜色。当您将自定义颜色添加到调色板时，调色板会更改，文件中使用先前颜色设置格式的任何元素也会更改。所以，当你改变调色板时，请非常小心。此外，这只是 XLS（Excel 97 - 2003）文件格式的限制，因为 XLSX 或其他高级 MS Excel（2007/2010 或 2013）文件格式没有此类限制。

{{% /alert %}}


