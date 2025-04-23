---  
title: إعداد الصفحة وخيارات الطباعة مع Node.js عبر C++  
linktitle: إعدادات الصفحة وخيارات الطباعة  
type: docs  
weight: 60  
url: /ar/nodejs-cpp/page-setup-and-printing-options/  
---  

{{% alert color="primary" %}}  
أحيانًا، يحتاج المطورون إلى تكوين إعدادات الصفحة وخيارات الطباعة للتحكم في عملية الطباعة. تقدم إعدادات الصفحة وخيارات الطباعة خيارات متنوعة ومعتمدة بشكل كامل في Aspose.Cells.  

يوضح هذا المقال كيفية إنشاء تطبيق سطر أوامر في Node.js عبر C++، وتطبيق إعدادات الصفحة وخيارات الطباعة على ورقة عمل مع بعض الأسطر البسيطة من الكود باستخدام API من Aspose.Cells.  
{{% /alert %}}  

## **العمل مع إعدادات الصفحة والطباعة**  

للتحقق من هذا المثال، قمنا بإنشاء دفتر عمل في Microsoft Excel واستخدمنا Aspose.Cells لضبط إعدادات الصفحة وخيارات الطباعة.  

### **استخدام Aspose.Cells لضبط خيارات إعداد الصفحة**  

ابدأ أولا بإنشاء ورقة عمل بسيطة في Microsoft Excel. ثم قم بتطبيق خيارات إعداد الصفحة عليها. سيقوم تنفيذ الكود بتغيير خيارات إعداد الصفحة كما هو موضح في صورة الشاشة أدناه.  

|**ملف الإخراج.**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|  

1. إنشاء ورقة عمل ببعض البيانات في Microsoft Excel:  
   1. افتح برنامج Excel الجديد في Microsoft Excel.  
   1. أضف بعض البيانات.  
1. ضبط خيارات إعداد الصفحة:  
   قم بتطبيق خيارات إعداد الصفحة على الملف. وفيما يلي صورة للخيارات الافتراضية، قبل تطبيق الخيارات الجديدة.  

|**خيارات إعداد الصفحة الافتراضية.**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|  

1. قم بتنزيل وتثبيت Aspose.Cells:  
   1. [تحميل](https://downloads.aspose.com/cells/nodejs-cpp) Aspose.Cells for Node.js via C++.  
   1. قم بتثبيته على كمبيوتر التطوير الخاص بك.  
      جميع مكونات Aspose، عند التثبيت، تعمل في وضع التقييم. وضع التقييم لا يحتوي على حد زمني ويقوم فقط بحقن العلامات المائية إلى الوثائق المنتجة.  
1. أنشئ مشروعًا:  
   1. ابدأ بيئة Node.js الخاصة بك.  
   1. أنشئ تطبيقًا جديدًا على الكونسول.  
      سيظهر هذا المثال تطبيق سطر أوامر Node.js، ولكن يمكنك أيضًا استخدام روابط C++.  
1. أضف مراجع:  
   1. يستخدم هذا المثال Aspose.Cells لذا أضف مرجعًا إلى تلك المكونة للمشروع. على سبيل المثال:  
      …\Program Files\Aspose\Aspose.Cells\Bin\Node.js-Cpp\Aspose.Cells.node  
1. اكتب التطبيق الذي يستدعي واجهة برمجة التطبيق:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "CustomerReport.xlsx");

// Open the template workbook
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the orientation to Portrait
worksheet.getPageSetup().setOrientation(AsposeCells.PageOrientationType.Portrait);

// Setting the number of pages to which the length of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesWide(1);

// Setting the paper size to A4
worksheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);

// Setting the print quality of the worksheet to 1200 dpi
worksheet.getPageSetup().setPrintQuality(1200);

// Setting the first page number of the worksheet pages
worksheet.getPageSetup().setFirstPageNumber(2);

// Save the workbook
workbook.save(path.join(dataDir, "PageSetup_out.xlsx"));
```  

### **ضبط خيارات الطباعة**  

إعدادات إعداد الصفحة توفر أيضًا العديد من خيارات الطباعة (المسمى أيضًا خيارات الورقة) التي تسمح للمستخدمين بالتحكم في كيفية طباعة صفحات ورق العمل. تسمح للمستخدمين ب:  

- تحديد منطقة طباعة معينة من ورقة عمل.
- طباعة العناوين.
- طباعة خطوط الشبكة.
- طباعة عناوين الصفوف/الأعمدة.
- تحقيق جودة مسودة.
- طباعة التعليقات.
- طباعة أخطاء الخلية.
- تعريف ترتيب الصفحات.  

المثال التالي يطبق خيارات الطباعة على الملف الذي تم إنشاؤه في المثال أعلاه (PageSetup.xls). يظهر اللقطة الشاشية أدناه الخيارات الافتراضية للطباعة قبل تطبيق الخيارات الجديدة.  

|**مستند الإدخال**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|  
تغيير خيارات الطباعة ينفذ الشيفرة.  

|**ملف الإخراج**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "PageSetup.xlsx");

// Open the template workbook
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

const pageSetup = worksheet.getPageSetup();

// Specifying the cells range (from A1 cell to E30 cell) of the print area
pageSetup.setPrintArea("A1:E30");

// Defining column numbers A & E as title columns
pageSetup.setPrintTitleColumns("$A:$E");

// Defining row numbers 1 as title rows
pageSetup.setPrintTitleRows("$1:$2");

// Allowing to print gridlines
pageSetup.setPrintGridlines(true);

// Allowing to print row/column headings
pageSetup.setPrintHeadings(true);

// Allowing to print worksheet in black & white mode
pageSetup.setBlackAndWhite(true);

// Allowing to print comments as displayed on worksheet
pageSetup.setPrintComments(AsposeCells.PrintCommentsType.PrintInPlace);

// Allowing to print worksheet with draft quality
pageSetup.setPrintDraft(true);

// Allowing to print cell errors as N/A
pageSetup.setPrintErrors(AsposeCells.PrintErrorsType.PrintErrorsNA);

// Setting the printing order of the pages to over then down
pageSetup.setOrder(AsposeCells.PrintOrderType.OverThenDown);

// Save the workbook
workbook.save(path.join(dataDir, "PageSetup_Print_out.xlsx"));
```  

