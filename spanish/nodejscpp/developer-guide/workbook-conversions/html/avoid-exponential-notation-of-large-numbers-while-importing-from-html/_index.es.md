---  
title: Evitar la notación exponencial de números grandes al importar desde HTML  
linktitle: Evitar la notación exponencial de números grandes al importar desde HTML  
type: docs  
weight: 10  
url: /es/nodejs-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/  
description: Aprende cómo evitar que números grandes se conviertan en notación exponencial al importar desde HTML usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

A veces, tu HTML contiene números como 1234567890123456, que son mayores a 15 dígitos, y cuando importas tu HTML a un archivo Excel, estos números se convierten a notación exponencial como 1.23457E+15. Si quieres que tu número se importe tal cual y no se convierta en notación exponencial, por favor, usa la propiedad [**HtmlLoadOptions.getKeepPrecision()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getKeepPrecision--) y configúrala a **true** al cargar tu HTML.  

{{% /alert %}}  

El siguiente código de ejemplo explica el uso de la propiedad [**HtmlLoadOptions.getKeepPrecision()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getKeepPrecision--). La API importará el número tal cual sin convertirlo en notación exponencial.  

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
