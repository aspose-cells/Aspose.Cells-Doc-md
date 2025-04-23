---
title: Renderizar línea de cuadrícula sólida al convertir Excel a PDF con Node.js mediante C++
linktitle: Renderizar línea de cuadrícula sólida al convertir Excel a PDF
type: docs
weight: 390
url: /es/nodejs-cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: Aprende cómo renderizar líneas de cuadrícula sólidas al convertir Excel a PDF usando Aspose.Cells for Node.js via C++. 
keywords: Renderizar línea de cuadrícula sólida en PDF Node.js mediante C++, Convertir Excel a PDF con línea de cuadrícula sólida en Node.js mediante C++, PdfSaveOptions para línea de cuadrícula sólida en Node.js mediante C++ 
---

Para compatibilidad con versiones anteriores, Aspose.Cells renderiza las líneas de cuadrícula como líneas punteadas por defecto al convertir Excel a PDF. Sin embargo, Excel moderno renderiza las líneas de cuadrícula como líneas sólidas hoy.

Con la opción [PdfSaveOptions.gridlineTypes](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions), Aspose.Cells for Node.js via C++ también puede renderizar líneas de cuadrícula como líneas sólidas.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create an empty Workbook
const wb = new AsposeCells.Workbook();

// Prepare data
wb.getWorksheets().get(0).getCells().get("D9").putValue("gridline");

// Enable to print gridline
wb.getWorksheets().get(0).getPageSetup().setPrintGridlines(true);

// Set to render gridline as solid line
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setGridlineType(AsposeCells.GridlineType.Hair);

// Save the pdf file with PdfSaveOptions
wb.save(path.join(dataDir, "test_Cs.pdf"), pdfSaveOptions);
```

![solid-gridline.png](solid-gridline.png)

