---
title: Salida de página en blanco cuando no hay nada que imprimir con Node.js vía C++
linktitle: Página en Blanco de Salida cuando no hay Nada que Imprimir
type: docs
weight: 90
url: /es/nodejs-cpp/output-blank-page-when-there-is-nothing-to-print/
---

## **Escenarios de uso posibles**

Si la hoja está vacía, entonces Aspose.Cells no imprimirá nada cuando exporte la hoja de trabajo a una imagen. Puede cambiar este comportamiento usando la propiedad [**ImageOrPrintOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOutputBlankPageWhenNothingToPrint--). Cuando la configura en **true**, imprimirá la página en blanco.

## **Página en Blanco de Salida cuando no hay Nada que Imprimir**

El siguiente ejemplo de código crea un libro de trabajo vacío que tiene una hoja de trabajo vacía y renderiza la hoja de trabajo vacía en una imagen después de establecer la propiedad [**ImageOrPrintOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOutputBlankPageWhenNothingToPrint--) en **true**. En consecuencia, genera la página en blanco, ya que no hay nada que imprimir, como se puede ver en la imagen a continuación.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet - it is empty sheet
const ws = wb.getWorksheets().get(0);

// Specify image or print options
// Since the sheet is blank, we will set OutputBlankPageWhenNothingToPrint to true
// So that empty page gets printed
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Png);
opts.setOutputBlankPageWhenNothingToPrint(true);

// Render empty sheet to png image
const sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, path.join(outputDir, "OutputBlankPageWhenNothingToPrint.png"));
```
