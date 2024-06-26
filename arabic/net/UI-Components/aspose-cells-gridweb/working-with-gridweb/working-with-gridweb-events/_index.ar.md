---
title: العمل مع أحداث GridWeb
type: docs
weight: 70
url: /ar/net/aspose-cells-gridweb/gridweb-events/
keywords: GridWeb، events، event
description: يقدم هذا المقال كيفية العمل مع أنواع من الأحداث في GridWeb.
---

{{% alert color="primary" %}} 

يجب على جميع المبرمجين أن يكونوا على دراية بالأحداث وغرضها. تُستخدم الأحداث لإرسال إشعارات بالتغييرات التي قد تحدث في التحكم أو الفئة. يحتوي Aspose.Cells.GridWeb على عدة أحداث يمكن استخدامها لأداء مهام محددة عند حدوث تغييرات معينة في التحكم.

يوفر هذا الموضوع مقدمة لجميع الأحداث المدعومة من قِبل تحكم Aspose.Cells.GridWeb مع بعض التفاصيل حول كيفية التعامل مع هذه الأحداث.

{{% /alert %}} 
## **العمل مع أحداث الشبكة**
### **مقدمة لأحداث الشبكة**
يدعم تحكم Aspose.Cells.GridWeb عدة أحداث توفر مزيدًا من التحكم لأداء العمليات عند حدوث أحداث معينة في التحكم. يمكن العثور على قائمة كاملة من الأحداث المدعومة من تحكم Aspose.Cells.GridWeb أدناه.

{{% alert color="primary" %}} 

لا تتضمن هذه القائمة الأحداث الموروثة من تحكم Aspose.Cells.GridWeb من الفئة Control.

{{% /alert %}} 

|**النشاطات** |**الوصف** |
| :- | :- |
|CellCommand |تحدث عندما يتم النقر على رابط الأمر في خلية. عند نشوب هذا الحدث، يوفر معلمة e.Argument اسم الأمر. |
|CellDoubleClick |يحدث عندما يتم النقر المزدوج على الخلية. |
|CellError |يحدث عندما يكون لدى قيمة الإدخال في الخلية خطأ ما. |
|ColumnDeleted |يحدث عندما يقوم المستخدم بحذف عمود من ورقة العمل باستخدام القائمة الجانبية للعميل. |
|ColumnDeleting |يحدث عندما يحاول المستخدم حذف عمود من ورقة العمل باستخدام القائمة الجانبية للعميل. |
|ColumnDoubleClick |يحدث عندما يتم النقر المزدوج على رأس العمود. |
|ColumnInserted |يحدث عندما يقوم المستخدم بإدراج عمود في ورقة العمل باستخدام القائمة الجانبية للعميل. |
|CustomCommand |يحدث عندما يقوم المستخدم بالنقر على زر الأمر المخصص. |
|LoadCustomData |يحدث عندما يتم تعيين خاصية EnableSession لعنصر التحكم على القيمة الخاطئة ويحتاج إلى تحميل بيانات ورقة العمل. يمكنك التعامل مع هذا الحدث في وضع بدون جلسة لتحميل بيانات ورقة العمل من ملف أو قاعدة بيانات. |
|PageIndexChanged |يحدث عند تغيير فهرس صفحة الورقة لعنصر التحكم. |
|RowDeleted |يحدث عندما يقوم المستخدم بحذف صف من ورقة العمل باستخدام القائمة الجانبية للعميل. |
|RowDeleting |يحدث عندما يحاول المستخدم حذف صف من ورقة العمل باستخدام القائمة الجانبية للعميل. |
|RowDoubleClick |يحدث عندما يتم النقر المزدوج على رأس الصف. |
|RowInserted |يحدث عندما يقوم المستخدم بإدراج صف في ورقة العمل باستخدام القائمة الجانبية للعميل. |
|SaveCommand |يحدث عندما يتم النقر على زر **حفظ**. |
|SheetDataUpdated |يحدث عندما يكون العنصر التحكم قد حمل البيانات المنشورة وقد حدث تحديث لبيانات ورقة العمل. |
|SheetTabClick |يحدث عندما يتم النقر على علامة التبويب للورقة. |
|SubmitCommand |يحدث عندما يتم النقر على زر **إرسال**. |
|UndoCommand |يحدث عندما يتم النقر على زر **تراجع**. |
|AjaxCallFinished |يتم تشغيله عند اكتمال تحديث AJAX لعنصر التحكم. (على الشروط أن تكون EnableAJAX بقيمة صحيحة). |
|CellModifiedOnAjax |يتم تشغيله عند تعديل الخلية في استدعاء AJAX. |
|OnAfterColumnFilter |يتم تشغيله بعد تطبيق التصفية على عمود. |
|OnBeforeColumnFilter |يتم تشغيله قبل تطبيق التصفية على عمود. |
## **معالجة أحداث الجدول**
لأداء عملية معينة عند حدوث حدث معين، يجب علينا إنشاء معالج حدث. يقوم معالج الحدث بأداء المهمة المطلوبة عند حدوث حدث معين. الخطوات الموضحة أدناه توضح كيفية معالجة حدث بسيط لجدول باستخدام Visual Studio.
### **الخطوة 1: تحديد حدث لعنصر تحكم Aspose.Cells.GridWeb**
1. حدد عنصر تحكم Aspose.Cells.GridWeb وافتح مربع الحوار الخاص به من الجهة اليمنى.
1. انقر فوق زر **علامة التبويب الخاصة بالأحداث**.
1. حدد حدثًا.
   في هذا المثال، تم اختيار حدث SaveCommand.
### **الخطوة 2: إنشاء معالج حدث**
1. انقر نقرًا مزدوجًا فوق حدث في مربع الحوار. 

   **النقر المزدوج على الحدث المحدد** 

![todo:image_alt_text](working-with-gridweb-events_1.png)




عند النقر المزدوج على الحدث، يتم إنشاء معالج حدث تلقائيًا بواسطة Visual Studio. 

**معالج الحدث الذي تم إنشاءه بواسطة Visual Studio** 

![todo:image_alt_text](working-with-gridweb-events_2.png)




1. أضف كودًا لأداء بعض الإجراء داخل معالج الحدث.

هنا، تمت إضافة سطر واحد من الكود الذي يحفظ محتوى الجدول في ملف Excel عند النقر على زر **Save**.

للحصول على مزيد من المعلومات، قم بتحريك المؤشر إلى الأعلى لعرض بعض الشيفرة ثم ستكتشف أن Visual Studio ذكي بما فيه الكفاية لإضافة معالج حدث إلى حدث SaveCommand في GridWeb.
### **الخطوة 3: تشغيل التطبيق**
1. قم ببناء التطبيق وتشغيله.
1. انقر على **حفظ**.

يتم حفظ محتوى الجدول في ملف Excel. 

**التطبيق في وضع التشغيل** 

![todo:image_alt_text](working-with-gridweb-events_3.png)
