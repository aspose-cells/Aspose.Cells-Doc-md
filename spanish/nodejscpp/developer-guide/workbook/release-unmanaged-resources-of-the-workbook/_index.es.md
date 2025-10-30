---
title: Liberar recursos no gestionados del libro con Node.js via C++
linktitle: Liberar recursos no administrados del libro
type: docs
weight: 310
url: /es/nodejs-cpp/release-unmanaged-resources-of-the-workbook/
description: Aprende cómo liberar los recursos no gestionados del objeto Workbook usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Aspose.Cells proporciona el método [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--) para liberar los recursos no gestionados del objeto [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). El patrón dispose se usa solo para objetos que acceden a recursos no gestionados, como manejadores de archivos y tuberías, manejadores del registro, manejadores de espera, o punteros a bloques de memoria no gestionada. Esto se debe a que el recolector de basura es muy eficiente en recuperar objetos gestionados no utilizados, pero no puede recuperar objetos no gestionados.

{{% /alert %}}

El objeto [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) ahora implementa la interfaz *System.IDisposable* que tiene un único método [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--). Puedes llamar directamente al método [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--) o usar la declaración *Using* para llamar a este método automáticamente.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create workbook object
const wb1 = new AsposeCells.Workbook();

// Call Dispose method
wb1.dispose();

// Call Dispose method via a scoped approach
(async () => {
const wb2 = new AsposeCells.Workbook();
// Any other code goes here
wb2.dispose();
})();
```
{{< app/cells/assistant language="nodejs-cpp" >}}
