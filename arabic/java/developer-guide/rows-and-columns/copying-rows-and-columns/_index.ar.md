---
title: نسخ الصفوف والأعمدة
type: docs
weight: 30
url: /ar/java/copying-rows-and-columns/
---

## **مقدمة**
في بعض الأحيان, قد تحتاج إلى نسخ الصفوف والأعمدة في ورقة العمل دون نسخ الورقة بأكملها. مع Aspose.Cells, من الممكن نسخ الصفوف والأعمدة داخل المصنف أو بين المصنفات.

عند نسخ صف (أو عمود), يتم نسخ البيانات الموجودة فيه, بما في ذلك الصيغ - بالمراجع المحدثة - والقيم, التعليقات, التنسيق, الخلايا المخفية, الصور, وغيرها من الكائنات التوضيحية.
## **نسخ الصفوف والأعمدة باستخدام Microsoft Excel**
1. حدد الصف أو العمود الذي ترغب في نسخه.
1. لنسخ الصفوف أو الأعمدة, انقر **نسخ** على شريط الأدوات **قياسي**, أو اضغط **CTRL**+**C**.
1. حدد صفًا أو عمودًا أسفل أو إلى اليمين من المكان الذي تريد نسخ تحديدك.
1. عند نسخ الصفوف أو الأعمدة, انقر **الخلايا المنسوخة** على قائمة **إدراج**.

{{% alert color="primary" %}} 

إذا قمت بالنقر على **لصق** على شريط الأدوات **قياسي** أو ضغط **CTRL**+**V** بدلاً من النقر على أمر في قائمة **إدراج**, فإن أي محتويات خلايا الوجهة يتم استبدالها.

{{% /alert %}} 

## **نسخ صف واحد**

توفر Aspose.Cells طريقة [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) في فئة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). تقوم هذه الطريقة بنسخ جميع أنواع البيانات بما في ذلك الصيغ, القيم, التعليقات, تنسيق الخلية, الخلايا المخفية, الصور, وكائنات الرسم الأخرى من الصف المصدر إلى الصف الوجهة.

يأخذ الطريقة [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) المعلمات التالية:

- كائن الخلايا [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) المصدر،
- فهرس الصف المصدر، و
- فهرس الصف الوجهة.

استخدم هذه الطريقة لنسخ صف داخل ورقة، أو لورقة أخرى. طريقة [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) تعمل بشكل مماثل لبرنامج Microsoft Excel. لذا، على سبيل المثال، لا تحتاج إلى تعيين ارتفاع الصف الوجهة بشكل صريح، تلك القيمة يتم نسخها أيضاً.

المثال التالي يوضح كيفية نسخ صف في ورقة العمل. يستخدم قالب ملف Microsoft Excel وينسخ الصف الثاني (مع البيانات والتنسيق والتعليقات والصور وما إلى ذلك) وينسخه إلى الصف الثاني عشر في نفس ورقة العمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingRows-CopyingRows.java" >}}



الناتج التالي يتم توليده عند تنفيذ الكود أدناه.

**يتم نسخ الصف بأعلى درجات الدقة والدقة** 

![todo:image_alt_text](copying-rows-and-columns_1.png)

{{% alert color="primary" %}} 

عند نسخ الصفوف، من المهم ملاحظة الصور المتصلة، الرسوم البيانية أو العناصر الرسومية الأخرى لأن هذا هو نفس الأمر مع برنامج Microsoft Excel:

1. إذا كان مؤشر الصف الأصلي هو 5، فإن الصورة، الرسم البياني، إلخ، تُنسخ إذا كانت موجودة في الثلاثة صفوف (مؤشر الصف البداية هو 4 ومؤشر الصف النهاية هو 6).
1. لن يتم إزالة الصور الموجودة، الرسوم البيانية، إلخ في الصف الوجهة.

{{% /alert %}} 

## **نسخ الصفوف المتعددة**

يمكنك أيضًا نسخ عدة صفوف على وجهة جديدة باستخدام الطريقة [**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int)) التي تأخذ معلمة إضافية من النوع الصحيح لتحديد عدد الصفوف المصدرية التي يجب نسخها.

أدناه هو لقطة شاشة لجدول البيانات الإدخالية الذي يحتوي على 3 صفوف من البيانات في حين يقوم مقتطف الكود الموفر أدناه بنسخ كل الصفوف الثلاثة إلى موقع جديد يبدأ من الصف السابع.

![todo:image_alt_text](copy-rows-and-columns_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleRows-CopyingMultipleRows.java" >}}

إليك العرض الناتج للجدول الإدخالي بعد تنفيذ مقتطف الكود أعلاه.

![todo:image_alt_text](copy-rows-and-columns_4.png)

## **نسخ العمود الفردي**

توفر Aspose.Cells طريقة [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) لكائن [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) هذه الطريقة تقوم بنسخ جميع أنواع البيانات، بما في ذلك الصيغ - مع الإشارات المحدثة - والقيم، التعليقات، تنسيقات الخلية، الخلايا المخفية، الصور وغيرها من الكائنات الرسومية من العمود المصدر إلى العمود الوجهة.

تأخذ الطريقة [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) المعلمات التالية:

- كائن الخلايا [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) المصدر،
- فهرس العمود المصدر، و
- فهرس العمود الوجهة.

استخدم الطريقة [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) لنسخ عمود داخل ورقة عمل أو إلى ورقة عمل أخرى.

هذا المثال ينسخ عمودًا من ورقة العمل ويلصقه في ورقة عمل في دفتر عمل آخر.

**تم نسخ عمود من مصفوفة العمل الواحدة إلى أخرى** 

![todo:image_alt_text](copying-rows-and-columns_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingColumns-CopyingColumns.java" >}}

## **نسخ الأعمدة المتعددة**

على غرار الطريقة [**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int))، توفر واجهات برمجة التطبيقات لـ Aspose.Cells أيضًا الطريقة [**Cells.copyColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns(com.aspose.cells.Cells,%20int,%20int,%20int)) لنسخ عدة أعمدة مصدر إلى موقع جديد.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleColumns-CopyingMultipleColumns.java" >}}

إليك كيف تبدو جداول البيانات المصدر والنتيجة في برنامج Excel.

![todo:image_alt_text](copy-rows-and-columns_7.png)

![todo:image_alt_text](copy-rows-and-columns_8.png)


## **لصق الصفوف/الأعمدة بخيارات اللصق**
توفر Aspose.Cells الآن [PasteOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PasteOptions) أثناء استخدام الوظائف [CopyRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRows\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.CopyOptions,%20com.aspose.cells.PasteOptions\)) و [CopyColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.PasteOptions\)). يسمح باختيار خيارات اللصق المناسبة بشكل مماثل لبرنامج Excel.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-PastingDataWithPasteOptions.java" >}}

