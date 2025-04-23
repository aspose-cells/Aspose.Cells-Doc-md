---
title: 导出批注至HTML文件时保存Excel
linktitle: 导出Excel文件为HTML时导出注释
type: docs
weight: 40
url: /zh/nodejs-cpp/export-comments-while-saving-excel-file-to/
---

## **可能的使用场景**

 保存Excel为HTML时，批注不会被导出。但Aspose.Cells for Node.js via C++提供了此功能，通过设置[**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/)属性。如果将其设置为**true**，则HTML中也会显示Excel中的批注。

## **在将 Excel 文件保存为 HTML 时导出批注**

下面的示例代码解释了 [**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/) 属性的用法。截图展示了当它设置为 **true** 时代码对 HTML 的影响。请下载[sample Excel file](50528260.xlsx)和[generated HTML](5052826.txt)以供参考。

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample Excel file
const sourceDir = path.join(__dirname, "data");
const wb = new AsposeCells.Workbook(path.join(sourceDir, "sampleExportCommentsHTML.xlsx"));

// Export comments - set IsExportComments property to true
const opts = new AsposeCells.HtmlSaveOptions();
opts.setIsExportComments(true);

// Save the Excel file to HTML
const outputDir = path.join(__dirname, "output");
wb.save(path.join(outputDir, "outputExportCommentsHTML.html"), opts);
```
