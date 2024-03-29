﻿---
title: استخدم خيارات تدقيق الأخطاء
type: docs
weight: 60
url: /ar/java/use-error-checking-options/
---
{{% alert color="primary" %}} 

Microsoft يسمح Excel للمستخدمين بتحديد خيارات وقواعد التحقق من الأخطاء. غالبًا ما يرى المستخدمون عمليات التحقق من الأخطاء عند إنشاء الصيغ ، حيث يتم تمييز مثلث صغير في الزاوية اليمنى العلوية للخلية عند وجود مشكلة في الخلية. يوفر Excel معلومات تساعد المستخدمين على تصحيح المشكلات الشائعة.

{{% /alert %}} 
## **أنواع الأخطاء**
تتطلب الأخطاء التي تعني أن الصيغة لا يمكنها إرجاع نتيجة - مثل قسمة رقم على صفر - اهتمامًا فوريًا ويتم عرض قيمة خطأ في الخلية. يؤدي النقر فوق المثلث الأخضر إلى إظهار علامة تعجب ، والنقر فوق هذا يفتح قائمة الخيارات.

يمكن حل الخطأ باستخدام الخيارات ، أو يمكن تجاهله. يعني تجاهل الخطأ أن هذا الخطأ لن يظهر في عمليات فحص الأخطاء الأخرى.

يوفر Aspose.Cells خصائص خيار فحص الأخطاء. تدير فئة ErrorCheckOptions أنواعًا مختلفة من فحوصات الأخطاء ، على سبيل المثال الأرقام المخزنة كنص وأخطاء حساب الصيغة وأخطاء التحقق من الصحة. استخدم تعداد ErrorCheckType لتعيين تدقيق الخطأ المطلوب.
## **Numbers تم تخزينه كنص**
من حين لآخر ، قد يتم تنسيق الأرقام وتخزينها في الخلايا كنص. يمكن أن يتسبب ذلك في حدوث مشكلات في العمليات الحسابية أو إنتاج أوامر فرز مربكة. تتم محاذاة Numbers المنسقة كنص إلى اليسار بدلاً من المحاذاة لليمين في الخانة. إذا كانت الصيغة التي يجب أن تؤدي عملية حسابية على الخلايا لا تُرجع قيمة ، فتحقق من المحاذاة في الخلايا التي تشير إليها الصيغة - قد تكون بعض هذه الخلايا أو كلها أرقامًا منسقة كنص.

يمكنك استخدام خيارات تدقيق الأخطاء لتحويل الأرقام المخزنة كنص إلى أرقام حقيقية بسرعة. في Microsoft Excel 2003:

1.  على ال**أدوات** القائمة ، انقر فوق**خيارات**.
1. حدد علامة التبويب تدقيق الأخطاء.
   **الرقم الذي تم تخزينه كنص** يتم تحديد الخيار افتراضيًا.
1. قم بتعطيله.
 انظر إلى الصورة أدناه حول كيفية عرض المثلث الأخضر للبيانات في MS Excel.

![ما يجب القيام به: image_بديل_نص](use-error-checking-options_1.png)

 يوضح نموذج التعليمات البرمجية التالي كيفية تعطيل الأرقام المخزنة كخيار تدقيق أخطاء النص لورقة عمل في ملف القالب XLS باستخدام واجهات برمجة التطبيقات Aspose.Cells.

**Java**

{{< highlight "csharp" >}}

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
