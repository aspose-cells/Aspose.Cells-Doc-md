---
title: 将文本数字数据转换为数字
type: docs
weight: 900
url: /zh/net/convert-text-numeric-data-to-number/
description: 了解如何使用 Aspose.Cells for .NET API 将 Excel 中以文本形式存储的数字转换为数字。
keywords: excel convert text to number, excel convert text to number c#, excel convert text numeric data to number, excel convert text numeric data to number c#, excel convert numeric text to number, excel convert numeric text to number c#, excel convert numeric text to number with c#, convert numeric text to number in excel with c#, convert numeric text to number in excel with c#, convert numeric string to number in excel with c#, excel convert text numeric data to number c#, excel convert numeric string to number c#
---
##  **可能的使用场景**
有时，您希望将作为文本输入的数字数据转换为数字。您可以在 Microsoft Excel 中以文本形式输入数字，方法是在数字前添加撇号，例如 *'12345**。然后 Excel 将该数字视为字符串。 Aspose.Cells 允许您将字符串转换为数字。


## 如何将以文本形式存储的数字转换为 Excel 中的数字
您可以按照几个简单的步骤将存储为文本的数字转换为数字。
1. 选择左上角有错误指示符的任何单个单元格或单元格区域。
1. 在选定的单元格或单元格区域旁边，单击出现的错误按钮。在菜单上，单击“转换为数字”。
<br>
<img src="4.png" width=70% />
1. 如果警报按钮不可用，请选择存在此问题的列。如果您不想转换整列，则可以选择一个或多个单元格。只需确保您选择的单元格位于同一列中，否则此过程将不起作用。 “文本分列”按钮通常用于拆分列，但也可用于将单列文本转换为数字。在“数据”选项卡上，单击“文本到列”。
<br>
<img src="1.png" width=70% />
1. 单击弹出框中的“完成”按钮。
<br>
<img src="2.png" width=70% />
1. 以文本形式存储的数字将转换为数字。
<br>
<img src="3.png" width=70% />

## 如何使用 Aspose.Cells for .NET 将存储为文本的数字转换为数字
Aspose.Cells 提供[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)方法可用于将所有字符串或文本数字数据转换为数字。

以下屏幕截图显示了单元格 *A1:A17** 中的字符串编号。字符串数字左对齐。
<br>
<img src="5.png" width=70% />

这些字符串数字已使用以下命令转换为数字[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)在下面的屏幕截图中。如您所见，它们现在右对齐。
<br>
<img src="6.png" width=70% />

##  C# 将字符串数值数据转换为实际数字的代码

以下示例代码说明了如何将所有工作表中的所有字符串数值数据转换为实际数字。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.cs" >}}
