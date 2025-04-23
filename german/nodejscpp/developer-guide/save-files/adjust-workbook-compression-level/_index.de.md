---  
title: Anpassen des Arbeitsbuch Kompressionslevels mit Node.js via C++  
linktitle: Arbeitsmappen Komprimierungsgrad anpassen  
type: docs  
weight: 180  
url: /de/nodejs-cpp/adjust-workbook-compression-level/  
description: Erfahren Sie, wie Sie das Kompressionsniveau des Arbeitsbuchs in Aspose.Cells for Node.js via C++ anpassen.  
---  

## **Arbeitsmappenkompressionsniveau anpassen**  

Entwickler können das Kompressionslevel des Arbeitsbuchs anpassen, wenn sie mit größeren Arbeitsmappen arbeiten. Entwickler können kleinere Dateigrößen gegenüber einer schnelleren Verarbeitung priorisieren oder umgekehrt. Aspose.Cells for Node.js via C++ bietet die Enumeration [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype), die Sie verwenden können, um das Kompressionsniveau des Arbeitsbuchs festzulegen. Die Enumeration [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) bietet die folgenden Member.  

- Level1: Die schnellste, aber wenig effektive Kompression.  
- Level2: Etwas langsamer, aber besser als Level 1.  
- Level3: Etwas langsamer, aber besser als Level 2.  
- Level4: Etwas langsamer, aber besser als Level 3.  
- Stufe5: Etwas langsamer als Stufe 4, aber mit besserer Kompression.  
- Stufe6: Ein gutes Gleichgewicht zwischen Geschwindigkeit und Kompressionseffizienz.  
- Level7: Sehr gute Kompression!  
- Stufe8: Bessere Kompression als Stufe7!  
- Level9: Die "beste" Kompression, wobei "beste" die größte Reduktion der Eingabedaten bedeutet. Dies ist auch die langsamste Kompression.  

Der folgende Codeausschnitt zeigt die Verwendung der [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) Enumeration und vergleicht die Konvertierungszeit für Level1, Level6 und Level9. Sie können auch die Größen der generierten Dateien vergleichen.  

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

