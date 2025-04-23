---
title: 用Node.js和C++计算页面设置缩放比例
linktitle: 计算页面设置缩放因子
type: docs
weight: 300
url: /zh/nodejs-cpp/calculate-page-setup-scaling-factor/
description: 本文提供示例代码，说明如何使用 Node.js API 与 C++ 一起，编程计算 Excel 工作表的页面设置缩放比例，采用“适合 n 页宽 m 页高”的选项。
keywords: 通过 C++ 计算 Node.js 的 Excel 页面设置缩放比例，采用“适合 n 页宽 m 页高”设置的 Excel Node.js
---

{{% alert color="primary" %}}

当你使用**适合 n 页宽 m 页高**选项设置页面缩放时，微软 Excel 会计算页面设置的缩放比例。你可以使用 [**SheetRender.getPageScale()**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#getPageScale--) 属性计算出相同的值。此属性返回一个 double 值，可以转换为百分比。例如，如果返回 0.5，则意味着缩放比例为 50%。

{{% /alert %}}

以下示例代码说明了如何使用[**SheetRender.getPageScale()**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#getPageScale--)属性计算页面设置缩放因子。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some data in these cells
worksheet.getCells().get("A4").putValue("Test");
worksheet.getCells().get("S4").putValue("Test");

// Set paper size
worksheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);

// Set fit to pages wide as 1
worksheet.getPageSetup().setFitToPagesWide(1);

// Calculate page scale via sheet render
const sr = new AsposeCells.SheetRender(worksheet, new AsposeCells.ImageOrPrintOptions());

// Convert page scale double value to percentage
const strPageScale = (sr.getPageScale() * 100).toFixed(0) + "%";

// Write the page scale value
console.log(strPageScale);
```
