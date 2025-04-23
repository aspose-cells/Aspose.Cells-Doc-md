---
title: 在使用 C++ 通过 Node.js 保存为 HTML 时禁用下层显示的评论
linktitle: 在保存为HTML时禁用旧版条件注释的显示
type: docs
weight: 20
url: /zh/nodejs-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: 学习如何在使用 Aspose.Cells for Node.js via C++ 将 Excel 文件保存为 HTML 时禁用下层显示的评论。
---

## **可能的使用场景**

当你将 Excel 文件保存为 HTML 时，Aspose.Cells 会显露 Downlevel 条件评论。这些条件评论大多与较旧版本的 IE 相关，与现代浏览器无关。你可以在以下链接详细了解它们。

- [条件注释 - Downlevel-revealed conditional comment](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells for Node.js via C++ 允许通过将 [**HtmlSaveOptions.getDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableDownlevelRevealedComments--) 属性设置为 **true** 来消除这些下层显示的评论。

## **在保存为HTML时禁用下级可见的批注**

以下示例代码展示了 [**HtmlSaveOptions.getDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableDownlevelRevealedComments--) 属性的用法。截图显示了未将此属性设置为 true 时的效果。请下载此代码用的[示例 Excel 文件](50528257.xlsx) 和生成的[输出 HTML](50528258.zip) 以供参考。

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **示例代码**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleDisableDownlevelRevealedComments.xlsx"));

// Disable DisableDownlevelRevealedComments
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDisableDownlevelRevealedComments(true);

// Save the workbook in html
workbook.save(path.join(outputDir, "outputDisableDownlevelRevealedComments_true.html"), opts);
```
