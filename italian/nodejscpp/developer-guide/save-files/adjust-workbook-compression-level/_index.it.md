---  
title: Regolare il livello di compressione del Workbook con Node.js tramite C++  
linktitle: Regola il livello di compressione del workbook  
type: docs  
weight: 180  
url: /it/nodejs-cpp/adjust-workbook-compression-level/  
description: Impara come regolare il livello di compressione del workbook in Aspose.Cells for Node.js via C++.  
---  

## **Regola il Livello di Compressione del Foglio di Lavoro**  

Gli sviluppatori possono impostare il livello di compressione del workbook quando si lavora con workbook di grandi dimensioni. Possono privilegiare dimensioni di file più piccole rispetto al tempo di elaborazione o viceversa. Aspose.Cells for Node.js via C++ fornisce l'enumerazione [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) che puoi usare per impostare il livello di compressione del workbook. L'enumerazione [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) fornisce i seguenti membri.  

- Livello1: La compressione più veloce ma meno efficace.  
- Livello2: Un po' più lenta, ma migliore, rispetto al livello 1.  
- Livello3: Un po' più lenta, ma migliore, rispetto al livello 2.  
- Livello4: Un po' più lenta, ma migliore, rispetto al livello 3.  
- Livello5: Un po' più lento del livello 4, ma con una migliore compressione.  
- Livello6: Un buon equilibrio tra velocità ed efficienza di compressione.  
- Livello7: Compressione piuttosto buona!  
- Livello8: Migliore compressione rispetto al Livello 7!  
- Livello9: La "migliore" compressione, dove migliore significa la maggiore riduzione delle dimensioni del flusso di dati di input. È anche la compressione più lenta.  

Il seguente frammento di codice mostra l'uso dell'enumerazione [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) e confronta il tempo di conversione per Livello1, Livello6 e Livello9. Puoi anche confrontare le dimensioni dei file generati.  

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
