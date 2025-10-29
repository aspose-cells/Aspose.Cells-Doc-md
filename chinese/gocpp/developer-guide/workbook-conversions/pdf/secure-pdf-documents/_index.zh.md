---
title: 通过C++用Golang加密PDF文档
linktitle: 安全的 PDF 文档
type: docs
weight: 120
url: /zh/go-cpp/secure-pdf-documents/
description: 学习如何使用Golang通过C++使用Aspose.Cells为PDF文档设置所有者和用户密码以保障安全。
---

{{% alert color="primary" %}}

有时，开发人员需要处理加密的PDF文件。例如：

- 通过所有者密码和用户密码保护文档，以防止任何人都能打开它。
- 在打开文档之后，设置文档的限制或权限。例如，限制文档内容是否可以打印或提取。

本文解释了在将电子表格保存为PDF时如何传递PDF安全选项。

{{% /alert %}}

 Aspose.Cells 提供 [**PdfSecurityOptions**](https://reference.aspose.com/cells/go-cpp/pdfsecurityoptions/) 支持安全性功能。保存为 PDF 时，可以设置所有者密码和用户密码。加密的 PDF 文件需要这些密码才能打开查看。

- 用户密码可以为null或空字符串，在这种情况下，用户打开PDF文档时将不需要密码。
 使用正确的所有者密码打开 PDF，允许完全访问（没有任何访问限制）。
- 使用正确的用户密码打开PDF文档（或打开没有用户密码的文档）允许进行有限访问，如权限所述。

下面的示例代码描述了如何使用Aspose.Cells保护PDF文件。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SecurePdfDocuments.go" >}}
{{% alert color="primary" %}}

 如果电子表格包含公式，建议在渲染为 PDF 之前调用 [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/)，确保公式相关的值被重新计算，生成正确的值。

{{% /alert %}}
