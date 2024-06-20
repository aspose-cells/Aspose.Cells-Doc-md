---
title: تقديم الحروف الأعلى من يونيكود في ملف PDF الناتج باستخدام Aspose.Cells
type: docs
weight: 350
url: /ar/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---

{{% alert color="primary" %}}

الحروف اليونيكود العادية طول كل منها 2 بايت بينما الحروف اليونيكود الأعلى طول كل منها 4 بايت. Aspose.Cells الآن يدعم تقديم هذه الحروف اليونيكود الأعلى بطول 4 بايت.

في معيار الحروف اليونيكود، الحروف الأعلى هي الحروف التي تم تخصيص نقاط الرموز لها من U+10000 إلى U+10FFFF. وبمعنى آخر، هذه هي الحروف اليونيكود التي تكون أكبر من U+FFFF.

- في UTF-8 طول كل من هذه الحروف هو 4 بايت.
- في UTF-16، هذه الحروف تتطلب 2 حروف دعائية (وحدات بت بطول 16).

{{% /alert %}}

## تقديم الحروف الأعلى من يونيكود في ملف PDF الناتج باستخدام Aspose.Cells

تظهر اللقطة الشاشة التالية كيف قدمت Aspose.Cells [ملف Excel المصدر](5115563.xlsx) إلى [PDF الناتج](5115564.pdf). كما يمكنك رؤية تم تقديم كل الحروف اليونيكود الأعلى الثلاثة بالضبط كما فعله Microsoft Excel.

![todo:image_alt_text](output.png)

## كود عينة

يمكنك استخدام هذا الكود العيني لتحويل [ملف Excel المصدر](5115563.xlsx) إلى [PDF الناتج](5115564.pdf).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderUnicodeInOutput-RenderUnicodeInOutput.cs" >}}
