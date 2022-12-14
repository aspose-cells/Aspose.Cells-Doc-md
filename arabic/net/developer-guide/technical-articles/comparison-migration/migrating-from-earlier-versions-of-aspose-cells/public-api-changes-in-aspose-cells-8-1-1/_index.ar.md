---
title: عام API التغييرات في Aspose.Cells 8.1.1
type: docs
weight: 50
url: /ar/net/public-api-changes-in-aspose-cells-8-1-1/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.1.0 إلى 8.1.1 ، والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة خاصية HtmlSaveOptions.PresentationPreference**
كشفت فئة HtmlSaveOptions عن خاصية PresentationPreference التي يمكن استخدامها لتقديم النتائج بتخطيط أفضل عند تصدير جداول البيانات إلى HTML أو MHTML. القيمة الافتراضية هي كاذبة. بينما إذا تم ضبطه على "صحيح" ، فإن Aspose.Cells API سيقوم بتصدير محتويات ورقة العمل مع عرض تقديمي أفضل.

{{% alert color="primary" %}} 

 يرجى مراجعة المقال المفصل على[استخدم خيار العرض التقديمي لتخطيط أفضل](/cells/ar/net/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}}
## **تمت إضافة دعم لسيناريوهات ورقة العمل**
 يُطلق على السيناريو اسم نموذج ماذا لو يتضمن خلايا إدخال متغيرة مرتبطة ببعضها البعض بواسطة صيغة واحدة أو أكثر وفقًا لذلك. قام Aspose.Cells API بعرض خاصية Worksheet.Senarios جنبًا إلى جنب مع الفئات التالية من أجل تسهيل المستخدمين في إنشاء السيناريوهات ومعالجتها وإزالتها من أوراق العمل ،

1. السيناريو: يمثل سيناريو فردي.
1. مجموعة سيناريو: يمثل مجموعة من السيناريوهات.
1. ScenarioInputCellCollection: يمثل قائمة خلايا الإدخال لسيناريو معين.
1. ScenarioInputCell: يمثل خلية إدخال من مجموعة خلايا الإدخال لسيناريو معين.

{{% alert color="primary" %}} 

 يرجى مراجعة المقال المفصل على[كيفية إنشاء السيناريوهات أو معالجتها أو إزالتها من أوراق العمل](/cells/ar/net/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
