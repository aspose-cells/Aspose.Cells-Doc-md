---
title: 删除工作簿中未使用的样式
type: docs
weight: 340
url: /zh/net/remove-unused-styles-inside-the-workbook/
---
{{% alert color="primary" %}}

excel 文件中未使用的样式不仅占用空间，而且在转换为不同格式（如 PDF、HTML 等）时会导致性能问题。Aspose.Cells 提供了[**工作簿.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles)删除工作簿中所有未使用的样式。

{{% /alert %}}

下面的代码解释了它的用法[**工作簿.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles) .代码加载[模板excel文件](5115520.xlsx)您可以从提供的链接下载。它包含一个未使用的样式，名为**Aspose风格**，此样式和所有其他未使用的样式将在代码执行后被删除。

![待办事项：图像_替代_文本](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveUnusedStyles-1.cs" >}}
