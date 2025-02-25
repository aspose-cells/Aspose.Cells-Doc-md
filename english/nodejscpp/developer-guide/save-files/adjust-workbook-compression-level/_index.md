---  
title: Adjust Workbook Compression Level with Node.js via C++  
linktitle: Adjust Workbook Compression Level  
type: docs  
weight: 180  
url: /nodejs-cpp/adjust-workbook-compression-level/  
description: Learn how to adjust the workbook compression level in Aspose.Cells for Node.js via C++.  
---  

## **Adjust Workbook Compression Level**  

Developers can adjust the compression level of the workbook when working with larger workbooks. Developers may prioritize smaller file sizes over processing time or vice versa. Aspose.Cells for Node.js via C++ provides the [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) enumeration which you can use to set the compression level of the workbook. The [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) enumeration provides the following members.  

- Level1: The fastest but least effective compression.  
- Level2: A little slower, but better, than level 1.  
- Level3: A little slower, but better, than level 2.  
- Level4: A little slower, but better, than level 3.  
- Level5: A little slower than level 4, but with better compression.  
- Level6: A good balance of speed and compression efficiency.  
- Level7: Pretty good compression!  
- Level8: Better compression than Level7!  
- Level9: The "best" compression, where best means greatest reduction in the size of the input data stream. This is also the slowest compression.  

The following code snippet demonstrates the use of [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) enumeration and compares the conversion time for Level1, Level6, and Level9. You may also compare the sizes of the generated files.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source and output directories
const sourceDir = RunExamples.Get_SourceDirectory();
const outDir = RunExamples.Get_OutputDirectory();

const filePath = path.join(sourceDir, "LargeSampleFile.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const options = new AsposeCells.XlsbSaveOptions();

options.setCompressionType(AsposeCells.OoxmlCompressionType.Level1);
let watch = process.hrtime();
await workbook.saveAsync(path.join(outDir, "LargeSampleFile_level_1_out.xlsb"), options);
let elapsedMs = process.hrtime(watch);
console.log("Level 1 Elapsed Time: " + (elapsedMs[0] * 1e3 + elapsedMs[1] / 1e6));

watch = process.hrtime();
options.setCompressionType(AsposeCells.OoxmlCompressionType.Level6);
await workbook.saveAsync(path.join(outDir, "LargeSampleFile_level_6_out.xlsb"), options);
elapsedMs = process.hrtime(watch);
console.log("Level 6 Elapsed Time: " + (elapsedMs[0] * 1e3 + elapsedMs[1] / 1e6));

watch = process.hrtime();
options.setCompressionType(AsposeCells.OoxmlCompressionType.Level9);
await workbook.saveAsync(path.join(outDir, "LargeSampleFile_level_9_out.xlsb"), options);
elapsedMs = process.hrtime(watch);
console.log("Level 9 Elapsed Time: " + (elapsedMs[0] * 1e3 + elapsedMs[1] / 1e6));
```  
  