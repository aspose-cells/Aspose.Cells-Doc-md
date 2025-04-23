---
title: 使用 C++ 通过 Node.js 加载无图表的源Excel文件
linktitle: 不带图表加载源Excel文件
type: docs
weight: 420
url: /zh/nodejs-cpp/load-source-excel-file-without-charts/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 在不含图表的情况下加载Excel文件。 
---

{{% alert color="primary" %}}

Aspose.Cells 允许您不加载图表，使用 [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) 属性实现。

{{% /alert %}}

## **加载不带图表的电子表格**

以下示例代码加载不含图表的Excel文件，并以输出PDF格式保存。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the load options and filter the data
const options = new AsposeCells.LoadOptions();

// Include everything except charts
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart));

// Load the workbook with specified load options
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xlsx"), options);

// Save the workbook in PDF format
workbook.save(path.join(dataDir, "ResultWithoutChart.pdf"), AsposeCells.SaveFormat.Pdf);
```
