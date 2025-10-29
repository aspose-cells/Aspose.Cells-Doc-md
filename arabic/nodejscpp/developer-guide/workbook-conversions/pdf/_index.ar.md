---
title: Pdf مع Node.js عبر C++
linktitle: Pdf
type: docs
weight: 220
url: /ar/nodejs-cpp/convert-excel-to-pdf/
description: تعلم كيفية تحويل دفتر عمل Excel إلى PDF باستخدام Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}
تدعم Aspose.Cells تحويل سجل العمل في Excel إلى PDF. في هذا المثال، سنرى التحويل الكامل لسجل عمل Excel إلى PDF.
{{% /alert %}}

## **تحويل سجل عمل Excel إلى PDF**

تستخدم ملفات PDF على نطاق واسع لتبادل المستندات بين المؤسسات والقطاعات الحكومية والأفراد. إنها صيغة مستند قياسية وغالبًا ما يُطلب من مطوري البرامج أن يجدوا طريقة لتحويل ملفات Microsoft Excel إلى مستندات PDF.

تدعم Aspose.Cells تحويل ملفات Excel إلى PDF وتحافظ على دقة الرؤية العالية في التحويل.

{{% alert color="primary" %}}
يكتب Aspose.Cells for Node.js via C++ مباشرةً معلومات حول API ورقم الإصدار في المستندات الناتجة. على سبيل المثال، عند تصيير المستند إلى PDF، يملأ حقل **إنتاج PDF** بالقيمة، مثل 'Aspose.Cells v23.2'.

يرجى ملاحظة أنه يمكنك تغيير هذه المعلومات في مستندات الإخراج عن طريق خاصية [**PdfSaveOptions.getProducer()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getProducer--).
{{% /alert %}}

### **التحويل المباشر**

يدعم Aspose.Cells for Node.js via C++ التحويل من جداول البيانات إلى PDF بشكل مستقل عن البرامج الأخرى. ببساطة، احفظ ملف Excel كملف PDF باستخدام طريقة [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) من فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). توفر طريقة [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) عضو التعداد [**SaveFormat.Pdf**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) الذي يحول ملفات Excel الأصلية إلى صيغة PDF.

اتبع الخطوات التالية لتحويل الجداول الحسابية في Excel مباشرة إلى تنسيق PDF:

1. قم بإنشاء كائن من فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) بالاتصال ببنائه الفارغ.
1. يمكنك فتح/تحميل ملف قالب موجود أو تخطي هذه الخطوة إذا كنت تقوم بإنشاء السجل العمل من البداية.
1. أدخل أي عمل (البيانات الدخلية، تطبيق التنسيق، ضبط الصيغ، إدراج الصور أو كائنات الرسم الأخرى، وما إلى ذلك) على ورق العمل باستخدام واجهات برمجة التطبيقات Aspose.Cells.
1. عندما يكتمل كود الجدول، استدعِ طريقة [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) من فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) لحفظ الجدول.

يجب أن يكون تنسيق الملف PDF، لذا حدد *Pdf* (قيمة محددة مسبقًا) من تعداد [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) لتوليد مستند PDF النهائي.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate the Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save the document in PDF format
workbook.save(path.join(dataDir, "output.pdf"), AsposeCells.SaveFormat.Pdf);
```

### **التحويل المتقدم**

يمكنك أيضًا استخدام الفصيلة [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) لتعيين خصائص مختلفة للتحويل. تعيين خصائص مختلفة للفصيلة [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) يمنحك السيطرة على إعدادات الطباعة، الخط، الأمان، والضغط لمخرج PDF. 

أهم خاصية هي [**getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--) التي تمكّنك من تعيين مستوى الامتثال لمعايير PDF. حاليًا، يمكنك حفظ إلى صيغ PDF 1.4، PDF 1.5، PDF 1.6، PDF 1.7، PDF/A-1a، PDF/A-1b، PDF/A-2a، PDF/A-2b، PDF/A-2u، PDF/A-3a، PDF/A-2ab، وصيغ PDF/A-3u. يرجى ملاحظة أنه مع صيغة PDF/A، يكون حجم الملف الناتج أكبر من حجم ملف PDF عادي.

#### **حفظ جدول البيانات إلى ملف PDF/A المتوافق**

مقطع الرمز المقدم أدناه يوضح كيفية استخدام فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) لحفظ ملفات Excel إلى تنسيق PDF/A متوافق مع PDF.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate new workbook
const workbook = new AsposeCells.Workbook();

// Insert a value into the A1 cell in the first worksheet
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Testing PDF/A");

// Define PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set the compliance type
pdfSaveOptions.setCompliance(AsposeCells.PdfCompliance.PdfA1b);

// Save the file
workbook.save(path.join(dataDir, "output.pdf"), pdfSaveOptions);
```

