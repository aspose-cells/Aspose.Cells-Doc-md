---
title: حدد كيفية عبور السلسلة في ملف PDF والصورة
type: docs
weight: 120
url: /ar/net/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **سيناريوهات الاستخدام الممكنة**

عندما تحتوي الخلية على نص أو سلسلة ولكنها أكبر من عرض الخلية ، فإن السلسلة تتجاوز إذا كانت الخلية التالية في العمود التالي فارغة أو فارغة. عند حفظ ملف Excel في ملف PDF / صورة ، يمكنك التحكم في هذا الفائض عن طريق تحديد النوع المتقاطع باستخدام امتداد[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype)تعداد. لديها القيم التالية

- **TextCrossType افتراضي**: عرض نص مثل MS Excel الذي يعتمد على الخلية التالية. إذا كانت الخلية التالية خالية ، فستتقاطع السلسلة أو سيتم اقتطاعها.

- **TextCrossType.CrossKeep**: اعرض السلسلة مثل MS Excel لتصدير PDF / صورة

- **TextCrossType.CrossOverride**: اعرض كل النص بعبور الخلايا الأخرى وتجاوز نص الخلايا المتقاطعة

- **TextCrossType.StrictInCell**: اعرض السلسلة فقط في عرض الخلية.

## **حدد كيفية عبور السلسلة في ملف PDF / صورة باستخدام TextCrossType**

يقوم نموذج التعليمات البرمجية التالي بتحميل نموذج ملف Excel وحفظه في تنسيق PDF / صورة بتحديد مختلف[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype)يمكن تنزيل نموذج ملف Excel وملفات الإخراج من الروابط التالية:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### عينة من الرموز

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderUsingTextCrossType-1.cs" >}}
