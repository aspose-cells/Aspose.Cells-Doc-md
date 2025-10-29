---  
title: عرض المقسم باستخدام Node.js عبر C++  
linktitle: تقديم قالب التصفية  
type: docs  
weight: 40  
url: /ar/nodejs-cpp/rendering-slicer/  
---  

## **سيناريوهات الاستخدام المحتملة**  
 يدعم Aspose.Cells for Node.js via C++ عرض أشكال المقسم. إذا قمت بتحويل ورقتك إلى صورة أو حفظ المصنف في تنسيقات PDF أو HTML، سترى أن المقسم يُعرض بشكل صحيح.  

## **تقديم المقطع**  
 الكود النموذجي التالي يحمل [ملف Excel النموذجي](67338479.xlsx) الذي يحتوي على مقسم موجود. يحول ورقة العمل إلى صورة عن طريق ضبط منطقة الطباعة لتغطية المقسم فقط. الصورة الناتجة هي [الصورة المخرجة](67338480.png) التي تظهر المقسم المعروض. كما ترى، تم عرض المقسم بشكل صحيح ويشبه موجوده في ملف Excel النموذجي.  

![todo:image_alt_text](rendering-slicer_1)  
## **الكود المثالي**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRenderingSlicer.xlsx");

// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Set the print area because we want to render slicer only.
ws.getPageSetup().setPrintArea("B15:E25");

// Specify image or print options, set one page per sheet and only area to true.
const imgOpts = new AsposeCells.ImageOrPrintOptions();
imgOpts.setHorizontalResolution(200);
imgOpts.setVerticalResolution(200);
imgOpts.setImageType(AsposeCells.ImageType.Png);
imgOpts.setOnePagePerSheet(true);
imgOpts.setOnlyArea(true);

// Create sheet render object and render worksheet to image.
const sr = new AsposeCells.SheetRender(ws, imgOpts);
sr.toImage(0, "outputRenderingSlicer.png");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
