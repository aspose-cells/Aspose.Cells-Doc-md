---
title: 格式化单元格
linktitle: 格式化单元格
type: docs
weight: 120
url: /zh/net/cells-formatting/
description: 在 .NET 框架、.NET 核心、Mono 或 Xamarin 平台上为 Excel 文件设置数字格式、边框和背景颜色。
---
## **介绍**

{{% alert color="primary" %}}

Aspose.Cells 提供了[**获取样式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)和[**设置样式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)的方法[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell)类，用于获取/设置单元格的格式样式。 Aspose.Cells还提供了[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)班级。

{{% /alert %}}

## **使用 GetStyle 和 SetStyle 方法格式化 Cells**

在单元格上应用不同类型的格式样式以设置背景或前景色、边框、字体、水平和垂直对齐方式、缩进级别、文本方向、旋转角度等等。

### **使用 GetStyle 和 SetStyle 方法**

如果开发人员需要对不同的单元格应用不同的格式样式，那么最好获取[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)细胞使用[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)方法，指定样式属性，然后使用[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)方法。下面给出了一个示例来演示这种在单元格上应用各种格式的方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

### **使用样式对象格式化不同 Cells**

如果开发人员需要将相同的格式样式应用于不同的单元格，那么他们可以使用[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)目的。请按照以下步骤使用[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)目的：

1. 添加一个[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)通过调用对象[**创建样式**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)的方法[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)班级
1. 访问新添加的[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)目的
1. 设置所需的属性/属性[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象以应用所需的格式设置
1. 分配配置的[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)反对你想要的细胞

这种方法可以大大提高应用程序的效率并节省内存。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

### **使用 Microsoft Excel 2007 预定义样式**

如果您需要为 Microsoft Excel 2007 应用不同的格式样式，请使用 Aspose.Cells API 应用样式。下面给出一个示例来演示这种在单元格上应用预定义样式的方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



## **格式化 Cell 中的选定字符**

处理字体设置解释了如何格式化单元格中的文本，但它只解释了如何格式化所有单元格内容。如果您只想格式化选定的字符怎么办？

Aspose.Cells 也支持此功能。本主题说明我们如何有效地使用此功能。

### **格式化所选字符**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏。中的每一项[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合代表一个对象[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级。

这[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类提供了[**人物**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)方法采用以下参数来选择单元格内的一系列字符：

- **起始索引**，选择开始的字符的索引。
- **字符数**要选择的字符数。

这[**人物**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)方法返回一个实例[**字体设置**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)允许开发人员以与单元格相同的方式设置字符格式的类，如下面的代码示例所示。在输出文件中，在 A1 单元格中，单词“Visit”的格式将使用默认字体但“Aspose！”是粗体和蓝色。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

如果您对单元格中的部分富文本格式感兴趣，请考虑使用[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) & [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)方法。这[[**Cell.GetCharacters**]](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters)方法将用于访问文本的部分，然后可以使用[**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)方法而**得到**方法返回一个数组[**字体设置**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)可以操作以设置各种属性的对象，例如字体名称、字体颜色、粗体等，以及**放**方法可用于应用更改。

{{% /alert %}}

## **格式化行和列**

有时，开发人员需要对行或列应用相同的格式。一个一个地对单元格应用格式通常需要更长的时间，这不是一个好的解决方案。
针对这个问题，Aspose.Cells提供了一种简单、快速的方法，本文详细讨论。

### **格式化行和列**

 Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏。这[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合提供了[**行数**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)收藏。

### **格式化一行**

中的每一项[**行数**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)集合代表一个[**排**](https://reference.aspose.com/cells/net/aspose.cells/row)目的。这[**排**](https://reference.aspose.com/cells/net/aspose.cells/row)对象提供了[**应用样式**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)用于设置行格式的方法。要对一行应用相同的格式，请使用[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)目的。下面的步骤显示了如何使用它。

1. 添加一个[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)反对[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)通过调用它的类[**创建样式**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)方法。
1. 设置[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的属性以应用格式设置。
1. 将相关属性设置为ON[**风格旗帜**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)目的。
1. 分配配置的[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)反对[**排**](https://reference.aspose.com/cells/net/aspose.cells/row)目的。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

### **格式化列**

这[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合还提供了[**列**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns)收藏。中的每一项[**列**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns)集合代表一个[**柱子**](https://reference.aspose.com/cells/net/aspose.cells/column)目的。类似于[**排**](https://reference.aspose.com/cells/net/aspose.cells/row)对象，[**柱子**](https://reference.aspose.com/cells/net/aspose.cells/column)对象还提供[**应用样式**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)格式化列的方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

## **推进主题**
- [对齐设置](/cells/zh/net/cells-alignment-settings/)
- [边框设置](/cells/zh/net/cells-border-settings/)
- [设置 Excel 和 ODS 文件的条件格式。](/cells/zh/net/conditional-formatting/)
- [Excel 主题和颜色](/cells/zh/net/excel-themes-and-colors/)
- [填充设置](/cells/zh/net/cells-fill-settings/)
- [字体设置](/cells/zh/net/cells-font-settings/)
- [在工作簿中格式化工作表 Cells](/cells/zh/net/format-worksheet-cells-in-a-workbook/)
- [实施 1904 日期系统](/cells/zh/net/implement-1904-date-system/)
- [合并和取消合并 Cells](/cells/zh/net/merging-and-unmerging-cells/)
- [号码设置](/cells/zh/net/cells-number-settings/)
- [获取和设置单元格样式](/cells/zh/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

