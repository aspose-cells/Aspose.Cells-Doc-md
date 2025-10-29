---
title: 通过Node.js与C++密码保护或取消保护共享工作簿
linktitle: 密码保护或取消保护共享工作簿
type: docs
weight: 10
url: /zh/nodejs-cpp/password-protect-or-unprotect-the-shared-workbook/
---

## **可能的使用场景**

 你可以像下面的截图所示，用Microsoft Excel保护或取消保护共享工作簿。Aspose.Cells for Node.js via C++也支持此功能，提供[**Workbook.protectSharedWorkbook(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#protectSharedWorkbook-string-)和[**Workbook.unprotectSharedWorkbook(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#unprotectSharedWorkbook-string-)方法。

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **密码保护或取消保护共享工作簿**

以下示例代码创建一个工作簿并保护它，同时启用共享，然后将其另存为 [输出 Excel 文件](55541777.xlsx)。截图显示当您尝试取消保护时，Microsoft Excel 会提示您输入密码以取消保护。

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **示例代码**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Create empty Excel file
const workbook = new AsposeCells.Workbook();

// Protect the Shared Workbook with Password
workbook.protectSharedWorkbook("1234");

// Uncomment this line to Unprotect the Shared Workbook
// workbook.unprotectSharedWorkbook("1234");

// Save the output Excel file
workbook.save("outputProtectSharedWorkbook.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
