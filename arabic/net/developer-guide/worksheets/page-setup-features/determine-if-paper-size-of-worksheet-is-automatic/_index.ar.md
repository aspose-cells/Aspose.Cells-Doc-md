---
title: تحديد ما إذا كان حجم الورق للورقة التفاعلي
type: docs
weight: 90
url: /ar/net/determine-if-paper-size-of-worksheet-is-automatic/
description: تشرح هذه المقالة كيفية استخدام واجهة برمجة التطبيقات C# أو مكتبة .NET الشيفرة العينية لتحديد ما إذا كان حجم الورق للورقة تلقائي برمجيًا.
keywords: تحديد ما إذا كان حجم ورقة الورق تلقائيًا باستخدام c#
---

## **سيناريوهات الاستخدام المحتملة**

في معظم الأحيان، يكون حجم ورقة الورق تلقائيًا. عندما يكون تلقائيًا، يتم تعيينه في كثير من الأحيان كـ *Letter*. أحيانًا يقوم المستخدم بتعيين حجم ورقة الورق حسب احتياجاته. في هذه الحالة، لا يكون حجم الورق تلقائيًا. يمكنك معرفة ما إذا كان حجم ورقة الورق للورقة تلقائيًا أم لا باستخدام خاصية [**Worksheet.PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/isautomaticpapersize).

## **تحديد ما إذا كان حجم الورق للورقة تلقائي**

الشيفرة العينية المعطاة أدناه تحمل الملفات الإكسل التاليتين

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

ثم ابحث عما إذا كان حجم الورق لأول ورقة فيهما تلقائيًا أم لا. في Microsoft Excel، يمكنك التحقق ما إذا كان حجم الورق تلقائيًا أو لا من خلال نافذة إعداد الصفحة كما هو موضح في هذه لقطة الشاشة.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.cs" >}}

## **مخرجات الوحدة**

هذا هو إخراج وحدة التحكم للشيفرة العينية أعلاه عند تنفيذها مع ملفات Excel العينية المعطاة.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
