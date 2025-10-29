---
title: 通过Node.js和C++获取工作表唯一ID
linktitle: 获取工作表的唯一标识
type: docs
weight: 190
url: /zh/nodejs-cpp/get-worksheet-unique-id/
description: 本文展示了如何使用Node.js库和C++ API以编程方式获取Excel工作表唯一ID。
keywords: 通过C++在Node.js中获取唯一ID的Excel工作表，通过C++在Node.js中获取唯一ID的工作表
---

## **获取工作表的唯一标识**

Aspose.Cells for Node.js via C++提供通过使用[**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--)属性获取工作表唯一ID的功能。以下代码片段演示了如何使用[**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--)属性打印工作表的唯一ID。此代码示例使用这个[示例Excel文件](105480213.xlsx)。

### 源代码

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");

// Load source Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Print Unique Id
console.log("Unique Id: " + worksheet.getUniqueId());
```
{{< app/cells/assistant language="nodejs-cpp" >}}
