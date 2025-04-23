---
title: 使用Node.js通过C++验证用来保护工作表的密码
linktitle: 验证用于保护工作表的密码
type: docs
weight: 370
url: /zh/nodejs-cpp/verify-password-used-to-protect-the-worksheet/
description: 学习如何使用Aspose.Cells for Node.js via C++验证保护工作表的密码。
---

{{% alert color="primary" %}}

Aspose.Cells API增强了[**Protection**](https://reference.aspose.com/cells/nodejs-cpp/protection)类，新增了一些有用的属性和方法。其中一个方法是[**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-)，它允许指定密码（字符串实例）并验证是否用该密码保护了[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)。

{{% /alert %}}

如果指定的密码与用于保护工作表的密码匹配，则[**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-)方法返回**true**，否则返回**false**。以下代码结合使用[**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-)方法和[**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--)属性来检测密码保护状态并验证密码。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");
// Create an instance of Workbook and load a spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Access the protected Worksheet
const sheet = workbook.getWorksheets().get(0);

// Check if Worksheet is password protected
if (sheet.getProtection().isProtectedWithPassword()) {
// Verify the password used to protect the Worksheet
if (sheet.getProtection().verifyPassword("1234")) {
console.log("Specified password has matched");
} else {
console.log("Specified password has not matched");
}
}
```
