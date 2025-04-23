---  
title: استخدام خيارات فحص الأخطاء مع Node.js عبر C++  
linktitle: استخدام خيارات التحقق من الأخطاء  
type: docs  
weight: 140  
url: /ar/nodejs-cpp/use-error-checking-options/  
description: تعلم كيفية استخدام خيارات فحص الأخطاء بشكل برمجي في أوراق عمل Excel باستخدام Aspose.Cells for Node.js via C++.  
keywords: تخزين الرقم كنص في Excel باستخدام Node.js عبر C++، فحص أخطاء Excel، خيارات فحص الأخطاء عبر Node.js عبر C++  
---  

{{% alert color="primary" %}}  
يسمح Microsoft Excel للمستخدمين بتعريف خيارات وقواعد التحقق من الأخطاء. يرى المستخدمون في كثير من الأحيان التحقق من الأخطاء عند إنشاء الصيغ، حيث يوضح مثلث صغير في الزاوية العلوية اليمنى للخلية عند وجود مشكلة في الخلية. يوفر Excel معلومات تساعد المستخدمين على تصحيح المشاكل الشائعة.  
{{% /alert %}}  

## **أنواع الأخطاء**  

الأخطاء التي تعني أن الصيغة لا يمكنها إرجاع نتيجة - مثل قسمة رقم على صفر - تتطلب اهتمامًا فوريًا وتعرض قيمة خطأ في الخلية. النقر على المثلث الأخضر يعرض علامة تعجب، والنقر عليها يفتح قائمة الخيارات.  

يمكن حل الخطأ باستخدام الخيارات أو تجاهله. تجاهل الخطأ يعني أن الخطأ لن يظهر في فحوصات الأخطاء المستقبلية.  

يوفر Aspose.Cells ميزات فحص الأخطاء. تدير فئة [**ErrorCheckOption**](https://reference.aspose.com/cells/nodejs-cpp/errorcheckoption) أنواع مختلفة من فحوصات الأخطاء، على سبيل المثال، الأرقام المخزنة كنص، أخطاء حساب الصيغة، وأخطاء التحقق من الصحة. استخدم تعداد [**ErrorCheckType**](https://reference.aspose.com/cells/nodejs-cpp/errorchecktype) لضبط فحص الأخطاء المطلوب.  

## **الأرقام المخزنة كنص**  

في بعض الأحيان، قد تكون الأرقام مهيأة ومخزنة في الخلايا كنص. يمكن أن يسبب هذا مشاكل في الحسابات أو إنتاج ترتيبات فرز مربكة. الأرقام التي تم تهيئتها كنص تكون محاذية إلى اليسار بدلاً من اليمين في الخلية. إذا لم تُعَد الصيغة التي يجب أن تقوم بعملية رياضية على الخلايا قيمة، فحقق محاذاة في الخلايا التي تشير إليها الصيغة - قد تكون بعض أو كل تلك الخلايا أرقامًا تم تهيئتها كنص.  

يمكنك استخدام خيارات التحقق من الأخطاء لتحويل الأرقام المخزنة كنص إلى أرقام حقيقية بسرعة. في Microsoft Excel 2003:  

1. على قائمة **الأدوات**، انقر على **خيارات**.  
1. حدد علامة التبويب التحقق من الأخطاء.  
   خيار **العدد المخزن كنص** يتم التحقق منه بشكل افتراضي.  
1. قم بتعطيله.  

يوضح الكود المصدري العينة التالي كيفية تعطيل خيار التحقق من الأخطاء للأرقام المخزنة كنص لورقة العمل في ملف XLS القالب باستخدام واجهات برمجة التطبيقات Aspose.Cells.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a workbook and opening a template spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);
// Instantiate the error checking options
const opts = sheet.getErrorCheckOptions();

const index = opts.add();
const opt = opts.get(index);
// Disable the numbers stored as text option
opt.setErrorCheck(AsposeCells.ErrorCheckType.NumberStoredAsText, false);
// Set the range
opt.addRange(AsposeCells.CellArea.createCellArea(0, 0, 1000, 50));

const outputFilePath = path.join(dataDir, "out_test.out.xlsx");
// Save the Excel file
workbook.save(outputFilePath);
```  
