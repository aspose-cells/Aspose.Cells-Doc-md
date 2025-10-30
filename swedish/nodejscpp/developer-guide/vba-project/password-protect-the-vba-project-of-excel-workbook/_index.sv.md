---  
title: Lås VBA projektet i Excel arbetsboken med Node.js via C++  
linktitle: Lösenordsskydda VBA projektet i Excel arbetsboken  
type: docs  
weight: 10  
url: /sv/nodejs-cpp/password-protect-the-vba-project-of-excel-workbook/  
description: Lär dig hur du lösenordsskyddar VBA projektet i en Excel arbetsbok med Aspose.Cells for Node.js via C++.  
---  

## **Lösenordsskydda VBA-projektet för Excel-arbetsboken i Node.js**  

Du kan lösenordsskydda VBA (Visual Basic for Applications)-projektet i en arbetsbok med Aspose.Cells med [**VbaProject.protect(boolean, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#protect-boolean-string-)-metoden.  

## **Exempelkod**  

Följande exempel laddar [provfilen](43352067.xlsm), kommer åt dess VBA-projekt och skyddar det med ett lösenord. Slutligen sparas den som [utdata Excel-fil](43352068.xlsm).  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
