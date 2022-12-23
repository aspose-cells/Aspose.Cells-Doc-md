---
title: 保护 PDF 文档
type: docs
weight: 120
url: /zh/net/secure-pdf-documents/
---
{{% alert color="primary" %}}

有时，开发人员需要处理加密的 PDF 文件。例如，他们需要使用用户密码和所有者密码来保护文档的安全，以免任何人都可以打开它们，或者想要限制文档内容是否可以打印或提取。

本文介绍如何在将电子表格保存到 PDF 时传入 PDF 安全选项。

{{% /alert %}}

Aspose.Cells 提供了[**Aspose.Cells.Rendering.PdfSecurity**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity)用于处理安全性的命名空间。下面的示例代码描述了如何使用 Aspose.Cells 保护 PDF。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SecurePDFDocuments-1.cs" >}}

{{% alert color="primary" %}}

如果电子表格包含公式，最好调用[**工作簿.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)就在将其呈现为 PDF 之前。这可确保重新计算公式相关值并在 PDF 中呈现正确的值。

{{% /alert %}}
