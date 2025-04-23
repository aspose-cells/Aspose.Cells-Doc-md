---
title: 通过Node.js的C++检查工作簿中的VBA项目是否已签名
linktitle: 检查工作簿中的VBA项目是否已签名
type: docs
weight: 70
url: /zh/nodejs-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: 学习如何使用Aspose.Cells for Node.js via C++检查工作簿中的VBA项目是否已签名。
---

{{% alert color="primary" %}}

您可以通过**工具 > 数字签名...**菜单命令，使用Microsoft Excel来检查您的VBA项目是否已签名。同样，您也可以使用Aspose.Cells的[**Workbook.getVbaProject()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getVbaProject--)属性以编程方式来检查。

{{% /alert %}}

## **在Node.js中检查工作簿中的VBA项目是否已签名**

以下代码加载工作簿，并使用[**Workbook.getVbaProject()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getVbaProject--)属性检测其VBA项目是否已签名。若已签名，返回**true**；否则返回**false**。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
console.log("VBA Project is Signed: " + workbook.getVbaProject().isSigned());
```
