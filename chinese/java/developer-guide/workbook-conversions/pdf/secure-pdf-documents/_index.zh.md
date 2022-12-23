---
title: 保护 PDF 文档
type: docs
weight: 260
url: /zh/java/secure-pdf-documents/
description: 从 Excel 文件转换时保护 PDF 文件。本文演示了使用 Aspose.Cells for Java API 从 Excel 生成安全的 PDF 文件。
keywords: secure pdf documents java, secure pdf documents, excel to secure pdf, excel to secure pdf java, convert excel to secure pdf, convert excel to secure pdf java, convert excel to password protected pdf, convert excel to password protected pdf java, excel to password protected pdf java, excel to password protected pdf
---
{{% alert color="primary" %}}

有时，开发人员需要处理加密的 PDF 文件。例如，他们需要使用用户密码和所有者密码来保护文档的安全，以免任何人都可以打开它们，或者想要限制文档内容是否可以打印或提取。

本文介绍如何在将电子表格保存到 PDF 时传入 PDF 安全选项。

{{% /alert %}} 

Aspose.Cells API 提供[**Pdf安全选项**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSecurityOptions)处理 PDF 文件格式安全性的类。下面的示例代码描述了如何使用 Aspose.Cells for Java API 创建安全的 PDF 文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

如果电子表格包含公式，最好调用[**工作簿.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) 就在将其呈现为 PDF 之前。这可确保重新计算公式相关值，并在 PDF 中呈现正确的值。

{{% /alert %}}
