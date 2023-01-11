﻿---
title: 将文本数值数据转换为数字
type: docs
weight: 900
url: /zh/net/convert-text-numeric-data-to-number/
description: 了解如何使用 Aspose.Cells for .NET API 将在 Excel 中存储为文本的数字转换为数字。
keywords: excel convert text to number, excel convert text to number c#, excel convert text numeric data to number, excel convert text numeric data to number c#, excel convert numeric text to number, excel convert numeric text to number c#, excel convert numeric text to number with c#, convert numeric text to number in excel with c#, convert numeric text to number in excel with c#, convert numeric string to number in excel with c#, excel convert text numeric data to number c#, excel convert numeric string to number c#
---
{{% alert color="primary" %}}

有时，您希望将作为文本输入的数字数据转换为数字。您可以在 Microsoft Excel 中将数字作为文本输入，方法是在数字前放置一个撇号，例如**'12345**.然后 Excel 将该数字视为字符串。 Aspose.Cells 允许您将字符串转换为数字。

{{% /alert %}}

Aspose.Cells 提供了[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)可用于将所有字符串或文本数字数据转换为数字的方法。

以下屏幕截图显示了单元格中的字符串编号**A1:A17**.字符串编号左对齐。

|**输入文件：作为文本字符串输入的数字**|
|:- |
|![待办事项：图片_替代_文本](convert-text-numeric-data-to-number_1.png)|

这些字符串数字已使用以下方法转换为数字[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)在下面的截图中。如您所见，它们现在是右对齐的。

|**输出文件：字符串已转换为数字**|
|:- |
|![待办事项：图片_替代_文本](convert-text-numeric-data-to-number_2.png)|

## C# 将字符串数字数据转换为实际数字的代码

以下示例代码说明了如何将所有字符串数字数据转换为所有工作表中的实际数字。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.cs" >}}