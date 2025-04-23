---
title: تحديد كيفية عبور السلسلة في ملف PDF الناتج والصورة
type: docs
weight: 120
url: /ar/net/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **سيناريوهات الاستخدام المحتملة**

عندما تحتوي خلية على نص أو سلسلة نصية ولكنها أكبر من عرض الخلية، فإن السلسلة ستتجاوز إذا كانت الخلية التالية في العمود التالي فارغة أو تكون سلسلة فارغة. عند حفظ ملف Excel الخاص بك إلى PDF/صورة، يمكنك التحكم في هذا التجاوز عن طريق تحديد نوع التقاطع باستخدام تعداد [**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype). يحتوي على القيم التالية

- **TextCrossType.Default**: عرض النص مثل MS Excel والذي يعتمد على الخلية التالية. إذا كانت الخلية التالية فارغة، سيتم عبور السلسلة أو سيتم قصها.

- **TextCrossType.CrossKeep**: عرض السلسلة مثل MS Excel عند تصديرها إلى PDF/صورة

- **TextCrossType.CrossOverride**: عرض كل النص بعبور الخلايا الأخرى وتجاوز النص المتجاوز

- **TextCrossType.StrictInCell**: عرض السلسلة فقط ضمن عرض الخلية.

## **تحديد كيفية عبور السلسلة في ملف PDF/صورة الناتج باستخدام TextCrossType**

يحمل الكود النموذجي التالي ملف Excel النموذجي ويحفظه بتنسيق PDF/صورة عن طريق تحديد [**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype) مختلفة. يمكن تنزيل ملف Excel النموذجي والملفات الناتجة من الروابط التالية:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### مثال على الكود

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderUsingTextCrossType-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
