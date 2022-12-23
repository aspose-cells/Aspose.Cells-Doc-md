---
title: نسخ أوراق العمل ونقلها
type: docs
weight: 20
url: /ar/java/copying-and-moving-worksheets/
---
{{% alert color="primary" %}}

في بعض الأحيان ، تحتاج إلى عدد من أوراق العمل ذات التنسيق المشترك والبيانات. على سبيل المثال ، إذا كنت تعمل باستخدام ميزانيات ربع سنوية ، فقد ترغب في إنشاء مصنف بأوراق تحتوي على نفس عناوين الأعمدة وعناوين الصفوف والصيغ. هناك طريقة للقيام بذلك: عن طريق إنشاء ورقة واحدة ثم نسخها.

Aspose.Cells يدعم نسخ أوراق العمل ونقلها داخل مصنفات العمل أو بينها. يتم نسخ ورقة العمل ، كاملة مع البيانات والتنسيق والجداول والمصفوفات والمخططات والصور والكائنات الأخرى ، بأعلى درجة من الدقة.

{{% /alert %}}

## **نقل أو نسخ الأوراق باستخدام Microsoft Excel**

فيما يلي الخطوات المتبعة لنسخ أوراق العمل ونقلها داخل المصنفات أو بينها.

1. لنقل الأوراق أو نسخها إلى مصنف آخر ، افتح المصنف الذي سيتلقى الأوراق.
1. قم بالتبديل إلى المصنف الذي يحتوي على الأوراق التي تريد نقلها أو نسخها ، ثم حدد الأوراق.
1.  على ال**تعديل** القائمة ، انقر فوق**نقل أو نسخ الورقة**.
1. في مربع الكتاب ، انقر فوق المصنف لتلقي الأوراق.
1.  لنقل الأوراق المحددة أو نسخها إلى مصنف جديد ، انقر فوق "موافق"**كتاب جديد**.
1.  في ال**قبل الورقة** في المربع ، انقر فوق الورقة التي تريد إدراج الأوراق المنقولة أو المنسوخة قبلها.
1.  لنسخ الأوراق بدلاً من نقلها ، حدد ملف**قم بإنشاء نسخة** خانة الاختيار.

## **نسخ أوراق العمل داخل مصنف**

 يوفر Aspose.Cells طريقة التحميل الزائد ،[**WorksheetCollection.addCopy ()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#addCopy(int)) ، يتم استخدامه لإضافة ورقة عمل إلى المجموعة ونسخ البيانات من ورقة عمل موجودة. إصدار واحد من الأسلوب يأخذ فهرس ورقة العمل المصدر كمعامل. الإصدار الآخر يأخذ اسم ورقة العمل المصدر.

يوضح المثال التالي كيفية نسخ ورقة عمل موجودة داخل مصنف.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWithinWorkbook-CopyWithinWorkbook.java" >}}

## **نسخ أوراق العمل بين المصنفات**

 يوفر Aspose.Cells طريقة ،[**Worksheet.copy ()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)، تُستخدم لنسخ البيانات والتنسيق من ورقة عمل مصدر إلى ورقة عمل أخرى داخل المصنفات أو بينها. تأخذ الطريقة كائن ورقة العمل المصدر كمعلمة.

يوضح المثال التالي كيفية نسخ ورقة عمل من مصنف إلى مصنف آخر.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetsBetweenWorkbooks-CopyWorksheetsBetweenWorkbooks.java" >}}

يوضح المثال التالي كيفية نسخ ورقة عمل من مصنف إلى آخر.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetFromWorkbookToOther-CopyWorksheetFromWorkbookToOther.java" >}}

## **انقل أوراق العمل داخل المصنف**

 يوفر Aspose.Cells طريقة ،[**Worksheet.moveTo ()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#moveTo(int)) ، يُستخدم لنقل ورقة عمل إلى موقع آخر في نفس جدول البيانات.

يوضح المثال التالي كيفية نقل ورقة عمل إلى موقع آخر داخل المصنف.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-MoveWorksheet-MoveWorksheet.java" >}}
