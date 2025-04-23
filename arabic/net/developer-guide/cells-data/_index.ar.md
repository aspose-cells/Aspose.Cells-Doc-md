---
title: إدارة بيانات ملفات إكسل
linktitle: بيانات الخلايا
type: docs
weight: 110
url: /ar/net/view-and-edit-excel-data/
description: يصف هذا المقال كيفية عرض وتحرير بيانات ملفات Excel باستخدام مكتبة Aspose.Cells.
keywords: Aspose.Cells C# إدارة بيانات ملف Excel، إضافة بيانات إلى ملف Excel، الحصول على بيانات من ملف Excel، كيفية تحسين كفاءة إضافة البيانات، إدارة بيانات الخلايا، تحديث بيانات الخلايا، الحصول على بيانات الخلايا، إدراج بيانات الخلايا
---

{{% alert color="primary" %}}

في [الوصول إلى الخلايا في ورق العمل](/cells/ar/net/accessing-cells-of-a-worksheet/)، ناقشنا الطرق الأساسية للوصول إلى الخلايا في ورقة العمل. يستخدم هذا المقال إحدى تلك الطرق لإضافة أنواع مختلفة من البيانات إلى الخلايا.

{{% /alert %}}

## **كيفية إضافة بيانات إلى الخلايا**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)، التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بالفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). يمثل كل عنصر في مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) كائنًا من الفئة [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

تسمح Aspose.Cells للمطورين بإضافة بيانات إلى الخلايا في ورقات العمل عن طريق استدعاء طريقة [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) لفئة [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). توفر Aspose.Cells إصدارات متعددة من الطريقة [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) التي تتيح للمطورين إضافة أنواع مختلفة من البيانات إلى الخلايا. باستخدام هذه الإصدارات المتعددة للطريقة [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)، يمكن إضافة قيم بوليانية، نصية، مزدوجة، صحيحة أو تاريخ / وقت،إلى الخلية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

## **كيفية تحسين الكفاءة**

إذا استخدمت الطريقة [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) لوضع كمية كبيرة من البيانات في ورقة عمل، يجب أولاً إضافة القيم إلى الخلايا حسب الصفوف ثم حسب الأعمدة. هذا النهج يحسن بشكل كبير كفاءة تطبيقاتك.

## **كيفية استرداد البيانات من الخلايا**

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تسمح بالوصول إلى أوراق العمل في الملف. تمثل ورقة العمل بالفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). كل عنصر في مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) يمثل كائنًا من الفئة [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

توفر الفئة [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) خصائصًا عدة تسمح للمطورين باسترداد القيم من الخلايا وفقًا لأنواع بياناتها. تتضمن هذه الخصائص:

- [**StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue): يعيد قيمة السلسلة للخلية.
- [**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue): يعيد قيمة مزدوجة للخلية.
- [**BoolValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue): يعيد قيمة Boolean للخلية.
- [**DateTimeValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue): يعيد قيمة تاريخ / وقت للخلية.
- [**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): يعيد قيمة عائمة للخلية.
- [**IntValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue): يعيد قيمة العدد الصحيح للخلية.

عندما لا يتم ملؤها، تثير الخلايا مع [**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue) أو [**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue) استثناء.

يمكن أيضًا فحص نوع البيانات الموجود في خلية باستخدام خاصية [**Type**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) لفئة [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) . في الواقع، تعتمد خاصية [**Type**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) لفئة [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) على تعداد [**CellValueType**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype) والذي تم سرده أسفله:

|**أنواع قيم الخلية**|**الوصف**|
| :- | :- |
|IsBool| يحدد أن قيمة الخلية هي بولية.
|IsDateTime| يحدد أن قيمة الخلية هي تاريخ/وقت.
|IsNull| تمثل خلية فارغة.
|IsNumeric| يحدد أن قيمة الخلية هي رقمية.
|IsString| يحدد أن قيمة الخلية هي نصية.
|IsUnknown| يحدد أن قيمة الخلية غير معروفة.

يمكنك أيضًا استخدام أنواع قيم الخلية المحددة مسبقًا أعلاه للمقارنة مع نوع البيانات الحاضرة في كل خلية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

أثناء العمل على أوراق العمل، قد يضيف المستخدمون أنواعًا مختلفة من البيانات في الخلايا. يمكن أن تشمل هذه الأنواع البيانية بولية وأعدادية ونقطية عائمة ونصية وقيم التاريخ/الوقت. باستخدام Aspose.Cells، يمكنك الحصول على القيم المناسبة من الخلايا وفقًا لأنواعها.

{{% /alert %}}

## **مواضيع متقدمة**
- [الوصول إلى الخلايا في ورقة العمل](/cells/ar/net/accessing-cells-of-a-worksheet/)
- [تحويل بيانات النص الرقمية إلى رقم](/cells/ar/net/convert-text-numeric-data-to-number/)
- [إنشاء المجاميع الفرعية](/cells/ar/net/creating-subtotals/)
- [تصفية البيانات](/cells/ar/net/data-filtering/)
- [فرز البيانات](/cells/ar/net/sort-data-of-excel/)
- [التحقق من البيانات](/cells/ar/net/data-validation/)
- [تصدير البيانات من ورقة العمل](/cells/ar/net/export-data-from-worksheet/)
- [العثور على البيانات أو البحث](/cells/ar/net/find-or-search-data/)
- [الحصول على قيمة سلسلة الخلية بتنسيق وبدون تنسيق](/cells/ar/net/get-cell-string-value-with-and-without-formatting/)
- [إضافة نص فائق النص الغني HTML داخل الخلية](/cells/ar/net/adding-html-rich-text-inside-the-cell/)
- [إدراج الروابط التشعبية في إكسل أو أوبن أوفيس](/cells/ar/net/insert-hyperlinks-to-excel/)
- [استيراد البيانات إلى ورقة العمل](/cells/ar/net/import-data-into-worksheet/)
- [كيفية استخدام العدادات وأين استخدامها](/cells/ar/net/how-and-where-to-use-enumerators/)
- [قياس عرض وارتفاع قيمة الخلية بوحدة البكسل](/cells/ar/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [قراءة قيم الخلية في مواضيع متعددة بشكل متزامن](/cells/ar/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [التحويل بين اسم الخلية وفهرس الصف/العمود](/cells/ar/net/names-and-indices/)
- [ملء البيانات أولاً حسب الصف ثم حسب العمود](/cells/ar/net/populate-data-first-by-row-then-by-column/)
- [الحفاظ على بادئة اقتباس واحدة لقيمة الخلية أو النطاق](/cells/ar/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [الوصول إلى وتحديث أجزاء النص الغني للخلية](/cells/ar/net/access-and-update-the-portions-of-rich-text-of-cell/)



{{< app/cells/assistant language="csharp" >}}
