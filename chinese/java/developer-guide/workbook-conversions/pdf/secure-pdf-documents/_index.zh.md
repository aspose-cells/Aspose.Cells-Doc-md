---
title: 安全的 PDF 文档
type: docs
weight: 260
url: /zh/java/secure-pdf-documents/
description: 在从Excel文件转换时保护PDF文件。 本文演示了如何使用 Aspose.Cells for Java API 从Excel生成安全的PDF文件。
keywords: java安全的pdf文档，安全的pdf文档，excel转安全pdf，excel转安全pdf java，转换excel为安全pdf，转换excel为安全pdf java，转换excel为密码保护pdf，转换excel为密码保护pdf java，excel转密码保护pdf java，excel转密码保护pdf
---

{{% alert color="primary" %}}

有时，开发人员需要处理加密的PDF文件。例如：

- 通过所有者密码和用户密码保护文档，以防止任何人都能打开它。
- 在打开文档之后，设置文档的限制或权限。例如，限制文档内容是否可以打印或提取。

本文解释了在将电子表格保存为PDF时如何传递PDF安全选项。

{{% /alert %}}

Aspose.Cells提供了[**PdfSecurityOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions/)以处理安全性。您可以在保存为PDF时设置所有者密码和用户密码。打开加密的PDF文档以查看时将需要所有者密码或用户密码。

- 用户密码可以为null或空字符串，在这种情况下，用户打开PDF文档时将不需要密码。
- 使用正确的所有者密码打开PDF文档允许对文档进行完全访问（未指定任何访问限制）。
- 使用正确的用户密码打开PDF文档（或打开没有用户密码的文档）允许进行有限访问，如权限所述。

下面的示例代码描述如何使用 Aspose.Cells for Java API 创建安全的PDF文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

如果电子表格中包含公式，最好在渲染为 PDF 之前调用 [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--)。这将确保重新计算公式依赖的值，并在 PDF 中呈现正确的值。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
