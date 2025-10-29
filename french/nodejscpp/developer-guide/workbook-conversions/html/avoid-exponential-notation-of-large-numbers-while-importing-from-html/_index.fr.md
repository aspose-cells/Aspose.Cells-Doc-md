---  
title: Éviter la notation exponentielle des grands nombres lors de l importation à partir d un fichier HTML  
linktitle: Éviter la notation exponentielle des grands nombres lors de l importation à partir d un fichier HTML  
type: docs  
weight: 10  
url: /fr/nodejs-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/  
description: Apprenez comment empêcher les grands nombres d être convertis en notation exponentielle lors de l importation depuis HTML avec Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Parfois, votre HTML contient des nombres comme 1234567890123456, qui font plus de 15 chiffres, et lorsque vous importez votre HTML dans un fichier Excel, ces nombres se convertissent en notation exponentielle comme 1.23457E+15. Si vous souhaitez que votre nombre soit importé tel quel et non converti en notation exponentielle, veuillez utiliser la propriété [**HtmlLoadOptions.getKeepPrecision()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getKeepPrecision--) et la définir à **true** lors du chargement de votre HTML.  

{{% /alert %}}  

Le code d'exemple suivant explique l'utilisation de la propriété [**HtmlLoadOptions.getKeepPrecision()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getKeepPrecision--). L'API importera le nombre tel quel sans le convertir en notation exponentielle.  

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
