---
title: تغيير توجيه الخلايا والاحتفاظ بالتنسيقات الحالية
description: استخدم مكتبة Aspose.Cells for Python via .NET لتغيير محاذاة الخلايا والحفاظ على التنسيق الحالي
keywords: Aspose.Cells for Python via .NET، محاذاة خلايا بايثون، الحفاظ على التنسيق الحالي
type: docs
weight: 340
url: /ar/python-net/change-cells-alignment-and-keep-existing-formatting/
---

## **سيناريوهات الاستخدام المحتملة**

 في بعض الأحيان، قد ترغب في تغيير محاذاة عدة خلايا ولكن مع الحفاظ على التنسيق الحالي. تتيح لك Aspose.Cells for Python via .NET القيام بذلك باستخدام الخاصية [**StyleFlag.alignments**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag/alignments). إذا قمت بتعيينها إلى **true**، فسيتم تطبيق تغييرات المحاذاة وإلا فلن يتم ذلك. يرجى ملاحظة أن كائن [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag) يُمرر كمعامل إلى طريقة [**Range.apply_style()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/apply_style) التي تطبق التنسيق فعلياً على نطاق من الخلايا.

## **تغيير توجيه الخلايا والاحتفاظ بالتنسيقات الحالية**

الكود النموذجي التالي يقوم بتحميل الملف الإكسل النموذجي، ينشئ المدى ويضبط توسيطه أفقيا وعموديا ويحتفظ بالتنسيق الحالي. الصورة النموذجية التالية تقارن ملف الإكسل النموذجي وملف الإكسل الناتج وتُظهر أن جميع التنسيقات الحالية للخلايا هي نفسها باستثناء أن الخلايا الآن موجهة في منتصف الخط أفقيًا وعموديًا.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ChangeCellsAlignmentAndKeepExistingFormatting.py" >}}

