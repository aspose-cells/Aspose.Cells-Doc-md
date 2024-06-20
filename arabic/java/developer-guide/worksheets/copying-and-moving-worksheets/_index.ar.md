---
title: نسخ ونقل ورقات العمل
type: docs
weight: 20
url: /ar/java/copying-and-moving-worksheets/
---

{{% alert color="primary" %}}

في بعض الأحيان، تحتاج إلى عدد من ورقات العمل مع تنسيقات وبيانات مشتركة. على سبيل المثال، إذا كنت تعمل مع الميزانيات الفصلية، قد ترغب في إنشاء دفتر عمل يحتوي على أوراق تحتوي على نفس عناوين الأعمدة وعناوين الصفوف والصيغ. هناك طريقة لفعل ذلك: من خلال إنشاء ورقة واحدة ثم نسخها.

تدعم Aspose.Cells نسخ ونقل أوراق العمل داخلها أو بين دفاتر العمل. تتم نسخ الورقة بالكامل بما في ذلك البيانات والتنسيق والجداول والمصفوفات والرسوم البيانية والصور والكائنات الأخرى بأعلى درجة من الدقة.

{{% /alert %}}

## **نقل أو نسخ الأوراق باستخدام Microsoft Excel**

فيما يلي الخطوات المعنية بنسخ ونقل ورقات العمل داخل أو بين سجلات العمل.

1. لنقل أو نسخ الأوراق إلى دفتر العمل الآخر، افتح دفتر العمل الذي سيتلقى الأوراق.
1. انتقل إلى دفتر العمل الذي يحتوي على الأوراق التي ترغب في نقلها أو نسخها، ثم حدد الأوراق.
1. في قائمة **تحرير**، انقر فوق **نقل أو نسخ الصفحة**.
1. في مربع الكتابة To book، انقر فوق جدول البيانات لاستلام الصفحات.
1. لنقل أو نسخ الصفحات المحددة إلى جدول بيانات جديد، انقر فوق **كتاب جديد**.
1. في مربع **قبل الصفحة**، انقر فوق الصفحة التي ترغب في إدراج الصفحات المنقولة أو المنسوخة قبلها.
7. لنسخ الصفحات بدلاً من نقلها، حدد مربع الاختيار **إنشاء نسخة**.

## **نسخ أوراق العمل داخل دفتر عمل**

توفر Aspose.Cells طريقة متحملة، [**WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#addCopy(int))، يتم استخدامها لإضافة ورقة عمل إلى المجموعة ونسخ البيانات من ورقة عمل موجودة. إحدى الإصدارات من الطريقة تأخذ فهرس الورقة المصدر كمعلمة. الإصدار الآخر يأخذ اسم الورقة المصدر.

المثال التالي يظهر كيفية نسخ ورقة عمل موجودة داخل سجل العمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWithinWorkbook-CopyWithinWorkbook.java" >}}

## **نسخ أوراق العمل بين دفاتر العمل**

يوفر Aspose.Cells طريقة، [**Worksheet.copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet))، المستخدمة لنسخ البيانات والتنسيق من صفحة العمل الأصلية إلى صفحة عمل أخرى داخل أو بين دفاتر العمل. تأخذ الطريقة كائن صفحة العمل الأصلية كمعلمة.

يظهر المثال التالي كيفية نسخ ورقة عمل من دفتر عمل إلى دفتر عمل آخر.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetsBetweenWorkbooks-CopyWorksheetsBetweenWorkbooks.java" >}}

المثال التالي يوضح كيفية نسخ ورقة عمل من مصنف إلى مصنف آخر.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetFromWorkbookToOther-CopyWorksheetFromWorkbookToOther.java" >}}

## **نقل أوراق العمل داخل الدفتر**

توفر Aspose.Cells طريقة، [**Worksheet.moveTo()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#moveTo(int))، المستخدمة لنقل صفحة العمل إلى موقع آخر في نفس جدول البيانات.

المثال التالي يظهر كيفية نقل ورقة عمل إلى موقع آخر داخل سجل العمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-MoveWorksheet-MoveWorksheet.java" >}}
