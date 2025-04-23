---
title: 将列宽设置为可缩放单位如em或百分比的Node.js和C++实现
linktitle: 将列宽设置为可缩放单位如em或百分比
type: docs
weight: 130
url: /zh/nodejs-cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: 学习如何在Aspose.Cells for Node.js via C++中将列宽设置为em或百分比等可缩放单位，从而改善生成HTML表格的展示效果。
---

从电子表格生成HTML文件是非常常见的。列宽通常定义为“pt”，在许多情况下可以使用。然而，有时这种固定大小可能不适用。例如，如果容器面板宽度为600px，而生成的表格宽度超过此值，则会出现水平滚动条。为了更好地展示，可以将固定大小改为可缩放单位如em或百分比，以下示例代码中，将[**HtmlSaveOptions.getWidthScalable()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getWidthScalable--)设置为**true**来创建可缩放宽度。

可从以下链接下载示例源文件和输出文件：

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample source file
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleForScalableColumns.xlsx");
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Specify Html Save Options
const options = new AsposeCells.HtmlSaveOptions();

// Set the property for scalable width
options.setWidthScalable(true);

// Specify image save format
options.setExportImagesAsBase64(true);

// Save the workbook in Html format with specified Html Save Options
const outputFilePath = path.join(dataDir, "outsampleForScalableColumns.html");
workbook.save(outputFilePath, options);
```
