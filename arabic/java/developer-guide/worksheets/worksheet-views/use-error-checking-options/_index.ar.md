---
title: استخدام خيارات التحقق من الأخطاء
type: docs
weight: 60
url: /ar/java/use-error-checking-options/
---

{{% alert color="primary" %}} 

تسمح Microsoft Excel للمستخدمين بتعريف خيارات وقواعد فحص الأخطاء. يشاهد المستخدمون غالبًا تحققات الأخطاء عند إنشاء الصيغ، حيث يُظهر مثلث صغير في الزاوية العلوية اليمنى من الخلية يبرز عند وجود مشكلة في الخلية. توفر Excel معلومات تساعد المستخدمين في تصحيح المشاكل الشائعة.

{{% /alert %}} 
## **أنواع الأخطاء**
الأخطاء التي تعني عدم قدرة الصيغة على إعادة نتيجة - مثل قسمة عدد على الصفر - تتطلب اهتمامًا فوريًا ويتم عرض قيمة خطأ في الخلية. بالنقر على المثلث الأخضر يظهر علامة تعجب، والنقر على هذا يفتح قائمة الخيارات. 

يمكن حل الخطأ باستخدام الخيارات، أو تجاهله. تجاهل الخطأ يعني أن هذا الخطأ لن يظهر في عمليات التحقق من الأخطاء في المستقبل.

توفر Aspose.Cells ميزات خيارات فحص الأخطاء. تدير فئة ErrorCheckOptions أنواعًا مختلفة من فحوصات الأخطاء، على سبيل المثال أرقام تم تخزينها كنص، وأخطاء حساب الصيغة وأخطاء التحقق من الصحة. استخدم تعداد ErrorCheckType لتعيين الفحص الذي ترغب فيه.
## **الأرقام المخزنة كنص**
في بعض الأحيان، قد تكون الأرقام مهيأة ومخزنة في الخلايا كنص. يمكن أن يسبب هذا مشاكل في الحسابات أو إنتاج ترتيبات فرز مربكة. الأرقام التي تم تهيئتها كنص تكون محاذية إلى اليسار بدلاً من اليمين في الخلية. إذا لم تُعَد الصيغة التي يجب أن تقوم بعملية رياضية على الخلايا قيمة، فحقق محاذاة في الخلايا التي تشير إليها الصيغة - قد تكون بعض أو كل تلك الخلايا أرقامًا تم تهيئتها كنص.

يمكنك استخدام خيارات التحقق من الأخطاء لتحويل الأرقام المخزنة كنص إلى أرقام حقيقية بسرعة. في Microsoft Excel 2003:

1. على قائمة **الأدوات**، انقر على **خيارات**.
1. حدد علامة التبويب التحقق من الأخطاء.
   خيار **العدد المخزن كنص** يتم التحقق منه بشكل افتراضي. 
1. قم بتعطيله.
   انظر الصورة أدناه لكيفية عرض المثلث الأخضر للبيانات في MS Excel.

![todo:image_alt_text](use-error-checking-options_1.png)

يوضح الكود المصدري العينة التالي كيفية تعطيل خيار التحقق من الأخطاء للأرقام المخزنة كنص لورقة العمل في ملف XLS القالب باستخدام واجهات برمجة التطبيقات Aspose.Cells. 

**Java**

{{< highlight csharp >}}

 //Create a workbook and opening a template spreadsheet

Workbook workbook = new Workbook("d:\\files\\Book1.xls");

//Get the first worksheet

Worksheet sheet = workbook.getWorksheets().get(0);

//Instantiate the error checking options

ErrorCheckOptionCollection opts = sheet.getErrorCheckOptions();

int index = opts.add();

ErrorCheckOption opt = opts.get(index);

//Disable the numbers stored as text option

opt.setErrorCheck(ErrorCheckType.TEXT_NUMBER, false);

//Set the range

opt.addRange(CellArea.createCellArea(0, 0, 65535, 255));

//Save the Excel file

workbook.save("d:\\files\\out_test.xls");



{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
