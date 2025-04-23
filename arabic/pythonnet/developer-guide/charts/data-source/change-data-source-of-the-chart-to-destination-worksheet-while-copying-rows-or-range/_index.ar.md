---
title: تغيير مصدر البيانات للرسم البياني إلى ورقة العمل الوجهة أثناء نسخ الصفوف أو النطاق
description: تعلم كيفية تغيير مصدر البيانات لرسم بياني إلى ورقة العمل الوجهة أثناء نسخ الصفوف أو مدى محدد في Aspose.Cells لبايثون via .NET. سيرينا دليلنا كيفية تحديث مدى بيانات الرسم البياني وربطه بورقة العمل الهدف، لضمان عكس الصفوف أو النطاق المنسوخ بشكل دقيق في الرسم البياني.
keywords: Aspose.Cells لبايثون via .NET، التصوير البياني، مصدر البيانات، ورقة العمل الوجهة، الصفوف، النطاق، النسخ، التحديث، مدى البيانات، الترابط.
type: docs
weight: 440
url: /ar/python-net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **سيناريوهات الاستخدام المحتملة**

عند نسخ الصفوف أو النطاق الذي يحتوي على رسوم بيانية إلى ورقة عمل جديدة، فإن مصدر البيانات للرسم البياني لا يتغير. على سبيل المثال، إذا كان مصدر بيانات الرسم البياني يُساوي =Sheet1!$A$1:$B$4، فبعد نسخ الصفوف أو النطاق إلى ورقة العمل الجديدة، سيظل مصدر البيانات هو نفسه أي أنه =Sheet1!$A$1:$B$4. ولا يزال يُشير إلى ورقة العمل القديمة أي Sheet1. وهذا هو أيضًا السلوك في Microsoft Excel. ولكن إذا كنت ترغب في أن يشير إلى ورقة العمل الوجهة الجديدة، فيرجى استخدام خاصية [**CopyOptions.refer_to_destination_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/copyoptions/refer_to_destination_sheet) وتعيينها إلى **صحيح** أثناء استدعاء الطريقة [**Cells.copy_rows()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows). الآن إذا كانت ورقة العمل الوجهة هي DestSheet، فإن مصدر بيانات الرسم البياني الخاص بك سيتغير من =Sheet1!$A$1:$B$4 إلى =DestSheet!$A$1:$B$4.

## **تغيير مصدر البيانات للرسم البياني إلى ورقة العمل الوجهة أثناء نسخ الصفوف أو النطاق**

يشرح الكود النموذجي التالي استخدام الخاصية [**CopyOptions.refer_to_destination_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/copyoptions/refer_to_destination_sheet) أثناء نسخ الصفوف أو النطاق الذي يحتوي على رسوم بيانية إلى ورقة عمل جديدة. يستخدم الكود ملف الإكسل النموذجي]5113699.xlsx] ويولد ملف الإكسل الناتج]5113697.xlsx[.

![todo:image_alt_text](1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChangeChartDataSource-1.py" >}}
