---
title: Desactivar la Exportación de Scripts de Marco y Propiedades del Documento con Node.js mediante C++
linktitle: Desactivar la Exportación de Scripts de Marco y Propiedades del Documento
type: docs
weight: 310
url: /es/nodejs-cpp/disable-exporting-frame-scripts-and-document-properties/
description: Aprende cómo desactivar la exportación de scripts de marco y propiedades del documento al convertir un libro de trabajo a HTML usando Aspose.Cells for Node.js via C++.
--- 

{{% alert color="primary" %}}

Aspose.Cells exporta scripts de marco y propiedades del documento al convertir un libro de trabajo en HTML. La versión 8.6.0 de Aspose.Cells for Node.js via C++ introduce una opción que permite desactivar opcionalmente la exportación de scripts de marco y propiedades del documento. Usa la propiedad `HtmlSaveOptions.exportFrameScriptsAndProperties` para desactivar la exportación.

{{% /alert %}}

## **Desactivar la exportación de scripts de marco y propiedades del documento**

El siguiente código de muestra te permite desactivar la exportación de scripts de marco y propiedades del documento. Una vez que conviertas un libro de trabajo a HTML, el archivo de salida no contendrá ningún script de marco ni propiedades del documento.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the required workbook to convert
const filePath = path.join(dataDir, "Sample1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Disable exporting frame scripts and document properties
const options = new AsposeCells.HtmlSaveOptions();
options.setExportFrameScriptsAndProperties(false);

// Save workbook as HTML
workbook.save(path.join(dataDir, "output.out.html"), options);
```
