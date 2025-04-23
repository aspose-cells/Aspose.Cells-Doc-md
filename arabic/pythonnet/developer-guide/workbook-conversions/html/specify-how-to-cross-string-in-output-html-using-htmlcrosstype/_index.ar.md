---
title: تحديد كيفية عبور النص في ملف الـHTML الناتج باستخدام HtmlCrossType
type: docs
weight: 140
url: /ar/python-net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **سيناريوهات الاستخدام المحتملة**

عندما تحتوي الخلية على نص أو سلسلة نصية ولكنها أكبر من عرض الخلية، ثم يتجاوز النص إذا كانت الخلية التالية في العمود التالي فارغة. عندما تحفظ ملف الإكسل الخاص بك في ملف HTML، يمكنك التحكم في هذا التجاوز عن طريق تحديد نوع العبور باستخدام تصنيف الصنف [**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype). له القيم التالية

- **HtmlCrossType.DEFAULT**: العرض كما في MS Excel، يعتمد على الخلية التالية. إذا كانت الخلية التالية فارغة، سيكون النص متقاطعًا أو مقطوعًا.

- **HtmlCrossType.MS_EXPORT**: عرض النص كما في تصدير HTML من MS Excel.

- **HtmlCrossType.CROSS**: عرض النص المتقاطع بصيغة HTML، أداء إنشاء ملفات HTML كبيرة سيكون أكثر من عشرة أضعاف أسرع من ضبط القيمة على Default أو FitToCell.

- **HtmlCrossType.CROSS_HIDE_RIGHT**: عرض النص المتقاطع في HTML وإخفاء النص الأيمن عندما تتداخل النصوص.

- **HtmlCrossType.FIT_TO_CELL**: عرض النص فقط داخل عرض الخلية.

## **تحديد كيفية تقاطع السلسلة في HTML الناتج باستخدام HtmlCrossType**

الكود العيني التالي يقوم بتحميل [ملف الإكسل العيني](51740732.xlsx) ويقوم بحفظه في تنسيق الـHTML بتحديد مختلف لـ[**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype). يُرجى تحميل [ملفات الـHTML الناتجة](51740734.zip) التي تم إنشاءها بهذا الكود. يحتوي ملف الـإكسل العيني على الصورة المحاطة باللون الأحمر كما هو موضح في هذه اللقطة الشاشية التي تُظهر تأثير قيم [**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype) على ملف الـHTML الناتج.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SpecifyHtmlCrossTypeInOutputHTML.py" >}}
