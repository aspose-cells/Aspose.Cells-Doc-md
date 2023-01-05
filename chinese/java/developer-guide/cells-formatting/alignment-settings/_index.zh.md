---
title: 对齐设置
type: docs
weight: 20
url: /zh/java/cells-alignment-settings/
---
## **配置对齐设置**

## **Microsoft Excel 中的对齐设置**

用过Microsoft Excel格式化单元格的人都会熟悉Microsoft Excel中的对齐设置。

从上图可以看出，有不同种类的对齐选项：

- 文本对齐方式（水平和垂直）
- 缩进。
- 方向。
- 文字控制。
- 文字方向。

Aspose.Cells 完全支持所有这些对齐设置，并在下面进行更详细的讨论。

## **Aspose.Cells 中的对齐设置**

Aspose.Cells提供[**获取样式**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle)和[**设置样式**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle)的方法[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)用于获取和设置单元格格式的类。这[**风格**](https://reference.aspose.com/cells/java/com.aspose.cells/style)类提供用于配置对齐设置的有用属性。

使用[**文本对齐类型**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype)枚举。中的预定义文本对齐类型[**文本对齐类型**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype)枚举是：

|**文本对齐类型**|**描述**|
|:- |:- |
|底部|表示底部文本对齐|
|中心|表示居中文本对齐|
|跨中心|表示跨文本居中对齐|
|分散式|表示分布式文本对齐|
|充满|表示填充文本对齐方式|
|一般的|表示一般文本对齐方式|
|证明合法|表示对齐文本对齐|
|剩下|表示文本左对齐|
|正确的|表示文本右对齐|
|最佳|表示顶部文本对齐|
|合理的低|将文本与调整后的阿拉伯文本 kashida 长度对齐。|
|泰国分布式|特别分发泰语文本，因为每个字符都被视为一个单词。|

{{% alert color="primary" %}}

您还可以使用 justify distributed 设置[**样式.IsJustifyDistributed**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsJustifyDistributed)财产。

{{% /alert %}}

## **水平、垂直对齐和缩进**

使用[**水平对齐**](https://reference.aspose.com/cells/java/com.aspose.cells/style#horizontalalignment)水平对齐文本的属性和[**垂直对齐**](https://reference.aspose.com/cells/java/com.aspose.cells/style#verticalalignment)垂直对齐文本的属性。
可以设置单元格中文本的缩进级别[**缩进级别**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IndentLevel)财产
而 tt 仅在水平对齐为左或右时有效。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-1.java" >}}


## **方向**

设置单元格中文本的方向（旋转）[**旋转角度**](https://reference.aspose.com/cells/java/com.aspose.cells/style#RotationAngle)财产。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-Orientation-1.java" >}}

## **文字控制**

以下部分讨论如何通过设置文本换行、收缩以适合和其他格式设置选项来控制文本。

### **环绕文字**

在单元格中环绕文本使其更易于阅读：单元格的高度会调整以适合所有文本，而不是将其切断或溢出到相邻的单元格中。使用[**IsTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped)财产。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LineBreakTextWrapping-WrapText-1.java" >}}

### **收缩以适应**

在字段中换行文本的一个选项是缩小文本大小以适合单元格的尺寸。这是通过设置[**缩小到适合**](https://reference.aspose.com/cells/java/com.aspose.cells/style#ShrinkToFit)财产。到**真的**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ShrinkingToFit-1.java" >}}

### **合并 Cells**

与Microsoft Excel一样，Aspose.Cells支持将多个单元格合并为一个单元格。 Aspose.Cells 提供了两种方法来完成这项任务。一种方法是调用[**合并**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)） 方法。该方法采用以下参数来合并单元格：

- 第一行：从哪里开始合并的第一行。
- 第一列：从哪里开始合并的第一列。
- 行数：要合并的行数。
- 列数：要合并的列数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "MergingCellsInWorksheet.-1.java" >}}


### **文字方向**

可以设置单元格中文本的阅读顺序。阅读顺序是字符、单词等显示的视觉顺序。例如，英语是从左到右的语言，而阿拉伯语是从右到左的语言。

阅读顺序设置为[**文本方向**](https://reference.aspose.com/cells/java/com.aspose.cells/style#TextDirection)财产。 Aspose.Cells 提供预定义的文本方向类型[**文本方向类型**](https://reference.aspose.com/cells/java/com.aspose.cells/TextDirection)枚举。

|**文本方向类型**|**描述**|
|:- |:- |
|语境|与第一个输入字符的语言一致的阅读顺序|
|左到右|从左到右的阅读顺序|
|右到左|从右到左的阅读顺序|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ChangeTextDirection-1.java" >}}

## **推进主题**
- [更改 Cells 对齐并保持现有格式](/cells/zh/java/change-cells-alignment-and-keep-existing-formatting/)
- [换行和文字换行](/cells/zh/java/line-breaks-and-text-wrapping/)
