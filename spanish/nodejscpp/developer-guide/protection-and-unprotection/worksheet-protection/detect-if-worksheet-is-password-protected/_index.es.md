---
title: Detectar si la hoja de cálculo está protegida con contraseña usando Node.js vía C++
linktitle: Detectar si la hoja de cálculo está protegida con contraseña
type: docs
weight: 360
url: /es/nodejs-cpp/detect-if-worksheet-is-password-protected/
description: Aprenda cómo detectar si una hoja de cálculo está protegida con contraseña usando Aspose.Cells for Node.js via C++. 
keywords: Detectar protección con contraseña en hoja de cálculo Node.js vía C++, Verificar si la hoja de cálculo está protegida con contraseña en Node.js vía C++, Aspose.Cells for Node.js via C++
---

{{% alert color="primary" %}}

Es posible proteger los libros y las hojas de cálculo por separado. Por ejemplo, una hoja de cálculo puede contener una o más hojas protegidas con contraseña, sin embargo, el libro en sí puede no estar protegido. Las APIs de Aspose.Cells proporcionan los medios para detectar si una hoja de cálculo dada está protegida con contraseña o no. Este artículo demuestra el uso de la API Aspose.Cells for Node.js via C++ para lograrlo.

{{% /alert %}}

Aspose.Cells for Node.js via C++ ha expuesto la propiedad [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--) para detectar si una hoja de cálculo está protegida con contraseña o no. La propiedad de tipo Boolean [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--) devuelve **true** si [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) está protegida con contraseña y **false** si no.

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
