---  
title: Obtenir le numéro de version de l application qui a créé le document Excel avec Node.js via C++  
linktitle: Obtenir le numéro de version de l application qui a créé le document Excel  
type: docs  
weight: 210  
url: /fr/nodejs-cpp/get-the-version-number-of-the-application-that-created-the-excel-document/  
---  

{{% alert color="primary" %}}  

Souvent, vous avez besoin de connaître le numéro de version de l'application qui a créé un document Microsoft Excel. Aspose.Cells for Node.js via C++ fournit la propriété [**Workbook.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getBuiltInDocumentProperties--) à cette fin.

{{% /alert %}}  

Le code d’exemple suivant montre comment utiliser la propriété [**Workbook.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getBuiltInDocumentProperties--). Il charge des fichiers Excel créés avec Microsoft Excel 2003, 2007, 2010 et 2013 et affiche le numéro de version de l’application qui a créé ces documents Excel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Print the version number of Excel 2003 XLS file
let workbook = new AsposeCells.Workbook(path.join(dataDir, "Excel2003.xls"));
console.log("Excel 2003 XLS Version: " + workbook.getBuiltInDocumentProperties().getVersion());

// Print the version number of Excel 2007 XLS file
workbook = new AsposeCells.Workbook(path.join(dataDir, "Excel2007.xls"));
console.log("Excel 2007 XLS Version: " + workbook.getBuiltInDocumentProperties().getVersion());

// Print the version number of Excel 2010 XLS file
workbook = new AsposeCells.Workbook(path.join(dataDir, "Excel2010.xls"));
console.log("Excel 2010 XLS Version: " + workbook.getBuiltInDocumentProperties().getVersion());

// Print the version number of Excel 2013 XLS file
workbook = new AsposeCells.Workbook(path.join(dataDir, "Excel2013.xls"));
console.log("Excel 2013 XLS Version: " + workbook.getBuiltInDocumentProperties().getVersion());

// Print the version number of Excel 2007 XLSX file
workbook = new AsposeCells.Workbook(path.join(dataDir, "Excel2007.xlsx"));
console.log("Excel 2007 XLSX Version: " + workbook.getBuiltInDocumentProperties().getVersion());

// Print the version number of Excel 2010 XLSX file
workbook = new AsposeCells.Workbook(path.join(dataDir, "Excel2010.xlsx"));
console.log("Excel 2010 XLSX Version: " + workbook.getBuiltInDocumentProperties().getVersion());

// Print the version number of Excel 2013 XLSX file
workbook = new AsposeCells.Workbook(path.join(dataDir, "Excel2013.xlsx"));
console.log("Excel 2013 XLSX Version: " + workbook.getBuiltInDocumentProperties().getVersion());
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
