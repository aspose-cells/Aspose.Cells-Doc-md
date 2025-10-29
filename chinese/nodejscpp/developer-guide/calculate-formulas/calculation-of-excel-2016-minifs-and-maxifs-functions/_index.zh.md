---
title: 使用Node.js通过C++计算Excel 2016中的MINIFS和MAXIFS函数
description: 本文介绍如何使用Aspose.Cells库在Microsoft Excel 2016中通过Node.js的C++调用来计算MINIFS和MAXIFS函数。加载现有Excel文件或创建新文件，然后使用Aspose.Cells的方法计算这些函数并将结果保存到磁盘。
keywords: Aspose.Cells，Excel，2016，MINIFS函数，MAXIFS函数，计算，Node.js通过C++
type: docs
weight: 300
url: /zh/nodejs-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **可能的使用场景**
Microsoft Excel 2016支持MINIFS和MAXIFS函数。这些函数在Excel 2013或更早版本中不支持。Aspose.Cells for Node.js via C++也支持这些函数的计算。以下截图显示了这些函数的用法。请阅读截图中的红色注释以了解这些函数的工作原理。

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **计算Excel 2016的MINIFS和MAXIFS函数**
以下示例代码加载[示例Excel文件](5115149.xlsx)，调用[Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)方法，通过Aspose.Cells for Node.js via C++进行公式计算，然后将结果保存为[输出PDF](5115154.pdf)。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleMINIFSAndMAXIFS.xlsx");

// Load your source workbook containing MINIFS and MAXIFS functions
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Perform Aspose.Cells formula calculation
workbook.calculateFormula();

// Save the calculations result in pdf format
const options = new AsposeCells.PdfSaveOptions();
options.setOnePagePerSheet(true);
const outputFilePath = path.join(dataDir, "outputMINIFSAndMAXIFS.pdf");
workbook.save(outputFilePath, options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
