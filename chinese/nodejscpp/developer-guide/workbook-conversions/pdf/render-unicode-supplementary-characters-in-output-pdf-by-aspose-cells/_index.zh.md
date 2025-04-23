---
title: 在输出 PDF 中渲染补充 Unicode 字符 Aspose.Cells for Node.js via C++
linktitle: 通过Aspose.Cells在输出PDF中呈现Unicode补充字符
type: docs
weight: 350
url: /zh/nodejs-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 在输出 PDF 中渲染 Unicode 补充字符。 
---

{{% alert color="primary" %}}

普通的Unicode字符长为2个字节，而Unicode补充字符长为4个字节。Aspose.Cells现在支持呈现这些4字节Unicode字符。

在Unicode字符标准中，补充字符是指分配的代码点范围从U+10000到U+10FFFF。换句话说，这些是大于U+FFFF的Unicode字符。

- 在UTF-8中，这些字符每个都是4个字节长。
- 在UTF-16中，这些字符需要2个代理对（16位单位）。

{{% /alert %}}

## 使用 Aspose.Cells for Node.js via C++ 在输出 PDF 中渲染 Unicode 补充字符

以下截图展示了 Aspose.Cells 如何将 [源 Excel 文件](5115563.xlsx) 转换为 [输出 PDF](5115564.pdf)。可以看到所有三个 Unicode 补充字符都被准确渲染，与 Microsoft Excel 完全一致。

![todo:image_alt_text](output.png)

## 示例代码

您可以使用此示例代码将[源Excel文件](5115563.xlsx)转换为[输出PDF](5115564.pdf)。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source excel file containing Unicode Supplementary characters
const workbook = new AsposeCells.Workbook(path.join(dataDir, "unicode-supplementary-characters.xlsx"));

// Save the workbook
workbook.save(path.join(dataDir, "RenderUnicodeInOutput_out.pdf"));
```
