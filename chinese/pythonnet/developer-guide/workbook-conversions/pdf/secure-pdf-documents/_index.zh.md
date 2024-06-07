---
title: 安全的PDF文档
type: docs
weight: 120
url: /zh/python-net/secure-pdf-documents/
description: 学习如何在使用Aspose.Cells for Python通过.NET API将电子表格保存为PDF时传入PDF安全选项
keywords: Python编写PDF安全选项，加密PDF文档 
---

{{% alert color="primary" %}}

有时，开发人员需要处理加密的PDF文件。例如：

- 用所有者密码和用户密码保护文档，这样不是每个人都可以打开它。
- 设置文档打开后的限制或权限。例如，限制文档内容是否可以打印或提取。

本文讲解了在将电子表格保存为PDF时如何传递PDF安全选项。

{{% /alert %}}

Aspose.Cells for Python通过.NET提供了用于处理安全性的[**PdfSecurityOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/)。您可以在保存为PDF时设置所有者密码和用户密码。打开加密的PDF文档以查看时将需要所有者密码或用户密码。

- 用户密码可以为null或空串，在这种情况下，用户打开PDF文档时不需要密码。
- 使用正确的所有者密码打开PDF文档可以完全访问（没有指定的访问限制）文档。
- 使用正确的用户密码打开PDF文档（或打开没有用户密码的文档）可以有限访问，如权限指定。

下面的示例代码描述了如何使用Aspose.Cells for Python通过.NET为PDF添加安全性

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-Articles-SecurePDFDocuments-1.py" >}}

{{% alert color="primary" %}}

如果电子表格包含公式，最好在将其渲染为PDF之前调用 [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)。这样可以确保重新计算基于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}
