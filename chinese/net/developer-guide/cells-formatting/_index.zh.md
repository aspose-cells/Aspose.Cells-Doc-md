---
title: 格式化单元格
description: 了解如何在Aspose.Cells for .NET中格式化和样式化单元格，包括数字格式化、日期格式化、字体样式和其他单元格样式选项。我们的指南将帮助您创建具有吸引力和专业外观的电子表格。
keywords: Aspose.Cells for .NET，单元格格式，样式，数字格式化，日期格式化，字体样式，单元格样式选项，电子表格，创建，专业外观，格式化行和列。
linktitle: 格式化单元格
type: docs
weight: 120
url: /zh/net/cells-formatting/
---

## **介绍**

{{% alert color="primary" %}}

Aspose.Cells提供了[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell)类的[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)和[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)方法，用于获取/设置单元格的格式样式。Aspose.Cells还提供了[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)类。

{{% /alert %}}

## **如何使用GetStyle和SetStyle方法格式化单元格**

在单元格上应用不同种类的格式样式，设置背景或前景颜色、边框、字体、水平和垂直对齐、缩进级别、文本方向、旋转角度等等。

### **如何使用GetStyle和SetStyle方法**

如果开发人员需要对不同的单元格应用不同的格式样式，则最好使用[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)的单元格使用[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)方法获取，指定样式属性，然后使用[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)方法应用格式。下面的示例演示了这种方法在单元格上应用各种格式的方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

### **如何使用样式对象来格式化不同的单元格**

如果开发人员需要将相同的格式样式应用于不同的单元格，则可以使用[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象。请按照以下步骤使用[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象：

1.通过调用[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类的[**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)方法添加一个[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象
1.访问新添加的[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象
1.设置[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的所需属性/属性以应用所需的格式设置
1.分配配置的[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象至您想要的单元格

这种方法可以极大地提高您的应用程序的效率，并节省内存。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

### **如何使用Microsoft Excel 2007预定义样式**

如果您需要为Microsoft Excel 2007应用不同的格式样式，请使用Aspose.Cells API应用样式。下面的示例演示了这种方法在单元格上应用预定义样式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



## **如何在单元格中格式化选定的字符**

处理字体设置解释了如何在单元格中格式化文本，但仅解释了如何格式化单元格中的所有内容。如果您只想格式化选定的字符，该怎么办？

Aspose.Cells也支持这个功能。本主题解释了如何有效使用这个功能。

### **如何格式化选定的字符**

Aspose.Cells提供了一个代表Microsoft Excel文件的类[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含了一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合中的每个项都代表[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类的一个对象。

[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类提供了[**Characters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)方法，该方法使用以下参数选择单元格内的一段字符范围：

- **起始索引**，选择开始的字符的索引。
- **字符数**，要选择的字符数。

[**Characters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)方法返回一个[**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)类的实例，允许开发人员以与单元格相同的方式格式化字符，如下代码示例所示。在输出文件中，A1单元格中，'Visit'这个词将使用默认字体格式，但'Aspose!'是粗体和蓝色。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

如果您有兴趣在单元格中格式化一部分富文本，请考虑使用[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters)和[**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)方法。[[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) 方法用于访问文本的部分，然后可以使用[**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)方法进行修改，而**Get**方法返回一个[**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) 对象的数组，可以进行操作以设置各种属性，如字体名称、字体颜色、粗体等。并且**Set**方法可用于应用更改。

{{% /alert %}}

## **如何格式化行和列**

有时，开发人员需要在行或列上应用相同的格式。逐个对单元格应用格式通常需要更长时间，而且并非是一个好的解决办法。
为了解决这个问题，Aspose.Cells提供了一种简单快捷的方式，在本文中有详细讨论。

### **格式化行和列**

Aspose.Cells提供了一个代表Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含了一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合提供了一个[**Rows**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)集合。

### **如何格式化一行**

[**Rows**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows) 集合中的每个项都代表一个[**Row**](https://reference.aspose.com/cells/net/aspose.cells/row) 对象。[**Row**](https://reference.aspose.com/cells/net/aspose.cells/row)对象提供了[**ApplyStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) 方法，用于设置行的格式。要将相同的格式应用到一行，可以使用[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) 对象。下面的步骤显示了如何使用它。

1. 通过调用其[**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)方法向[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类添加一个[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象。
1. 将[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的属性设置为应用格式设置。
1. 为[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)对象启用相关属性。
1. 将已配置的[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象分配给[**Row**](https://reference.aspose.com/cells/net/aspose.cells/row)对象。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

### **如何格式化列**

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合还提供[**Columns**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns)集合。 [**Columns**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns)集合中的每个项目代表一个[**Column**](https://reference.aspose.com/cells/net/aspose.cells/column)对象。与[**Row**](https://reference.aspose.com/cells/net/aspose.cells/row)对象类似，[**Column**](https://reference.aspose.com/cells/net/aspose.cells/column)对象还提供[**ApplyStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)方法用于格式化列。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

## **高级主题**
- [对齐设置](/cells/zh/net/cells-alignment-settings/)
- [边框设置](/cells/zh/net/cells-border-settings/)
- [设置Excel和ODS文件的条件格式。](/cells/zh/net/conditional-formatting/)
- [Excel主题和颜色](/cells/zh/net/excel-themes-and-colors/)
- [填充设置](/cells/zh/net/cells-fill-settings/)
- [字体设置](/cells/zh/net/cells-font-settings/)
- [在工作簿中格式化工作表单元格](/cells/zh/net/format-worksheet-cells-in-a-workbook/)
- [实施1904日期系统](/cells/zh/net/implement-1904-date-system/)
- [合并和取消合并单元格](/cells/zh/net/merging-and-unmerging-cells/)
- [数字设置](/cells/zh/net/cells-number-settings/)
- [获取并设置单元格样式](/cells/zh/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

