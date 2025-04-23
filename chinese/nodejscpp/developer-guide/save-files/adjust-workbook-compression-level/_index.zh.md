---  
title: 用 Node.js 通过 C++ 调整工作簿压缩级别  
linktitle: 调整工作簿压缩级别  
type: docs  
weight: 180  
url: /zh/nodejs-cpp/adjust-workbook-compression-level/  
description: 学习如何在 Aspose.Cells for Node.js via C++ 中调整工作簿的压缩级别。  
---  

## **调整工作簿压缩级别**  

开发者可以在处理大型工作簿时，调整工作簿的压缩级别。可以优先考虑更小的文件体积或更快的处理速度。Aspose.Cells for Node.js via C++ 提供了 [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) 枚举，供设置工作簿的压缩级别。[**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) 枚举包含以下成员。  

- Level1：速度最快，但压缩效果最差。  
- Level2：比级别1略慢，但效果更好。  
- Level3：比级别2略慢，效果更佳。  
- Level4：比级别3略慢，效果更佳。  
- Level5: 比级别4略慢，但压缩效果更好。  
- Level6: 速度和压缩效率的良好平衡。  
- Level7：压缩效果非常不错！  
- Level8: 比Level7压缩更好！  
- Level9：最"佳"压缩，这里的"佳"意味着最大程度地减小输入数据流的大小。这也是最慢的压缩方式。  

以下代码片段演示了使用 [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) 枚举，并比较了 Level1、Level6 和 Level9 的转换时间。 您还可以比较生成文件的大小。  

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

