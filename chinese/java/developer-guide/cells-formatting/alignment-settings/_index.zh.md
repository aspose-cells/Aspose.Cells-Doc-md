---
title: 对齐设置
type: docs
weight: 20
url: /zh/java/cells-alignment-settings/
---

## **配置对齐设置**

## **Microsoft Excel中的对齐设置**

任何使用Microsoft Excel格式化单元格的人都会熟悉Microsoft Excel中的对齐设置。

从上面的图中可以看出，有不同种类的对齐选项：

- 文本对齐(水平和垂直)
- 缩进
- 方向
- 文本控制
- 文本方向

Aspose.Cells完全支持所有这些对齐设置，并在下面详细讨论。

## **Aspose.Cells中的对齐设置**

Aspose.Cells为[**GetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle)和[**SetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle)提供了[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类的方法，用于获取和设置单元格的格式。[**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style)类提供了有用的属性来配置对齐设置。

使用[**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype)枚举选择任何文本对齐类型。[**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype)枚举中预定义的文本对齐类型包括：

|**文本对齐类型**|**描述**|
| :- | :- |
|Bottom|表示底部文本对齐
|Center|表示居中文本对齐
|CenterAcross|表示跨列居中文本对齐
|Distributed|表示分散文本对齐
|Fill|表示填充文本对齐
|General|表示常规文本对齐
|Justify|表示两端对齐文本对齐
|Left|表示左对齐文本对齐
|Right|表示右对齐文本对齐
|Top|表示顶部文本对齐|
|JustifiedLow|用于阿拉伯文本具有调整的卡什达长度。|
|ThaiDistributed|分布泰文，因为每个字符被视为一个单词。|

{{% alert color="primary" %}}

您还可以使用[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsJustifyDistributed)属性应用两端对齐分布设置。

{{% /alert %}}

## **水平，垂直对齐和缩进**

使用[**HorizontalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#horizontalalignment)属性水平对齐文本，使用[**VerticalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#verticalalignment)属性垂直对齐文本。
使用[**IndentLevel**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IndentLevel)属性可以设置单元格中文本的缩进级别。 
仅在水平对齐为左对齐或右对齐时有效。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-1.java" >}}


## **方向**

使用[**RotationAngle**](https://reference.aspose.com/cells/java/com.aspose.cells/style#RotationAngle)属性设置单元格中文本的方向（旋转）。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-Orientation-1.java" >}}

## **文本控制**

以下部分讨论了如何通过设置文本换行、缩小以适应和其他格式设置选项来控制文本。

### **自动换行文本**

在单元格中进行文本换行可以更容易阅读：单元格的高度调整以适应所有文本，而不是截断或溢出到相邻单元格。使用[**IsTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped)属性设置文本换行开启或关闭。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LineBreakTextWrapping-WrapText-1.java" >}}

### **缩小以适应**

在字段中包装文本的一个选项是将文本尺寸缩小以适应单元格的尺寸。通过设置[**ShrinkToFit**](https://reference.aspose.com/cells/java/com.aspose.cells/style#ShrinkToFit)属性来实现这一点。设为**true**。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ShrinkingToFit-1.java" >}}

### **合并单元格**

像Microsoft Excel一样，Aspose.Cells支持将多个单元格合并为一个。Aspose.Cells提供了两种方法来执行此任务。一种方式是调用[**Merge**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int))方法。该方法接受以下参数来合并单元格：

- 第一行：开始合并的第一行。
- 第一列：开始合并的第一列。
- 行数：要合并的行数。
- 列数：要合并的列数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "MergingCellsInWorksheet.-1.java" >}}


### **文本方向**

可以设置单元格中文本的阅读顺序。阅读顺序是以字符、单词等显示的视觉顺序。例如，英语是从左到右的语言，而阿拉伯语是从右到左的语言。

阅读顺序是通过[**TextDirection**](https://reference.aspose.com/cells/java/com.aspose.cells/style#TextDirection)属性进行设置。Aspose.Cells在[**TextDirectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextDirection)枚举中提供预定义的文本方向类型。

|**文本方向类型**|**描述**|
| :- | :- |
|Context|与第一个输入字符的语言一致的阅读顺序
|LeftToRight|从左到右的阅读顺序
|RightToLeft|从右到左的阅读顺序

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ChangeTextDirection-1.java" >}}

## **高级主题**
- [更改单元格对齐方式并保留现有格式](/cells/zh/java/change-cells-alignment-and-keep-existing-formatting/)
- [换行和文本换行](/cells/zh/java/line-breaks-and-text-wrapping/)
