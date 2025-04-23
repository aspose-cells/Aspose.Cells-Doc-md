---
title: Verificación de la contraseña utilizada para proteger la hoja de cálculo con Node.js vía C++
linktitle: Verificar la contraseña utilizada para proteger la hoja de cálculo
type: docs
weight: 370
url: /es/nodejs-cpp/verify-password-used-to-protect-the-worksheet/
description: Aprenda cómo verificar la contraseña utilizada para proteger una hoja de cálculo usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Las APIs de Aspose.Cells han mejorado la clase [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/protection) introduciendo algunas propiedades y métodos útiles. Uno de estos métodos es [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-), que permite especificar una contraseña como una instancia de *string* y verifica si se ha utilizado la misma contraseña para proteger el [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

{{% /alert %}}

El método [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-) devuelve **true** si la contraseña especificada coincide con la contraseña utilizada para proteger la hoja de cálculo, y **false** si no coincide. El siguiente fragmento de código usa el método [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-) junto con la propiedad [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--) para detectar la protección por contraseña y verificar la contraseña.

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
