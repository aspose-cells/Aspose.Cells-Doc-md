---
title: فرز البيانات
type: docs
weight: 130
url: /ar/net/sort-data-of-excel/
---
{{% alert color="primary" %}}

يعد فرز البيانات أحد ميزات Microsoft المفيدة العديدة لبرنامج Excel. يسمح للمستخدمين بطلب البيانات لتسهيل مسحها ضوئيًا. يتيح Aspose.Cells للمطورين فرز بيانات ورقة العمل أبجديًا أو رقميًا والتي تعمل بنفس الطريقة التي يعمل بها Microsoft Excel لفرز البيانات.

{{% /alert %}}

## **فرز البيانات في Microsoft Excel**

لفرز البيانات في Microsoft Excel:

1.  يختار**بيانات** من**فرز** قائمة. سيتم عرض مربع حوار الترتيب.
1. حدد خيار الفرز.

بشكل عام ، يتم إجراء الفرز على قائمة - يتم تعريفها على أنها مجموعة متجاورة من البيانات حيث يتم عرض البيانات في أعمدة.

## **فرز البيانات مع Aspose.Cells**

 يوفر Aspose.Cells ملف[**DataSorter**](https://reference.aspose.com/cells/net/aspose.cells/datasorter)فئة تستخدم لفرز البيانات بترتيب تصاعدي أو تنازلي. يحتوي الفصل على بعض الأعضاء المهمين ، على سبيل المثال ، خصائص مثل Key1 ... Key3 و Order1 ... Order3. يتم استخدام هؤلاء الأعضاء لتحديد المفاتيح التي تم فرزها وتحديد ترتيب فرز المفاتيح.

 يجب عليك تحديد المفاتيح وتعيين ترتيب الفرز قبل تنفيذ فرز البيانات. يوفر الفصل[**فرز**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index)الطريقة المستخدمة لإجراء فرز البيانات استنادًا إلى بيانات الخلية في ورقة العمل.

 ال[**فرز**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1)تقبل الطريقة المعلمات التالية:

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)، خلايا ورقة العمل الأساسية.
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)، نطاق الخلايا. حدد منطقة الخلية قبل تطبيق فرز البيانات.

يستخدم هذا المثال ملف القالب "Book1.xls" الذي تم إنشاؤه في Microsoft Excel. بعد تنفيذ الكود أدناه ، يتم فرز البيانات بشكل مناسب.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

 إذا كنت تريد الفرز*من اليسار إلى اليمين* ، استخدم ال[**فرز البيانات**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright) ينسب.

{{% /alert %}}

### **فرز البيانات مع لون الخلفية**

 يوفر Excel ميزات لفرز البيانات بناءً على لون الخلفية. يتم توفير نفس الميزة باستخدام Aspose.Cells باستخدام DataSorter حيث[**SortOnType**](https://reference.aspose.com/cells/net/aspose.cells/sortontype) يمكن استخدام لون الخلية في تنسيق[**AddKey ()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey) لفرز البيانات بناءً على لون الخلفية. جميع الخلايا التي تحتوي على لون محدد في ملف[**AddKey ()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey)، يتم وضع الوظيفة في الأعلى أو الأسفل وفقًا لإعداد SortOrder ولا يتم تغيير ترتيب باقي الخلايا على الإطلاق.

فيما يلي نماذج الملفات التي يمكن تنزيلها لاختبار هذه الميزة:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

## **موضوعات مسبقة**
- [فرز البيانات في العمود باستخدام قائمة الفرز المخصصة](/cells/ar/net/sort-data-in-column-with-custom-sort-list/)
- [تحديد تحذير الفرز أثناء فرز البيانات](/cells/ar/net/specifying-sort-warning-while-sorting-data/)
