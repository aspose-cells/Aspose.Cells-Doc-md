---
title: 删除工作簿中未使用的样式
type: docs
weight: 340
url: /zh/net/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}}

Excel 文件中的未使用样式不仅占用空间，还会在转换为不同格式（如 PDF、HTML 等）时造成性能问题。Aspose.Cells 提供了 [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles) 以删除工作簿中所有未使用的样式。

{{% /alert %}}

以下代码解释了如何使用 [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles)。这段代码加载了您可以从提供的链接中下载的 [模板 Excel 文件](5115520.xlsx)。它包含一个名为 **AsposeStyle** 的未使用样式，在执行代码后，此样式和所有其他未使用样式都将被删除。

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveUnusedStyles-1.cs" >}}
