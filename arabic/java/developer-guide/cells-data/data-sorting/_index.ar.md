---
title: فرز البيانات
type: docs
weight: 90
url: /ar/java/sort-data-of-excel/
---
{{% alert color="primary" %}}

يعد فرز البيانات أحد ميزات Microsoft المفيدة العديدة لبرنامج Excel. يسمح للمستخدمين بطلب البيانات لتسهيل مسحها ضوئيًا.

يسمح لك Aspose.Cells بفرز بيانات ورقة العمل أبجديًا أو رقميًا. وهو يعمل بنفس الطريقة التي يعمل بها Microsoft Excel لفرز البيانات.

{{% /alert %}}

## **فرز البيانات في Microsoft Excel**

لفرز البيانات في Microsoft Excel:

1.  يختار**بيانات** من**فرز** قائمة.
 يتم عرض مربع الحوار "فرز".
1. حدد خيار الفرز.

بشكل عام ، يتم إجراء الفرز على قائمة - يتم تعريفها على أنها مجموعة متجاورة من البيانات حيث يتم عرض البيانات في أعمدة.

**مربع حوار الفرز في Microsoft Excel**

![ما يجب القيام به: image_بديل_نص](data-sorting_1.png)

## **فرز البيانات مع Aspose.Cells**

 يوفر Aspose.Cells ملف[**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) فئة تستخدم لفرز البيانات بترتيب تصاعدي أو تنازلي. يحتوي الفصل على بعض الأعضاء المهمين ، على سبيل المثال ، طرق مثل[**تعيين مفتاح 1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key1) ... [**تعيين مفتاح 2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key2) و[**setOrder1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order1) ... [**setOrder2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order2)يتم استخدام هؤلاء الأعضاء لتحديد المفاتيح التي تم فرزها وتحديد ترتيب فرز المفاتيح.

 يجب عليك تحديد المفاتيح وتعيين ترتيب الفرز قبل تنفيذ فرز البيانات. يوفر الفصل[**فرز**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort()) الطريقة المستخدمة لإجراء فرز البيانات استنادًا إلى بيانات الخلية في ورقة العمل.

 ال[**فرز**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort()) تقبل الطريقة المعلمات التالية:

- [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)، خلايا ورقة العمل.
- [**CellArea**](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)، نطاق الخلايا. حدد منطقة الخلية قبل تطبيق فرز البيانات.

يوضح هذا المثال كيفية فرز البيانات باستخدام Aspose.Cells API. يستخدم المثال ملف قالب "Book1.xls" ويفرز البيانات لنطاق البيانات (A1: B14) في ورقة العمل الأولى:

يستخدم هذا المثال ملف القالب "Book1.xls" الذي تم إنشاؤه في Microsoft Excel.

**نموذج ملف Excel كامل بالبيانات**

![ما يجب القيام به: image_بديل_نص](data-sorting_2.png)

بعد تنفيذ الكود أدناه ، يتم فرز البيانات بشكل مناسب كما ترى من ملف Excel الناتج.

**إخراج ملف Excel بعد فرز البيانات**

![ما يجب القيام به: image_بديل_نص](data-sorting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DataSorting-DataSorting.java" >}}

{{% alert color="primary" %}}

 لفرز*من اليسار إلى اليمين* ، استخدم ال[**فرز البيانات**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortLeftToRight) ينسب.

{{% /alert %}}

## **فرز البيانات مع لون الخلفية**

 يوفر Excel ميزة فرز البيانات بناءً على لون الخلفية. يتم توفير نفس الميزة باستخدام Aspose.Cells باستخدام[**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) أين[**SortOnType.CELL_COLOR**](https://reference.aspose.com/cells/java/com.aspose.cells/sortontype#CELL_COLOR) يمكن استخدامها في[**addKey ()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int) ) لفرز البيانات بناءً على لون الخلفية. جميع الخلايا التي تحتوي على لون محدد في ملف[**addKey ()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int)) ، يتم وضع الوظيفة في الأعلى أو الأسفل وفقًا لإعداد SortOrder ولا يتم تغيير ترتيب باقي الخلايا على الإطلاق.

فيما يلي نماذج الملفات التي يمكن تنزيلها لاختبار هذه الميزة:

[sampleBackGroundFile.xlsx](sampleBackGroundFile.xlsx)

[outputsampleBackGroundFile.xlsx](outputsampleBackGroundFile.xlsx)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

## **موضوعات مسبقة**
- [فرز البيانات في العمود باستخدام قائمة الفرز المخصصة](/cells/ar/java/sort-data-in-column-with-custom-sort-list/)
- [تحديد تحذير الفرز أثناء فرز البيانات](/cells/ar/java/specifying-sort-warning-while-sorting-data/)

