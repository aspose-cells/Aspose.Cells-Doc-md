---
title: 对齐设置
linktitle: 对齐设置
description: 在Aspose.Cells库中，可以使用单元格对齐设置通过Node.js与C++调整文本的布局和显示。本文提供详细步骤和示例代码，用于设置单元格对齐。
keywords: Aspose.Cells，单元格对齐，水平对齐，垂直对齐，文本换行 Node.js通过C++
type: docs
weight: 20
url: /zh/nodejs-cpp/cells-alignment-settings/
---

## **配置对齐设置**

### **Microsoft Excel中的对齐设置**

任何使用Microsoft Excel格式化单元格的人都会熟悉Microsoft Excel中的对齐设置。

从上面的图中可以看出，有不同种类的对齐选项：

- 文本对齐(水平和垂直)
- 缩进
- 方向
- 文本控制
- 文本方向

Aspose.Cells完全支持所有这些对齐设置，并在下面详细讨论。

### **Aspose.Cells中的对齐设置**

Aspose.Cells 提供了一个类 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)，代表一个 Excel 文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) 集合，可以访问 Excel 文件中的每一个工作表。一个工作表由 [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类提供了一个 [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) 集合。[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) 集合中的每个项目代表一个 [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) 类的对象。

Aspose.Cells 提供 [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) 和 [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) 方法，用于 [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) 类中获取和设置单元格的格式。[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) 类提供了有用的属性，用于配置对齐设置。

使用 [**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype) 枚举选择任何文本对齐类型。[**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype) 枚举中预定义的文本对齐类型包括：

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

您也可以使用 [**Style.setIsJustifyDistributed(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsJustifyDistributed-boolean-) 方法应用分散对齐设置。

{{% /alert %}}

#### **水平对齐**

使用 [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) 对象的 [**setHorizontalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/#setHorizontalAlignment-textalignmenttype-) 方法水平对齐文本。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-HorizontalAlignment.js" >}}



#### **垂直对齐**

与水平对齐类似，使用 [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) 对象的 [**setVerticalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/#setVerticalAlignment-textalignmenttype-) 方法垂直对齐文本。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-VerticalAlignment.js" >}}


#### **缩进**

可以通过 [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) 对象的 [**setIndentLevel**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIndentLevel-number-) 方法设置单元格中文本的缩进级别。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-Indentation.js" >}}



#### **方向**

通过 [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) 对象的 [**setRotationAngle**](https://reference.aspose.com/cells/nodejs-cpp/style/#setRotationAngle-number-) 方法设置单元格中文本的方向（旋转）。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-Orientation.js" >}}

#### **文本控制**

以下部分讨论了如何通过设置文本换行、缩小以适应和其他格式设置选项来控制文本。

##### **自动换行文本**

在单元格中换行文本可以更容易阅读：单元格的高度会调整以适应全部文本，而不是裁剪或溢出到相邻的单元格。通过 [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) 对象的 [**setIsTextWrapped(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsTextWrapped-boolean-) 方法开启或关闭文本换行。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-WrapText.js" >}}


##### **缩小以适应**

一种字段中换行文本的选项是缩小文本大小以适应单元格尺寸。这通过将 [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) 对象的 [**setShrinkToFit(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setShrinkToFit-boolean-) 方法设置为 **true** 实现。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-ShrinkToFit.js" >}}


##### **合并单元格**

像 Microsoft Excel 一样，Aspose.Cells 支持将多个单元格合并为一个。Aspose.Cells 提供两种方法，一种是调用 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) 集合的 [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) 方法。[**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) 方法需要以下参数来合并单元格：

- 第一行：开始合并的第一行。
- 第一列：开始合并的第一列。
- 行数：要合并的行数。
- 列数：要合并的列数。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-MergeCells.js" >}}


另一种方法是首先调用 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) 集合的 [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) 方法创建要合并的单元格范围。[**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) 方法接受与上面讨论的 [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) 方法相同的参数集，并返回一个 [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) 对象。[**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) 对象还提供一个 [**merge**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--) 方法，将指定范围中的单元格范围合并。

##### **文本方向**

可以设置单元格中文本的阅读顺序。阅读顺序是以字符、单词等显示的视觉顺序。例如，英语是从左到右的语言，而阿拉伯语是从右到左的语言。

读取顺序由 [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) 对象的 [**TextDirection**](https://reference.aspose.com/cells/nodejs-cpp/style/#setTextDirection-textdirectiontype-) 属性设置。Aspose.Cells 在 [**TextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/textdirectiontype) 枚举中预定义了文本方向类型。

|**文本方向类型**|**描述**|
| :- | :- |
|Context|与第一个输入字符的语言一致的阅读顺序
|LeftToRight|从左到右的阅读顺序
|RightToLeft|从右到左的阅读顺序

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-TextDirection.js" >}}


## **高级主题**
- [更改单元格对齐方式并保留现有格式](/cells/zh/nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/)
- [换行和文本换行](/cells/zh/nodejs-cpp/line-breaks-and-text-wrapping/)

{{< app/cells/assistant language="nodejs-cpp" >}}
