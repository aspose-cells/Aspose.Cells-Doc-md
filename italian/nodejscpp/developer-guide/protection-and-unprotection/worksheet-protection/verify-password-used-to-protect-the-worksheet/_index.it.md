---
title: Verifica la password usata per proteggere il foglio di lavoro con Node.js tramite C++
linktitle: Verificare la password utilizzata per proteggere il foglio di lavoro
type: docs
weight: 370
url: /it/nodejs-cpp/verify-password-used-to-protect-the-worksheet/
description: Scopri come verificare la password usata per proteggere un foglio di lavoro usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Le API di Aspose.Cells hanno migliorato la classe [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/protection) introducendo alcune proprietà e metodi utili. Uno di questi metodi è il [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-) che permette di specificare una password come istanza di *stringa* e verifica se la stessa password è stata usata per proteggere il [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

{{% /alert %}}

Il metodo [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-) restituisce **true** se la password specificata corrisponde a quella usata per proteggere il foglio di lavoro dato e **false** se la password specificata non corrisponde. Il seguente esempio di codice utilizza il metodo [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-) in combinazione con la proprietà [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--) per rilevare la protezione tramite password e verifica la password.

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
