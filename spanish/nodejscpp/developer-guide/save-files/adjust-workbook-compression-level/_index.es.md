---  
title: Ajustar el nivel de compresión del libro de trabajo con Node.js vía C++  
linktitle: Ajustar nivel de compresión del libro de trabajo  
type: docs  
weight: 180  
url: /es/nodejs-cpp/adjust-workbook-compression-level/  
description: Aprenda cómo ajustar el nivel de compresión en Aspose.Cells for Node.js via C++.  
---  

## **Ajustar el Nivel de Compresión del Libro de Trabajo**  

Los desarrolladores pueden ajustar el nivel de compresión del libro de trabajo al trabajar con libros de mayor tamaño. Los desarrolladores pueden priorizar tamaños de archivos más pequeños sobre el tiempo de procesamiento o viceversa. Aspose.Cells for Node.js via C++ proporciona la enumeración [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) que puede usar para establecer el nivel de compresión del libro. La enumeración [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) proporciona los siguientes miembros.  

- Nivel1: La compresión más rápida pero menos eficiente.  
- Nivel2: Un poco más lento, pero mejor que el nivel 1.  
- Nivel 3: Un poco más lento, pero mejor, que el nivel 2.  
- Nivel 4: Un poco más lento, pero mejor, que el nivel 3.  
- Nivel5: Un poco más lento que el nivel 4, pero con una mejor compresión.  
- Nivel6: Un buen equilibrio entre velocidad y eficiencia de compresión.  
- Nivel 7: ¡Compresión bastante buena!  
- Nivel8: ¡Mejor compresión que Nivel7!  
- Nivel 9: La compresión "mejor", donde mejor significa la mayor reducción en el tamaño del flujo de datos de entrada. Esta también es la compresión más lenta.  

El siguiente fragmento de código demuestra el uso de la enumeración [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) y compara el tiempo de conversión para Nivel1, Nivel6 y Nivel9. También puedes comparar los tamaños de los archivos generados.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source and output directories
const sourceDir = path.join(__dirname, "data");
const outDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "LargeSampleFile.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const options = new AsposeCells.XlsbSaveOptions();

options.setCompressionType(AsposeCells.OoxmlCompressionType.Level1);
let watch = process.hrtime();
workbook.saveAsync(path.join(outDir, "LargeSampleFile_level_1_out.xlsb"), options);
let elapsedMs = process.hrtime(watch);
console.log("Level 1 Elapsed Time: " + (elapsedMs[0] * 1e3 + elapsedMs[1] / 1e6));

watch = process.hrtime();
options.setCompressionType(AsposeCells.OoxmlCompressionType.Level6);
workbook.saveAsync(path.join(outDir, "LargeSampleFile_level_6_out.xlsb"), options);
elapsedMs = process.hrtime(watch);
console.log("Level 6 Elapsed Time: " + (elapsedMs[0] * 1e3 + elapsedMs[1] / 1e6));

watch = process.hrtime();
options.setCompressionType(AsposeCells.OoxmlCompressionType.Level9);
workbook.saveAsync(path.join(outDir, "LargeSampleFile_level_9_out.xlsb"), options);
elapsedMs = process.hrtime(watch);
console.log("Level 9 Elapsed Time: " + (elapsedMs[0] * 1e3 + elapsedMs[1] / 1e6));
```  

