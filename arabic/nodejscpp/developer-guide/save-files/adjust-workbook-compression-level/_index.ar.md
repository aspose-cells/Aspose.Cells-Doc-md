---  
title: تعديل مستوى ضغط الملف بكفاءة في Node.js عبر C++  
linktitle: ضبط مستوى ضغط ملف العمل  
type: docs  
weight: 180  
url: /ar/nodejs-cpp/adjust-workbook-compression-level/  
description: تعلم كيفية ضبط مستوى ضغط ملف العمل في Aspose.Cells for Node.js via C++.  
---  

## **ضبط مستوى ضغط الورقة العمل**  

يمكن للمطورين ضبط مستوى ضغط ملف العمل عند العمل مع ملفات أكبر. قد يفضل المطورون أحجام ملفات أصغر على زمن المعالجة أو العكس. يوفر Aspose.Cells for Node.js via C++ التعداد [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) الذي يمكنك استخدامه لتعيين مستوى ضغط ملف العمل. يوفر التعداد [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) الأعضاء التالية.  

- المستوي 1: أسرع ضغط ولكن أقل فعالية.  
- المستوى 2: أبطأ قليلاً، ولكن أفضل من المستوى 1.  
- المستوى 3: أبطأ قليلاً، ولكن أفضل من المستوى 2.  
- المستوى 4: أبطأ قليلاً، ولكن أفضل من المستوى 3.  
- المستوى 5: أبطأ قليلاً من المستوى 4، لكن مع ضغط أفضل.  
- المستوى 6: توازن جيد بين السرعة وكفاءة الضغط.  
- المستوى 7: ضغط جيد جدًا!  
- المستوى8: ضغط أفضل من المستوى7!  
- المستوى 9: أفضل ضغط، حيث تعني الأفضل أقل حجم لتيار البيانات المدخلة. هذا هو أيضًا أبطأ ضغط.  

يوضح الشريحة الكودية التالية استخدام تعداد [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) ومقارنة وقت التحويل للمستوى 1 والمستوى 6 والمستوى 9. يمكنك أيضًا مقارنة أحجام الملفات المولدة.  

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
