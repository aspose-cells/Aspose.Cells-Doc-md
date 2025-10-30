---
title: Establecer el ancho de columna a una unidad escalable como em o porcentaje con Node.js mediante C++
linktitle: Establecer ancho de columna a unidad escalable como em o porcentaje
type: docs
weight: 130
url: /es/nodejs-cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Aprende cómo establecer el ancho de columna a unidades escalables como em o porcentaje en Aspose.Cells for Node.js via C++. Mejora la presentación de las tablas HTML generadas.
---

Generar un archivo HTML a partir de una hoja de cálculo es muy común. El tamaño de las columnas se define en "pt," lo cual funciona en muchos casos. Sin embargo, puede haber situaciones donde este tamaño fijo no sea necesario. Por ejemplo, si el ancho de un panel contenedor es de 600px, donde se está visualizando esta página HTML, puede aparecer una barra de desplazamiento horizontal si el ancho de la tabla generada es mayor. Se requiere que este tamaño fijo se cambie a una unidad escalable como em o porcentaje para mejorar la presentación. El siguiente código de ejemplo se puede usar donde [**HtmlSaveOptions.getWidthScalable()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getWidthScalable--) se establece en **true** para crear un ancho escalable.

Se pueden descargar archivos fuente de muestra y archivos de salida desde los siguientes enlaces:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample source file
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleForScalableColumns.xlsx");
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Specify Html Save Options
const options = new AsposeCells.HtmlSaveOptions();

// Set the property for scalable width
options.setWidthScalable(true);

// Specify image save format
options.setExportImagesAsBase64(true);

// Save the workbook in Html format with specified Html Save Options
const outputFilePath = path.join(dataDir, "outsampleForScalableColumns.html");
workbook.save(outputFilePath, options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
