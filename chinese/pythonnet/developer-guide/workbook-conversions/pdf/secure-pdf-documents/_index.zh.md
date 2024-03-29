---
title: 安全 PDF 文件
type: docs
weight: 120
url: /zh/python-net/secure-pdf-documents/
description: 了解如何在使用 Aspose.Cells for Python via .NET API 将电子表格保存到 PDF 时传入 PDF 安全选项。
keywords: Python write security options to pdf, encrypt PDF document 
---
{{% alert color="primary" %}}

有时，开发人员需要使用加密的 PDF 文件。例如：

- 使用所有者和用户密码保护文档，这样任何人都可以打开它。
- 打开文档后对文档设置限制或权限。例如限制文档内容是否可以打印或提取。

本文介绍了在将电子表格保存到 PDF 时如何传入 PDF 安全选项。

{{% /alert %}}

 Aspose.Cells for Python via .NET 提供[**Pdf安全选项**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/)用于安全工作。保存到 PDF 时，您可以设置所有者和用户密码。打开加密的 PDF 文档进行查看时需要所有者密码或用户密码。

- 用户密码可以为空或空字符串，在这种情况下，打开 PDF 文档时不需要用户输入密码。
- 使用正确的所有者密码打开 PDF 文档可以完全访问该文档（没有指定任何访问限制）。
- 使用正确的用户密码打开 PDF 文档（或打开没有用户密码的文档）将允许按照指定的权限进行有限访问。

下面的示例代码介绍了如何使用 Aspose.Cells for Python via .NET 保护 PDF。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-Articles-SecurePDFDocuments-1.py" >}}

{{% alert color="primary" %}}

如果电子表格包含公式，最好调用[**工作簿.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)就在将其渲染到 PDF 之前。这可确保重新计算公式相关值，并在 PDF 中渲染正确的值。

{{% /alert %}}
