---
title: 在使用 C++ 通过 Node.js 保存为 HTML 时禁用 CSS
linktitle: 禁用CSS在保存为HTML时
type: docs
weight: 320
url: /zh/nodejs-cpp/disable-css-while-saving-to-html/
description: 学习如何在使用 Aspose.Cells for Node.js via C++ 保存 Excel 文件为 HTML 时禁用 CSS。 
---

## **可能的使用场景**

当将您的 Excel 文件保存为单页面 HTML 时，通常 CSS 元素会嵌入在 HTML 文件中，并位于 HEAD 段中。如果您将此文件作为电子邮件的内容/正文附件，大多数电子邮件客户端会剥离 CSS 元素，导致排版不正确。Aspose.Cells 24.12 版本引入了一个选项，允许您可选择禁用 CSS，从而使样式可以直接应用于 HTML 元素本身。如果要将 HTML 作为电子邮件内容/正文，请使用 [**HtmlSaveOptions.getDisableCss()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableCss--) 属性并将其设置为 **true**。

## ** 禁用CSS在保存为HTML时**

以下示例代码演示了 [**HtmlSaveOptions.getDisableCss()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableCss--) 属性的用法。 

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleDisableCss.xlsx"));

// Disable CSS
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDisableCss(true);

// Save the workbook in HTML
workbook.save(path.join(outputDir, "outputDisable.html"), opts);
```
