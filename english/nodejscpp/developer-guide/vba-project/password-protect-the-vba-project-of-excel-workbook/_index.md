---  
title: Password Protect the VBA Project of Excel Workbook with Node.js via C++  
linktitle: Password Protect the VBA Project of Excel Workbook  
type: docs  
weight: 10  
url: /nodejs-cpp/password-protect-the-vba-project-of-excel-workbook/  
description: Learn how to password protect the VBA project of an Excel workbook using Aspose.Cells for Node.js via C++.  
---  

## **Password Protect the VBA Project of Excel Workbook in Node.js**  

You can password protect the VBA (Visual Basic for Applications) Project of a workbook with Aspose.Cells using [**VbaProject.protect()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#protect-string) method.  

## **Sample Code**  

The following sample code loads the [sample Excel file](43352067.xlsm), accesses its VBA Project and protects it with a password. Finally, it saves it as the [output Excel file](43352068.xlsm).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source Excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "samplePasswordProtectVBAProject.xlsm"));

// Access the VBA project of the workbook.
const vbaProject = workbook.getVbaProject();

// Lock the VBA project for viewing with password.
vbaProject.protect(true, "11");

// Save the output Excel file
workbook.save(path.join(dataDir, "outputPasswordProtectVBAProject.xlsm"));
```  
  