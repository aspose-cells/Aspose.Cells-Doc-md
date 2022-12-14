---
title: قم بتغيير Cells المحاذاة والاحتفاظ بالتنسيق الموجود
type: docs
weight: 260
url: /ar/java/change-cells-alignment-and-keep-existing-formatting/
---
## **سيناريوهات الاستخدام الممكنة**

في بعض الأحيان ، تريد تغيير محاذاة عدة خلايا ولكنك تريد أيضًا الاحتفاظ بالتنسيق الحالي. يسمح لك Aspose.Cells بالقيام بذلك باستخدام ملف[**StyleFlag. التحالفات**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#Alignments) منشأه. إذا كنت ستقوم بتعيينه**حقيقي** ، ستحدث التغييرات في المحاذاة وإلا لم يحدث ذلك. يرجى الملاحظة،[**النمط**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) يتم تمرير الكائن كمعامل إلى[**Range.applyStyle ()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)) الأسلوب الذي يطبق التنسيق فعليًا على نطاق الخلايا.

## **قم بتغيير Cells المحاذاة والاحتفاظ بالتنسيق الموجود**

يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](67338592.xlsx)، ينشئ النطاق ويقوم المركز بمحاذاة أفقيًا ورأسيًا ويحافظ على التنسيق الحالي كما هو. تقارن لقطة الشاشة التالية نموذج ملف Excel و[إخراج ملف Excel](67338591.xlsx)ويوضح أن جميع التنسيقات الموجودة للخلايا هي نفسها فيما عدا أن الخلايا أصبحت الآن محاذاة للوسط أفقيًا وعموديًا.

![ما يجب القيام به: image_بديل_نص](change-cells-alignment-and-keep-existing-formatting_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.java" >}}
