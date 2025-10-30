---
title: Convertir libro de Excel a Ods, Sxc y Fods (OpenOffice / LibreOffice Calc) vía Node.js
linktitle: Ods
type: docs
weight: 20
url: /es/nodejs-cpp/convert-excel-to-ods/
description: Cómo convertir Excel a Ods (OpenOffice / LibreOffice Calc) o convertir Ods (OpenOffice / LibreOffice Calc) a Excel con Aspose.Cells for Node.js via C++.
---

## **Acerca de OpenDocument**
El [formato de documento abierto (ODF)](https://es.wikipedia.org/wiki/OpenDocument) es un formato de archivo gratuito y abierto para documentos de oficina electrónicos desarrollado originalmente por Sun para la suite Open Office. OpenDocument Spreadsheet (ODS) es el formato de archivo para documentos de Excel. OpenDocument es actualmente un estándar OASIS e ISO.

## **Convertir Ods (OpenOffice / LibreOffice calc) a Excel**
Aspose.Cells for Node.js via C++ admite cargar Ods, Sxc y Fods que son compatibles con OpenOffice / LibreOffice Calc, y convertir [Ods](book1.ods), [Sxc](book1.sxc) y [Fods](book1.fods) a archivos Excel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load Excel workbook
const excelFilePath = path.join(__dirname, "book1.xlsx");
let workbook = new AsposeCells.Workbook(excelFilePath);

// Save as ods file
workbook.save("ods_out.ods");

// Save as sxc file
workbook.save("sxc_out.sxc");

// Save as fods file
workbook.save("fods_out.fods");
```

## **Convertir Excel a Ods (OpenOffice / LibreOffice Calc)**
Aspose.Cells for Node.js via C++ admite convertir archivos de Excel a archivos Ods, Sxc y Fods. El ejemplo de código a continuación muestra cómo convertir la [plantilla](book1.xlsx) a archivos Ods, Sxc y Fods.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath1 = path.join(dataDir, "book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath1);
// Save as ods file 
workbook.save("Out.ods");
// Save as sxc file 
workbook.save("Out.sxc");
// Save as fods file 
workbook.save("Out.fods");
```

## **Temas avanzados**
- [Guardar archivo ODS en las especificaciones de ODF 1.1 y 1.2](/cells/es/nodejs-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [Trabajar con fondo en archivos ODS](/cells/es/nodejs-cpp/working-with-background-in-ods-files/)
{{< app/cells/assistant language="nodejs-cpp" >}}
