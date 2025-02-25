---
title: Unprotect a Worksheet with Node.js via C++
linktitle: Unprotect a Worksheet
type: docs
weight: 20
url: /nodejs-cpp/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

If a developer needs to remove protection from a protected worksheet at runtime so that some changes can be made to the file? This can easily be done with Aspose.Cells.

{{% /alert %}}

## **Unprotect a Worksheet**

### **Using Microsoft Excel**

To remove protection from a worksheet:

From the **Tools** menu, select **Protection** followed by **Unprotect Sheet**. Protection will be removed unless the worksheet is password protected. In this case, a dialog prompts for the password. Enter the password and the worksheet will be unprotected then.

### **Unprotecting a Simply Protected Worksheet Using Aspose.Cells**

A worksheet can be unprotected by calling the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class' [**unprotect**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/methods/unprotect/index) method. A simply protected worksheet is one which is not protected with a password. Such worksheets can be unprotected by calling the [**unprotect**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/methods/unprotect/index) method without passing a parameter.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);
            
// Unprotecting the worksheet without a password
worksheet.unprotect();

// Saving the Workbook
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Unprotecting a Password Protected Worksheet Using Aspose.Cells**

A password protected worksheet is one that is protected with a password. Such worksheets can be unprotected by calling an overloaded version of the [**unprotect**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/unprotect/methods/1) method that takes the password as a parameter.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unprotecting the worksheet with a password
worksheet.unprotect("");

// Save Workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```
