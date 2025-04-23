---
title: 在使用Node.js通过C++在工作簿中加载HTML时自动调整列和行大小
linktitle: 在加载 HTML 到工作簿时自动调整列和行
type: docs
weight: 120
url: /zh/nodejs-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: 了解如何在使用Aspose.Cells for Node.js via C++加载HTML文件时自动调整工作簿中的列和行大小。
---

## **可能的使用场景**

你可以在加载工作簿中的HTML文件时自动调整列和行大小。请将[**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--)属性设置为**true**以实现此目的。

## **加载HTML至工作簿时自适应调整列和行**

以下示例代码首先在没有任何加载选项的情况下将示例HTML加载到工作簿中，并保存为XLSX格式。然后再次加载样本文HTML，但这次将[**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--)属性设置为**true**，然后保存为XLSX格式。请下载两个输出Excel文件，即[无自动调整列行的输出Excel]和[自动调整列行的输出Excel]。下方截图显示了[**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--)属性对两个输出Excel文件的影响。

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Sample HTML.
const sampleHtml = "<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>";

// Load HTML string into memory stream.
const ms = Uint8Array.from(sampleHtml, c => c.charCodeAt(0));

// Load memory stream into workbook.
let wb = new AsposeCells.Workbook(ms);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputWithout_AutoFitColsAndRows.xlsx"));

// Specify the HTMLLoadOptions and set AutoFitColsAndRows = true.
const opts = new AsposeCells.HtmlLoadOptions();
opts.setAutoFitColsAndRows(true);

// Load memory stream into workbook with the above HTMLLoadOptions.
wb = new AsposeCells.Workbook(ms, opts);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputWith_AutoFitColsAndRows.xlsx"));
```

