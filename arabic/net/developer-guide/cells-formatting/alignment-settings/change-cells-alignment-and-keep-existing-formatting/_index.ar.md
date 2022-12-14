---
title: قم بتغيير Cells المحاذاة والاحتفاظ بالتنسيق الموجود
type: docs
weight: 340
url: /ar/net/change-cells-alignment-and-keep-existing-formatting/
---
## **سيناريوهات الاستخدام الممكنة**

في بعض الأحيان ، تريد تغيير محاذاة عدة خلايا ولكنك تريد أيضًا الاحتفاظ بالتنسيق الحالي. يسمح لك Aspose.Cells بالقيام بذلك باستخدام ملف[**StyleFlag. التحالفات**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments) منشأه. إذا كنت ستقوم بتعيينه**حقيقي** ، ستحدث التغييرات في المحاذاة وإلا لم يحدث ذلك. يرجى الملاحظة،[**النمط**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) يتم تمرير الكائن كمعامل إلى[**النطاق.**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle)الطريقة التي تطبق بالفعل التنسيق على نطاق من الخلايا.

## **قم بتغيير Cells المحاذاة والاحتفاظ بالتنسيق الموجود**

 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](67338585.xlsx) ، ينشئ النطاق ويقوم المركز بمحاذاة أفقيًا ورأسيًا ويحافظ على التنسيق الحالي كما هو. تقارن لقطة الشاشة التالية نموذج ملف Excel و[إخراج ملف Excel](67338586.xlsx)ويوضح أن جميع التنسيقات الموجودة للخلايا هي نفسها فيما عدا أن الخلايا أصبحت الآن محاذاة للوسط أفقيًا وعموديًا.

![ما يجب القيام به: image_بديل_نص](change-cells-alignment-and-keep-existing-formatting_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
