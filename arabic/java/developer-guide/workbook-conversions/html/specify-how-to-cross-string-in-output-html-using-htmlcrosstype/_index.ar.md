---
title: حدد كيفية عبور السلسلة في إخراج HTML باستخدام HtmlCrossType
type: docs
weight: 140
url: /ar/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---
## **سيناريوهات الاستخدام الممكنة**

عندما تحتوي الخلية على نص أو سلسلة ولكنها أكبر من عرض الخلية ، فإن السلسلة تتجاوز إذا كانت الخلية التالية في العمود التالي فارغة أو فارغة. عند حفظ ملف Excel في HTML ، يمكنك التحكم في هذا الفائض عن طريق تحديد النوع المتقاطع باستخدام امتداد[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)تعداد. لديها القيم التالية

- [**HtmlCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT): عرض مثل MS Excel الذي يعتمد على الخلية التالية. إذا كانت الخلية التالية خالية ، فستتقاطع السلسلة أو سيتم اقتطاعها.

- [**HtmlCrossType.MS_EXPORT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#MS_EXPORT): اعرض السلسلة مثل تصدير MS Excel بتنسيق HTML.

- [**HtmlCrossType.CROSS**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS) : عرض سلسلة HTML المتقاطعة ، سيكون أداء إنشاء ملفات HTML كبيرة أسرع بعشر مرات من تعيين القيمة إلى[**إفتراضي**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT) أو[**FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL).

- [**HtmlCrossType.CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT): عرض سلسلة HTML المتقاطعة وإخفاء السلسلة الصحيحة عند تداخل النصوص.

- [**HtmlCrossType.FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL): عرض السلسلة فقط في عرض الخلية.

## **حدد كيفية عبور السلسلة في إخراج HTML باستخدام HtmlCrossType**

يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](51740747.xlsx)ويحفظه في تنسيق HTML بتحديد مختلف[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)يرجى تنزيل ملف[إخراج HTML](51740745.zip) الملفات التي تم إنشاؤها باستخدام هذا الرمز. يحتوي ملف Excel النموذجي على صورة ذات لون أحمر كما هو موضح في لقطة الشاشة هذه التي توضح تأثير ملف[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)القيم على الناتج HTML.

![ما يجب القيام به: image_بديل_نص](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}
