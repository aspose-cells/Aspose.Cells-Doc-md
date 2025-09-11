---  
title: Protect and Unprotect Workbook Structure with Node.js via C++  
linktitle: Protect and Unprotect Workbook Structure  
type: docs  
weight: 40  
url: /nodejs-cpp/protect-and-unprotect-workbook-structure/  
description: Protect and unprotect workbook structure of Excel files using Node.js via C++.  
---  


{{% alert color="primary" %}}  
To prevent other users from viewing hidden worksheets, adding, moving, deleting, or hiding worksheets, and renaming worksheets, you can protect the structure of your Excel workbook with a password.  
{{% /alert %}}  


## **Protect and unprotect Workbook Structure in MS Excel**  

**![protect and unprotect workbook structure](protect-and-unprotect-workbook-structure.png)**  

1. Click **Review > Protect Workbook**.  
1. Enter a password in **the Password box**.  
1. Select **OK**, re-enter the password to confirm it, and then select **OK** again.  


## **Protect Workbook Structure Using Aspose.Cells for Node.js via C++**  
Only need the following simple lines of code to implement protecting workbook structure of Excel files.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Create a new file.
const workbook = new AsposeCells.Workbook();
// Protect workbook structure.
workbook.protect(AsposeCells.ProtectionType.Structure, "password");
// Save Excel file.
workbook.save(filePath);
```  

## **Unprotect Workbook Structure Using Aspose.Cells for Node.js via C++**  
Unprotecting workbook structure is easy with Aspose.Cells API.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open an Excel file which workbook structure is protected.
const workbook = new AsposeCells.Workbook(filePath);
// Unprotect workbook structure.
workbook.unprotect("password");
// Save Excel file.
workbook.save(filePath);
```  

{{% alert color="primary" %}}  
Note: a correct password is required.  
{{% /alert %}}  
  
{{< app/cells/assistant language="nodejs-cpp" >}}