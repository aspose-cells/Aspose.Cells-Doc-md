---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 8.1.1
type: docs
weight: 50
url: /ar/net/public-api-changes-in-aspose-cells-8-1-1/
---

{{% alert color="primary" %}} 

توضح هذه الوثيقة التغييرات التي طرأت على واجهة برمجة التطبيقات في Aspose.Cells من الإصدار 8.1.0 إلى 8.1.1، والتي قد تكون مهمة لمطوري الوحدات/التطبيقات. وتتضمن ليس فقط الطرق العامة الجديدة والمحدثة، ولكن أيضا وصفًا لأي تغيير في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة خاصية HtmlSaveOptions.PresentationPreference**
قدمت فئة HtmlSaveOptions خاصية PresentationPreference التي يمكن استخدامها لعرض النتائج بتخطيط أفضل عند تصدير جداول البيانات إلى HTML أو MHTML. القيمة الافتراضية هي خاطئة. في حال تعيينها على true، ستصدر واجهة برمجة التطبيقات Aspose.Cells محتويات الورقة العملية بتوزيع أفضل.

{{% alert color="primary" %}} 

يرجى التحقق من المقال المفصل حول [خيار Use PresentationPreference لتحسين التخطيط](/cells/ar/net/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}}
## **تمت إضافة دعم لسيناريوهات الورقة العمل**
السيناريو هو نموذج تخمين يشمل الخلايا المتغيرة المرتبطة ببعضها بواسطة صيغ واحد أو أكثر على التوالي. قدمت واجهة برمجة التطبيقات Aspose.Cells خاصية Worksheet.Scenarios بجانب الفئات التالية لتسهيل عمل المستخدمين في إنشاء وتلاعب وإزالة السيناريوهات من الأوراق العملية: 

1. السيناريو: يمثل سيناريو فردي.
1. مجموعة السيناريو: تمثل مجموعة من السيناريوهات.
3. ScenarioInputCellCollection: يمثل قائمة الخلايا الداخلية لسيناريو معين.
4. ScenarioInputCell: يمثل خلية الدخل من قائمة الخلايا الداخلية لسيناريو معين.

{{% alert color="primary" %}} 

يرجى التحقق من المقال المفصل حول [كيفية إنشاء، تلاعب أو إزالة السيناريوهات من الأوراق العملية](/cells/ar/net/create-manipulate-or-remove-scenarios-from-worksheets/)

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
