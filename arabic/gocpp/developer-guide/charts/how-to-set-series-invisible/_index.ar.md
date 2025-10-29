---
title: كيفية جعل السلسلة غير مرئية مع Golang عبر C++
linktitle: كيفية إخفاء سلسلة
description: في مخطط Excel، قد تحتاج إلى جعل السلسلة غير مرئية. يصف هذا المقال كيفية استخدام Aspose.Cells مع Golang عبر C++ للقيام بذلك.
keywords: رسم بياني Excel، سلسلة، غير مرئية، مُفلترة.
type: docs
weight: 74
url: /ar/go-cpp/how-to-set-series-invisible/
---

## كيفية إخفاء سلسلة في مخطط إكسل

في مخطط إكسل، يمكنك النقر بزر الماوس الأيمن على مخطط، ثم اختيار "تحديد البيانات"، وفي النافذة المنبثقة، يمكنك تحديد ما إذا كانت السلسلة مرئية عبر الاختيار أو إلغاء الاختيار. يمكنك تحميل [ملف النموذج](SeriesFiltered.xlsx) التالي واستخدامه في إكسل لتحقيق هذه الوظيفة، وسنشرح لاحقًا كيفية تحقيق ذلك باستخدام مكتبة Aspose.Cells.

![todo:image_alt_text](series-invisible.png)

## كيفية إخفاء سلسلة باستخدام Aspose.Cells 

نستخدم الكود التالي لإخفاء سلسلة باستخدام Aspose.Cells:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetSeriesInvisible.go" >}}
يمكنك الحصول على الملف المدخل التالي [Input file](SeriesFiltered.xlsx) وملف الإخراج [output file](output.xlsx).

كما هو موضح في الشكل أدناه، السلسلتان الأوليان اللتان كانتا مرئيتين أصلاً، أصبحتا غير مرئيتين في ملف الإخراج.  
![todo:image_alt_text](output.png)
