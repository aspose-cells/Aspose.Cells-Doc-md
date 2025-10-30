---
title: Verifiera lösenordet som användes för att skydda kalkbladet med Node.js via C++
linktitle: Verifiera lösenord som används för att skydda arbetsbladet
type: docs
weight: 370
url: /sv/nodejs-cpp/verify-password-used-to-protect-the-worksheet/
description: Lär dig hur man verifierar lösenordet som används för att skydda ett kalkblad med Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Aspose.Cells API har förbättrat [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/protection)-klassen genom att introducera några användbara egenskaper och metoder. En sådan metod är [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-) som tillåter att ange ett lösenord som ett *string*-objekt och verifierar om samma lösenord har använts för att skydda [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

{{% /alert %}}

Metoden [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-) returnerar **true** om det angivna lösenordet matchar lösenordet som användes för att skydda kalkbladet och **false** om det inte matchar. Följande kod använder [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-) i samband med [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--)-egenskapen för att upptäcka lösenordsskyddet och verifiera lösenordet.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");
// Create an instance of Workbook and load a spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Access the protected Worksheet
const sheet = workbook.getWorksheets().get(0);

// Check if Worksheet is password protected
if (sheet.getProtection().isProtectedWithPassword()) {
// Verify the password used to protect the Worksheet
if (sheet.getProtection().verifyPassword("1234")) {
console.log("Specified password has matched");
} else {
console.log("Specified password has not matched");
}
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
