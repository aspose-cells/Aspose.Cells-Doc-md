---
title: نسخة الشرارة عن طريق تحديد نطاق البيانات وموقع مجموعة الشرائط
type: docs
weight: 120
url: /ar/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

يسمح Microsoft Excel لك بنسخ مخطط الشريط عن طريق تحديد نطاق البيانات وموقع مجموعة مخطط الشريط. اتبع هذه الخطوات لنسخ مخطط الشريط إلى خلايا أخرى.

تسمح Microsoft Excel لك بنسخ سبارك لين عن طريق تحديد نطاق البيانات ومكان مجموعة السبارك لين. اتبع هذه الخطوات لنسخ سبارك لين إلى خلايا أخرى.

- حدد الخلية التي تحتوي على مخطط الشريط الخاص بك.
- حدد **تحرير البيانات** من قسم **مخطط الشريط** داخل علامة التبويب **التصميم**
- اختر **تحرير موقع المجموعة والبيانات...**
 - حدد نطاق البيانات والموقع وانقر فوق موافق.

## مثال

توفر Aspose.Cells الطريقة [**SparklineCollection.add(dataRange, row, column)**](https://reference.aspose.com/cells/java/com.aspose.cells/SparklineCollection) لتحديد نطاق البيانات والموقع لمجموعة Sparkline.

### لقطات من الملفات الأصلية والملفات الناتجة

تعرض اللقطة الشاشية التالية الملف Excel الأصلي المستخدم داخل الكود. يوضح المنطقة المحددة باللون الأحمر خيار "**تحرير موقع وبيانات المجموعة...**" لتحديد نطاق البيانات والموقع لمجموعة Sparkline. تعرض الخلية P4 السباركلاين الذي سيتم نسخه إلى الخلايا الأربعة التالية المملوءة باللون الأصفر باستخدام Aspose.Cells.

![todo:image_alt_text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_1.png)

تعرض اللقطة الشاشية التالية الملف Excel الناتج الذي تم إنشاؤه بواسطة الكود العينة. كما يمكنك رؤية، تم نسخ السباركلاين في الخلية P4 إلى الخلايا الأربعة التالية في العمود P كل منها بنطاق بيانات مختلف.

![todo:image_alt_text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_2.png)

### كود جافا لنسخ السباركلاين عن طريق تحديد نطاق البيانات والموقع لمجموعة سباركلاين

يحمل الكود العينة التالي ملف Excel الأصلي كما هو موضح في اللقطة الشاشية أعلاه، ثم يصل إلى أول مجموعة سباركلاين ويضيف نطاقات البيانات والمواقع داخل مجموعة السباركلاين. وأخيراً، يكتب ملف Excel الناتج على القرص كما هو موضح أيضا في اللقطة الشاشية أعلاه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopySparkline-CopySparkline.java" >}}
{{< app/cells/assistant language="java" >}}
