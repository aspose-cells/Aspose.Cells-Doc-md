---
title: تحديد ما إذا كان حجم الورق للورقة التفاعلي
type: docs
weight: 20
url: /ar/java/determine-if-paper-size-of-worksheet-is-automatic/
---

## **سيناريوهات الاستخدام المحتملة**

في معظم الأحيان، يكون حجم الورقة في ورقة العمل تلقائيًا. عندما يكون تلقائيًا، فإنه غالبًا ما يُعين على أن يكون *Letter*. أحيانًا يقوم المستخدم بتعيين حجم الورقة في ورقة العمل حسب احتياجاته. في هذه الحالة، لا يكون حجم الورقة تلقائيًا. يمكنك معرفة ما إذا كان حجم الورقة في ورقة العمل تلقائيًا أم لا باستخدام الطريقة ( [**Worksheet.getPageSetup().isAutomaticPaperSize()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#IsAutomaticPaperSize) ).

## **تحديد ما إذا كان حجم الورق للورقة تلقائي**

الشيفرة العينية المعطاة أدناه تحمل الملفات الإكسل التاليتين

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496700.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496701.xlsx)

ثم ابحث عما إذا كان حجم الورق لأول ورقة فيهما تلقائيًا أم لا. في Microsoft Excel، يمكنك التحقق ما إذا كان حجم الورق تلقائيًا أو لا من خلال نافذة إعداد الصفحة كما هو موضح في هذه لقطة الشاشة.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.java" >}}

## **مخرجات الوحدة**

هذا هو إخراج وحدة التحكم للشيفرة العينية أعلاه عند تنفيذها مع ملفات Excel العينية المعطاة.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: false

First Worksheet of Second Workbook - IsAutomaticPaperSize: true

{{< /highlight >}}
