---
title: Guardar en ODF 1.1, 1.2 y 1.3 con Node.js a través de C++
linktitle: Guardar archivo ODS en ODF 1.1, 1.2 y 1.3
description: Convertir Excel a las especificaciones ODF 1.1, 1.2 y 1.3 con Aspose.Cells for Node.js via C++.
type: docs
weight: 230
url: /es/nodejs-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells soporta guardar un archivo ODS (**Hoja de cálculo del Documento Abierto**) en las especificaciones ODF (**Formato del Documento Abierto**) 1.1, 1.2 y 1.3. Aspose.Cells tiene una propiedad [**OdsSaveOptions.getOdfStrictVersion()**](https://reference.aspose.com/cells/nodejs-cpp/odssaveoptions/#getOdfStrictVersion--) que especifica la versión ODF para guardar archivos ODS. El valor predeterminado de esta propiedad es [**OpenDocumentFormatVersionType.odf12**](https://reference.aspose.com/cells/nodejs-cpp/opendocumentformatversiontype/), por lo que el archivo ODS guardado sin esta configuración utiliza las especificaciones 1.2.

{{% /alert %}}

El código de ejemplo a continuación crea un objeto de libro de trabajo, añade algunos valores a la celda A1 en la primera hoja y luego guarda el archivo ODS en las especificaciones ODF 1.1, 1.2 y 1.3. Por defecto, el archivo ODS se guarda en la especificación ODF 1.2.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some value in cell A1
const cell = worksheet.getCells().get("A1");
cell.putValue("Welcome to Aspose!");

// Save ODS in ODF 1.2 version which is default
let options = new AsposeCells.OdsSaveOptions();
workbook.save(path.join(dataDir, "ODF1.2_out.ods"), options);

// Save ODS in ODF 1.1 version
options.setOdfStrictVersion(AsposeCells.OpenDocumentFormatVersionType.Odf11);
workbook.save(path.join(dataDir, "ODF1.1_out.ods"), options);

// Save ODS in ODF 1.3 version
options.setOdfStrictVersion(AsposeCells.OpenDocumentFormatVersionType.Odf13);
workbook.save(path.join(dataDir, "ODF1.3_out.ods"), options);
```
