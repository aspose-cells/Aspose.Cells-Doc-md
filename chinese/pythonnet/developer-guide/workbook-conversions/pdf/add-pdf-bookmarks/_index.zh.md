---
title: 添加PDF书签
type: docs
weight: 10
url: /zh/python-net/add-pdf-bookmarks/
description: 学习如何使用 Aspose.Cells for Python via .NET API 添加PDF书签。
keywords: Python添加PDF书签，使用Python添加PDF书签via NET，插入PDF书签
---

{{% alert color="primary" %}}

本文提供了将电子表格转换为PDF时如何插入PDF书签的信息。

Aspose.Cells for Python via .NET 允许您动态添加书签。PDF书签可以极大地提高长文档的可导航性。在向PDF文档添加书签链接时，您可以精确控制您想要的确切视图，您不受限于链接到某一页。您可以通过定位目标页来设置精确的视图，然后创建书签。

{{% /alert %}}

请参考以下示例代码，了解如何添加PDF书签。该代码生成一个简单的工作簿，指定具有目标位置的PDF书签，并生成PDF文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AddPDFBookmarks-1.py" >}}

{{% alert color="primary" %}}

如果您的电子表格中含有公式，最好在将电子表格呈现为PDF格式之前调用 [**Workbook.calculate_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)。这样可以确保依赖公式的值在PDF中正确刷新和呈现。

{{% /alert %}}
