---  
title: تحويل ورقة العمل إلى صورة باستخدام خيارات ImageOrPrint مع Node.js عبر C++  
linktitle: تحويل ورقة العمل إلى صورة باستخدام خيارات الصورة أو الطباعة  
type: docs  
weight: 90  
url: /ar/nodejs-cpp/converting-worksheet-to-image-using-imageorprint-options/  
description: تعلم كيفية تحويل ورقة العمل إلى ملف صورة وتطبيق خيارات مختلفة للصورة والطباعة باستخدام Aspose.Cells for Node.js via C++.   
---  

{{% alert color="primary" %}}  
هذا المستند مصمم لتوفير فهم مفصل حول كيفية تحويل ورقة العمل إلى ملف صورة وتطبيق خيارات مختلفة للصورة وخيارات الطباعة للصورة، مثل الدقة وضغط TIFF وتنسيق الصورة وجودة الصفحة وغيرها.  
{{% /alert %}}  

## **حفظ الأوراق العمل إلى صور - نهج مختلفة**  

في بعض الأحيان، قد تحتاج إلى عرض ورقات العمل الخاصة بك كتمثيل بصري. عليك حقاً تقديم صور ورقة العمل في تطبيقاتك أو صفحات الويب. قد تحتاج إلى إدراج الصور في وثيقة Word أو ملف PDF أو عرض PowerPoint، أو استخدامها في سيناريو آخر ما. ببساطة ترغب في عرض ورقة عمل مقدمة كصورة بحيث يمكنك استخدامها في مكان آخر. Aspose.Cells يدعم تحويل ورقات العمل في ملفات Excel إلى صور. أيضًا، يدعم Aspose.Cells ضبط خيارات مختلفة مثل تنسيق الصورة، الدقة (عمودي وأفقي على حد سواء)، جودة الصورة، وخيارات الصورة والطباعة الأخرى.  

قد تجرب أوتوماتيكية Office لكن لها عيوبها الخاصة. هناك العديد من الأسباب والمشكلات المعنية: على سبيل المثال، الأمان، الاستقرار، القابلية للتوسع والسرعة، السعر، والميزات. باختصار، هناك العديد من الأسباب، وأهمها أن شركة مايكروسوفت توصي بشدة بعدم استخدام أوتوماتيكية Office من حلول البرمجيات.  

يوضح هذا المقال كيفية إنشاء تطبيق وحدة تحكم في Visual Studio .NET، وأداء تحويل ورقة العمل إلى صورة باستخدام خيارات مختلفة للصورة والطباعة ببضع وأبسط أسطر من الشفرة باستخدام API Aspose.Cells.  

تمثل فئة [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/) ورقة عمل لتحويل الصور، ولها طريقة [**toImage(number)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-) محملة زائدة يمكنها تحويل ورقة عمل مباشرة إلى ملف صور مطابق لخصائصك أو خياراتك المرغوبة. يمكنها إرجاع كائن يمكنك من خلاله حفظ ملف صورة على القرص/تدفق. تدعم عدة تنسيقات صور، مثل BMP، PNG، GIF، JPEG، TIFF، EMF وغيرها.  

## **استخدام Aspose.Cells لتحويل ورقة العمل إلى صورة باستخدام خيارات الصورة أو الطباعة**  

### **إنشاء ملف عمل قالب في Microsoft Excel**  

لقد أنشأت ورق عمل جديد في MS Excel وأضافت بعض البيانات في الورقة العمل الأولى. الآن، سأقوم بتحويل ورقة العمل في ملف القالب "Sheet1" إلى ملف صورة "SheetImage.tiff" وسأطبق خيارات الصور المختلفة مثل الدقة الأفقية والعمودية وضغط Tiff وما إلى ذلك.  

### **تنزيل وتثبيت Aspose.Cells**  

أولاً، تحتاج إلى [تحميل](https://downloads.aspose.com/cells/nodejs-cpp) Aspose.Cells for Node.js via C++. قم بتثبيته على جهاز التطوير الخاص بك. تعمل جميع مكونات [Aspose](http://www.aspose.com/)، عند تثبيتها، في وضع التقييم. وضع التقييم بدون حد زمني ويقتصر على إدراج علامات مائية في المستندات المُنتجة.  

### **إنشاء مشروع**  

ابدأ بيئة التطوير المفضلة لديك (مثل Visual Studio). أنشئ تطبيق وحدة تحكم جديد.  

### **إضافة الإشارات**  

سيستخدم هذا المشروع Aspose.Cells. لذلك، عليك إضافة مرجع إلى مكون Aspose.Cells في مشروعك. على سبيل المثال، أضف مرجعاً إلى ....\Program Files\Aspose\Aspose.Cells for Node.js via C++\Bin\Aspose.Cells.node  

### **تحويل ورقة العمل إلى ملف صورة**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Open template
const filePath = path.join(sourceDir, "sampleWorksheetToAnImage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Apply different Image and Print options
const options = new AsposeCells.ImageOrPrintOptions(); // Corrected: Added the instantiation for ImageOrPrintOptions.

// Set Horizontal Resolution
options.setHorizontalResolution(300);

// Set Vertical Resolution
options.setVerticalResolution(300);

// Set TiffCompression
options.setTiffCompression(AsposeCells.TiffCompression.CompressionLZW);

// Set Image Format
options.setImageType(AsposeCells.ImageType.Tiff);

// Set printing page type
options.setPrintingPage(AsposeCells.PrintingPageType.Default);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, options);

// Render/save the image for the sheet
const pageIndex = 3;
sr.toImage(pageIndex, path.join(outputDir, `outputWorksheetToAnImage_${pageIndex + 1}.tiff`));
```  

## **خيارات التحويل**  

من الممكن حفظ صفحات محددة إلى صورة. يحول الرمز التالي الصفحتين الأولى والثانية في دفتر عمل إلى صور JPG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template excel file
const filePath = path.join(sourceDir, "sampleSpecificPagesToImages.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Specify page index to be rendered
const idxPage = 3;

// Render the third image for the sheet
const bitmap = sr.toImage(idxPage);

// Save the image file
const fs = require("fs");
fs.writeFileSync(path.join(outputDir, `outputSpecificPagesToImage_${idxPage + 1}.jpg`), bitmap);
```  

## **تحويل الصور باستخدام WorkbookRender**  

يمكن أن تحتوي صورة TIFF على أكثر من إطار واحد. يمكنك حفظ دفتر العمل بأكمله إلى صورة TIFF واحدة متعددة الإطارات أو الصفحات:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleUseWorkbookRenderForImageConversion.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Tiff);

const workbookRender = new AsposeCells.WorkbookRender(workbook, opts);
workbookRender.toImage(path.join(outputDir, "outputUseWorkbookRenderForImageConversion.tiff"));
```  


