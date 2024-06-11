---
title: 删除工作簿中的未使用样式
type: docs
weight: 340
url: /zh/net/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}}

Excel文件中未使用的样式不仅占用空间，而且在转换为PDF、HTML等不同格式时会导致性能问题。Aspose.Cells提供了[**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles)以删除工作簿中所有未使用的样式。

{{% /alert %}}

下面的代码解释了[**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles)的用法。该代码加载了可以从提供的链接下载的[模板Excel文件](5115520.xlsx)。它包含一个名为**AsposeStyle**的未使用样式，此样式和所有其他未使用的样式将在执行代码后被移除。

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveUnusedStyles-1.cs" >}}
