---
title: حدد ما إذا كان حجم الورق الخاص بورقة العمل تلقائيًا
type: docs
weight: 90
url: /ar/net/determine-if-paper-size-of-worksheet-is-automatic/
---
## **سيناريوهات الاستخدام الممكنة**

 في معظم الأحيان ، يكون حجم الورق الخاص بورقة العمل تلقائيًا. عندما يكون تلقائيًا ، غالبًا ما يتم تعيينه كـ*رسالة* . في بعض الأحيان يقوم المستخدم بتعيين حجم الورق لورقة العمل وفقًا لمتطلباته. في هذه الحالة ، لا يكون حجم الورق تلقائيًا. يمكنك معرفة ما إذا كان حجم ورقة العمل تلقائيًا أم لا باستخدام ملف[**ورقة العمل. PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/isautomaticpapersize)خاصية.

## **حدد ما إذا كان حجم الورق الخاص بورقة العمل تلقائيًا**

يقوم نموذج التعليمات البرمجية المعطى أدناه بتحميل ملفي Excel التاليين

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

ومعرفة ما إذا كان حجم الورق لورقة العمل الأولى تلقائيًا أم لا. في Microsoft Excel ، يمكنك التحقق مما إذا كان حجم الورق تلقائيًا أم لا عبر نافذة إعداد الصفحة كما هو موضح في لقطة الشاشة هذه.

![ما يجب القيام به: image_بديل_نص](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.cs" >}}

## **إخراج وحدة التحكم**

فيما يلي إخراج وحدة التحكم لنموذج التعليمات البرمجية أعلاه عند تنفيذه باستخدام ملفات Excel النموذجية المحددة.

{{< highlight "java" >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
