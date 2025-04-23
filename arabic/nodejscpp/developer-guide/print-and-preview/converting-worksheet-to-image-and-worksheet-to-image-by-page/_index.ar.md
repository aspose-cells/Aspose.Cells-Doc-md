---  
title: تحويل ورقة العمل إلى صورة وورقة العمل إلى صورة حسب الصفحة باستخدام Node.js عبر C++  
linktitle: تحويل ورقة العمل إلى صورة وورقة العمل إلى صورة بواسطة الصفحة  
type: docs  
weight: 80  
url: /ar/nodejs-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/  
---  

{{% alert color="primary" %}}  
تم تصميم هذا المستند لتوفير فهم مفصل للمطورين حول كيفية تحويل ورقة العمل إلى ملف صورة وورقة عمل متعددة الصفحات إلى ملفات صور لكل صفحة.  

في بعض الأحيان قد تحتاج إلى تقديم ورقات العمل على شكل صور، على سبيل المثال، لاستخدامها في التطبيقات أو صفحات الويب. قد تحتاج إلى إدراج الصور في مستند Word أو ملف PDF أو عرض PowerPoint، أو استخدامها في سيناريو آخر. ببساطة، ترغب في عرض ورقة العمل على شكل صورة. تدعم Aspose.Cells تحويل ورقات العمل في ملفات Microsoft Excel إلى صور. بالإضافة إلى ذلك، تدعم Aspose.Cells تحويل دفتر العمل إلى عدة ملفات صور، واحدة لكل صفحة.  

قد تستخدم أتمتة Office لتحقيق هذا، ولكن أتمتة Office لها عيوبها الخاصة. هناك عدة أسباب وقضايا معقدة، على سبيل المثال الأمان والاستقرار والتوسعة / السرعة والسعر والميزات. بإختصار، هناك العديد من الأسباب، ولكن السبب الرئيسي هو أن شركة Microsoft نفسها توصي بشدة ضد أتمتة Office.  
{{% /alert %}}  

## **باستخدام Aspose.Cells for Node.js via C++ لتحويل ورقة العمل إلى ملف صورة**  

توضح هذه المقالة كيفية إنشاء تطبيق وحدة تحكم، وتحويل ورقة عمل إلى صورة، وتحويل ورقة عمل إلى صورة واحدة لكل ورقة عمل باستخدام أقل عدد من الأسطر وأبسطها باستخدام API الخاص بـ Aspose.Cells.  

تحتاج إلى استيراد عدة فئات قيمة مرتبطة بوظائف التصيير إلى برنامجك أو مشروعك، مثل [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/)، [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/)، [**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender/)، وهكذا. فئة [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/) تمثل ورقة عمل لتحويلها إلى صور، ولها طريقة [**toImage(number)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-) محملة زائدة يمكنها تحويل ورقة العمل مباشرة إلى ملفات الصور مع أي سمات أو خيارات مضبوطة. يمكنها إرجاع كائن صورة ويمكنك حفظ ملف صورة على القرص/تدفق. تدعم العديد من تنسيقات الصور، على سبيل المثال، BMP، PNG، GIF، JPG، JPEG، TIFF، EMF، وغيرها.  

يشرح هذا المقال كيفية:  

- تحويل ورقة العمل إلى صورة  
- تحويل كل صفحة في ورقة العمل إلى صورة  

تظهر هذه المهمة كيفية استخدام Aspose.Cells لتحويل ورقة عمل من دفتر العمل القالب إلى ملف صورة.  

### **إعداد المشروع**  

1. أولاً، [قم بتنزيل Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).  
1. قم بتثبيته على جهاز التطوير الخاص بك. جميع مكونات [Aspose](http://www.aspose.com/)، عند تثبيتها، تعمل في وضع التقييم. وضع التقييم لا يحده زمن ويمكنه فقط إدراج علامات مائية في المستندات المنتجة. الآن، ابدأ بيئة التطوير الخاصة بك وأنشئ تطبيق وحدة تحكم جديد. هذا المثال يستخدم تطبيق وحدة تحكم Node.js، ولكن يمكنك استخدام أي إعداد يتكامل مع Node.js. أضف مرجعًا إلى Aspose.Cells في المشروع الذي أنشأته.  

### **تحويل ورقة العمل إلى ملف صورة**  

أنشأت دفتر عمل جديد في Microsoft Excel وأضفت بعض البيانات في ورقة العمل الأولى: **Testbook.xlsx** (ورقة عمل واحدة). ثم قم بتحويل ورقة العمل في الملف القالب Sheet1 إلى ملف صورة يُعرف باسم SheetImage.jpg.  

التالي هو الكود الذي استخدمته العنصر لإنجاز المهمة. يحول Sheet1 في **Testbook.xlsx** إلى ملف صورة لشرح سهولة هذا التحويل.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template excel file
const filePath = path.join(sourceDir, "sampleConvertWorksheettoImageFile.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setOnePagePerSheet(true);

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Save the image file
const outputFilePath = outputDir + "outputConvertWorksheettoImageFile.jpg";

sr.toImage(0, outputFilePath);
```  

## **باستخدام Aspose.Cells for Node.js via C++ لتحويل ورقة العمل إلى ملف صورة حسب الصفحة**  

يوضح هذا المثال كيفية استخدام Aspose.Cells لتحويل ورقة عمل من مصنف قوالب يحتوي على عدة صفحات إلى ملف صورة واحد لكل صفحة.  

### **تحويل ورقة العمل إلى صورة حسب الصفحة**  

لقد أنشأت ورق عمل جديد في Microsoft Excel وأضافت بعض البيانات في ورقة العمل الأولى: ملفTestbook2.xlsx (ورقة عمل واحدة).  

الآن، قم بتحويل ورقة العمل Sheet1 في ملف القالب إلى ملفات صور (ملف واحد لكل صفحة). حيث أنني قمت بالفعل بإنشاء تطبيق الوحدة التحكم لأداء مهمة النسخ، سأتجاوز خطوات إنشاء تطبيق الوحدة التحكم تلك وأنتقل مباشرة إلى خطوات تحويل ورقة العمل.  

وفيما يلي الكود الذي يستخدمه المكون لإنجاز المهمة. يقوم بتحويل الشريحة Sheet1 في Testbook2.xlsx إلى ملفات صورة حسب الصفحة.  

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
sr.toImage(j, outputDir + "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif");
}
```  


