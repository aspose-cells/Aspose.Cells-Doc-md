---
title: Verify Password Used to Protect the Worksheet with Node.js via C++
linktitle: Verify Password Used to Protect the Worksheet
type: docs
weight: 370
url: /nodejs-cpp/verify-password-used-to-protect-the-worksheet/
description: Learn how to verify the password used to protect a worksheet using Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Aspose.Cells APIs have enhanced the [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/protection) class by introducing some useful properties & methods. One such method is the [**verifyPassword**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-boolean-) which allows specifying a password as an instance of *string* and verifies if the same password has been used to protect the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

{{% /alert %}}

The [**Protection.verifyPassword**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-boolean-) method returns **true** if the specified password matches the password used to protect the given worksheet and **false** if the specified password does not match. Following piece of code uses the [**Protection.verifyPassword**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-boolean-) method in conjunction with [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword-boolean-) property to detect the password protection, and verifies the password.

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
