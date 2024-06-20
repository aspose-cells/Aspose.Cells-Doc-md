---
title: تحديد كيفية عبور النص في ملف الـHTML الناتج باستخدام HtmlCrossType
type: docs
weight: 140
url: /ar/net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **سيناريوهات الاستخدام المحتملة**

عندما تحتوي الخلية على نص أو سلسلة نصية ولكنها أكبر من عرض الخلية، ثم يتجاوز النص إذا كانت الخلية التالية في العمود التالي فارغة. عندما تحفظ ملف الإكسل الخاص بك في ملف HTML، يمكنك التحكم في هذا التجاوز عن طريق تحديد نوع العبور باستخدام تصنيف الصنف [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype). له القيم التالية

- **HtmlCrossType.Default**: عرض مثل برنامج MS Excel، يعتمد على الخلية التالية. إذا كانت الخلية التالية فارغة، سيتجاوز النص أو سيتم قصه.

- **HtmlCrossType.MSExport**: عرض النص كما في تصدير HTML من برنامج MS Excel.

- **HtmlCrossType.Cross**: عرض النص المتقاطع في ملف الـHTML، سيكون الأداء لإنشاء ملفات HTML الكبيرة أكثر من عشر مرات أسرع من تعيين القيمة على الافتراضي أو FitToCell.

- **HtmlCrossType.FitToCell**: عرض النص فقط داخل عرض الخلية.

## **تحديد كيفية تقاطع السلسلة في HTML الناتج باستخدام HtmlCrossType**

الكود العيني التالي يقوم بتحميل [ملف الإكسل العيني](51740732.xlsx) ويقوم بحفظه في تنسيق الـHTML بتحديد مختلف لـ[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype). يُرجى تحميل [ملفات الـHTML الناتجة](51740734.zip) التي تم إنشاءها بهذا الكود. يحتوي ملف الـإكسل العيني على الصورة المحاطة باللون الأحمر كما هو موضح في هذه اللقطة الشاشية التي تُظهر تأثير قيم [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) على ملف الـHTML الناتج.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.cs" >}}
