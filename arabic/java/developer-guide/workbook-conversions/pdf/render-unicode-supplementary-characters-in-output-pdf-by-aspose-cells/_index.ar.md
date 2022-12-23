---
title: تقديم أحرف تكميلية Unicode في الإخراج PDF بواسطة Aspose.Cells
type: docs
weight: 690
url: /ar/java/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---
{{% alert color="primary" %}} 

يبلغ طول أحرف Unicode العادية 2 بايت بينما يبلغ طول أحرف Unicode الإضافية 4 بايت. يدعم Aspose.Cells الآن تحويل أحرف Unicode هذه ذات 4 بايت.

في معيار أحرف Unicode ، الأحرف التكميلية هي الأحرف المعينة لنقاط الرمز من U + 10000 إلى U + 10FFFF. بمعنى آخر ، هذه هي أحرف Unicode الأكبر من U + FFFF.

- في UTF-8 ، يبلغ طول هذه الأحرف 4 بايت.
- في UTF-16 ، تتطلب هذه الأحرف بديلين (وحدات 16 بت).

{{% /alert %}} 
## **تقديم أحرف تكميلية Unicode في الإخراج PDF بواسطة Aspose.Cells**
 توضح لقطة الشاشة التالية كيف قدم Aspose.Cells ملف[ملف اكسل المصدر](5473390.xlsx) داخل ال[الإخراج PDF](5473391.pdf). كما ترى ، تم تقديم جميع أحرف Unicode التكميلية الثلاثة تمامًا كما فعلت بواسطة Microsoft Excel.

![ما يجب القيام به: image_بديل_نص](render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells_1.png)

يمكنك استخدام نموذج التعليمات البرمجية هذا لتحويل ملف[ملف اكسل المصدر](5473390.xlsx) داخل[الإخراج PDF](5473391.pdf).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-RenderUnicodeSupplimentaryCharacterToPDF-1.java" >}}
