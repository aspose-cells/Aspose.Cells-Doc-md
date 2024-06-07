---
title: 对齐设置
type: docs
weight: 20
url: /zh/java/cells-alignment-settings/
---

## **配置对齐设置**

## **Microsoft Excel中的对齐设置**

任何使用Microsoft Excel格式化单元格的人都将熟悉Microsoft Excel中的对齐设置。

如您从上图看到的，有不同种类的对齐选项：

- 文本对齐(水平和垂直)
- 缩进。
- 方向。
- 文本控制。
- 文本方向。

Aspose.Cells完全支持所有这些对齐设置，并在下面更详细地讨论。

## **Aspose.Cells中的对齐设置**

Aspose.Cells为[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类提供[**GetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle)和[**SetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle)方法，用于获取和设置单元格的格式设置。[**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style)类提供了配置对齐设置的有用属性。

使用[**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype)枚举选择任何文本对齐类型。[**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype)枚举中预定义的文本对齐类型有:

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

您还可以使用[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsJustifyDistributed)属性应用两端分散设置。

{{% /alert %}}

## **水平，垂直对齐和缩进**

使用[**HorizontalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#horizontalalignment)属性水平对齐文本，使用[**VerticalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#verticalalignment)属性垂直对齐文本。
可以使用[**IndentLevel**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IndentLevel)属性设置单元格中文本的缩进级别。 
只有在水平对齐为左对齐或右对齐时才会生效。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-1.java" >}}


## **方向**

可以使用[**RotationAngle**](https://reference.aspose.com/cells/java/com.aspose.cells/style#RotationAngle)属性设置单元格中文本的方向（旋转）。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-Orientation-1.java" >}}

## **文本控制**

以下部分讨论如何通过设置文本换行、适应和其他格式设置选项来控制文本。

### **文本换行**

在单元格中换行文本可以使其更易于阅读：单元格的高度会调整以适应所有文本，而不是截断文本或溢出到相邻单元格中。使用[**IsTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped)属性打开或关闭文本换行。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LineBreakTextWrapping-WrapText-1.java" >}}

### **缩小以适应**

在字段中换行文本的一个选项是缩小文本大小以适应单元格的尺寸。通过将[**ShrinkToFit**](https://reference.aspose.com/cells/java/com.aspose.cells/style#ShrinkToFit)属性设置为**true**来实现。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ShrinkingToFit-1.java" >}}

### **合并单元格**

与Microsoft Excel一样，Aspose.Cells支持将多个单元格合并为一个单元格。Aspose.Cells提供了两种方法来完成这个任务。一种方法是调用[**Merge**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)）方法。该方法使用以下参数来合并单元格：

- 第一行：开始合并的第一行。
- 第一列：从哪里开始合并的第一列。
- 行数：要合并的行数。
- 列数：要合并的列数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "MergingCellsInWorksheet.-1.java" >}}


### **文本方向**

可以设置单元格中文本的阅读顺序。 阅读顺序是显示字符、单词等的视觉顺序。 例如，英语是一种从左到右的语言，而阿拉伯语是一种从右到左的语言。

阅读顺序使用[**TextDirection**](https://reference.aspose.com/cells/java/com.aspose.cells/style#TextDirection)属性进行设置。Aspose.Cells在[**TextDirectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextDirection)枚举中提供了预定义的文本方向类型。

|**文本方向类型**|**描述**|
| :- | :- |
|Context|与第一个输入字符的语言一致的阅读顺序|
|LeftToRight|从左到右的阅读顺序|
|RightToLeft|从右到左的阅读顺序|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ChangeTextDirection-1.java" >}}

## **高级主题**
- [更改单元格对齐方式并保留现有格式](/cells/zh/java/change-cells-alignment-and-keep-existing-formatting/)
- [换行和文本换行](/cells/zh/java/line-breaks-and-text-wrapping/)
