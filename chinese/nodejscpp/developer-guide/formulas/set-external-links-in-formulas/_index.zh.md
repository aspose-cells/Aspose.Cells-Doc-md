---
title: 通过 C++ 在 Node.js 中设置公式中的外部链接
linktitle: 设置公式中的外部链接
type: docs
weight: 20
url: /zh/nodejs-cpp/set-external-links-in-formulas/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 在公式中设置外部链接。 
keywords: 通过 C++ 在 Node.js 中在公式中设置外部链接，包含外部文件到公式中 
---

{{% alert color="primary" %}} 

有时需要在公式中包含指向外部文件的链接，例如对它们的单元格或范围值进行评估。Aspose.Cells for Node.js via C++ 提供了此功能，本文档介绍了如何使用它。

{{% /alert %}} 

下面的示例代码显示了如何在公式中包含外部文件。



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get first Worksheet
const sheet = workbook.getWorksheets().get(0);

// Get Cells collection
const cells = sheet.getCells();

// Set formula with external links
cells.get("A1").setFormula(`=SUM('[${filePath}]Sheet1'!A2, '[${filePath}]Sheet1'!A4)`);

// Set formula with external links
cells.get("A2").setFormula(`='[${filePath}]Sheet1'!A8`);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
