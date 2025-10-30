---  
title: Verhindern Sie die Exponentialnotation großer Zahlen beim Importieren aus HTML  
linktitle: Verhindern Sie die Exponentialnotation großer Zahlen beim Importieren aus HTML  
type: docs  
weight: 10  
url: /de/nodejs-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/  
description: Erfahren Sie, wie Sie verhindern, dass große Zahlen beim Import aus HTML in die Exponentialschreibweise umgewandelt werden, mit Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

 Manchmal enthält Ihr HTML Zahlen wie 1234567890123456, die länger als 15 Ziffern sind. Beim Import in eine Excel-Datei werden diese Zahlen in die Exponentialnotation 1.23457E+15 umgewandelt. Wenn Sie möchten, dass Ihre Zahl unverändert importiert wird, setzen Sie die Eigenschaft [**HtmlLoadOptions.getKeepPrecision()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getKeepPrecision--) auf **true** beim Laden Ihres HTML.  

{{% /alert %}}  

 Das folgende Beispiel zeigt, wie die [**HtmlLoadOptions.getKeepPrecision()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getKeepPrecision--)-Eigenschaft verwendet wird. Die API importiert die Zahl genau so, ohne sie in Exponentialnotation umzuwandeln.  

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
