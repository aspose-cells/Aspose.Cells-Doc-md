---
title: عرض أحرف Unicode التكميلية في الإخراج PDF بواسطة Aspose.Cells for Python via .NET
type: docs
weight: 350
url: /ar/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: تعرف على كيفية عرض أحرف Unicode التكميلية أثناء تحويل Excel إلى PDF مع Aspose.Cells for Python via .NET API.
keywords: Python Render Unicode Supplementary characters while saving file to PDF, Print Unicode Supplementary characters while saving Excel to PDF using Python, Python Show Unicode Supplementary characters when converting Excel to PDF, Output Unicode Supplementary characters for excel to pdf
---
{{% alert color="primary" %}}

يبلغ طول أحرف Unicode العادية 2 بايت بينما يبلغ طول أحرف Unicode التكميلية 4 بايت. Aspose.Cells for Python via .NET يدعم الآن عرض أحرف Unicode ذات 4 بايت.

في Unicode Character Standard، الأحرف التكميلية هي الأحرف المخصصة لنقاط التعليمات البرمجية من U+10000 إلى U+10FFFF. بمعنى آخر، هذه هي أحرف Unicode الأكبر من U+FFFF.

- في UTF-8 يبلغ طول هذه الأحرف 4 بايت.
- في UTF-16، تتطلب هذه الأحرف بديلين (وحدات 16 بت).

{{% /alert %}}

##  عرض أحرف Unicode التكميلية في الإخراج PDF بواسطة Aspose.Cells for Python via .NET

 توضح لقطة الشاشة التالية كيف تم عرض Aspose.Cells for Python via .NET[ملف اكسيل المصدر](5115563.xlsx) داخل ال[الإخراج PDF](5115564.pdf). كما ترون، تم عرض جميع أحرف Unicode التكميلية الثلاثة تمامًا كما حدث بواسطة Microsoft Excel.

![ما يجب القيام به:image_alt_text](output.png)

##  عينة من الرموز

يمكنك استخدام نموذج التعليمات البرمجية هذا للتحويل[ملف اكسيل المصدر](5115563.xlsx) داخل[الإخراج PDF](5115564.pdf).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUnicodeInOutput.py" >}}
