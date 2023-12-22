---
title: حدد كيفية عبور السلسلة في الإخراج PDF والصورة
type: docs
weight: 120
url: /ar/python-net/specify-how-to-cross-string-in-output-pdf-and-image/
description: تعلم كيفية عبور السلسلة في الإخراج PDF والصورة مع Aspose.Cells for Python via .NET API.
keywords: Python Cross String in output PDF and image
---
##  **سيناريوهات الاستخدام المحتملة**

عندما تحتوي خلية على نص أو سلسلة ولكنها أكبر من عرض الخلية، فإن السلسلة تفيض إذا كانت الخلية التالية في العمود التالي فارغة أو فارغة. عندما تقوم بحفظ ملف Excel الخاص بك في PDF/Image، يمكنك التحكم في هذا التجاوز عن طريق تحديد النوع المتقاطع باستخدام[**نوع النص المتقاطع**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)تعداد. لديها القيم التالية

- *TextCrossType.DEFAULT**: عرض نص مثل MS Excel والذي يعتمد على الخلية التالية. إذا كانت الخلية التالية فارغة، فسيتم تقاطع السلسلة أو سيتم اقتطاعها.

- *TextCrossType.CROSS_KEEP**: عرض السلسلة مثل تصدير MS Excel PDF/Image

- *TextCrossType.CROSS_OVERRIDE**: عرض النص بالكامل عن طريق عبور الخلايا الأخرى وتجاوز نص الخلايا المتقاطعة

- *TextCrossType.STRICT_IN_CELL**: عرض السلسلة فقط ضمن عرض الخلية.

##  **حدد كيفية عبور السلسلة في الإخراج PDF/الصورة باستخدام TextCrossType**

يقوم نموذج التعليمات البرمجية التالي بتحميل ملف Excel النموذجي وحفظه بتنسيق PDF/Image عن طريق تحديد مختلف[**نوع النص المتقاطع**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)يمكن تنزيل نموذج ملف Excel وملفات الإخراج من الروابط التالية:

[SampleCrossType.xlsx](81920905.xlsx)

[OutputCrossType.pdf](81920903.pdf)

[OutputCrossType.png](81920904.png)

###  عينة من الرموز

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUsingTextCrossType-1.py" >}}
