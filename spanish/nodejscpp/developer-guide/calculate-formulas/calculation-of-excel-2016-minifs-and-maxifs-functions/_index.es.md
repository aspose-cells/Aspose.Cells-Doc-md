---
title: Cálculo de las funciones MINIFS y MAXIFS de Excel 2016 con Node.js vía C++
description: Este artículo introduce cómo usar la biblioteca Aspose.Cells para calcular las funciones MINIFS y MAXIFS en Microsoft Excel 2016 usando Node.js vía C++. Carga un archivo de Excel existente o crea uno nuevo, luego usa los métodos de Aspose.Cells para calcular estas funciones y guardar los resultados en disco.
keywords: Aspose.Cells, Excel, 2016, función MINIFS, función MAXIFS, cálculo Node.js vía C++
type: docs
weight: 300
url: /es/nodejs-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Escenarios de uso posibles**
Microsoft Excel 2016 soporta las funciones MINIFS y MAXIFS. Estas funciones no son compatibles en Excel 2013 o versiones anteriores. Aspose.Cells for Node.js via C++ también soporta el cálculo de estas funciones. La siguiente captura de pantalla ilustra el uso de estas funciones. Por favor, lee los comentarios en rojo dentro de la captura para saber cómo funcionan estas funciones.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Cálculo de las funciones MINIFS y MAXIFS de Excel 2016**
El siguiente código de muestra carga el archivo de Excel de ejemplo y llama al método [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) para realizar el cálculo de fórmulas vía Aspose.Cells for Node.js via C++ y luego guarda los resultados en el PDF de salida.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleMINIFSAndMAXIFS.xlsx");

// Load your source workbook containing MINIFS and MAXIFS functions
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Perform Aspose.Cells formula calculation
workbook.calculateFormula();

// Save the calculations result in pdf format
const options = new AsposeCells.PdfSaveOptions();
options.setOnePagePerSheet(true);
const outputFilePath = path.join(dataDir, "outputMINIFSAndMAXIFS.pdf");
workbook.save(outputFilePath, options);
```
