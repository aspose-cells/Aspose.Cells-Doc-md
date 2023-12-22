---
title: 访问并更新Cell的富文本部分
linktitle: 丰富的格式化文本
type: docs
weight: 40
url: /zh/net/access-and-update-the-portions-of-rich-text-of-cell/
description: 了解如何通过 Aspose.Cells for .NET API 访问和更新 Cell 的富文本部分。
keywords: Access and Update Rich Text of Cell, Get Rich Text of Cell, Edit Rich Text of Cell, Access Rich Text of Cell, Update Rich Text of Cell, Change Rich Text of Cell
---
{{% alert color="primary" %}}

 Aspose.Cells 允许您访问和更新单元格的富文本部分。为此，您可以使用[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index)和[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)方法。这些方法将返回并接受数组[**字体设置**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)您可以使用这些对象来访问和更新字体的各种属性，例如字体名称、字体颜色、粗体等。

{{% /alert %}}

##  **访问并更新Cell的富文本部分**

下面的代码演示了使用[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index)和[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)方法使用[源 Excel 文件](5112369.xlsx)您可以从提供的链接下载。源 Excel 文件在单元格 A1 中包含富文本。它有 3 个部分，每个部分都有不同的字体。以下代码片段访问这些部分并使用新的字体名称更新第一部分。最后，它将工作簿另存为[输出Excel文件](5112366.xlsx)。当您打开它时，您会发现文本第一部分的字体已更改为*“Arial”**。

###  C# 用于访问和更新 Cell 富文本部分的代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

### 示例代码生成的控制台输出

这是上述示例代码的控制台输出，使用[源 Excel 文件](5112369.xlsx).

{{< highlight "java" >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}

