---
title: عام API التغييرات في Aspose.Cells 8.1.1
type: docs
weight: 60
url: /ar/java/public-api-changes-in-aspose-cells-8-1-1/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.1.0 إلى 8.1.1 ، والتي قد تهم مطوري البرامج والتطبيقات. لا يشمل فقط[الأساليب العامة الجديدة والمحدثة](/cells/ar/java/public-api-changes-in-aspose-cells-8-1-1/) ، ولكن أيضًا وصفًا لأي[التغييرات في السلوك](/cells/ar/java/public-api-changes-in-aspose-cells-8-1-1/) خلف الكواليس عام Aspose.Cells.

{{% /alert %}} 
## **الخصائص والميزات المضافة**
### **تمت إضافة خاصية HtmlSaveOptions.PresentationPreference**
كشفت فئة HtmlSaveOptions عن خاصية getter / setter لخاصية PresentationPreference والتي يمكن استخدامها لعرض النتائج بتخطيط أفضل عند تصدير جداول البيانات إلى HTML أو MHTML. القيمة الافتراضية هي كاذبة. بينما إذا تم ضبطه على "صحيح" ، يقوم Aspose.Cells API بتصدير محتويات ورقة العمل مع عرض تقديمي أفضل.

{{% alert color="primary" %}} 

 يرجى مراجعة المقال المفصل على[استخدم خيار العرض التقديمي لتخطيط أفضل](/cells/ar/java/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}} 
### **تمت إضافة دعم لسيناريوهات ورقة العمل**
السيناريو هو نموذج ماذا لو يتضمن خلايا إدخال متغيرة مرتبطة ببعضها البعض بواسطة صيغة واحدة أو أكثر. لقد كشف Aspose.Cells برنامج getter و setter لخاصية Worksheet.Senarios جنبًا إلى جنب مع الفئات التالية لمساعدة المطورين على إنشاء السيناريوهات ومعالجتها وإزالتها.

1. السيناريو: يمثل سيناريو فردي.
1. مجموعة سيناريو: يمثل مجموعة من السيناريوهات.
1. ScenarioInputCellCollection: يمثل قائمة خلايا الإدخال لسيناريو معين.
1. ScenarioInputCell: يمثل خلية إدخال من مجموعة خلايا الإدخال لسيناريو معين.

{{% alert color="primary" %}} 

 يرجى مراجعة المقال المفصل على[كيفية إنشاء السيناريوهات أو معالجتها أو إزالتها من أوراق العمل](/cells/ar/java/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
## **التغيير في سلوك CellsException**
مع الإصدارات السابقة من Aspose.Cells for Java API ، عندما تم تحميل جدول بيانات معطوب في مثيل Workbook ، كان API يميل إلى إلقاء رسالة عامة دون الإشارة إلى مكان المشكلة. لقد قمنا بتغيير هذا السلوك لـ 8.1.1 بحيث يطرح API استثناءً برسالة ذات مغزى تشير إلى أين (أي خلية) وماذا (تعبير الصيغة) يسبب الاستثناء عند قراءة ملف القالب.
