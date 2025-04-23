---
title: Prevenir la exportación de contenidos ocultos de hojas de cálculo al guardar en HTML con Node.js mediante C++
linktitle: Evitar la exportación de contenidos ocultos de la hoja de cálculo al guardar en HTML
type: docs
weight: 210
url: /es/nodejs-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Aprende cómo prevenir la exportación de contenidos ocultos de hojas de cálculo al guardar archivos de Excel en HTML usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Puede guardar libros de Excel en HTML. Sin embargo, si el libro contiene hojas de cálculo ocultas, por defecto Aspose.Cells exporta los contenidos ocultos de la hoja de cálculo al directorio de salida HTML (_files) que contiene archivos como hojas de cálculo, imágenes, tabstrip.htm, stylesheet.css, etc. A veces, exportar el contenido de las hojas de cálculo ocultas de esta manera no es apropiado. Por ejemplo, si la hoja de cálculo oculta contiene imágenes que no deben ser exportadas al directorio _files.

{{% /alert %}}

Aspose.Cells for Node.js via C++ ofrece la propiedad [**HtmlSaveOptions.getExportHiddenWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportHiddenWorksheet--). Por defecto, está configurada como **true** y las hojas ocultas se exportan a HTML. Si la configuras como **false**, Aspose.Cells no exportará los contenidos de las hojas ocultas.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "WorkbookWithHiddenContent.xlsx"));

// Do not export hidden worksheet contents
const options = new AsposeCells.HtmlSaveOptions();
options.setExportHiddenWorksheet(false);

// Save the workbook
workbook.save(path.join(dataDir, "HtmlWithoutHiddenContent_out.html"), options);
```

