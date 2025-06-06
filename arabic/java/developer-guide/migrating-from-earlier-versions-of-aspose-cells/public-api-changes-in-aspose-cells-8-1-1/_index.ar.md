---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 8.1.1
type: docs
weight: 60
url: /ar/java/public-api-changes-in-aspose-cells-8-1-1/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات الخارجية API لـ Aspose.Cells من الإصدار 8.1.0 إلى 8.1.1، التي قد تكون مثيرة للاهتمام لمطوري الوحدات والتطبيقات. يتضمن ليس فقط [الأساليب العامة الجديدة والمُحدّثة](/cells/ar/java/public-api-changes-in-aspose-cells-8-1-1/)، بل أيضًا وصفًا لأية [تغييرات في السلوك](/cells/ar/java/public-api-changes-in-aspose-cells-8-1-1/) خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **الخصائص والميزات المضافة**
### **تمت إضافة خاصية HtmlSaveOptions.PresentationPreference**
فئة HtmlSaveOptions قد عرضت getter/setter لخاصية PresentationPreference والتي يمكن استخدامها لتقديم النتائج بتخطيط أفضل عند تصدير الجداول الخاصة بك إلى HTML أو MHTML. القيمة الافتراضية هي false. حيث إذا تم تعيينها على true، فإن API Aspose.Cells تصدر محتويات الورقة العمل بتقديم أفضل.

{{% alert color="primary" %}} 

يرجى التحقق من المقال المفصل حول [استخدام خيار PresentationPreference لتحسين التخطيط](/cells/ar/java/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}} 
### **تمت إضافة دعم لسيناريوهات الورقة العمل**
السيناريو هو نموذج ماذا لو يشمل خلايا الإدخال المتغيرة مرتبطة بصيغة واحدة أو أكثر. فقد عرض Aspose.Cells getter وsetter لخاصية Worksheet.Scenarios بالإضافة إلى الفئات التالية لمساعدة المطورين في إنشاء وتلاعب وإزالة السيناريوهات.

1. السيناريو: يمثل سيناريو فردي.
1. مجموعة السيناريو: تمثل مجموعة من السيناريوهات.
1. مجموعة خلايا الإدخال السيناريو: تمثل قائمة بالخلايا الخاصة بالإدخال لسيناريو معين.
1. خلية الإدخال السيناريو: تمثل خلية إدخال من مجموعة خلايا الإدخال لسيناريو معين.

{{% alert color="primary" %}} 

يرجى التحقق من المقال المفصل حول [كيفية إنشاء أو تعديل أو إزالة السيناريوهات من الأوراق العمل](/cells/ar/java/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
## **تغيير في سلوك لاستثناء الخلايا**
مع الإصدارات السابقة لAspose.Cells for Java API، عند تحميل جدول بيانات محتمل تالف في نسخة من دفتر العمل، كانت الواجهة تقوم برمي رسالة عامة دون ذكر مكان حدوث المشكلة. لقد قمنا بتغيير هذا السلوك لـ 8.1.1 حتى تقوم الواجهة برمي استثناء مع رسالة ذات معنى تشير إلى مكان (أي خلية) وما (تعبير الصيغة) الذي يتسبب في الاستثناء عند قراءة ملف القالب.
{{< app/cells/assistant language="java" >}}
