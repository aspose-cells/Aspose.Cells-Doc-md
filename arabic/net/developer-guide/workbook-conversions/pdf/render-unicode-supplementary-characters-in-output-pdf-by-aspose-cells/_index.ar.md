---
title: تقديم أحرف تكميلية Unicode في الإخراج PDF بواسطة Aspose.Cells
type: docs
weight: 350
url: /ar/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---
{{% alert color="primary" %}}

يبلغ طول أحرف Unicode العادية 2 بايت بينما يبلغ طول أحرف Unicode الإضافية 4 بايت. يدعم Aspose.Cells الآن تحويل أحرف Unicode هذه ذات 4 بايت.

في معيار أحرف Unicode ، الأحرف التكميلية هي الأحرف المعينة لنقاط الرمز من U + 10000 إلى U + 10FFFF. بمعنى آخر ، هذه هي أحرف Unicode الأكبر من U + FFFF.

- في UTF-8 ، يبلغ طول هذه الأحرف 4 بايت.
- في UTF-16 ، تتطلب هذه الأحرف بديلين (وحدات 16 بت).

{{% /alert %}}

## تقديم أحرف تكميلية Unicode في الإخراج PDF بواسطة Aspose.Cells

 توضح لقطة الشاشة التالية كيف قدم Aspose.Cells ملف[ملف اكسل المصدر](5115563.xlsx) داخل ال[الإخراج PDF](5115564.pdf). كما ترى ، تم تقديم جميع أحرف Unicode التكميلية الثلاثة تمامًا كما فعلت بواسطة Microsoft Excel.

![ما يجب القيام به: image_بديل_نص](output.png)

## عينة من الرموز

 يمكنك استخدام نموذج التعليمات البرمجية هذا للتحويل[ملف اكسل المصدر](5115563.xlsx) داخل[الإخراج PDF](5115564.pdf).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderUnicodeInOutput-RenderUnicodeInOutput.cs" >}}
