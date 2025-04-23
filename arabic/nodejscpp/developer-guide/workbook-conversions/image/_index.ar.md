---  
title: صورة مع Node.js عبر C++  
linktitle: صورة  
type: docs  
weight: 300  
url: /ar/nodejs-cpp/convert-excel-to-image/  
---  

{{% alert color="primary" %}}  
تتيح Aspose.Cells لك تصدير ورقة عمل من دفتر عمل وتحويلها إلى تنسيقات مختلفة. يشرح هذا المقال كيفية تحويل ورقة عمل إلى تنسيقات مختلفة.  
{{% /alert %}}  

## تحويل دفتر العمل إلى TIFF  

يمكن لملف Excel أن يحتوي على عدة أوراق مع صفحات متعددة. [**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender) يسمح لك بتحويل Excel إلى TIFF بصفحات متعددة. يمكنك أيضًا التحكم في خيارات متعددة لـ TIFF، مثل [ImageOrPrintOptions.getTiffCompression()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTiffCompression--)، [ImageOrPrintOptions.getTiffColorDepth()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTiffColorDepth--)، دقة ([ImageOrPrintOptions.getHorizontalResolution()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--)، [ImageOrPrintOptions.getVerticalResolution()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--)).  

يوضح مقتطف الكود التالي كيفية تحويل Excel إلى TIFF مع عدة صفحات. المرفقات تشمل [ملف الإكسل المصدر](workbook-to-tiff-with-mulitiple-pages.xlsx) و [صورة TIFF المولدة](workbook-to-tiff-with-mulitiple-pages.tiff) للرجوع اليها.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "workbook-to-tiff-with-mulitiple-pages.xlsx");

// Load the workbook
const wb = new AsposeCells.Workbook(filePath);

const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setImageType(AsposeCells.ImageType.Tiff);

// Set resolution to 200
imgOptions.setHorizontalResolution(200);
imgOptions.setVerticalResolution(200);

// Set TIFF compression to LZW
imgOptions.setTiffCompression(AsposeCells.TiffCompression.CompressionLZW);

const workbookRender = new AsposeCells.WorkbookRender(wb, imgOptions);
workbookRender.toImage("workbook-to-tiff-with-mulitiple-pages.tiff");
```  

## **تحويل ورقة عمل إلى صورة**  

تحتوي الأوراق العمل على البيانات التي ترغب في تحليلها. على سبيل المثال، يمكن أن تحتوي ورقة العمل على معلمات وإجماليات ونسب واستثناءات وحسابات.  

كمطور، قد تحتاج إلى عرض الأوراق العمل كصور. على سبيل المثال، قد تحتاج إلى استخدام صورة لورقة عمل في تطبيق أو صفحة ويب. قد ترغب في إدراج صورة في مستند Microsoft Word أو ملف PDF أو عرض PowerPoint أو نوع مستند آخر. ببساطة، ترغب في عرض ورقة عمل كصورة حتى تتمكن من استخدامها في مكان آخر.  

[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender)
[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions)
[**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender)

تمثل فئة [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender) ورقة عمل يتم عرضها كصور. لديها طريقة مفرطة التحميل، [**SheetRender.toImage(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-string-)، التي يمكنها تحويل ورقة العمل إلى ملف(ات) صورة بخصائص أو خيارات مختلفة. تعيد كائن Buffer ويمكنك حفظ ملف صورة على القرص أو بثه. مدعومة عدة تنسيقات صور، على سبيل المثال BMP، PNG، GIF، JPG، JPEG، TIFF، EMF.  

يوضح مقتطف الكود التالي كيفية تحويل ورقة عمل في ملف Excel إلى ملف صورة.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleConvertWorksheetToImageByPage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

const options = new AsposeCells.ImageOrPrintOptions();
options.setHorizontalResolution(200);
options.setVerticalResolution(200);
options.setImageType(AsposeCells.ImageType.Tiff);

// Sheet2Image By Page conversion
const sr = new AsposeCells.SheetRender(sheet, options);
for (let j = 0; j < sr.getPageCount(); j++) 
{
let path = "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif";
sr.toImage(j, path);
}
```  

{{% alert color="primary" %}}  
حاليًا، لا يدعم الواجهة البرمجية لتحويل ورقة عمل إلى صور دعم مخططات الفقاعات ثلاثية الأبعاد.  
{{% /alert %}}  

## **تحويل ورقة عمل إلى SVG**  

تعني SVG Scalable Vector Graphics. SVG هو مواصفة تعتمد على معايير XML للرسومات الناقلة ثنائية الأبعاد. إنها معيار مفتوح تحت تطوير من قبل الجمعية العالمية للويب (W3C) منذ عام 1999.  

تمكن Aspose.Cells for Node.js via C++ من تحويل أوراق العمل إلى SVG منذ الإصدار 7.1.0. يُظهر الكود التالي كيفية تحويل ورقة عمل في ملف Excel إلى ملف صورة SVG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(dataDir, "output");

// Instantiate a workbook
const workbook = new AsposeCells.Workbook();

// Put sample text in the first cell of the first worksheet in the newly created workbook
workbook.getWorksheets().get(0).getCells().get("A1").putValue("DEMO TEXT ON SHEET1");

// Add second worksheet in the workbook
workbook.getWorksheets().add(AsposeCells.SheetType.Worksheet);

// Set text in the first cell of the second sheet
workbook.getWorksheets().get(1).getCells().get("A1").putValue("DEMO TEXT ON SHEET2");

// Set currently active sheet index to 1 i.e. Sheet2
workbook.getWorksheets().setActiveSheetIndex(1);

// Save workbook to SVG. It shall render the active sheet only to SVG
workbook.save(path.join(outputDir, "ConvertWorksheetToSVG_out.svg"));
```  

## **مواضيع متقدمة**  
- [تحويل مخطط Excel إلى صورة](/cells/ar/nodejs-cpp/convert-an-excel-chart-to-image/)  
- [تحويل مخطط إلى صورة بتنسيق SVG](/cells/ar/nodejs-cpp/converting-chart-to-image-in-svg-format/)  
- [تصدير مخطط إلى SVG باستخدام سمة viewBox](/cells/ar/nodejs-cpp/export-chart-to-svg-with-viewbox-attribute/)  
- [تتبع تقدّم تحويل Excel إلى TIFF](/cells/ar/nodejs-cpp/track-conversion-progress-of-excel-to-tiff/)  

