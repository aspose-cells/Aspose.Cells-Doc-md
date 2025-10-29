---  
title: ورقة العمل إلى صورة  ضبط صيغة البكسل للصورة المعروضه باستخدام Node.js عبر C++  
linktitle: ورقة العمل إلى صورة  ضبط تنسيق البكسل للصورة المقدمة  
type: docs  
weight: 200  
url: /ar/nodejs-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/  
---  

{{% alert color="primary" %}}  
أحيانًا ترغب في تحديد تنسيق البكسل عند تحويل ورقة العمل إلى صيغة صورة. بشكل افتراضي، تستخدم Aspose.Cells 32 بت لكل بكسل. تتيح لك Aspose.Cells تخصيص تنسيق البكسل (عمق البت) باستخدام الخيارات للصورة المقدمة.  
{{% /alert %}}  

يرجى رؤية الرمز البريدي الخاص بك أدناه الذي يظهر كيفية ضبط تنسيق البكسل المطلوب أثناء تقديم صور الأوراق.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Load an Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleSetPixelFormatRenderedImage.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the ImageOrPrintOptions with desired color depth (24 bits per pixel) and image format type
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setTiffColorDepth(AsposeCells.ColorDepth.Format24bpp);
opts.setImageType(AsposeCells.ImageType.Tiff);

// Instantiate SheetRender object based on the first worksheet
const sheetRender = new AsposeCells.SheetRender(worksheet, opts);

// Save the image (first page of the sheet) with the specified options
sheetRender.toImage(0, path.join(outputDir, "outputSetPixelFormatRenderedImage.tiff"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
