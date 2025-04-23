---
title: 禁用导出框架脚本与文档属性，使用 C++ 通过 Node.js
linktitle: 在保存为HTML时禁用导出框架脚本和文档属性
type: docs
weight: 310
url: /zh/nodejs-cpp/disable-exporting-frame-scripts-and-document-properties/
description: 学习如何在使用 Aspose.Cells for Node.js via C++ 将工作簿转换为 HTML 时禁用导出框架脚本和文档属性。
--- 

{{% alert color="primary" %}}

Aspose.Cells 在将工作簿转换为 HTML 时会导出框架脚本和文档属性。8.6.0 版本的 Aspose.Cells for Node.js via C++ 引入了一个选项，允许您可选择禁用导出框架脚本和文档属性。请使用 `HtmlSaveOptions.exportFrameScriptsAndProperties` 属性禁用导出。

{{% /alert %}}

## **禁用导出框架脚本和文档属性**

以下示例代码允许您禁用导出框架脚本和文档属性。一旦您将工作簿转换为HTML，输出文件将不包含任何框架脚本和文档属性。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the required workbook to convert
const filePath = path.join(dataDir, "Sample1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Disable exporting frame scripts and document properties
const options = new AsposeCells.HtmlSaveOptions();
options.setExportFrameScriptsAndProperties(false);

// Save workbook as HTML
workbook.save(path.join(dataDir, "output.out.html"), options);
```
