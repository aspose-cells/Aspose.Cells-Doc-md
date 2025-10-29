---  
title: تحويل JSON إلى CSV باستخدام Node.js عبر C++  
linktitle: تحويل JSON إلى CSV  
type: docs  
weight: 210  
url: /ar/nodejs-cpp/convert-json-to-csv/  
description: تعلم كيفية تحويل بيانات JSON إلى CSV باستخدام Aspose.Cells for Node.js via C++.  
---  

## **تحويل JSON إلى CSV**  

 يدعم Aspose.Cells تحويل JSON البسيط والمتداخل إلى CSV. لهذا، توفر API فئتين [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) و [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility). تقدم الفئة [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) الخيارات لتخطيط JSON مثل [**JsonLayoutOptions.getArrayAsTable()**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions/#getArrayAsTable--) (يعالج المصفوفة كجدول). تعالج الفئة [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility) JSON باستخدام خيارات التخطيط المحددة مع فئة [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions).  

يوضح الكود التالي استخدام فئتي [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) و [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility) لتحميل ملف JSON المصدر ([104398869.json]) وتوليد ملف CSV الإخراجي ([104398870.csv]).  

### **الكود المثالي**  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");


// Create sample JSON if missing
const jsonPath = path.join(sourceDir, "SampleJson.json");

// Read JSON file
const str = fs.readFileSync(jsonPath, "utf-8");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();

// Set JsonLayoutOptions
const importOptions = new AsposeCells.JsonLayoutOptions();
importOptions.setConvertNumericOrDate(true);
importOptions.setArrayAsTable(true);
importOptions.setIgnoreTitle(true);
AsposeCells.JsonUtility.importData(str, cells, 0, 0, importOptions);

// Save Workbook
workbook.save(outputDir + "SampleJson_out.csv");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
