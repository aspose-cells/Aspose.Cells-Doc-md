---  
title: Justera arbetsboken komprimeringsnivå med Node.js via C++  
linktitle: Justera arbetsbokens komprimeringsnivå  
type: docs  
weight: 180  
url: /sv/nodejs-cpp/adjust-workbook-compression-level/  
description: Lär dig hur du justerar arbetsbokens komprimeringsnivå i Aspose.Cells for Node.js via C++.  
---  

## **Justera arbetsbokens kompressionsnivå**  

Utvecklare kan justera komprimeringsnivån för arbetsboken vid hantering av större arbetsböcker. Utvecklare kan prioritera mindre filstorlekar framför bearbetningstid eller vice versa. Aspose.Cells for Node.js via C++ tillhandahåller enumeration [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) som du kan använda för att ställa in arbetsbokens komprimeringsnivå. Enumeration [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) innehåller följande medlemmar.  

- Level1: Den snabbaste men minst effektiva komprimeringen.  
- Level2: Lite långsammare, men bättre än nivå 1.  
- Level3: Lite långsammare, men bättre än nivå 2.  
- Nivå4: Lite långsammare, men bättre, än nivå 3.  
- Nivå5: Lite långsammare än nivå 4, men med bättre kompression.  
- Nivå6: En bra balans mellan hastighet och kompressionseffektivitet.  
- Nivå7: Ganska bra komprimering!  
- Nivå8: Bättre kompression än nivå 7!  
- Nivå9: Den "bästa" komprimeringen, där bäst betyder störst minskning i storleken på indataströmmen. Detta är också den långsammaste komprimeringen.  

Följande kodsnutt demonstrerar användningen av [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) uppräkningen och jämför konverteringstiden för Nivå1, Nivå6 och Nivå9. Du kan också jämföra storlekarna på de genererade filerna.  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
