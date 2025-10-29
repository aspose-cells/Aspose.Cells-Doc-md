---
title: حدد كيفية عبور النص في HTML الناتج باستخدام نوع عبور HTML مع Golang عبر C++
linktitle: تحديد HtmlCrossType في HTML الناتج
type: docs
weight: 140
url: /ar/go-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: تعلم كيفية التحكم في تجاوز النص في HTML باستخدام Aspose.Cells for C++ مع HtmlCrossType.
---

## **سيناريوهات الاستخدام المحتملة**

عند احتواء خلية على نص أو سلسلة أكبر من عرض الخلية، يتجاوز النص إذا كانت الخلية التالية في العمود التالي فارغة أو غير موجودة. عند حفظ ملف Excel الخاص بك إلى HTML، يمكنك التحكم في هذا التجاوز عن طريق تحديد نوع التقاطع باستخدام تعداد [**HtmlCrossType**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype/). يحتوي على القيم التالية:

- **HtmlCrossType.Default**: عرض مثل برنامج MS Excel، يعتمد على الخلية التالية. إذا كانت الخلية التالية فارغة، سيتجاوز النص أو سيتم قصه.

- **HtmlCrossType.MSExport**: عرض النص كما في تصدير HTML من برنامج MS Excel.

- **HtmlCrossType.Cross**: عرض النص المتقاطع في ملف الـHTML، سيكون الأداء لإنشاء ملفات HTML الكبيرة أكثر من عشر مرات أسرع من تعيين القيمة على الافتراضي أو FitToCell.

- **HtmlCrossType.FitToCell**: عرض النص فقط ضمن عرض الخلية.

## **تحديد كيفية تقاطع السلسلة في HTML الناتج باستخدام HtmlCrossType**

الشفرة النموذجية التالية تقوم بتحميل [ملف Excel النموذجي](51740732.xlsx) وتخزينه بتنسيق HTML عن طريق تحديد قيم [**HtmlCrossType**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype/) المختلفة. يرجى تنزيل [ملفات HTML الناتجة](51740734.zip) التي تم إنشاؤها باستخدام هذه الشفرة. يحتوي ملف Excel النموذجي على صورة محاطة باللون الأحمر كما هو موضح في لقطة الشاشة التي توضح تأثير قيم [**HtmlCrossType**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype/) على HTML الناتج.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyHowToCrossStringInOutputHtmlUsingHtmlcrosstype.go" >}}
