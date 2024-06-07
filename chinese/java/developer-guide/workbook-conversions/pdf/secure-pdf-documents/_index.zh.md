---
title: 安全的PDF文档
type: docs
weight: 260
url: /zh/java/secure-pdf-documents/
description: 使用Aspose.Cells for Java API从Excel生成安全的PDF文件。本文演示了如何使用Aspose.Cells for Java API从Excel生成安全的PDF文件。
keywords: 安全的PDF文档java，安全的PDF文档，Excel转安全的PDF，Excel转安全的PDF java，转换Excel为安全的PDF，转换Excel为安全的PDF java，将Excel转为受密码保护的PDF，将Excel转为受密码保护的PDF java，Excel转为受密码保护的PDF java，Excel转为受密码保护的PDF
---

{{% alert color="primary" %}}

有时，开发人员需要处理加密的PDF文件。例如：

- 用所有者密码和用户密码保护文档，这样不是每个人都可以打开它。
- 设置文档打开后的限制或权限。例如，限制文档内容是否可以打印或提取。

本文讲解了在将电子表格保存为PDF时如何传递PDF安全选项。

{{% /alert %}}

Aspose.Cells提供[**PdfSecurityOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions/)来处理安全。您可以在保存为PDF时设置所有者密码和用户密码。打开加密的PDF文档查看时将需要所有者密码或用户密码。

- 用户密码可以为null或空串，在这种情况下，用户打开PDF文档时不需要密码。
- 使用正确的所有者密码打开PDF文档可以完全访问（没有指定的访问限制）文档。
- 使用正确的用户密码打开PDF文档（或打开没有用户密码的文档）可以有限访问，如权限指定。

下面的示例代码描述了如何使用Aspose.Cells for Java API创建受保护的PDF文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

如果电子表格包含公式，最好在将其渲染为PDF之前调用[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()。这样可以确保重新计算公式依赖的值，并在PDF中呈现正确的值。

{{% /alert %}}
