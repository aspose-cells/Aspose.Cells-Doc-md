---
title: 使用Node.js通过C++隐藏工作表中的零值显示
linktitle: 隐藏工作表中零值的显示
type: docs
weight: 50
url: /zh/nodejs-cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: 本文将展示如何使用Node.js库通过C++编程方式隐藏Excel电子表格中的零值示例代码。
keywords: 在Node.js中通过C++隐藏Excel工作表中的零值
---

{{% alert color="primary" %}} 

有时，您需要在电子表格中隐藏零值。这可能是个人偏好或格式化标准。

{{% /alert %}} 

要在Microsoft Excel中隐藏工作表中的零值（例如Microsoft Excel 2003）：

1. 从**工具**菜单中选择**选项**，然后选择**视图**选项卡。
1. 取消选中**零值**选项。
1. 点击**确定**。

请参见以下示例代码，演示如何使用Aspose.Cells for Node.js via C++隐藏零值。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Create a new Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Get First worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Hide the zero values in the sheet
sheet.setDisplayZeros(false);

// Save the workbook
workbook.save(path.join(dataDir, "outputfile.out.xlsx"));
```
