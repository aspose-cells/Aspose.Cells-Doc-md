---
title: حدد كيفية عبور السلسلة في الإخراج PDF والصورة
type: docs
weight: 20
url: /ar/python-java/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **حدد كيفية عبور السلسلة في الإخراج PDF والصورة**
 عندما تحتوي الخلية على نص أو سلسلة أكبر من عرض الخلية ، فإن السلسلة تتجاوز إذا كانت الخلية التالية في العمود التالي فارغة أو فارغة. عند حفظ ملف Excel في PDF / صورة ، يمكنك التحكم في هذا الفائض عن طريق تحديد النوع المتقاطع باستخدام[TextCrossType](https://reference.aspose.com/cells/python/asposecells.api/TextCrossType) تعداد. لديها القيم التالية

- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT): العرض مثل MS Excel ، يعتمد على الخلية التالية. إذا كانت الخلية التالية خالية ، فستتقاطع السلسلة أو سيتم اقتطاعها.
- [TextCrossType. CROSS_KEEP](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP): اعرض السلسلة المشابهة لـ MS Excel تصدير PDF / صورة
- [TextCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE)اعرض كل النص بعبور الخلايا الأخرى وتجاوز نص الخلايا المتقاطعة
- [TextCrossType.STRICT_في_زنزانة](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL): عرض السلسلة فقط في عرض الخلية.

يقوم نموذج التعليمات البرمجية التالي بتحميل نموذج ملف Excel وحفظه بتنسيق PDF / Image عن طريق تحديد TextCrossType مختلف. يمكن تنزيل نموذج ملف Excel وملفات الإخراج من الروابط التالية:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)
## **عينة من الرموز**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}
