---
title: 访问和更新单元格的富文本部分
linktitle: 富格式文本
type: docs
weight: 40
url: /zh/net/access-and-update-the-portions-of-rich-text-of-cell/
description: 通过 Aspose.Cells for .NET API 学习如何访问和更新单元格的富文本部分。
keywords: 访问和更新单元格的富文本，获取单元格的富文本，编辑单元格的富文本，访问单元格的富文本，更新单元格的富文本，更改单元格的富文本
---

{{% alert color="primary" %}}

Aspose.Cells允许您访问和更新单元格的富文本的部分。为此，您可以使用[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index)和[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)方法。这些方法将返回并接受[**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)对象数组，您可以使用它们来访问和更新字体的各种属性，如字体名称、字体颜色、粗体等。

{{% /alert %}}

## **访问和更新单元格的富文本部分**

以下代码演示了如何使用[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index)和[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters)方法，该方法使用[source excel file](5112369.xlsx)，您可以从提供的链接中下载。源Excel文件在单元格A1中有富文本。它有3个部分，每个部分都有不同的字体。以下代码片段访问这些部分，并使用新的字体名称更新第一个部分。最后，它将工作簿另存为[output excel file](5112366.xlsx)。当您打开它时，您会发现文本的第一个部分的字体已更改为"Arial"。

###访问和更新单元格的富文本部分的C#代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

### 样本代码生成的控制台输出

以下是使用[source excel file](5112369.xlsx)的上述示例代码的控制台输出。

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

