---
title: 访问和更新单元格的富文本部分
linktitle: 富格式文本
type: docs
weight: 40
url: /zh/python-net/access-and-update-the-portions-of-rich-text-of-cell/
description: 通过Aspose.Cells for Python via .NET API学习如何访问和更新单元格的富文本部分。
keywords: Python Excel库，Python访问和更新单元格的富文本，Python获取单元格的富文本，Python编辑单元格的富文本，Python访问单元格的富文本，Python更新单元格的富文本，Python更改单元格的富文本。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET允许您访问和更新单元格的富文本部分。为此，您可以使用[**Cell.get_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters/#)和[**Cell.set_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters/#list)方法。这些方法将返回和接受[**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting)对象的数组，您可以使用这些对象来访问和更新字体的各种属性，例如字体名称、字体颜色、加粗等。

{{% /alert %}}

## **访问和更新单元格的富文本部分**

以下代码演示了如何使用[source excel file](5112369.xlsx)中的[**Cell.get_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters/#)和[**Cell.set_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters/#list)方法。您可以从提供的链接下载源Excel文件。源Excel文件中的单元格A1中有富文本。它有3个部分，每个部分都有不同的字体。以下代码段访问这些部分，并使用新的字体名称更新第一个部分。最后，它将工作簿另存为[output excel file](5112366.xlsx)。当您打开它时，您会发现文本的第一部分的字体已经更改为**"Arial"**。

###访问和更新单元格的富文本部分的C#代码

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-UpdateRichTextCells-1.py" >}}

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

