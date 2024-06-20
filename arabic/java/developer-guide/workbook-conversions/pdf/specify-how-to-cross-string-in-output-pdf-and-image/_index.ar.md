---
title: تحديد كيفية عبور السلسلة في ملف PDF الناتج والصورة
type: docs
weight: 110
url: /ar/java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **سيناريوهات الاستخدام المحتملة**

عندما يحتوي الخلية على نص أو سلسلة نصية ولكنها أكبر من عرض الخلية، فإن السلسلة تتجاوز إذا كانت الخلية التالية في العمود التالي فارغة أو تحتوي على قيمة فارغة. عندما تقوم بحفظ ملف Excel الخاص بك إلى ملف PDF/صورة، يمكنك التحكم في هذا التجاوز عن طريق تحديد نوع التقاطع باستخدام تعداد [**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType). لديه القيم التالية

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT): يعرض مثل MS Excel، يعتمد على الخلية التالية. إذا كانت الخلية التالية فارغة، سيتم تجاوز السلسلة أو سيتم قصها.

- [**TextCrossType. CROSS_KEEP**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_KEEP): يعرض السلسلة مثل تصدير MS Excel إلى PDF/صورة

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_OVERRIDE): يعرض كل النص بتجاوز الخلايا الأخرى ويستبدل نص الخلايا المتجاوزة

- [**TextCrossType.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT_IN_CELL): يعرض فقط السلسلة ضمن عرض الخلية.

## **تحديد كيفية عبور السلسلة في ملف PDF/صورة الناتج باستخدام TextCrossType**

يحمل الكود النموذجي التالي ملف Excel النموذجي ويحفظه بتنسيق PDF/صورة عن طريق تحديد [**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType) مختلفة. يمكن تنزيل ملف Excel النموذجي والملفات الناتجة من الروابط التالية:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}
