---  
title: Evita la notazione esponenziale dei grandi numeri durante l importazione da HTML  
linktitle: Evita la notazione esponenziale dei grandi numeri durante l importazione da HTML  
type: docs  
weight: 10  
url: /it/nodejs-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/  
description: Impara come prevenire che numeri grandi vengano convertiti in notazione esponenziale durante l importazione da HTML usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

A volte il tuo HTML contiene numeri come 1234567890123456, più lunghi di 15 cifre, e quando importi il tuo HTML in un file Excel, questi numeri vengono convertiti in notazione esponenziale come 1.23457E+15. Se desideri che il numero venga importato così com'è e non convertito in notazione esponenziale, utilizza la proprietà [**HtmlLoadOptions.getKeepPrecision()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getKeepPrecision--) e impostala a **true** durante il caricamento del tuo HTML.  

{{% /alert %}}  

Il seguente esempio di codice spiega l'uso della proprietà [**HtmlLoadOptions.getKeepPrecision()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getKeepPrecision--). L'API importerà il numero così com'è senza convertirlo in notazione esponenziale.  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
