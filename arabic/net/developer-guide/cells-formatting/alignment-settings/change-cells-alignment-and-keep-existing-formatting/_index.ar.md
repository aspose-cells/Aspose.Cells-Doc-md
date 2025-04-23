---
title: تغيير توجيه الخلايا والاحتفاظ بالتنسيقات الحالية
description: استخدم مكتبة Aspose.Cells لتغيير توجيه الخلية والحفاظ على التنسيق الحالي
keywords: Aspose.Cells، C#، توجيه الخلية، الحفاظ على التنسيق الحالي
type: docs
weight: 340
url: /ar/net/change-cells-alignment-and-keep-existing-formatting/
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، ترغب في تغيير توجيه خلايا متعددة ولكنك ترغب أيضًا في الاحتفاظ بالتنسيق الحالي. Aspose.Cells يسمح لك بالقيام به باستخدام الخاصية [**StyleFlag.Alignments**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments). إذا قمت بضبطها على **true**, سيحدث تغيير في التوجيه وإلا لن يحدث. يرجى ملاحظة، يتم تمرير كائن [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) كمعلمة إلى طريقة [**Range.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle) التي تقوم بتطبيق التنسيق على مجموعة من الخلايا.

## **تغيير توجيه الخلايا والاحتفاظ بالتنسيقات الحالية**

الكود النموذجي التالي يقوم بتحميل الملف الإكسل النموذجي، ينشئ المدى ويضبط توسيطه أفقيا وعموديا ويحتفظ بالتنسيق الحالي. الصورة النموذجية التالية تقارن ملف الإكسل النموذجي وملف الإكسل الناتج وتُظهر أن جميع التنسيقات الحالية للخلايا هي نفسها باستثناء أن الخلايا الآن موجهة في منتصف الخط أفقيًا وعموديًا.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
{{< app/cells/assistant language="csharp" >}}
