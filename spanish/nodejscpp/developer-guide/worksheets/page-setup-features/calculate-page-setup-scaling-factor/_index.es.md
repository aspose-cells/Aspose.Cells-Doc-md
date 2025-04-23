---
title: Calcular el factor de escala de la configuración de página con Node.js vía C++
linktitle: Calcular Factor de Escala de Configuración de Página
type: docs
weight: 300
url: /es/nodejs-cpp/calculate-page-setup-scaling-factor/
description: Este artículo proporciona un código de ejemplo que explica cómo usar la API de Node.js con C++ para calcular el factor de escala de la configuración de página usando la opción de Ajuste a n páginas de ancho por m de alto de la hoja de cálculo de Excel programáticamente.
keywords: Ajuste a n páginas de ancho por m de alto en Excel con Node.js vía C++, calcular el factor de escala de la configuración de página con Node.js vía C++
---

{{% alert color="primary" %}}

Cuando se establece la escala de la configuración de página usando la opción **Ajustar a n páginas de ancho por m de alto**, Microsoft Excel calcula el factor de escala de la configuración de página. Puedes calcularlo usando la propiedad [**SheetRender.getPageScale()**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#getPageScale--). Esta propiedad devuelve un valor doble que puede convertirse en porcentaje. Por ejemplo, si devuelve 0.5, significa que el factor de escala es del 50%.

{{% /alert %}}

El siguiente código de ejemplo ilustra cómo calcular el factor de escala de configuración de página utilizando la propiedad [**SheetRender.getPageScale()**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#getPageScale--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some data in these cells
worksheet.getCells().get("A4").putValue("Test");
worksheet.getCells().get("S4").putValue("Test");

// Set paper size
worksheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);

// Set fit to pages wide as 1
worksheet.getPageSetup().setFitToPagesWide(1);

// Calculate page scale via sheet render
const sr = new AsposeCells.SheetRender(worksheet, new AsposeCells.ImageOrPrintOptions());

// Convert page scale double value to percentage
const strPageScale = (sr.getPageScale() * 100).toFixed(0) + "%";

// Write the page scale value
console.log(strPageScale);
```
