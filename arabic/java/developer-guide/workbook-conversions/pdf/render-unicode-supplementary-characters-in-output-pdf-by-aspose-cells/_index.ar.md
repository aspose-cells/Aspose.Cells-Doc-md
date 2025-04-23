---
title: تقديم الحروف الأعلى من يونيكود في ملف PDF الناتج باستخدام Aspose.Cells
type: docs
weight: 690
url: /ar/java/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---

{{% alert color="primary" %}} 

الحروف اليونيكود العادية طول كل منها 2 بايت بينما الحروف اليونيكود الأعلى طول كل منها 4 بايت. Aspose.Cells الآن يدعم تقديم هذه الحروف اليونيكود الأعلى بطول 4 بايت.

في معيار الحروف اليونيكود، الحروف الأعلى هي الحروف التي تم تخصيص نقاط الرموز لها من U+10000 إلى U+10FFFF. وبمعنى آخر، هذه هي الحروف اليونيكود التي تكون أكبر من U+FFFF.

- في UTF-8 طول كل من هذه الحروف هو 4 بايت.
- في UTF-16، هذه الحروف تتطلب 2 حروف دعائية (وحدات بت بطول 16).

{{% /alert %}} 
## **عرض الحروف اليونيكود الإضافية في ملف PDF الناتج باستخدام Aspose.Cells**
تُظهر اللقطة الشاشة التالية كيف قام Aspose.Cells بعرض [ملف الإكسل المصدر](5473390.xlsx) في [ملف PDF الناتج](5473391.pdf). كما ترون، تم عرض جميع الأحرف التكميلية اليونيكود بالشكل نفسه كما فعلت Microsoft Excel.

![todo:image_alt_text](render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells_1.png)

يمكنك استخدام كود النموذج التالي لتحويل [ملف الإكسل المصدر](5473390.xlsx) إلى [ملف PDF الناتج](5473391.pdf).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-RenderUnicodeSupplimentaryCharacterToPDF-1.java" >}}
{{< app/cells/assistant language="java" >}}
