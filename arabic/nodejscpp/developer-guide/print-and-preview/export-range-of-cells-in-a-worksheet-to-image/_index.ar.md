---  
title: تصدير نطاق خلايا في ورقة عمل إلى صورة باستخدام Node.js عبر C++  
linktitle: تصدير مجموعة من الخلايا في ورقة عمل إلى صورة  
type: docs  
weight: 60  
url: /ar/nodejs-cpp/export-range-of-cells-in-a-worksheet-to-image/  
---  

## **سيناريوهات الاستخدام المحتملة**  

 يمكنك عمل صورة لورقة عمل باستخدام Aspose.Cells for Node.js via C++. ومع ذلك، أحيانًا تحتاج إلى تصدير نطاق خلايا فقط من ورقة العمل إلى صورة. يشرح هذا المقال كيفية تحقيق ذلك.  

## **تصدير مجموعة من الخلايا في ورقة عمل إلى صورة**  

للحصول على صورة لنطاق، اضبط منطقة الطباعة على النطاق المطلوب ثم اضبط الهوامش على 0. أيضًا قم بضبط [**ImageOrPrintOptions.getOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOnePagePerSheet--) على **true**. يأخذ الكود التالي صورة للنطاق D8:G16. فيما يلي لقطة شاشة لملف Excel النموذجي المستخدم في الكود. يمكنك تجربة الكود مع أي ملف Excel.  

## **صورة للملف الإكسل العيني وصورته المصدرية**  

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**  

تنفيذ الكود ينشئ صورة للمدى D8:G16 فقط.  

**![todo:image_alt_text](Output-Image.png)**  

## **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook from source file.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleExportRangeOfCellsInWorksheetToImage.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the print area with your desired range
worksheet.getPageSetup().setPrintArea("D8:G16");

// Set all margins as 0
worksheet.getPageSetup().setLeftMargin(0);
worksheet.getPageSetup().setRightMargin(0);
worksheet.getPageSetup().setTopMargin(0);
worksheet.getPageSetup().setBottomMargin(0);

// Set OnePagePerSheet option as true
const options = new AsposeCells.ImageOrPrintOptions();
options.setOnePagePerSheet(true);
options.setImageType(AsposeCells.ImageType.Jpeg);
options.setHorizontalResolution(200);
options.setVerticalResolution(200);

// Take the image of your worksheet
const sr = new AsposeCells.SheetRender(worksheet, options);
sr.toImage(0, path.join(outputDir, "outputExportRangeOfCellsInWorksheetToImage.jpg"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
