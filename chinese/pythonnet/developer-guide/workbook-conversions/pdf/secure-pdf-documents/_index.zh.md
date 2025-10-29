---
title: 安全的 PDF 文档
type: docs
weight: 120
url: /zh/python-net/secure-pdf-documents/
description: 了解在使用Aspose.Cells for Python via .NET API保存电子表格为PDF时如何传递PDF安全选项。
keywords: Python将安全选项写入PDF，加密PDF文档 
---

{{% alert color="primary" %}}

有时，开发人员需要处理加密的PDF文件。例如：

- 通过所有者密码和用户密码保护文档，以防止任何人都能打开它。
- 在打开文档之后，设置文档的限制或权限。例如，限制文档内容是否可以打印或提取。

本文解释了在将电子表格保存为PDF时如何传递PDF安全选项。

{{% /alert %}}

Aspose.Cells for Python via .NET提供了[**PdfSecurityOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/)用于处理安全性。您可以在保存为PDF时设置所有者和用户密码。在查看加密的PDF文档时，将需要所有者密码或用户密码。

- 用户密码可以为null或空字符串，在这种情况下，用户打开PDF文档时将不需要密码。
- 使用正确的所有者密码打开PDF文档允许对文档进行完全访问（未指定任何访问限制）。
- 使用正确的用户密码打开PDF文档（或打开没有用户密码的文档）允许进行有限访问，如权限所述。

下面的示例代码描述了如何使用Aspose.Cells for Python via .NET保护PDF。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-Articles-SecurePDFDocuments-1.py" >}}

{{% alert color="primary" %}}

如果电子表格包含公式，最好在将其呈现为PDF之前调用[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)。这样可以确保重新计算依赖公式的值，并且在PDF中呈现正确的值。

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
