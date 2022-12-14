---
title: حدد كيفية عبور السلسلة في إخراج HTML باستخدام HtmlCrossType
type: docs
weight: 140
url: /ar/net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---
## **سيناريوهات الاستخدام الممكنة**

عندما تحتوي الخلية على نص أو سلسلة ولكنها أكبر من عرض الخلية ، فإن السلسلة تتجاوز إذا كانت الخلية التالية في العمود التالي فارغة أو فارغة. عند حفظ ملف Excel في HTML ، يمكنك التحكم في هذا الفائض عن طريق تحديد النوع المتقاطع باستخدام امتداد[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) تعداد. لديها القيم التالية

- **HtmlCrossType. الافتراضي**: العرض مثل MS Excel ، يعتمد على الخلية التالية. إذا كانت الخلية التالية خالية ، فستتقاطع السلسلة أو سيتم اقتطاعها.

- **HtmlCrossType.MSExport**: اعرض السلسلة مثل تصدير MS Excel بتنسيق HTML.

- **HtmlCrossType**: عرض سلسلة HTML المتقاطعة ، سيكون أداء إنشاء ملفات HTML كبيرة أكثر من عشر مرات أسرع من تعيين القيمة إلى افتراضي أو FitToCell.

- **HtmlCrossType.FitToCell**: عرض السلسلة فقط في عرض الخلية.

## **حدد كيفية عبور السلسلة في إخراج HTML باستخدام HtmlCrossType**

 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](51740732.xlsx) ويحفظه في تنسيق HTML بتحديد مختلف[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) . يرجى تنزيل ملف[إخراج HTMLs](51740734.zip) ولدت مع هذا الرمز. يحتوي ملف Excel النموذجي على صورة ذات لون أحمر كما هو موضح في لقطة الشاشة هذه التي توضح تأثير ملف[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) القيم على الناتج HTML.

![ما يجب القيام به: image_بديل_نص](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.cs" >}}