{{% alert color="primary" %}}
يرجى ملاحظة، تمت إضافة الخاصية [**getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--) مع إصدار Aspose.Cells for Node.js via C++ 5.3.0.
{{% /alert %}}

#### **تعيين وقت إنشاء ملف PDF**

مع فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)، يمكنك الحصول على أو تعيين وقت إنشاء PDF. يوضح الرمز التالي استخدام الخاصية [**PdfSaveOptions.getCreatedTime()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCreatedTime--) لتعيين وقت إنشاء ملف PDF.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");
// Load excel file containing charts
const workbook = new AsposeCells.Workbook(inputPath);

// Create an instance of PdfSaveOptions
const options = new AsposeCells.PdfSaveOptions();
options.setCreatedTime(new Date());

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save(path.join(dataDir, "output.pdf"), options);
```

#### **تعيين خيار ContentCopyForAccessibility**

مع فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)، يمكنك الحصول على أو تعيين خيار [**getAccessibilityExtractContent()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsecurityoptions/#getAccessibilityExtractContent--) للتحكم في وصول المحتوى في ملف PDF المحول.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const inputPath = path.join(sourceDir, "BookWithSomeData.xlsx");

// Load excel file containing some data
const workbook = new AsposeCells.Workbook(inputPath);

// Create an instance of PdfSaveOptions and pass SaveFormat to the constructor
const pdfSaveOpt = new AsposeCells.PdfSaveOptions();

// Create an instance of PdfSecurityOptions
const securityOptions = new AsposeCells.PdfSecurityOptions();

// Set AccessibilityExtractContent to true
securityOptions.setAccessibilityExtractContent(false);

// Set the security option in the PdfSaveOptions
pdfSaveOpt.setSecurityOptions(securityOptions);

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save(path.join(outputDir, "outFile.pdf"), pdfSaveOpt);
```

#### **تصدير الخصائص المخصصة إلى ملف PDF**

مع فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)، يمكنك تصدير الخصائص المخصصة في دفتر العمل المصدر إلى PDF. وتوفر مُعدّلة [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/nodejs-cpp/pdfcustompropertiesexport/) لتحديد الطريقة التي يتم بها تصدير الخصائص. يمكن ملاحظة هذه الخصائص في Adobe Acrobat Reader بالنقر فوق ملف ثم الخصائص كما هو موضح في الصورة التالية. يمكن تنزيل ملف القالب "sourceWithCustProps.xlsx" من [هنا](sourceWithCustProps.xlsx) للفحص وملف PDF الناتج "outSourceWithCustProps" متاح [هنا](outSourceWithCustProps.pdf) للتحليل.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sourceWithCustProps.xlsx");

