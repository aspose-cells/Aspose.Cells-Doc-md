---
title: 在 Aspose.Cells for Node.js via C++ 中使用 FormulaText 函数
linktitle: 在Aspose.Cells中使用FormulaText函数
description: 本文介绍了如何使用 Aspose.Cells 库中的 FormulaText 函数处理 Microsoft Excel 中的公式。学习如何获取和设置单元格的公式文本，以及使用 Node.js via C++ 保存修改后的 Excel 文件。
keywords: Aspose.Cells，Excel，FormulaText 函数，Node.js via C++
type: docs
weight: 60
url: /zh/nodejs-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText 是 Excel 2013 及之后版本的函数。不支持旧版本如 Excel 2010 或 2007 等。如其名所示，它会显示给定单元格中公式的文本。本文将展示如何使用 Aspose.Cells for Node.js via C++ 调用此函数。

{{% /alert %}} 

以下示例代码演示如何在 Aspose.Cells for Node.js via C++ 中使用 FormulaText。代码首先在单元格 A1 输入一个公式，然后在 A2 单元格使用 FormulaText 打印出该公式的文本。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create a workbook object
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some formula in cell A1
const cellA1 = worksheet.getCells().get("A1");
cellA1.setFormula("=Sum(B1:B10)");

// Get the text of the formula in cell A2 using FORMULATEXT function
const cellA2 = worksheet.getCells().get("A2");
cellA2.setFormula("=FormulaText(A1)");

// Calculate the workbook
workbook.calculateFormula();

// Print the results of A2, It will now print the text of the formula inside cell A1
console.log(cellA2.getStringValue());
```
## **控制台输出**
这是上面示例代码的控制台输出。

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
