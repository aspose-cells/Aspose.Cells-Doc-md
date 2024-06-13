---
title: 将文本数值数据转换为数字
type: docs
weight: 150
url: /zh/java/convert-text-numeric-data-to-number/
description: 学习如何使用 Aspose.Cells for Java API 将存储为文本的数字转换为数字。
keywords: excel将文本转换为数字，excel将文本转换为数字java，excel将文本数值数据转换为数字，excel将文本数值数据转换为数字java，excel将数字文本转换为数字，excel将数字文本转换为数字java，excel将文本数值数据转换为数字java，excel将文本数值数据转换为数字java，将数字文本转换为数字的excel，将数字文本转换为数字的exceljava，用java将数字文本转换为数字的excel，excel将文本数值数据转换为数字java，excel将数字文本转换为数字java
---

## **可能的使用场景**
有时，您希望将以文本形式输入的数字数据转换为实际数字。您可以在Microsoft Excel中在数字前加上撇号（'）来将数字输入为文本，例如**'12345**。Excel会将该数字视为字符串。Aspose.Cells允许您将字符串转换为数字。


## 在Excel中将存储为文本的数字转换为数字
您可以按照以下几个简单步骤将存储为文本的数字转换为数字。
1. 选择任何一个具有左上角错误指示器的单元格或单元格范围。
1. 在所选单元格或单元格范围旁边，单击出现的错误按钮。在菜单上，单击转换为数字。 
<br>
<img src="4.png" width=70% />
1. 如果警报按钮不可用，请选择具有此问题的列。如果您不想转换整个列，可以选择一个或多个单元格。只需确保您选择的单元格在同一列中，否则此过程将无法工作。文本到列按钮通常用于拆分列，但也可以用于将单个文本列转换为数字。在数据选项卡上，单击文本到列。
<br>
<img src="1.png" width=70% />
1. 在弹出框中单击完成按钮。
<br>
<img src="2.png" width=70% />
1. 存储为文本的数字已转换为数字。
<br>
<img src="3.png" width=70% />

## 使用Aspose.Cells for JAVA将存储为文本的数字转换为数字
Aspose.Cells for Java API提供了[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue--)方法，可用于将所有字符串或文本数字数据转换为数字。

以下截图显示了单元格**A1:A17**中的字符串数字。字符串数字对齐到左边。
<br>
<img src="5.png" width=70% />

这些字符串数字已经使用[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue--) 转换为数字，如下面的截图所示。您可以看到，它们现在是右对齐的。
<br>
<img src="6.png" width=70% />

## 将字符串数值数据转换为实际数值的Java代码
以下示例代码说明了如何在所有工作表中将所有字符串数值数据转换为实际数值。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertTextNumericDatatoNumber-ConvertTextNumericDatatoNumber.java" >}}
