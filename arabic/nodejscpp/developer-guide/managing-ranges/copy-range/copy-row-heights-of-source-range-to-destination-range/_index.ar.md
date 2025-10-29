---  
title: نسخ ارتفاعات الصف من النطاق المصدر إلى النطاق الوجهة باستخدام Node.js عبر C++  
linktitle: نسخ ارتفاعات الصف من النطاق المصدر إلى النطاق الوجهة  
type: docs  
weight: 590  
url: /ar/nodejs-cpp/copy-row-heights-of-source-range-to-destination-range/  
---  

{{% alert color="primary" %}}  

في بعض الأحيان يحتاج المستخدمون إلى نسخ ارتفاعات الصف من نطاق مصدر إلى نطاق وجهة. يوفر Aspose.Cells for Node.js via C++ تعداد [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/) لهذا الغرض. عند تعيين الخاصية [**PasteOptions.getPasteType()**](https://reference.aspose.com/cells/nodejs-cpp/pasteoptions/#getPasteType--) باستخدام [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/)، سيتم نسخ ارتفاعات جميع الصفوف داخل النطاق المصدر إلى النطاق الوجهة.  

{{% /alert %}}  

يوضح الكود النموذجي التالي كيفية استخدام تعداد [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/) لنسخ ارتفاعات الصف من النطاق المصدر إلى النطاق الوجهة. بمجرد فتح ملف Excel الناتج الذي تم إنشاؤه بواسطة هذا الكود في Microsoft Excel، ستلاحظ أن ارتفاعات الصفوف في النطاق الوجهة مطابقة تمامًا لارتفاعات النطاق المصدر.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Source worksheet
const srcSheet = workbook.getWorksheets().get(0);

// Add destination worksheet
const dstSheet = workbook.getWorksheets().add("Destination Sheet");

// Set the row height of the 4th row. This row height will be copied to destination range
srcSheet.getCells().setRowHeight(3, 50);

// Create source range to be copied
const srcRange = srcSheet.getCells().createRange("A1:D10");

// Create destination range in destination worksheet
const dstRange = dstSheet.getCells().createRange("A1:D10");

// PasteOptions, we want to copy row heights of source range to destination range
const opts = new AsposeCells.PasteOptions();
opts.setPasteType(AsposeCells.PasteType.RowHeights);

// Copy source range to destination range with paste options
dstRange.copy(srcRange, opts);

// Write informative message in cell D4 of destination worksheet
dstSheet.getCells().get("D4").putValue("Row heights of source range copied to destination range");

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
