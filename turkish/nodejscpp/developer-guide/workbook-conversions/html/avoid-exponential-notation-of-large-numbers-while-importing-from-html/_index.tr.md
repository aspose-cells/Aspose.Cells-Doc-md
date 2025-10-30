---  
title: Html den içe aktarırken büyük sayıların üstel gösterimini önleme  
linktitle: Html den içe aktarırken büyük sayıların üstel gösterimini önleme  
type: docs  
weight: 10  
url: /tr/nodejs-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/  
description: HTML den büyük sayıları üs notasyonuna dönüştürmeden içeri aktarırken nasıl engelleyeceğinizi öğrenin  Aspose.Cells for Node.js via C++ ile.  
---  

{{% alert color="primary" %}}  

Bazen HTML'nizde 1234567890123456 gibi uzun sayılar bulunur, bunlar 15 haneden uzun olduğu için Excel'e aktarıldığında 1.23457E+15 gibi üs notasyonuna dönüşür. Sayınızın olduğu gibi kalmasını ve üssüz gösterilmesini istiyorsanız, lütfen [**HtmlLoadOptions.getKeepPrecision()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getKeepPrecision--) özelliğini kullanın ve yükleme sırasında **true** olarak ayarlayın.  

{{% /alert %}}  

Aşağıdaki örnek kod [**HtmlLoadOptions.getKeepPrecision()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getKeepPrecision--) özelliğinin kullanımını açıklar. API, sayıyı üs notasyonuna çevirmeden olduğu gibi içeri aktarır.  

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
