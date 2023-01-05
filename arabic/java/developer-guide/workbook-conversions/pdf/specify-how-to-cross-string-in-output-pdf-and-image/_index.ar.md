---
title: حدد كيفية عبور السلسلة في الإخراج PDF والصورة
type: docs
weight: 110
url: /ar/java/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **سيناريوهات الاستخدام الممكنة**

عندما تحتوي الخلية على نص أو سلسلة ولكنها أكبر من عرض الخلية ، فإن السلسلة تتجاوز إذا كانت الخلية التالية في العمود التالي فارغة أو فارغة. عند حفظ ملف Excel في PDF / صورة ، يمكنك التحكم في هذا الفائض عن طريق تحديد النوع المتقاطع باستخدام[**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType)تعداد. لديها القيم التالية

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT): العرض مثل MS Excel ، يعتمد على الخلية التالية. إذا كانت الخلية التالية خالية ، فستتقاطع السلسلة أو سيتم اقتطاعها.

- [**TextCrossType. CROSS_KEEP**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_KEEP): اعرض السلسلة مثل تصدير MS Excel PDF / Image

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_OVERRIDE): اعرض كل النص بعبور الخلايا الأخرى وتجاوز نص الخلايا المتقاطعة

- [**TextCrossType.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT_IN_CELL): عرض السلسلة فقط في عرض الخلية.

## **حدد كيفية عبور السلسلة في الإخراج PDF / صورة باستخدام TextCrossType**

يقوم نموذج التعليمات البرمجية التالي بتحميل نموذج ملف Excel وحفظه بتنسيق PDF / صورة بتحديد مختلف[**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType). يمكن تنزيل نموذج ملف Excel وملفات الإخراج من الروابط التالية:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}
