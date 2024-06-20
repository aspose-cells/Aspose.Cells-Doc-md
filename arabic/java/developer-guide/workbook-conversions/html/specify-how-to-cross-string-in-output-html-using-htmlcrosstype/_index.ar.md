---
title: تحديد كيفية عبور النص في ملف الـHTML الناتج باستخدام HtmlCrossType
type: docs
weight: 140
url: /ar/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **سيناريوهات الاستخدام المحتملة**

عندما يحتوي الخلية على نص أو سلسلة ولكنه أكبر من عرض الخلية، فيمكن أن يحدث تجاوز السلسلة إذا كانت الخلية التالية في العمود التالي فارغة أو فارغة. عند حفظ ملف Excel الخاص بك في صيغة HTML، يمكنك التحكم في هذا التجاوز من خلال تحديد نوع التقاطع باستخدام تعداد [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType). لديه القيم التالية

- [**HtmlCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT): العرض مثل MS Excel الذي يعتمد على الخلية التالية. إذا كانت الخلية التالية فارغة، سيتم تقاطع السلسلة أو سيتم قصها.

- [**HtmlCrossType.MS_EXPORT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#MS_EXPORT): عرض السلسلة مثل تصدير MS Excel للصفحة HTML.

- [**HtmlCrossType.CROSS**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS): عرض تقاطع السلسلة الخاص بـ HTML، وستكون الأداء في إنشاء ملفات HTML الكبيرة أكثر من عشر مرات أسرع من تعيين القيمة إلى [**DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT) أو [**FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL).

- [**HtmlCrossType.CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT): عرض تقاطع السلسلة الخاص بـ HTML وإخفاء السلسلة اليمنى عند تداخل النصوص.

- [**HtmlCrossType.FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL): إظهار السلسلة فقط ضمن عرض الخلية.

## **تحديد كيفية تقاطع السلسلة في HTML الناتج باستخدام HtmlCrossType**

الكود النموذجي التالي يحمل [ملف Excel عيّنة](51740747.xlsx) ويحفظه بتنسيق HTML بتحديد [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType) مختلفة. يرجى تنزيل [ملف HTML الناتج](51740745.zip) الذي تم إنشاؤه بواسطة هذا الكود. يحتوي ملف Excel العينة على الصورة المحاطة بلون أحمر كما هو موضح في هذه اللقطة الشاشية التي تظهر تأثير القيم [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType) على ملف الـ HTML الناتج.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}
