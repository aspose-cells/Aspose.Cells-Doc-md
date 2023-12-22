---
title: قم بتغيير المحاذاة Cells واحتفظ بالتنسيق الموجود
description: استخدم مكتبة Aspose.Cells لتغيير محاذاة الخلية والحفاظ على التنسيق الحالي
keywords: Aspose.Cells, C#, Cell alignment, preserve existing formatting
type: docs
weight: 340
url: /ar/net/change-cells-alignment-and-keep-existing-formatting/
---
##  **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، تريد تغيير محاذاة خلايا متعددة ولكنك تريد أيضًا الاحتفاظ بالتنسيق الحالي. Aspose.Cells يسمح لك بالقيام بذلك باستخدام[**StyleFlag.Alignments**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments) ملكية. إذا قمت بتعيينه *صحيح**، فإن التغييرات في المحاذاة ستحدث وإلا فلن يحدث ذلك. يرجى الملاحظة،[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) يتم تمرير الكائن كمعلمة إلى[**Range.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle)الطريقة التي تطبق التنسيق فعليًا على نطاق من الخلايا.

##  **قم بتغيير المحاذاة Cells واحتفظ بالتنسيق الموجود**

 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[عينة من ملف إكسل](67338585.xlsx) ، يقوم بإنشاء النطاق ومحاذاته في الوسط أفقيًا وعموديًا ويحافظ على التنسيق الحالي كما هو. تقارن لقطة الشاشة التالية نموذج ملف Excel و[إخراج ملف إكسل](67338586.xlsx) ويبين أن جميع التنسيقات الموجودة للخلايا هي نفسها فيما عدا أن الخلايا أصبحت الآن محاذاة للوسط أفقيًا وعموديًا.

![ما يجب القيام به:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

##  **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
