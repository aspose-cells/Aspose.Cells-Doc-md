---
title: ترتيب البيانات
type: docs
weight: 90
url: /ar/java/sort-data-of-excel/
---

{{% alert color="primary" %}}

فرز البيانات هو واحد من الميزات المفيدة في Microsoft Excel. يتيح للمستخدمين ترتيب البيانات لجعل عملية المسح أسهل.

تسمح Aspose.Cells لك بفرز بيانات ورق العمل ترتيبا أبجديا أو رقميا. وهو يعمل بنفس طريقة عمل Microsoft Excel لفرز البيانات.

{{% /alert %}}

## **فرز البيانات في Microsoft Excel**

لفرز البيانات في Microsoft Excel:

1. حدد **البيانات** من قائمة **ترتيب**.
   يتم عرض مربع حوار الترتيب.
1. حدد خيار الفرز.

عموماً، يتم إجراء الفرز على قائمة - المعرفة بأنها مجموعة متواصلة من البيانات حيث يتم عرض البيانات في أعمدة.

**مربع حوار الفرز في Microsoft Excel**

![todo:image_alt_text](data-sorting_1.png)

## **فرز البيانات مع Aspose.Cells**

توفر Aspose.Cells الفئة [**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) المستخدمة لفرز البيانات تصاعديًا أو تنازليًا. تحتوي الفئة على بعض الأعضاء المهمة، على سبيل المثال، الطرق مثل [**setKey1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key1) و [**setKey2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key2)   و [**setOrder1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order1) و [**setOrder2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order2). يتم استخدام هذه الأعضاء لتحديد المفاتيح المرتبة وتحديد ترتيب فرز المفتاح.

يجب عليك تعريف المفاتيح وتعيين ترتيب الفرز قبل تنفيذ فرز البيانات. توفر الفئة الطريقة [**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort--) المستخدمة لأداء فرز البيانات بناءً على بيانات الخلية في ورقة العمل.

تقبل الطريقة [**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort--) البيانات التالية:

- [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)، خلايا ورقة العمل.
- [**CellArea**](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)، نطاق الخلايا. قم بتحديد منطقة الخلية قبل تطبيق فرز البيانات.

هذا المثال يوضح كيفية فرز البيانات باستخدام واجهة برمجة التطبيقات Aspose.Cells. يستخدم المثال ملف قالب "Book1.xls" ويفرز البيانات لنطاق البيانات (A1:B14) في ورقة العمل الأولى:

يستخدم هذا المثال ملف القالب "Book1.xls" الذي تم إنشاؤه في Microsoft Excel.

**ملف إكسل القالب المكتمل مع البيانات**

![todo:image_alt_text](data-sorting_2.png)

بعد تشغيل الكود أدناه، يتم فرز البيانات بشكل مناسب كما يمكن رؤيته من ملف الإكسل الناتج.

**ملف إكسل الناتج بعد فرز البيانات**

![todo:image_alt_text](data-sorting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DataSorting-DataSorting.java" >}}

{{% alert color="primary" %}}

لفرز *من اليمين إلى اليسار*، استخدم السمة [**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortLeftToRight).

{{% /alert %}}

## **فرز البيانات مع لون الخلفية**

يوفر Excel ميزة ترتيب البيانات استنادًا إلى لون الخلفية. يُعرض نفس الميزة باستخدام Aspose.Cells باستخدام [**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) حيث يمكن استخدام [**SortOnType.CELL_COLOR**](https://reference.aspose.com/cells/java/com.aspose.cells/sortontype#CELL-COLOR) في [**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-) لترتيب البيانات استنادًا إلى لون الخلفية. يُوضع جميع الخلايا التي تحتوي على اللون المحدد في [**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-) في الجزء العلوي أو السفلي حسب إعداد SortOrder ولا يتم تغيير ترتيب بقية الخلايا على الإطلاق.

فيما يلي الملفات العينية التي يمكن تنزيلها لاختبار هذه الميزة:

[sampleBackGroundFile.xlsx](sampleBackGroundFile.xlsx)

[outputsampleBackGroundFile.xlsx](outputsampleBackGroundFile.xlsx)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

## **مواضيع متقدمة**
- [فرز البيانات في العمود بقائمة فرز مخصصة](/cells/ar/java/sort-data-in-column-with-custom-sort-list/)
- [تحديد تحذير الفرز أثناء فرز البيانات](/cells/ar/java/specifying-sort-warning-while-sorting-data/)

{{< app/cells/assistant language="java" >}}
