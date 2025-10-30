---  
title: Ajuste Automático de Filas para Renderizado con Node.js vía C++  
linktitle: Autoajustar filas para renderizado  
type: docs  
weight: 130  
url: /es/nodejs-cpp/autofit-rows-for-rendering/  
description: Aprenda cómo ajustar automáticamente las filas para renderizado en Excel usando Aspose.Cells for Node.js via C++. Prevenga la recorte de texto en archivos PDF guardados.  
---  

En general, cuando desea mostrar todo el texto en una celda, puede ajustar automáticamente la fila en la vista normal con zoom del 100% en Microsoft Excel. Esto permite que el texto sea completamente visible en vista normal, e incluso cuando imprima o guarde el archivo como PDF, el texto se mostrará correctamente.

Sin embargo, en algunos casos, el ajuste automático de la fila funciona bien en vista normal, pero cuando cambia a vista de impresión o guarda el archivo como PDF, el texto se recorta. Por favor, verifique el archivo fuente [Book1.xlsx](Book1.xlsx) y las capturas de pantalla.

![el texto está recortado en la vista de impresión](text_clipped_in_printview.png)

Si desea evitar que el texto se recorte en el archivo PDF guardado, puede ajustar automáticamente la fila con la opción [AutoFitterOptions.getForRendering()](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getForRendering--)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Init workbook instance.
const workbook = new AsposeCells.Workbook(filePath);

// Set autofit options for rendering.
const autoFitterOptions = new AsposeCells.AutoFitterOptions();
autoFitterOptions.setForRendering(true);

// Autofit rows with options.
workbook.getWorksheets().get(0).autoFitRows(autoFitterOptions);

// Save to pdf.
workbook.save("output.pdf", AsposeCells.SaveFormat.Pdf);
```

Ahora, el texto no está recortado en el archivo PDF de salida.

![el texto no está recortado en el PDF guardado](text_not_clipped_in_saved_pdf.png)  
{{< app/cells/assistant language="nodejs-cpp" >}}
