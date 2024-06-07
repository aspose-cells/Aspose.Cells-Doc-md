---
title: 对齐设置
description: 在Aspose.Cells库中，您可以使用单元格对齐设置来调整文本的布局和显示。通过调整水平对齐、垂直对齐和文本换行等设置，您可以更好地控制文本在单元格中的流动。本文档将为您提供详细步骤和示例代码，帮助您快速掌握如何使用Aspose.Cells进行单元格对齐设置。
keywords: Aspose.Cells，单元格对齐，水平对齐，垂直对齐，文本换行
type: docs
weight: 20
url: /zh/net/cells-alignment-settings/
---

## **配置对齐设置**

### **Microsoft Excel中的对齐设置**

任何使用Microsoft Excel格式化单元格的人都将熟悉Microsoft Excel中的对齐设置。

如您从上图看到的，有不同种类的对齐选项：

- 文本对齐(水平和垂直)
- 缩进。
- 方向。
- 文本控制。
- 文本方向。

Aspose.Cells完全支持所有这些对齐设置，并在下面更详细地讨论。

### **Aspose.Cells中的对齐设置**

Aspose.Cells提供了一个类[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个Excel文件。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合中的每个项目表示[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类的对象。

Aspose.Cells为[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类提供[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)和[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)方法，用于获取和设置单元格的格式设置。[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)类提供了配置对齐设置的有用属性。

使用[**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype)枚举选择任何文本对齐类型。[**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype)枚举中预定义的文本对齐类型有:

|**文本对齐类型**|**描述**|
| :- | :- |
|Bottom|代表底部文本对齐|
|Center|代表居中文本对齐|
|CenterAcross|代表跨越式居中文本对齐|
|Distributed|代表分布式文本对齐|
|Fill|代表填充文本对齐|
|General|代表一般文本对齐|
|Justify|代表两端对齐文本对齐|
|Left|代表左文本对齐|
|Right|代表右文本对齐|
|Top|代表顶部文本对齐|
|JustifiedLow|将文本与调整后的Kashida长度对齐，用于阿拉伯文本。|
|ThaiDistributed|特别分布泰文文本，因为每个字符被视为一个单词。|

{{% alert color="primary" %}}

您还可以使用[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed)属性应用两端分散设置。

{{% /alert %}}

#### **水平对齐**

使用[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**HorizontalAlignment**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment)属性将文本水平对齐。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

#### **垂直对齐**

类似于水平对齐，使用[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**VerticalAlignment**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment)属性垂直对齐文本。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

#### **缩进**

可以使用[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**IndentLevel**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel)属性设置单元格中文本的缩进级别。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

#### **方向**

使用 [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) 对象的 [**RotationAngle**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle) 属性设置单元格中文本的方向（旋转）。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

#### **文本控制**

以下部分讨论如何通过设置文本换行、适应和其他格式设置选项来控制文本。

##### **文本换行**

在单元格中换行文本使文本更容易阅读：单元格的高度会根据文本调整以容纳所有文本，而不是将其切断或溢出到相邻单元格。 使用 [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) 对象的 [**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped) 属性设置文本换行开或关闭。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

##### **缩小以适应**

在字段中将文本换行的选择是缩小文本大小以适应单元格尺寸。 这是通过将 [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) 对象的 [**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped) 属性设置为 **true** 来完成的。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

##### **合并单元格**

与 Microsoft Excel 类似，Aspose.Cells 支持将多个单元格合并为一个。Aspose.Cells 提供两种方法来执行此任务。 一种方法是调用 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) 集合的 [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) 方法。 [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) 方法接受以下参数来合并单元格：

- 第一行：开始合并的第一行。
- 第一列：从哪里开始合并的第一列。
- 行数：要合并的行数。
- 列数：要合并的列数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

另一种方法是首先调用 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) 集合的 [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) 方法来创建要合并的单元格范围。 [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) 方法采用与上述所述 [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) 方法相同的参数集，并返回 [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) 对象。 [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) 对象还提供了一个 [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) 方法，用于合并 [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) 对象中指定的范围。

##### **文本方向**

可以设置单元格中文本的阅读顺序。 阅读顺序是显示字符、单词等的视觉顺序。 例如，英语是一种从左到右的语言，而阿拉伯语是一种从右到左的语言。

阅读顺序是通过 [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) 对象的 [**TextDirection**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection) 属性设置的。Aspose.Cells 在 [**TextDirectionType**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype) 枚举中提供了预定义的文本方向类型。

|**文本方向类型**|**描述**|
| :- | :- |
|Context|与第一个输入字符的语言一致的阅读顺序|
|LeftToRight|从左到右的阅读顺序|
|RightToLeft|从右到左的阅读顺序|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

## **高级主题**
- [更改单元格对齐方式并保留现有格式](/cells/zh/net/change-cells-alignment-and-keep-existing-formatting/)
- [换行和文本换行](/cells/zh/net/line-breaks-and-text-wrapping/)

