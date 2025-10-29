---  
title: Ajustez le niveau de compression du classeur avec Node.js via C++  
linktitle: Ajuster le niveau de compression du classeur  
type: docs  
weight: 180  
url: /fr/nodejs-cpp/adjust-workbook-compression-level/  
description: Apprenez comment ajuster le niveau de compression du classeur dans Aspose.Cells for Node.js via C++.  
---  

## **Ajuster le niveau de compression du classeur**  

Les développeurs peuvent ajuster le niveau de compression du classeur lorsqu'ils manipulent des classeurs plus volumineux. Ils peuvent privilégier des fichiers plus petits au détriment du temps de traitement ou vice versa. Aspose.Cells for Node.js via C++ fournit l'énumération [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) que vous pouvez utiliser pour définir le niveau de compression du classeur. L'énumération [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) propose les membres suivants.  

- Niveau1 : La compression la plus rapide mais la moins efficace.  
- Niveau2 : Un peu plus lent, mais meilleur, que le niveau 1.  
- Niveau3 : Un peu plus lent, mais meilleur, que le niveau 2.  
- Niveau4 : Un peu plus lent, mais meilleur, que le niveau 3.  
- Level5: Un peu plus lent que le niveau 4, mais avec une meilleure compression.  
- Level6: Un bon équilibre entre la vitesse et l'efficacité de la compression.  
- Niveau7 : Compression vraiment bonne!  
- Level8: Meilleure compression que le niveau 7!  
- Niveau9 : La meilleure compression, où la meilleure signifie la plus grande réduction de la taille du flux de données d'entrée. C'est aussi la compression la plus lente.  

Le code suivant démontre l'utilisation de l'énumération [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) et compare le temps de conversion pour le Niveau1, Niveau6 et Niveau9. Vous pouvez également comparer les tailles des fichiers générés.  

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
