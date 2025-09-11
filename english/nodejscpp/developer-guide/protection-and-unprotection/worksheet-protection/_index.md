---  
title: Protect and Unprotect Worksheet with Node.js via C++  
linktitle: Protect and Unprotect Worksheet  
type: docs  
weight: 40  
url: /nodejs-cpp/protect-and-unprotect-worksheets/  
description: Protect and unprotect worksheet of Excel files with Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
To prevent other users from accidentally or deliberately changing, moving, or deleting data in a worksheet, you can lock the cells on your Excel worksheet and then protect the sheet with a password.  
{{% /alert %}}  

## **Protect and unprotect Worksheet in MS Excel**  

**![protect and unprotect Worksheet](protect-and-unprotect-worksheet.png)**  

1. Click **Review > Protect Worksheet**.  
1. Enter a password in **the Password box**.  
1. Select **allow** options.  
1. Select **OK**, re-enter the password to confirm it, and then select **OK** again.  

## **Protect Worksheet Using Aspose.Cells for Node.js via C++**  
Only need the following simple lines of code to implement protecting workbook structure of Excel files.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a new file.
const workbook = new AsposeCells.Workbook();
// Gets the first worksheet.
const sheet = workbook.getWorksheets().get(0);
// Protect contents of the worksheet.
sheet.protect(AsposeCells.ProtectionType.Contents);
// Protect worksheet with password.
sheet.getProtection().setPassword("test");
// Save as Excel file.
workbook.save("Book1.xlsx");
```  

## **Unprotect Worksheet Using Aspose.Cells for Node.js via C++**  
Unprotecting the worksheet is easy with Aspose.Cells API. If the worksheet is password-protected, a correct password is required.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Create a new file.
const workbook = new AsposeCells.Workbook(filePath);
// Gets the first worksheet.
const sheet = workbook.getWorksheets().get(0);
// Protect contents of the worksheet.
sheet.unprotect("password");
// Save Excel file.
workbook.save("Book1.xlsx");
```  

## **Advance topics**  
- [Advanced Protection Settings since Excel XP](/cells/nodejs-cpp/advanced-protection-settings-since-excel-xp/)  
- [Detect if Worksheet is Password Protected](/cells/nodejs-cpp/detect-if-worksheet-is-password-protected/)  
- [Protecting Worksheets](/cells/nodejs-cpp/protecting-worksheets/)  
- [Unprotect a Worksheet](/cells/nodejs-cpp/unprotect-a-worksheet/)  
- [Verify Password Used to Protect the Worksheet](/cells/nodejs-cpp/verify-password-used-to-protect-the-worksheet/)  
  
{{< app/cells/assistant language="nodejs-cpp" >}}