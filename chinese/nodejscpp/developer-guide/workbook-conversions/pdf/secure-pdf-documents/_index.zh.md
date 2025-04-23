---
title: 通过 Node.js 和 C++ 使用 Node.js 安全保护 PDF 文档
linktitle: 安全的 PDF 文档
type: docs
weight: 120
url: /zh/nodejs-cpp/secure-pdf-documents/
description: 学习如何使用所有者密码和用户密码保护 PDF 文档，并使用 Aspose.Cells for Node.js via C++ 设置 PDF 文件的权限。
---

{{% alert color="primary" %}}

有时，开发人员需要处理加密的PDF文件。例如：

- 通过所有者密码和用户密码保护文档，以防止任何人都能打开它。
- 在打开文档之后，设置文档的限制或权限。例如，限制文档内容是否可以打印或提取。

本文解释了在将电子表格保存为PDF时如何传递PDF安全选项。

{{% /alert %}}

 Aspose.Cells 提供 [**PdfSecurityOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsecurityoptions/) 支持安全性功能。保存为 PDF 时，可以设置所有者密码和用户密码。加密的 PDF 文件需要这些密码才能打开查看。

- 用户密码可以为空或空字符串；在这种情况下，打开 PDF 文档时不需要用户密码。
 使用正确的所有者密码打开 PDF，允许完全访问（没有任何访问限制）。
- 使用正确的用户密码打开PDF文档（或打开没有用户密码的文档）允许进行有限访问，如权限所述。

下面的示例代码描述了如何使用Aspose.Cells保护PDF文件。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const saveOption = new AsposeCells.PdfSaveOptions();
saveOption.setSecurityOptions(new AsposeCells.PdfSecurityOptions());

saveOption.getSecurityOptions().setUserPassword("user");
saveOption.getSecurityOptions().setOwnerPassword("owner");
saveOption.getSecurityOptions().setExtractContentPermission(false);
saveOption.getSecurityOptions().setPrintPermission(false);

workbook.save(path.join(dataDir, "securepdf_test.out.pdf"), saveOption);
```

{{% alert color="primary" %}}

如果电子表格包含公式，最好在将其呈现为PDF之前调用[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)。这样可以确保重新计算依赖公式的值，并且在PDF中呈现正确的值。

{{% /alert %}}
