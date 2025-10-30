---
title: Detektera om arbetsblad är lösenordsskyddat med Node.js via C++
linktitle: Upptäck om arbetsbladet är lösenordsskyddat
type: docs
weight: 360
url: /sv/nodejs-cpp/detect-if-worksheet-is-password-protected/
description: Lär dig hur man detekterar om ett arbetsblad är lösenordsskyddat med Aspose.Cells for Node.js via C++. 
keywords: Detektera arbetsblad Lösenordsskydd Node.js via C++, Kontrollera om arbetsblad är lösenordsskyddat Node.js via C++, Aspose.Cells for Node.js via C++
---

{{% alert color="primary" %}}

Det är möjligt att skydda arbetsboken och arbetsblad separat. Till exempel kan ett kalkylblad innehålla ett eller flera arbetsblad som är lösenordsskyddade, men själva kalkylbladet kan eller inte kan vara skyddat. Aspose.Cells API:er ger möjligheten att detektera om ett givet arbetsblad är lösenordsskyddat eller inte. Denna artikel visar hur man använder Aspose.Cells for Node.js via C++ API för att uppnå detta.

{{% /alert %}}

Aspose.Cells for Node.js via C++ har exponerat egenskapen [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--) för att detektera om ett arbetsblad är lösenordsskyddat eller inte. Boolean-typ egenskapen [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--) returnerar **true** om [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) är lösenordsskyddat och **false** om inte.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook and load a spreadsheet
const book = new AsposeCells.Workbook(filePath);

// Access the protected Worksheet
const sheet = book.getWorksheets().get(0);

// Check if Worksheet is password protected
if (sheet.getProtection().isProtectedWithPassword()) {
console.log("Worksheet is password protected");
} else {
console.log("Worksheet is not password protected");
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
