---
title: إضافة تحقق دالة جانب الخادم المخصص
type: docs
weight: 110
url: /ar/net/aspose-cells-gridweb/add-custom-server-side-function-validation/
keywords: GridWeb، التحقق من جانب الخادم
description: يقدم هذا المقال كيفية العمل مع التحقق من جانب الخادم في GridWeb.
---

## **سيناريوهات الاستخدام المحتملة**
في بعض الأحيان، قد تحتاج أحيانًا إلى تنفيذ التحقق من البيانات على الخادم. يسمح Aspose.Cells.GridWeb لك بإضافة التحقق المخصص للبيانات من جانب الخادم. يجب عليك تحديد نطاق الخلية أو المنطقة. يمكنك أيضًا تعيين وظائف التحقق من جانب العميل للاستدعاءات مع التحقق المخصص من جانب الخادم.
## **إضافة تحقق دالة جانب الخادم المخصص**
تحتاج إلى ضبط فئة التحقق من الخادم التي تنفذ واجهة **GridCustomServerValidation** عبر **GridValidation.ServerValidation** السمة. تحتاج أيضًا لضبط وظيفة التحقق من العميل (يجب كتابتها في JavaScript على الجانب العميل)، يتعين أن تكون هذه الوظيفة إجبارية للتحقق من البيانات على الجانب العميل عند الاستدعاء. يمكنك ضبط سلسلة رسالة الخطأ عبر خصائص **GridValidation.ErrorMessage** وعنوانها عبر خصائص **GridValidation.ErrorTitle** لاحتياجاتك. يرجى الاطلاع على سلسلة من لقطات الشاشة التي تظهر كيفية عملها (خطوة بخطوة) في سيناريو معين بعد تنفيذ الرمز المثالي أدناه. في المثال، لا يمكنك تحديث البيانات في خلايا B2:C3. عند محاولة تحرير تلك الخلايا في الورقة، ستحصل على بعض رسائل الخطأ وسيتم استعادة القيمة السابقة. يمكنك فتح نافذة Console (في متصفحك) لطباعة معلومات/تفاصيل الخلية لأحداث معينة. 

![todo:image_alt_text](add-custom-server-side-function-validation_1.png)

![todo:image_alt_text](add-custom-server-side-function-validation_2.png)

![todo:image_alt_text](add-custom-server-side-function-validation_3.png)

![todo:image_alt_text](add-custom-server-side-function-validation_4.png)

![todo:image_alt_text](add-custom-server-side-function-validation_5.png)
## **الكود المثالي**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Cells-AddCustomServerSideFunctionValidation.aspx.cs" >}}
