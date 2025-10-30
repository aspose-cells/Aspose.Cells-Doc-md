---  
title: Hur man upptäcker filformat och kontrollerar om filen är krypterad med Node.js via C++  
linktitle: Hur man upptäcker ett filformat och kontrollerar om filen är krypterad  
type: docs  
weight: 2700  
url: /sv/nodejs-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/  
description: Lär dig att upptäcka filformat och kontrollera om en fil är krypterad med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Ibland måste du upptäcka ett fils format innan du öppnar det eftersom filändelsen inte garanterar att filens innehåll är lämpligt. Filen kan vara krypterad (en lösenordsskyddad fil) så att den inte kan läsas direkt, eller så bör vi inte läsa den. Aspose.Cells for Node.js via C++ tillhandahåller den statiska metoden [**FileFormatUtil.detectFileFormat(Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#detectFileFormat-uint8array-) och några relevanta API:er som du kan använda för att bearbeta dokument.  
{{% /alert %}}  

Följande exempelkod illustrerar hur man upptäcker ett filformat (med hjälp av filvägen) och kontrollerar dess förlängning. Du kan också avgöra om filen är krypterad.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Detect file format
const info = AsposeCells.FileFormatUtil.detectFileFormat(new Uint8Array(require("fs").readFileSync(filePath)));

// Gets the detected load format
console.log("The spreadsheet format is: " + AsposeCells.FileFormatUtil.loadFormatToExtension(info.getLoadFormat()));

// Check if the file is encrypted.
console.log("The file is encrypted: " + info.isEncrypted());
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
