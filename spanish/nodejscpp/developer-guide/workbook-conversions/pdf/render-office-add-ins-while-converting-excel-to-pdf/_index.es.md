---
title: Renderizar complementos de Office al convertir Excel a PDF con Node.js a través de C++
linktitle: Renderizar complementos de Office al convertir Excel a PDF
type: docs
weight: 100
url: /es/nodejs-cpp/render-office-add-ins-while-converting-excel-to-pdf/
---

## **Escenarios de uso posibles**

Anteriormente, Aspose.Cells no podía renderizar complementos de Office cuando se guardaba un archivo Excel en formato PDF. Ahora Aspose.Cells los renderiza correctamente. No es necesario usar ningún método o propiedad especial para renderizar complementos de Office en el PDF de salida. Solo guarde su archivo Excel en formato PDF y se renderizarán los complementos de Office.

## **Renderizar complementos de Office al convertir Excel a PDF**

El siguiente código de ejemplo guarda el [archivo de Excel de muestra](60489769.xlsx), que contiene los complementos de Office. Por favor, mira el [PDF de salida generado con la versión anterior, es decir, 17.11](60489770.pdf) y el [PDF de salida generado con la versión más reciente, es decir, 17.12 y posteriores](60489771.pdf). La salida de la versión anterior es en blanco, pero la versión más reciente muestra los complementos de Office.

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRenderOfficeAdd-Ins.xlsx");
// Load the sample Excel file containing Office Add-Ins
const wb = new AsposeCells.Workbook(filePath);

// Save it to Pdf format
wb.save(`output-${AsposeCells.CellsHelper.getVersion()}.pdf`);
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
