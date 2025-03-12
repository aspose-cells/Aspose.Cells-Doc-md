---
title: Password Protect or Unprotect the Shared Workbook with Node.js via C++
linktitle: Password Protect or Unprotect the Shared Workbook
type: docs
weight: 10
url: /nodejs-cpp/password-protect-or-unprotect-the-shared-workbook/
---

## **Possible Usage Scenarios**

You can protect or unprotect the shared workbook with Microsoft Excel as shown in the following screenshot. Aspose.Cells for Node.js via C++ also supports this feature with the [**Workbook.protectSharedWorkbook(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#protectSharedWorkbook-string-) and [**Workbook.unprotectSharedWorkbook(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#unprotectSharedWorkbook-string-) methods.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Password Protect or Unprotect the Shared Workbook**

The following sample code creates a workbook and protects it while enabling sharing and saves it as [output Excel file](55541777.xlsx). The screenshot shows that when you try to unprotect it, Microsoft Excel prompts you to enter the password to unprotect it.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Sample Code**

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
