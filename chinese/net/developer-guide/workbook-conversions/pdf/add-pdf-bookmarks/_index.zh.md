---
title: 添加PDF书签
type: docs
weight: 10
url: /zh/net/add-pdf-bookmarks/
---

{{% alert color="primary" %}}

本文提供了将电子表格转换为PDF时如何插入PDF书签的信息。

Aspose.Cells允许您动态添加书签。 PDF书签可以大大提高长文档的可导航性。 添加书签链接到PDF文档时，您可以精确控制希望的精确视图，您不限于链接到页面。 您可以通过定位目标页来设置精确视图，然后创建书签。

{{% /alert %}}

请参考以下示例代码，了解如何添加PDF书签。该代码生成一个简单的工作簿，指定具有目标位置的PDF书签，并生成PDF文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddPDFBookmarks-1.cs" >}}

{{% alert color="primary" %}}

如果您的电子表格中含有公式，最好在将电子表格呈现为PDF格式之前调用 [**Workbook.CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)。这样可以确保依赖公式的值在PDF中正确刷新和呈现。

{{% /alert %}}
