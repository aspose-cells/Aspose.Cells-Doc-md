---
title: انسخ Sparkline عن طريق تحديد نطاق البيانات وموقع مجموعة Sparkline
type: docs
weight: 120
url: /ar/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---
انسخ Sparkline عن طريق تحديد نطاق البيانات وموقع Sparkline Group في MS Excel

Microsoft يسمح لك Excel بنسخ Sparkline عن طريق تحديد نطاق البيانات والموقع لمجموعة Sparkline. اتبع هذه الخطوات لنسخ خط المؤشر الخاص بك إلى خلايا أخرى.

- حدد الخلية التي تحتوي على خط المؤشر الخاص بك.
-  يختار**تحرير البيانات** من**سباركلاين** قسم داخل**تصميم** التبويب
-  أختر**تحرير موقع المجموعة وبياناتها ...**
- حدد نطاق البيانات والموقع وانقر فوق موافق.

## مثال

 يوفر Aspose.Cells ملف[**SparklineCollection.add (نطاق البيانات ، الصف ، العمود)**](https://reference.aspose.com/cells/java/com.aspose.cells/SparklineCollection) طريقة لتحديد نطاق البيانات وموقع مجموعة Sparkline.

### لقطات من المصدر والملفات الناتجة

تُظهر لقطة الشاشة التالية ملف Excel المصدر المستخدم داخل الكود. تظهر المنطقة المظللة باللون الأحمر "**تحرير موقع المجموعة وبياناتها ...**"الخيار لتحديد نطاق البيانات وموقع مجموعة خط المؤشر. تُظهر الخلية P4 خط المؤشر الذي سيتم نسخه إلى الخلايا الأربع الأخرى المملوءة باللون الأصفر باستخدام Aspose.Cells.

![ما يجب القيام به: image_بديل_نص](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_1.png)

تُظهر لقطة الشاشة التالية ملف Excel الناتج الذي تم إنشاؤه بواسطة نموذج التعليمات البرمجية. كما ترى ، تم نسخ خط المؤشر في الخلية P4 إلى الخلايا الأربع التالية في العمود P لكل منها نطاق بيانات مختلف.

![ما يجب القيام به: image_بديل_نص](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_2.png)

### Java كود لنسخ خط المؤشر بتحديد نطاق البيانات وموقع مجموعة خط المؤشر

يقوم نموذج التعليمات البرمجية التالي بتحميل ملف Excel المصدر كما هو موضح في لقطة الشاشة أعلاه ، ثم يصل إلى أول مجموعة خط مؤشر ويضيف نطاقات البيانات والمواقع داخل مجموعة خط المؤشر. أخيرًا ، يكتب ملف Excel الناتج على القرص والذي يظهر أيضًا في لقطة الشاشة أعلاه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopySparkline-CopySparkline.java" >}}
