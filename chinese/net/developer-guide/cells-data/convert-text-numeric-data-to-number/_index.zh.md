---
title: 将文本数值数据转换为数字
type: docs
weight: 900
url: /zh/net/convert-text-numeric-data-to-number/
description: 通过 Aspose.Cells for .NET API 学习如何将 Excel 中存储的文本数字转换为数字。
keywords: Excel 将文本转换为数字，Excel 将文本转换为数字  c#，Excel 将文本数值数据转换为数字，Excel 将文本数值数据转换为数字  c#，Excel 将数值文本转换为数字，Excel 将数值文本转换为数字  c#，Excel 将数值文本转换为数字使用 c#，在 Excel 中将数值文本转换为数字使用 c#，在 Excel 中将数值文本转换为数字使用 c#，在 Excel 中将数值字符串转换为数字使用 c#，Excel 将文本数值数据转换为数字  c#，Excel 将数值字符串转换为数字  c#
---

## **可能的使用场景**
有时，您希望将输入为文本的数值数据转换为数字。您可以通过在数字前加上撇号（'）在 Microsoft Excel 中将数字输入为文本，例如**'12345**。然后 Excel 将该数字视为字符串。Aspose.Cells 允许您将字符串转换为数字。


## 如何在 Excel 中将存储为文本的数字转换为数字
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

## 如何使用 Aspose.Cells for .NET 将存储为文本的数字转换为数字
Aspose.Cells 提供了 [**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue) 方法，可以将所有字符串或文本数值数据转换为数字。

以下截图显示了单元格**A1:A17**中的字符串数字。 字符串数字左对齐。
<br>
<img src="5.png" width=70% />

这些字符串数字已经在以下截图中使用[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue) 转换为数字。 如您所见，它们现在已右对齐。
<br>
<img src="6.png" width=70% />

##将字符串数值数据转换为实际数值的C#代码

以下示例代码说明了如何将所有工作表中的字符串数值数据转换为实际数值。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.cs" >}}
