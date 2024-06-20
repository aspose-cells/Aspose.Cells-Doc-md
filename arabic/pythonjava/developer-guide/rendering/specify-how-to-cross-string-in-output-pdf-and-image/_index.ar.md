---
title: تحديد كيفية عبور السلسلة في ملف PDF الناتج والصورة
type: docs
weight: 20
url: /ar/python-java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **تحديد كيفية عبور السلسلة في ملف PDF والصورة**
عندما يحتوي الخلية على نص أو سلسلة نصية أكبر من عرض الخلية، يتجاوز النص إذا كانت الخلية التالية في العمود التالي فارغة أو فارغة. عند حفظ ملف Excel الخاص بك في PDF/صورة، يمكنك التحكم في هذا التجاوز عن طريق تحديد نوع التقاطع باستخدام تعداد [TextCrossType](https://reference.aspose.com/cells/python/asposecells.api/TextCrossType). يحتوي على القيم التالية

- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT): عرض مثل MS Excel، يعتمد على الخلية التالية. إذا كانت الخلية التالية فارغة، سيتجاوز النص أو سيتم اقتطاعه.
- [TextCrossType. CROSS_KEEP](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP) : عرض النص بشكل مماثل لتصدير MS Excel إلى PDF/صورة
- [TextCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE) : عرض كل النص بتجاوز الخلايا الأخرى وتجاوز نص الخلايا المتجاوزة
- [TextCrossType.STRICT_IN_CELL](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL) : عرض النص فقط داخل عرض الخلية.

الكود العيني التالي يقوم بتحميل ملف Excel عيني ويحفظه بتنسيق PDF/صورة عن طريق تحديد أنواع مختلفة من TextCrossType. يمكن تنزيل ملف Excel العيني وملفات الإخراج من الروابط التالية:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)
## **الكود المثالي**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}
