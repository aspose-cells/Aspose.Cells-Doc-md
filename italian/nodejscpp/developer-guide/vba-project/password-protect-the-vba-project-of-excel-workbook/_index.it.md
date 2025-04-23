---  
title: Proteggi con password il progetto VBA del file Excel con Node.js tramite C++  
linktitle: Proteggi con password il progetto VBA del workbook di Excel  
type: docs  
weight: 10  
url: /it/nodejs-cpp/password-protect-the-vba-project-of-excel-workbook/  
description: Impara come proteggere con password il progetto VBA di un file Excel usando Aspose.Cells for Node.js via C++.  
---  

## **Proteggi con password il progetto VBA del file Excel in Node.js**  

Puoi proteggere con password il progetto VBA (Visual Basic for Applications) di un file con Aspose.Cells usando il metodo [**VbaProject.protect(boolean, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#protect-boolean-string-).  

## **Codice di Esempio**  

Il seguente esempio di codice carica il file Excel di esempio, accede al suo progetto VBA e lo protegge con una password. Infine, lo salva come file Excel di output.  

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

