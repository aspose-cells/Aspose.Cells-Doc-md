---
title: تخصيص معلمات التهيئة
type: docs
weight: 10
url: /ar/net/aspose-cells-gridweb/customize-parameters-in-client-side-script/
keywords: GridWeb، تخصيص، تخصيص المعلمات
description: كيفية تخصيص معلمات التهيئة في النص النصي الجانبي لـ Aspose.Cells.GridWeb.
---

{{% alert color="primary" %}} 

يمكن للمطورين تعيين قيمة معلمة التهيئة المختلفة لتنفيذ سلوك مختلف لعنصر التحكم Aspose.Cells.GridWeb في acwmain.js.  

{{% /alert %}} 

### **معلمات**

|**المعلمة**|**الوصف**|
| :- | :- |
|needInitAlignmentAdjust| ما إذا كان سيتم تنفيذ محاذاة رأسية لمحتوى الخلية عند البدء، سيتسبب ذلك في بعض الوقت لإجراء عمل المحاذاة، إذا كانت لديها الجداول الخلية كبيرة، ستكون الأداء سيئًا، إذا كان المستخدم لا يهتم بالمحاذاة الرأسية، فيمكنه تعيينها على false، القيمة الافتراضية هي true|
|focusinside| ما إذا كان يتم التركيز داخل نطاق الخلية، القيمة الافتراضية هي true|
|copy_with_style| ما إذا كان يتم النسخ مع النمط، القيمة الافتراضية هي false مما يعني فقط نسخ محتوى الخلية|
|useESCAsLeave| السلوك الافتراضي عند الضغط على esc يعمل كعملية إلغاء تحرير الخلية، إذا قمنا بتعيين هذه القيمة على true، سنعتبرها مفتاحًا قصيرًا لمغادرة الخلية دون تغيير العودة إلى القيمة السابقة، وسيغير أيضًا طريقة التحرير الداخلية إلى طريقة التحرير السريعة، القيمة الافتراضية هي false|
|needValidateall| ما إذا كان سيتم التحقق من جميع التحققات على ورقة العمل النشطة عند التحقق، (في صفحة التحكم aspx قم بتعيين ForceValidation="True") . القيمة الافتراضية هي false|
|scrollToInvalidate| ما إذا كان سيتم التمرير وجلب أول خلية غير صالحة إلى العرض عند needValidateall يتم تعيينها على true. القيمة الافتراضية هي true|


يظهر إخراج مثال الكود أدناه، يرجى التحقق من [ملف الإكسل النموذجي](valign.xlsx):

**needInitAlignmentAdjust=true** 

![todo:image_alt_text](align_true.png)

**needInitAlignmentAdjust=false** 

![todo:image_alt_text](align_false.png)

**focusinside=true** 
طريقة التحرير الداخلية - عند إدخال النص، سيظل قيمة الخلية القديمة محفوظة   

![todo:image_alt_text](focus_inside_true.png)

**focusinside=false** 
طريقة التحرير السريعة - عند إدخال النص، سيتم كتابة قيمة الخلية القديمة، إذا كنت ترغب في التحرير استنادًا إلى القيمة القديمة للخلية، يمكنك النقر على الخلية

![todo:image_alt_text](focus_inside_false.png)



