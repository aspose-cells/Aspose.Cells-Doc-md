---
title: Autoajustar columnas y filas al cargar HTML en Workbook con Node.js mediante C++
linktitle: Ajustar automáticamente columnas y filas al cargar HTML en el libro de trabajo
type: docs
weight: 120
url: /es/nodejs-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Aprende cómo autoajustar columnas y filas al cargar archivos HTML en un Workbook usando Aspose.Cells for Node.js via C++.
---

## **Escenarios de uso posibles**

Puedes autoajustar columnas y filas al cargar tu archivo HTML dentro del objeto Workbook. Por favor, configura la propiedad [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) a **true** para este propósito.

## **Ajustar automáticamente columnas y filas al cargar HTML en el libro de trabajo**

El siguiente código de ejemplo primero carga el HTML de muestra en Workbook sin opciones de carga y lo guarda en formato XLSX. Luego carga nuevamente el HTML de muestra en Workbook pero esta vez, carga el HTML después de configurar la propiedad [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) a **true** y lo guarda en formato XLSX. Por favor, descarga ambos archivos de Excel de salida, es decir, [Archivo Excel de salida sin AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) y [Archivo Excel de salida con AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). La siguiente captura de pantalla muestra el efecto de la propiedad [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) en ambos archivos de Excel de salida.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Sample HTML.
const sampleHtml = "<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>";

// Load HTML string into memory stream.
const ms = Uint8Array.from(sampleHtml, c => c.charCodeAt(0));

// Load memory stream into workbook.
let wb = new AsposeCells.Workbook(ms);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputWithout_AutoFitColsAndRows.xlsx"));

// Specify the HTMLLoadOptions and set AutoFitColsAndRows = true.
const opts = new AsposeCells.HtmlLoadOptions();
opts.setAutoFitColsAndRows(true);

// Load memory stream into workbook with the above HTMLLoadOptions.
wb = new AsposeCells.Workbook(ms, opts);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputWith_AutoFitColsAndRows.xlsx"));
```

{{< app/cells/assistant language="nodejs-cpp" >}}
