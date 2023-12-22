---
title: فرز البيانات
type: docs
weight: 130
url: /ar/net/sort-data-of-excel/
description: تعرف على كيفية فرز البيانات باستخدام Aspose.Cells for .NET API.
keywords: Sort data in ascending or descending order, Sort data based on the background color
---
{{% alert color="primary" %}}

يعد فرز البيانات أحد الميزات العديدة المفيدة في برنامج Excel Microsoft. يتيح للمستخدمين طلب البيانات لتسهيل عملية المسح. يتيح Aspose.Cells للمطورين فرز بيانات ورقة العمل أبجديًا أو رقميًا والذي يعمل بنفس الطريقة التي يعمل بها Microsoft Excel لفرز البيانات.

{{% /alert %}}

##  **فرز البيانات في Microsoft إكسل**

لفرز البيانات في Microsoft إكسل:

1.  يختار**بيانات** من**نوع** قائمة طعام. سيتم عرض مربع الحوار "فرز".
1. حدد خيار الفرز.

بشكل عام، يتم إجراء الفرز على قائمة - يتم تعريفها على أنها مجموعة متجاورة من البيانات حيث يتم عرض البيانات في أعمدة.

##  **فرز البيانات مع Aspose.Cells**

 Aspose.Cells يوفر[**فارز البيانات**](https://reference.aspose.com/cells/net/aspose.cells/datasorter)فئة تستخدم لفرز البيانات بترتيب تصاعدي أو تنازلي. تحتوي الفئة على بعض الأعضاء المهمين، على سبيل المثال، خصائص مثل Key1 ... Key3 و Order1 ... Order3. يتم استخدام هؤلاء الأعضاء لتحديد المفاتيح التي تم فرزها وتحديد ترتيب فرز المفاتيح.

 يجب عليك تحديد المفاتيح وتعيين ترتيب الفرز قبل تنفيذ فرز البيانات. يوفر الفصل[**نوع**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index)الطريقة المستخدمة لإجراء فرز البيانات بناءً على بيانات الخلية الموجودة في ورقة العمل.

 ال[**نوع**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1)تقبل الطريقة المعلمات التالية:

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)، خلايا ورقة العمل الأساسية.
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)، نطاق الخلايا. حدد منطقة الخلية قبل تطبيق فرز البيانات.

يستخدم هذا المثال ملف القالب "Book1.xls" الذي تم إنشاؤه في Microsoft Excel. بعد تنفيذ التعليمات البرمجية أدناه، يتم فرز البيانات بشكل مناسب.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

 إذا كنت تريد فرز *LeftToRight*، فاستخدم الملف[**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright) يصف.

{{% /alert %}}

###  **فرز البيانات مع لون الخلفية**

يوفر Excel ميزات لفرز البيانات بناءً على لون الخلفية. يتم توفير نفس الميزة باستخدام Aspose.Cells باستخدام DataSorter حيث[**SortOnType**](https://reference.aspose.com/cells/net/aspose.cells/sortontype) يمكن استخدام .CellColor في[**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey) لفرز البيانات بناءً على لون الخلفية. كافة الخلايا التي تحتوي على اللون المحدد في[**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey)، يتم وضع الوظيفة في الأعلى أو الأسفل وفقًا لإعداد SortOrder ولا يتغير ترتيب بقية الخلايا على الإطلاق.

فيما يلي نماذج الملفات التي يمكن تنزيلها لاختبار هذه الميزة:

[SampleBackGroundFile.xlsx](81920906.xlsx)

[OutputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

##  **مواضيع متقدمة**
- [فرز البيانات في العمود باستخدام قائمة الفرز المخصصة](/cells/ar/net/sort-data-in-column-with-custom-sort-list/)
- [تحديد تحذير الفرز أثناء فرز البيانات](/cells/ar/net/specifying-sort-warning-while-sorting-data/)
