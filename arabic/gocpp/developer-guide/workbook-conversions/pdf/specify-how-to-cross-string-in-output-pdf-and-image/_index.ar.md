---
title: تحديد كيفية تخطي النص في ملف PDF والصور المخرجة مع Golang عبر C++
linktitle: تحديد كيفية عبور السلسلة في ملف PDF الناتج والصورة
type: docs
weight: 120
url: /ar/go-cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: تعلم كيفية التحكم في تجاوز النص في مخرجات PDF والصورة باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

عندما تحتوي الخلية على نص أو سلسلة أكبر من عرض الخلية، يتجاوز النص إذا كانت الخلية التالية في العمود التالي فارغة أو null. عند حفظ ملف Excel الخاص بك إلى PDF أو صورة، يمكنك التحكم في هذا التجاوز عن طريق تحديد نوع التقاطع باستخدام تعداد [**TextCrossType**](https://reference.aspose.com/cells/go-cpp/textcrosstype/). القيم التالية هي:

- **TextCrossType.Default**: عرض النص مثل MS Excel ويعتمد على الخلية التالية. إذا كانت الخلية التالية null، سيتجاوز النص أو سيتم اقتطاعه.

- **TextCrossType.CrossKeep**: عرض النص مثل تصدير MS Excel إلى PDF/صور.

- **TextCrossType.CrossOverride**: عرض كل النص عن طريق عبور خلايا أخرى وتجاوز نص الخلايا المعترضة.

- **TextCrossType.StrictInCell**: عرض السلسلة فقط ضمن عرض الخلية.

## **تحديد كيفية عبور السلسلة في ملف PDF/صورة الناتج باستخدام TextCrossType**

يعرض الرمز النموذجي التالي تحميل ملف Excel النموذجي وحفظه إلى تنسيق PDF/صور عن طريق تحديد قيم مختلفة [**TextCrossType**](https://reference.aspose.com/cells/go-cpp/textcrosstype/). يمكن تنزيل ملف Excel النموذجي والملفات الناتجة من الروابط التالية:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### مثال على الكود

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyHowToCrossStringInOutputPdfAndImage.go" >}}
