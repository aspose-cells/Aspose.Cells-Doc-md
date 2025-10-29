---
title: تحديد كيفية عبور السلسلة في ملف PDF الناتج والصورة
type: docs
weight: 120
url: /ar/python-net/specify-how-to-cross-string-in-output-pdf-and-image/
description: تعلم كيفية عبور النص في ملف PDF وصورة الإخراج باستخدام واجهة برمجة التطبيقات Aspose.Cells for Python via .NET.
keywords: عبور النص بلغة Python في ملف PDF وصورة الإخراج
---

## **سيناريوهات الاستخدام المحتملة**

عندما تحتوي خلية على نص أو سلسلة نصية ولكنها أكبر من عرض الخلية، فإن السلسلة ستتجاوز إذا كانت الخلية التالية في العمود التالي فارغة أو تكون سلسلة فارغة. عند حفظ ملف Excel الخاص بك إلى PDF/صورة، يمكنك التحكم في هذا التجاوز عن طريق تحديد نوع التقاطع باستخدام تعداد [**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/). يحتوي على القيم التالية

- **TextCrossType.DEFAULT**: عرض النص مثل MS Excel والذي يعتمد على الخلية التالية. إذا كانت الخلية التالية فارغة، سيعبر النص أو سيتم قصه.

- **TextCrossType.CROSS_KEEP**: عرض النص مثل MS Excel عند تصديرها إلى صيغة PDF/صورة.

- **TextCrossType.CROSS_OVERRIDE**: عرض كامل النص عن طريق عبور الخلايا الأخرى وتجاوز النص المتقاطع للخلايا.

- **TextCrossType.STRICT_IN_CELL**: عرض النص فقط ضمن عرض الخلية.

## **تحديد كيفية عبور السلسلة في ملف PDF/صورة الناتج باستخدام TextCrossType**

يحمل الكود النموذجي التالي ملف Excel النموذجي ويحفظه بتنسيق PDF/صورة عن طريق تحديد [**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/) مختلفة. يمكن تنزيل ملف Excel النموذجي والملفات الناتجة من الروابط التالية:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### مثال على الكود

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUsingTextCrossType-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
