---
title: Rileva se il foglio di lavoro è protetto da password con Node.js tramite C++
linktitle: Scoprire se il foglio di lavoro è protetto da password
type: docs
weight: 360
url: /it/nodejs-cpp/detect-if-worksheet-is-password-protected/
description: Impara come rilevare se un foglio di lavoro è protetto da password usando Aspose.Cells for Node.js via C++. 
keywords: Rileva la protezione da password del foglio di lavoro con Node.js tramite C++, verifica se il foglio di lavoro è protetto da password con Node.js tramite C++, Aspose.Cells for Node.js via C++
---

{{% alert color="primary" %}}

 È possibile proteggere separatamente i fogli di lavoro e i libri di lavoro. Ad esempio, un foglio di calcolo può contenere uno o più fogli protetti da password, tuttavia, il foglio di calcolo stesso può o meno essere protetto. Le API Aspose.Cells forniscono i mezzi per rilevare se un determinato foglio di lavoro è protetto da password o meno. Questo articolo dimostra l'uso dell'API Aspose.Cells for Node.js via C++ per ottenere lo stesso risultato.

{{% /alert %}}

Aspose.Cells for Node.js via C++ ha esposto la proprietà [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--) per rilevare se un foglio di lavoro è protetto da password o meno. La proprietà di tipo booleana [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--) restituisce **true** se [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) è protetto da password e **false** se non lo è.

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
