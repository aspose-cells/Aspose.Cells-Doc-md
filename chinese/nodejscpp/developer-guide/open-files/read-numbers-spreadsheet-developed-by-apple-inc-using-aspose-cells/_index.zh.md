---
title: 阅读由 Apple Inc. 开发的数字电子表格 Aspose.Cells for Node.js via C++
linktitle: 读取由Apple Inc.开发的Numbers电子表格
type: docs
weight: 140
url: /zh/nodejs-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 读取由 Apple Inc. 开发的数字电子表格。 
---

## **可能的使用场景**

Numbers 是由 Apple Inc. 开发的一款电子表格应用程序。Aspose.Cells 可以读取 Numbers 电子表格，但不支持写入。它可以读取 Numbers 电子表格中的数据、样式和公式。

## **使用 Aspose.Cells for Node.js via C++ 读取由 Apple Inc. 开发的数字电子表格**

以下示例代码加载[示例数字电子表格]（sampleNumbersByAppleInc.numbers），并将其转换为[输出 PDF 格式]（outputNumbersByAppleInc.pdf）。您需要在构造函数中使用 [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) 类并指定 [**LoadFormat.Numbers**](https://reference.aspose.com/cells/nodejs-cpp/loadformat) 作为参数来成功加载。请从提供的链接下载它们。您可以用任何数字电子表格尝试代码。也请阅读代码注释以获取更多帮助。

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleNumbersByAppleInc.numbers");
const outputFilePath = path.join(dataDir, "outputNumbersByAppleInc.pdf");

// Specify load options, we want to load Numbers spreadsheet
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Numbers);

// Load the Numbers spreadsheet in workbook with above load options
const wb = new AsposeCells.Workbook(sourceFilePath, opts);

// Save the workbook to pdf format
wb.save(outputFilePath, AsposeCells.SaveFormat.Pdf);
```

