---  
title: Undvik exponentiell notation för stora tal vid import från HTML  
linktitle: Undvik exponentiell notation för stora tal vid import från HTML  
type: docs  
weight: 10  
url: /sv/nodejs-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/  
description: Lär dig hur du förhindrar att stora nummer omvandlas till exponential notation vid import från HTML med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Ibland innehåller din HTML nummer som 1234567890123456, vilka är längre än 15 siffror, och när du importerar din HTML till en Excel-fil, konverteras dessa nummer till exponential notation som 1.23457E+15. Om du vill att numret ska importeras som det är och inte konverteras till exponential notation, använd då [**HtmlLoadOptions.getKeepPrecision()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getKeepPrecision--) egenskapen och ställ den till **true** vid laddning av HTML.  

{{% /alert %}}  

Följande exempel förklarar användningen av [**HtmlLoadOptions.getKeepPrecision()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getKeepPrecision--) egenskapen. API:n kommer att importera numret som det är utan att omvandla till exponential notation.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Sample Html containing large number with digits greater than 15
const html = "<html><body><p>1234567890123456</p></body></html>";

// Convert Html to byte array
const byteArray = new TextEncoder().encode(html);

// Set Html load options and keep precision true
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
loadOptions.setKeepPrecision(true);

// Convert byte array into stream
const stream = byteArray;

// Create workbook from stream with Html load options
const workbook = new AsposeCells.Workbook(stream, loadOptions);

// Access first worksheet
const sheet = workbook.getWorksheets().get(0);

// Auto fit the sheet columns
sheet.autoFitColumns();

// Save the workbook
const outputDir = path.join(__dirname, "output/");
workbook.save(path.join(outputDir, "outputAvoidExponentialNotationWhileImportingFromHtml.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