// Load excel file containing custom properties
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set CustomPropertiesExport property to PdfCustomPropertiesExport.Standard
pdfSaveOptions.setCustomPropertiesExport(AsposeCells.PdfCustomPropertiesExport.Standard);

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save("outSourceWithCustProps.pdf", pdfSaveOptions);
```

### **سمات التحويل**

نحن نعمل على تعزيز ميزات التحويل مع كل إصدار جديد. لا تزال عملية تحويل Excel إلى PDF من Aspose.Cells تحتوي على بعض القيود. لا يتم دعم MapChart عند التحويل إلى تنسيق PDF. أيضًا، بعض الكائنات الرسومية لا تتمتع بدعم جيد.

الجدول التالي يقوم بسرد جميع الميزات المدعومة جزئيًا أو بالكامل عند التصدير إلى PDF باستخدام Aspose.Cells. هذا الجدول ليس نهائيًا ولا يغطي جميع خصائص جدول البيانات ولكنه يحدد تلك الميزات التي لا تتم دعمها أو يتم دعمها جزئيًا للتحويل إلى PDF.

|**عنصر المستند**|**السمة**|**مدعوم**|**ملاحظات**|
| :- | :- | :- | :- |
|المحاذاة| |نعم| |
|إعدادات الخلفية| |نعم| |
|الحدود|لون|نعم| |
|الحدود|نمط الخط|نعم| |
|الحدود|سمك الخط|نعم| |
|بيانات الخلية| |نعم| |
|التعليقات| |نعم| |
|تنسيق شرطي| |نعم| |
|خصائص المستند| |نعم| |
|كائنات الرسم| |جزئيا|لا يتم دعم الظل والتأثيرات ثلاثية الأبعاد لكائنات الرسم بشكل جيد؛ WordArt و SmartArt يتم دعمهما جزئيا.|
|الخط|الحجم|نعم| |
|الخط|اللون|نعم| |
|الخط|النمط|نعم| |
|الخط|التسطير|نعم| |
|الخط|التأثيرات|نعم||
|الصور| |نعم| |
|الارتباط| |نعم| |
|الرسوم البيانية| |جزئيا|لم يتم دعم MapChart.|
|الخلايا المدمجة| |نعم| |
|فاصل الصفحة| |نعم| |
|إعداد الصفحة|الرأس/التذييل|نعم| |
|إعداد الصفحة|الهوامش|نعم| |
|إعداد الصفحة|اتجاه الصفحة|نعم| |
|إعداد الصفحة|حجم الصفحة|نعم| |
|إعداد الصفحة|منطقة الطباعة|نعم| |
|إعداد الصفحة|عناوين الطباعة|نعم| |
|إعداد الصفحة|تحجيم|نعم| |
|ارتفاع الصف/عرض العمود| |نعم| |
|لغة من اليمين إلى اليسار| |نعم| |

{{% alert color="primary" %}}
إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل استدعاء [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) قبل تحويل جدول البيانات إلى تنسيق PDF. وذلك سيضمن إعادة حساب قيم الصيغ الخاصة وتقديم القيم الصحيحة في الملف الناتج PDF.
{{% /alert %}}

## **مواضيع متقدمة**
- [إضافة علامات مرجعية لملف PDF باستخدام وجهات مسماة](/cells/ar/nodejs-cpp/add-pdf-bookmarks-with-named-destinations/)
- [تجنب الصفحة الفارغة في ملف PDF الناتج عندما لا يوجد شيء للطباعة](/cells/ar/nodejs-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [تغيير الخط المستخدم للرموز اليونيكود الخاصة عند حفظ الملف إلى PDF](/cells/ar/nodejs-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [تحويل ملف XLSX إلى تنسيق PDF](/cells/ar/nodejs-cpp/convert-xlsx-file-to-pdf-format/)
- [تحويل ملف Excel إلى تنسيق PDF متوافق مع PDFA-1a](/cells/ar/nodejs-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [تحويل ملف XLS مع صور أو رسوم بيانية إلى تنسيق PDF](/cells/ar/nodejs-cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [إنشاء PdfBookmarkEntry لورقة الرسم البياني](/cells/ar/nodejs-cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [تناسب جميع أعمدة ورقة العمل على صفحة PDF واحدة](/cells/ar/nodejs-cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [الحصول على DrawObject والحدود أثناء تقديمها إلى PDF باستخدام فئة DrawObjectEventHandler](/cells/ar/nodejs-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [الحصول على تحذيرات بديلة للخط أثناء تحويل ملف Excel إلى PDF](/cells/ar/nodejs-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [تجاهل الأخطاء أثناء تحويل Excel إلى PDF](/cells/ar/nodejs-cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [تحديد عدد الصفحات التي يتم إنشاؤها – تحويل من Excel إلى PDF](/cells/ar/nodejs-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [طباعة التعليقات عند الحفظ إلى PDF](/cells/ar/nodejs-cpp/print-comments-while-saving-to-pdf/)
- [تقديم الإضافات المكتبية أثناء تحويل Excel إلى PDF](/cells/ar/nodejs-cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [تقديم صفحة PDF واحدة لكل ورقة عمل إكسل - تحويل إكسل إلى PDF](/cells/ar/nodejs-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [عرض الحروف اليونيكود الإضافية في ملف PDF الناتج باستخدام Aspose.Cells](/cells/ar/nodejs-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [إعادة عينات الصور المضافة - تحويل إكسل إلى PDF](/cells/ar/nodejs-cpp/resampling-added-images-excel-to-pdf-conversion/)
- [حفظ كل ورقة عمل في ملف PDF مختلف](/cells/ar/nodejs-cpp/save-each-worksheet-to-a-different-pdf-file/)
- [حفظ إكسل في ملف PDF بحجم قياسي أو حد أدنى](/cells/ar/nodejs-cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [حفظ ورقات العمل المحددة في ملف PDF](/cells/ar/nodejs-cpp/save-specified-worksheets-to-pdf/)
- [مستندات PDF آمنة](/cells/ar/nodejs-cpp/secure-pdf-documents/)
- [تحديد كيفية عبور السلسلة في ملف PDF والصورة](/cells/ar/nodejs-cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
{{< app/cells/assistant language="nodejs-cpp" >}}
