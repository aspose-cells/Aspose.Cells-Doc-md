---
title: 格式单元格
description: 了解如何在Aspose.Cells for Python via .NET中格式化和样式单元格，包括数字格式、日期格式、字体样式和其他单元格样式选项。我们的指南将帮助你创建漂亮且专业的电子表格。
keywords: Aspose.Cells for Python via .NET，单元格格式化，样式，数字格式，日期格式，字体样式，单元格样式选项，电子表格，创建，专业外观，格式化行列。
linktitle: 格式单元格
type: docs
weight: 120
url: /zh/python-net/cells-formatting/
---

## **介绍**

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET提供了 [Cell](https://reference.aspose.com/cells/python-net/aspose.cells/cell) 类的 [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) 和 [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) 方法，用于获取/设置单元格的格式样式。还提供了一个 [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) 类。

{{% /alert %}}

## **使用GetStyle和SetStyle方法格式化单元格**

在单元格上应用不同种类的格式样式，设置背景或前景颜色、边框、字体、水平和垂直对齐、缩进级别、文本方向、旋转角度等。

### **使用GetStyle和SetStyle方法**

如果开发人员需要对不同单元格应用不同的格式样式，则最好使用[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)方法获取单元格，使用[**Cell.get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style)方法指定样式属性，然后使用[**Cell.set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style)方法应用格式。下面给出了一个示例，演示了如何在单元格上应用各种格式。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.py" >}}

### **如何使用样式对象为不同单元格设置格式**

如果开发人员需要将相同的格式应用于不同的单元格，他们可以使用[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)对象。请按照下面的步骤使用[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)对象：

1. 通过调用[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类的[**create_style**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/create_style)方法添加[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)对象
1. 访问新添加的[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)对象
1. 设置[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)对象的所需属性/属性，以应用所需的格式设置
1. 将配置的[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)对象分配给所需的单元格

这种方法可以极大地提高您的应用程序的效率，并节省内存。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingStyleObject-1.py" >}}

### **如何使用Microsoft Excel 2007预定义样式**

如果你需要对Microsoft Excel 2007应用不同的格式，可以使用Aspose.Cells for Python via .NET API应用样式。以下示例演示了如何在单元格上应用预定义样式。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.py" >}}



## **如何格式化单元格中的选定字符**

处理字体设置解释了如何格式化单元格中的文本，但它只解释了如何格式化所有单元格内容。如果您只想格式化选定的字符怎么办？

Aspose.Cells for Python via .NET也支持此功能。本主题讲解了如何有效使用此功能。

### **如何格式化选定的字符**

Aspose.Cells for Python via .NET提供了一个 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类，代表一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类包含一个 [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) 集合，允许访问Excel文件中的每个工作表。一个工作表由 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类提供一个 [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) 集合。[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) 集合中的每个项代表一个 [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) 类的对象。

[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)类提供[**characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/characters)方法，该方法接受以下参数以选择单元格中的字符范围：

- **起始索引**，选择开始的字符的索引。
- **字符数**，要选择的字符数。

[**characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/characters)方法返回[**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting)类的实例，允许开发人员以与单元格相同的方式格式化字符，如下面的代码示例所示。在输出文件中，A1单元格中的'Visit'单词将使用默认字体格式，但'Aspose!'将以粗体和蓝色格式显示。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormattingSelectedCharacters-1.py" >}}

{{% alert color="primary" %}}

如果你对格式化单元格中的部分富文本感兴趣，可以考虑使用 [**Cell.get_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters) 和 [**Cell.set_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters) 方法。[**Cell.get_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters) 方法用于访问文本的部分，然后可以使用 [**Cell.set_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters) 方法进行修改，而 “Get” 方法返回一个 [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) 对象数组，可以操控设置各种属性，如字体名称、字体颜色、加粗等，使用 “Set” 方法应用更改。

{{% /alert %}}

## **如何格式化行和列**

有时，开发人员需要在行或列上应用相同的格式。逐个单元格应用格式通常需要更长时间，不是一个好的解决方案。
为了解决此问题，Aspose.Cells for Python via .NET提供了一个简单、快速的方法，详细内容请参阅本文。

### **格式化行和列**

Aspose.Cells for Python via .NET提供了一个 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类，代表一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类包含一个 [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) 集合，可以访问Excel文件中的每个工作表。一个工作表由 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类提供一个 [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) 集合。[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) 集合提供一个 [**rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/rows) 集合。

### **如何格式化一行**

集合中的每个项目代表一个[**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row)对象。[**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row)对象提供了[**apply_style**](https://reference.aspose.com/cells/python-net/aspose.cells/row/apply_style)方法，用于设置行的格式。要将相同的格式应用于一行，请使用[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)对象。以下步骤显示如何使用它。

1. 通过调用其[**create_style**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/create_style)方法向[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类添加一个[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)对象。
1. 设置[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)对象的属性以应用格式设置。
1. 使[**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag)对象的相关属性为ON。
1. 将配置的[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)对象分配给[**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row)对象。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormatRowsColumns-FormattingARow-1.py" >}}

### **如何格式化一列**

[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)集合还提供一个[**columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/columns)集合。集合中的每个项目代表一个[**Column**](https://reference.aspose.com/cells/python-net/aspose.cells/column)对象。类似于[**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row)对象，[**Column**](https://reference.aspose.com/cells/python-net/aspose.cells/column)对象还提供了[**apply_style**](https://reference.aspose.com/cells/python-net/aspose.cells/row/apply_style)方法，用于格式化列。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormatRowsColumns-FormattingAColumn-1.py" >}}

## **高级主题**
- [对齐设置](/cells/zh/python-net/cells-alignment-settings/)
- [边框设置](/cells/zh/python-net/cells-border-settings/)
- [设置Excel和ODS文件的条件格式。](/cells/zh/python-net/conditional-formatting/)
- [Excel 主题和颜色](/cells/zh/python-net/excel-themes-and-colors/)
- [填充设置](/cells/zh/python-net/cells-fill-settings/)
- [字体设置](/cells/zh/python-net/cells-font-settings/)
- [在工作簿中格式化工作表单元格](/cells/zh/python-net/format-worksheet-cells-in-a-workbook/)
- [实现1904日期系统](/cells/zh/python-net/implement-1904-date-system/)
- [合并和取消合并单元格](/cells/zh/python-net/merging-and-unmerging-cells/)
- [数字设置](/cells/zh/python-net/cells-number-settings/)
- [获取和设置单元格的样式](/cells/zh/python-net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

{{< app/cells/assistant language="python-net" >}}
