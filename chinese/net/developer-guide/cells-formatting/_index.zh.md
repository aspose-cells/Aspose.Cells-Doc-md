---
title: 设置单元格格式
description: 了解如何在 Aspose.Cells for .NET 中设置单元格格式和样式，包括数字格式、日期格式、字体样式和其他单元格样式选项。我们的指南将帮助您创建有吸引力且具有专业外观的电子表格。
keywords: Aspose.Cells for .NET, cell formatting, styling, number formatting, date formatting, font style, cell style options, spreadsheet, create, professional look, format rows and columns.
linktitle: 设置单元格格式
type: docs
weight: 120
url: /zh/net/cells-formatting/
---
##  **介绍**

{{% alert color="primary" %}}

 Aspose.Cells 提供[**获取样式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)和[**设置样式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)的方法[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell)类，用于获取/设置单元格的格式样式。 Aspose.Cells还提供了[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)班级。

{{% /alert %}}

##  **如何使用 GetStyle 和 SetStyle 方法格式化 Cells**

在单元格上应用不同类型的格式样式以设置背景或前景色、边框、字体、水平和垂直对齐方式、缩进级别、文本方向、旋转角度等等。

###  **如何使用 GetStyle 和 SetStyle 方法**

如果开发人员需要对不同的单元格应用不同的格式样式，那么最好获取[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)细胞使用[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)方法，指定样式属性，然后使用应用格式[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)方法。下面给出了一个示例来演示这种在单元格上应用各种格式的方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

###  **如何使用样式对象格式化不同的Cells**

如果开发人员需要将相同的格式样式应用于不同的单元格，那么他们可以使用[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)目的。请按照以下步骤使用[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)目的：

1. 添加一个[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象通过调用[**创建样式**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)的方法[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)班级
1. 访问新添加的[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style) object
1. 设置所需的属性/属性[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象应用所需的格式设置
1. 分配已配置的[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)反对你想要的细胞

这种方法可以极大地提高应用程序的效率并节省内存。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

###  **如何使用 Microsoft Excel 2007 预定义样式**

如果您需要为 Microsoft Excel 2007 应用不同的格式样式，请使用 Aspose.Cells API 应用样式。下面给出了一个示例来演示在单元格上应用预定义样式的方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



##  **如何格式化 Cell 中选定的字符**

处理字体设置解释了如何设置单元格中文本的格式，但它仅解释了如何设置所有单元格内容的格式。如果您只想格式化选定的字符怎么办？

Aspose.Cells也支持此功能。本主题解释了如何有效地使用此功能。

###  **如何设置选定字符的格式**

Aspose.Cells提供一堂课，[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)代表 Microsoft Excel 文件。这[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中的每个工作表的集合。工作表由以下形式表示[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏。中的每一项[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合代表一个对象[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级。

这[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类提供了[**人物**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)方法采用以下参数来选择单元格内的一系列字符：

- *起始索引**，选择开始的字符的索引。
- *字符数**，要选择的字符数。

这[**人物**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)方法返回一个实例[**字体设置**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)类，允许开发人员以与单元格相同的方式设置字符格式，如下面的代码示例所示。在输出文件的 A1 单元格中，单词“Visit”将使用默认字体设置格式，但为“Aspose!”是粗体和蓝色的。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

如果您对单元格中部分富文本格式感兴趣，请考虑使用[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) & [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)方法。这[[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters)方法用于访问文本的各个部分，然后可以使用[**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)方法而**得到**方法返回一个数组[**字体设置**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)可以操作的对象来设置各种属性，例如字体名称、字体颜色、粗体等**放**方法可用于应用更改。

{{% /alert %}}

##  **如何设置行和列的格式**

有时，开发人员需要对行或列应用相同的格式。逐个对单元格应用格式通常需要更长的时间，并且不是一个好的解决方案。
为了解决这个问题，Aspose.Cells提供了一种简单、快速的方法，本文将详细讨论。

###  **设置行和列的格式**

Aspose.Cells提供了一个类，[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)代表 Microsoft Excel 文件。这[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中的每个工作表的集合。工作表由以下形式表示[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏。这[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合提供了[**行数**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)收藏。

###  **如何设置行格式**

中的每一项[**行数**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)集合代表一个[**排**](https://reference.aspose.com/cells/net/aspose.cells/row)目的。这[**排**](https://reference.aspose.com/cells/net/aspose.cells/row)对象提供了[**应用样式**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)用于设置行格式的方法。要将相同的格式应用于行，请使用[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)目的。以下步骤展示了如何使用它。

1. 添加一个[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)反对[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类通过调用它的[**创建样式**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)方法。
1. 设置[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的属性来应用格式设置。
1. 使相关属性为ON[**样式标志**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)目的。
1. 分配已配置的[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)反对[**排**](https://reference.aspose.com/cells/net/aspose.cells/row)目的。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

###  **如何设置列格式**

这[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合还提供了[**列**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns)收藏。中的每一项[**列**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns)集合代表一个[**柱子**](https://reference.aspose.com/cells/net/aspose.cells/column)目的。类似于[**排**](https://reference.aspose.com/cells/net/aspose.cells/row)对象，即[**柱子**](https://reference.aspose.com/cells/net/aspose.cells/column)对象还提供了[**应用样式**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)格式化列的方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

##  **高级主题**
- [对齐设置](/cells/zh/net/cells-alignment-settings/)
- [边框设置](/cells/zh/net/cells-border-settings/)
- [设置Excel和ODS文件的条件格式。](/cells/zh/net/conditional-formatting/)
- [Excel 主题和颜色](/cells/zh/net/excel-themes-and-colors/)
- [填充设置](/cells/zh/net/cells-fill-settings/)
- [字体设置](/cells/zh/net/cells-font-settings/)
- [设置工作簿中工作表 Cells 的格式](/cells/zh/net/format-worksheet-cells-in-a-workbook/)
- [实施 1904 日期系统](/cells/zh/net/implement-1904-date-system/)
- [合并与取消合并 Cells](/cells/zh/net/merging-and-unmerging-cells/)
- [号码设置](/cells/zh/net/cells-number-settings/)
- [获取和设置单元格的样式](/cells/zh/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

