---
title: نسخ الصفوف والأعمدة
type: docs
weight: 30
url: /ar/java/copying-rows-and-columns/
---
## **مقدمة**
في بعض الأحيان ، تحتاج إلى نسخ الصفوف والأعمدة في ورقة العمل دون نسخ ورقة العمل بأكملها. باستخدام Aspose.Cells ، يمكن نسخ الصفوف والأعمدة داخل أو بين المصنفات.

عند نسخ صف (أو عمود) ، يتم أيضًا نسخ البيانات الموجودة فيه ، بما في ذلك الصيغ - مع المراجع المحدثة - والقيم والتعليقات والتنسيق والخلايا المخفية والصور والكائنات الرسومية الأخرى.
## **نسخ الصفوف والأعمدة باستخدام Microsoft Excel**
1. حدد الصف أو العمود الذي تريد نسخه.
1.  لنسخ الصفوف أو الأعمدة ، انقر فوق**ينسخ** على ال**اساسي** شريط الأدوات ، أو اضغط على**كنترول**+ ** ج **.
1. حدد صفًا أو عمودًا أدناه أو على يمين المكان الذي تريد نسخ تحديدك إليه.
1.  عندما تقوم بنسخ صفوف أو أعمدة ، انقر فوق**منسوخة Cells** على ال**إدراج** قائمة.

{{% alert color="primary" %}} 

 إذا قمت بالنقر فوق**معجون** على ال**اساسي** شريط الأدوات أو اضغط**كنترول**+** V ** بدلاً من النقر فوق أمر على ملف**إدراج قائمة ** ، يتم استبدال أي محتويات للخلايا الوجهة.

{{% /alert %}} 

## **نسخ صف واحد**

 يوفر Aspose.Cells ملف[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\) ) طريقة ال[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)صف دراسي. تنسخ هذه الطريقة جميع أنواع البيانات بما في ذلك الصيغ والقيم والتعليقات وتنسيقات الخلايا والخلايا المخفية والصور والكائنات الرسومية الأخرى من صف المصدر إلى صف الوجهة.

 ال[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) تأخذ الطريقة المعلمات التالية:

-  المصدر[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)هدف،
- فهرس صف المصدر و
- فهرس صف الوجهة.

 استخدم هذه الطريقة لنسخ صف داخل ورقة أو إلى ورقة أخرى. ال[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) تعمل بطريقة مشابهة لـ Microsoft Excel. لذلك ، على سبيل المثال ، لا تحتاج إلى تعيين ارتفاع صف الوجهة بشكل صريح ، حيث يتم نسخ هذه القيمة أيضًا.

يوضح المثال التالي كيفية نسخ صف في ورقة عمل. يستخدم قالب Microsoft ملف Excel ويقوم بنسخ الصف الثاني (كاملاً بالبيانات والتنسيق والتعليقات والصور وما إلى ذلك) ولصقه في الصف الثاني عشر في نفس ورقة العمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingRows-CopyingRows.java" >}}



يتم إنشاء الإخراج التالي عند تنفيذ الكود أدناه.

**يتم نسخ الصف بأعلى درجات الدقة والدقة** 

![ما يجب القيام به: image_بديل_نص](copying-rows-and-columns_1.png)

{{% alert color="primary" %}} 

عند نسخ الصفوف ، من المهم ملاحظة الصور أو المخططات أو الكائنات الرسومية الأخرى ذات الصلة لأن هذا هو نفسه مع Microsoft Excel:

1. إذا كان فهرس صف المصدر هو 5 ، يتم نسخ الصورة والرسم البياني وما إلى ذلك إذا كانت موجودة في الصفوف الثلاثة (مؤشر صف البداية هو 4 ومؤشر صف النهاية هو 6).
1. لن تتم إزالة الصور والمخططات الموجودة وما إلى ذلك في صف الوجهة.

{{% /alert %}} 

## **نسخ صفوف متعددة**

 يمكنك أيضًا نسخ صفوف متعددة إلى وجهة جديدة أثناء استخدام ملف[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int)) الطريقة التي تأخذ معلمة إضافية من النوع الصحيح لتحديد عدد صفوف المصدر المراد نسخها.

يوجد أدناه لقطة لجدول بيانات الإدخال الذي يحتوي على 3 صفوف من البيانات بينما ينسخ مقتطف الشفرة المقدم أدناه جميع الصفوف الثلاثة إلى موقع جديد بدءًا من الصف السابع.

![ما يجب القيام به: image_بديل_نص](copy-rows-and-columns_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleRows-CopyingMultipleRows.java" >}}

فيما يلي عرض جدول البيانات الناتج بعد تنفيذ مقتطف الشفرة أعلاه.

![ما يجب القيام به: image_بديل_نص](copy-rows-and-columns_4.png)

## **نسخ عمود واحد**

 يوفر Aspose.Cells ملف[نسخ العمود](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\) ) طريقة ال[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)class ، هذه الطريقة تنسخ جميع أنواع البيانات ، بما في ذلك الصيغ - مع المراجع المحدثة - والقيم والتعليقات وتنسيقات الخلايا والخلايا المخفية والصور وكائنات الرسم الأخرى من العمود المصدر إلى عمود الوجهة.

 ال[نسخ العمود](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) تأخذ الطريقة المعلمات التالية:

-  المصدر[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)هدف،
- فهرس عمود المصدر و
- فهرس عمود الوجهة.

 استخدم ال[نسخ العمود](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) طريقة لنسخ عمود داخل ورقة أو إلى ورقة أخرى.

يقوم هذا المثال بنسخ عمود من ورقة عمل ولصقه في ورقة عمل في مصنف آخر.

**يتم نسخ عمود من مصنف إلى آخر** 

![ما يجب القيام به: image_بديل_نص](copying-rows-and-columns_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingColumns-CopyingColumns.java" >}}

## **نسخ أعمدة متعددة**

 مشابه ل[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int) ) ، فإن واجهات برمجة التطبيقات Aspose.Cells توفر أيضًا امتداد[**Cells.copyColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns(com.aspose.cells.Cells,%20int,%20int,%20int)) لنسخ أعمدة مصدر متعددة إلى موقع جديد.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleColumns-CopyingMultipleColumns.java" >}}

إليك كيفية ظهور جداول البيانات المصدر والنتيجة في Excel.

![ما يجب القيام به: image_بديل_نص](copy-rows-and-columns_7.png)

![ما يجب القيام به: image_بديل_نص](copy-rows-and-columns_8.png)


## **لصق الصفوف / الأعمدة بخيارات اللصق**
 Aspose.Cells يوفر الآن[خيارات لصق](https://reference.aspose.com/cells/java/com.aspose.cells/PasteOptions) أثناء استخدام الوظائف[CopyRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRows\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.CopyOptions,%20com.aspose.cells.PasteOptions\) ) و[CopyColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.PasteOptions\)). يسمح بتعيين خيارات لصق مناسبة مشابهة لبرنامج Excel.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-PastingDataWithPasteOptions.java" >}}

