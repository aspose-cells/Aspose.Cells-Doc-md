---  
title: Настройка уровня сжатия рабочей книги с помощью Node.js через C++  
linktitle: Настройка уровня сжатия рабочей книги  
type: docs  
weight: 180  
url: /ru/nodejs-cpp/adjust-workbook-compression-level/  
description: Узнайте, как настроить уровень сжатия рабочей книги в Aspose.Cells for Node.js via C++.  
---  

## **Настройка уровня сжатия книги**  

Разработчики могут настраивать уровень сжатия рабочей книги при работе с большими файлами. Разработчики могут отдавать приоритет меньшему размеру файла или времени обработки. Aspose.Cells for Node.js via C++ предоставляет перечисление [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype), которое можно использовать для установки уровня сжатия рабочей книги. Перечисление [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) содержит следующие члены.  

- Level1: Самое быстрое, но наименее эффективное сжатие.  
- Level2: Немного медленнее, но лучше, чем уровень 1.  
- Level3: Немного медленнее, но лучше, чем уровень 2.  
- Level4: Немного медленнее, но лучше, чем уровень 3.  
- Level5: Немного медленнее, чем уровень 4, но с лучшим сжатием.  
- Level6: Хороший баланс скорости и эффективности сжатия.  
- Level7: Очень хорошее сжатие!  
- Уровень8: Лучшее сжатие, чем на уровне 7!  
- Level9: "Лучшее" сжатие, где под лучшим понимается максимальное сокращение размера входного потока данных. Это также самое медленное сжатие.  

В следующем фрагменте кода демонстрируется использование перечисления [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) и сравнение времени преобразования для уровней 1, 6 и 9. Также можно сравнить размеры созданных файлов.  

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
