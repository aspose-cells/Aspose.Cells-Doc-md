---
title: 将文本数值数据转换为数字
type: docs
weight: 150
url: /zh/java/convert-text-numeric-data-to-number/
description: 学习如何使用Aspose.Cells for Java API将存储为文本的数字转换为数字。
keywords: excel将文本转换为数字，excel将文本转换为数字java，excel将文本数值数据转换为数字，excel将文本数值数据转换为数字java，excel将数值文本转换为数字，excel将数值文本转换为数字java，excel使用java将数值文本转换为数字，使用java在excel中将数值文本转换为数字，使用java在excel中将数值文本转换为数字，使用java在excel中将数值字符串转换为数字，excel将文本数值数据转换为数字java，excel将数值字符串转换为数字java。
---

## **可能的使用场景**
有时，您希望将输入为文本的数值数据转换为数字。您可以通过在数字前加上撇号（'）在 Microsoft Excel 中将数字输入为文本，例如**'12345**。然后 Excel 将该数字视为字符串。Aspose.Cells 允许您将字符串转换为数字。


## 在Excel中将存储为文本的数字转换为数字
您可以通过几个简单的步骤将存储为文本的数字转换为数字。
1. 选择具有错误指示器的任何单个单元格或单元格范围。
1. 在所选单元格或单元格范围旁边，单击出现的错误按钮。在菜单上，单击转换为数字。 
<br>
<img src="4.png" width=70% />
1. 如果警报按钮不可用，请选择具有此问题的列。如果您不想转换整个列，可以选择一个或多个单元格。只需确保您选择的单元格位于同一列，否则该过程将无法正常工作。文本到列按钮通常用于拆分列，但也可用于将单列文本转换为数字。在“数据”选项卡上，单击“文本到列”。
<br>
<img src="1.png" width=70% />
1. 单击弹出框中的完成按钮。
<br>
<img src="2.png" width=70% />
1. 存储为文本的数字将被转换为数字。
<br>
<img src="3.png" width=70% />

## 使用Aspose.Cells for JAVA将存储为文本的数字转换为数字
Aspose.Cells for Java API提供了一个方法，可用于将所有字符串或文本数字数据转换为数字。

以下截图显示了单元格**A1:A17**中的字符串数字。 字符串数字左对齐。
<br>
<img src="5.png" width=70% />

以下截图显示了使用[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue())将这些字符串数字转换为数字。如您所见，它们现在居中对齐。
<br>
<img src="6.png" width=70% />

## 将字符串数字数据转换为实际数字的Java代码
以下示例代码说明了如何将所有工作表中的字符串数值数据转换为实际数值。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertTextNumericDatatoNumber-ConvertTextNumericDatatoNumber.java" >}}
