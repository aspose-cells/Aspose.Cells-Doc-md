---
title: تغيير مصدر البيانات للرسم البياني إلى ورقة العمل الوجهة أثناء نسخ الصفوف أو النطاق
type: docs
weight: 850
url: /ar/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **سيناريوهات الاستخدام المحتملة**
عند نسخ الصفوف أو النطاق الذي يحتوي على رسوم بيانية إلى ورقة عمل جديدة، فإن مصدر بيانات الرسم البياني لا يتغير. على سبيل المثال، إذا كان مصدر بيانات الرسم البياني هو =Sheet1!$A$1:$B$4، فبعد نسخ الصفوف أو النطاق إلى ورقة عمل جديدة، سيظل مصدر البيانات هو نفسه أي =Sheet1!$A$1:$B$4. لا يزال يشير إلى ورقة العمل القديمة أي Sheet1. وهذا هو سلوك Microsoft Excel أيضًا. ولكن إذا كنت ترغب في أن يشير إلى ورقة العمل الوجهة الجديدة، فيرجى استخدام خاصية CopyOptions.ReferToDestinationSheet وتعيينها على القيمة صحيح أثناء استدعاء طريقة Cells.CopyRows(). الآن إذا كانت ورقة العمل الوجهة الخاصة بك هي DestSheet، فسيتغير مصدر البيانات لرسمك البياني من =Sheet1!$A$1:$B$4 إلى =DestSheet!$A$1:$B$4.
## **تغيير مصدر البيانات للرسم البياني إلى ورقة العمل الوجهة أثناء نسخ الصفوف أو النطاق**
الكود العيني التالي يشرح استخدام خاصية CopyOptions.ReferToDestinationSheet أثناء نسخ الصفوف أو النطاق الذي يحتوي على رسم بياني إلى ورقة عمل جديدة. يستخدم الكود [ملف الإكسل العيني](5472284.xlsx) ويولد [ملف الإكسل الناتج](5472283.xlsx). توضح اللقطة الشاشة أن مصدر البيانات للرسم البياني في [ملف الإكسل الناتج](5472283.xlsx) الآن يشير إلى DestSheet بدلاً من Sheet1.

![todo:image_alt_text](change-data-source-of-the-chart_1.png)







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeDataSource-ChangeDataSource.java" >}}






