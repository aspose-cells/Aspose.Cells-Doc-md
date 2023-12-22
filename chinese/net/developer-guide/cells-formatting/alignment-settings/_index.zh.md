---
title: 对齐设置
description: 在Aspose.Cells库中，您可以使用单元格对齐设置来调整文本的布局和显示。通过调整水平对齐、垂直对齐和文本换行等设置，您可以更好地控制文本在单元格中的流动方式。本文档将为您提供详细的步骤和示例代码，帮助您快速掌握如何使用Aspose.Cells进行单元格对齐设置。
keywords: Aspose.Cells, cell alignment, horizontal alignment, vertical alignment, text wrapping
type: docs
weight: 20
url: /zh/net/cells-alignment-settings/
---
##  **配置对齐设置**

###  **Microsoft Excel 中的对齐设置**

任何使用过 Microsoft Excel 设置单元格格式的人都会熟悉 Microsoft Excel 中的对齐设置。

从上图可以看出，有不同种类的对齐选项：

- 文本对齐（水平和垂直）
- 缩进。
- 方向。
- 文本控制。
- 文字方向。

Aspose.Cells 完全支持所有这些对齐设置，并将在下面进行更详细的讨论。

###  **Aspose.Cells 中的对齐设置**

Aspose.Cells提供一堂课，[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Excel 文件。这[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中的每个工作表的集合。工作表由以下形式表示[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏。中的每一项[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合代表一个对象[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级。

 Aspose.Cells提供[**获取样式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)和[**设置样式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)的方法[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)用于获取和设置单元格格式的类。这[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)类提供了用于配置对齐设置的有用属性。

使用选择任何文本对齐类型[**文本对齐类型**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype)枚举。预定义的文本对齐类型[**文本对齐类型**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype)枚举有：

|**文本对齐类型**|**描述**|
| :- | :- |
|底部|代表底部文本对齐方式|
|中心|代表文本居中对齐|
|中心交叉|代表文本居中对齐|
|分散式|代表分布式文本对齐方式|
|充满|代表填充文本对齐方式|
|一般的|表示一般文本对齐方式|
|证明合法|代表对齐文本对齐方式|
|左边|代表文本左对齐|
|正确的|代表文本右对齐|
|顶部|代表顶部文本对齐|
|合理低位|将文本与阿拉伯文本的调整后的 kashida 长度对齐。|
|泰国分布式|特别分发泰语文本，因为每个字符都被视为一个单词。|

{{% alert color="primary" %}}

您还可以使用以下命令应用对齐分布式设置[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed)财产。

{{% /alert %}}

####  **水平对齐**

使用[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**水平对齐**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment)属性来水平对齐文本。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

####  **垂直对齐**

与水平对齐类似，使用[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**垂直对齐**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment)属性垂直对齐文本。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

####  **缩进**

可以使用以下命令设置单元格中文本的缩进级别[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**缩进级别**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel)财产。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

####  **方向**

使用以下命令设置单元格中文本的方向（旋转）[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**旋转角度**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle)财产。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

####  **文本控制**

以下部分讨论如何通过设置文本换行、缩小以适合和其他格式选项来控制文本。

#####  **文字换行**

将文本换行在单元格中使其更易于阅读：单元格的高度会调整以适合所有文本，而不是将其剪切或溢出到相邻单元格中。使用以下命令打开或关闭文本换行[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**文本是否换行**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)财产。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

#####  **缩小以适应**

在字段中换行文本的一个选项是缩小文本大小以适合单元格的尺寸。这是通过设置来完成的[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**文本是否换行**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)属性为 *true**。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

#####  **合并Cells**

与 Microsoft Excel 一样，Aspose.Cells 支持将多个单元格合并为一个单元格。 Aspose.Cells 提供了两种方法来完成此任务。一种方法是调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏的[**合并**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)方法。这[**合并**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)方法采用以下参数来合并单元格：

- 第一行：从开始合并的第一行。
- 第一列：从哪里开始合并的第一列。
- 行数：要合并的行数。
- 列数：要合并的列数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

另一种方法是首先调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏的[**创建范围**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index)方法创建要合并的单元格范围。这[**创建范围**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index)方法采用与方法相同的参数集[**合并**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)上面讨论的方法并返回一个[**范围**](https://reference.aspose.com/cells/net/aspose.cells/range)目的。这[**范围**](https://reference.aspose.com/cells/net/aspose.cells/range)对象还提供了一个[**合并**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge)合并指定范围的方法[**范围**](https://reference.aspose.com/cells/net/aspose.cells/range)目的。

#####  **文字方向**

可以设置单元格中文本的阅读顺序。阅读顺序是字符、单词等显示的视觉顺序。例如，英语是从左到右的语言，而阿拉伯语是从右到左的语言。

阅读顺序设置为[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**文本方向**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection)财产。 Aspose.Cells 提供预定义的文本方向类型[**文本方向类型**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype)枚举。

|**文本方向类型**|**描述**|
| :- | :- |
|语境|阅读顺序与第一个输入字符的语言一致|
|左到右|从左到右的阅读顺序|
|右到左|从右到左的阅读顺序|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

##  **高级主题**
- [更改 Cells 对齐方式并保留现有格式](/cells/zh/net/change-cells-alignment-and-keep-existing-formatting/)
- [换行和文本换行](/cells/zh/net/line-breaks-and-text-wrapping/)

