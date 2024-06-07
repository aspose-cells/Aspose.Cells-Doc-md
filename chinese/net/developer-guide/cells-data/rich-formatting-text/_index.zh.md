---
title: 访问和更新单元格中的富文本部分
linktitle: 富文本格式化
type: docs
weight: 40
url: /zh/net/access-and-update-the-portions-of-rich-text-of-cell/
description: 学习如何通过Aspose.Cells for .NET API访问并更新单元格中的富文本部分。
keywords: 访问和更新单元格中的富文本、获取单元格的富文本、编辑单元格的富文本、访问单元格的富文本、更新单元格的富文本、更改单元格的富文本
---

{{% alert color="primary" %}}

Aspose.Cells允许您访问并更新单元格中富文本的部分。为此，您可以使用[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index)和[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)方法。这些方法将返回和接受一系列[**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)对象，您可以使用这些对象访问并更新字体的各种属性，如字体名称、字体颜色、粗体等。

{{% /alert %}}

## **访问和更新单元格中的富文本部分**

以下代码演示了如何使用[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index)和[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)方法，使用[源Excel文件](5112369.xlsx) ，您可以从提供的链接下载。源Excel文件中的单元格A1中有富文本。它有3个部分，每个部分都有不同的字体。以下代码段访问这些部分，并将第一个部分更新为新的字体名称。最后，将工作簿保存为[输出Excel文件](5112366.xlsx)。当您打开它时，您会发现文本的第一个部分的字体已更改为"Arial"。

### 用于访问和更新单元格中的富文本部分的C#代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

### 由示例代码生成的控制台输出

这是使用[源Excel文件](5112369.xlsx)的上述示例代码生成的控制台输出。

{{< highlight java >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}

