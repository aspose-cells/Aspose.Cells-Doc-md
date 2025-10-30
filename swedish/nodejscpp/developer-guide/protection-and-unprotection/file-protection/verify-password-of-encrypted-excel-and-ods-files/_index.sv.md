---  
title: Verifikation av lösenord för krypterade filer med Node.js via C++  
linktitle: Verifiera lösenordet för krypterade filer  
type: docs  
weight: 10  
url: /sv/nodejs-cpp/verify-password-of-encrypted-excel-and-ods-files/  
description: Verifiera lösenordet för krypterade Excel (xlsx, xlsb, xls, xlsm) och Open Office (ODS) filer med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Om Excel (xlsx, xlsb, xls, xlsm) och Open Office (ODS)-filer är låsta med ett lösenord, stöder Aspose enkel lösenordsverifikation utan att analysera specifika filuppgifter.  
{{% /alert %}}  

## **Verifiera lösenordet för den krypterade filen**  

För att verifiera lösenordet för den krypterade filen, tillhandahåller Aspose.Cells for Node.js via C++ [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-)-metoden. Denna metod tar emot två parametrar, filströmmen och lösenordet som ska verifieras.  
Följande kodavsnitt demonstrerar användningen av metod [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-) för att verifiera om det angivna lösenordet är giltigt eller inte.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "EncryptedBook1.xlsx");

// Create a Stream object
const fs = require("fs");
const fstream = fs.readFileSync(filePath);

const isPasswordValid = AsposeCells.FileFormatUtil.verifyPassword(fstream, "1234");

console.log("Password is Valid: " + isPasswordValid);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
