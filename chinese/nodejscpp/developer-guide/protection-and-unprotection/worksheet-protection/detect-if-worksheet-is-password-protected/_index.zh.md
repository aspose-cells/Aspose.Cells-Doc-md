---
title: 用Node.js通过C++检测工作表是否密码保护
linktitle: 检测工作表是否受密码保护
type: docs
weight: 360
url: /zh/nodejs-cpp/detect-if-worksheet-is-password-protected/
description: 学习如何使用Aspose.Cells for Node.js via C++检测工作表是否受密码保护。 
keywords: 用Node.js通过C++检测工作表密码保护，检查工作表是否受密码保护，Aspose.Cells for Node.js via C++
---

{{% alert color="primary" %}}

可以分别保护工作簿和工作表。例如，电子表格可能包含一个或多个密码保护的工作表，但电子表格本身可能受到保护也可能不受保护。Aspose.Cells API提供检测特定工作表是否受密码保护的方法。本文展示了如何使用Aspose.Cells for Node.js via C++ API实现该功能。

{{% /alert %}}

Aspose.Cells for Node.js via C++已暴露[**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--)属性，用于检测工作表是否受到密码保护。布尔类型的[**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--)属性，如果[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)被密码保护，则返回**true**，否则返回**false**。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook and load a spreadsheet
const book = new AsposeCells.Workbook(filePath);

// Access the protected Worksheet
const sheet = book.getWorksheets().get(0);

// Check if Worksheet is password protected
if (sheet.getProtection().isProtectedWithPassword()) {
console.log("Worksheet is password protected");
} else {
console.log("Worksheet is not password protected");
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
