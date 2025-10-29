---
title: إدارة بيانات ملفات إكسل
linktitle: بيانات الخلايا
type: docs
weight: 110
url: /ar/nodejs-cpp/view-and-edit-excel-data/
description: يصف هذا المقال كيفية عرض وتحرير بيانات ملفات Excel باستخدام مكتبة Aspose.Cells لـ Node.js عبر C++.
keywords: Aspose.Cells Node.js عبر C++، إدارة بيانات ملف Excel، إضافة بيانات إلى ملف Excel، الحصول على البيانات من ملف Excel، تحسين كفاءة إضافة البيانات، إدارة بيانات الخلايا، تحديث بيانات الخلايا، الحصول على بيانات الخلايا، إدراج بيانات الخلايا
---

{{% alert color="primary" %}}

في [الوصول إلى خلايا ورقة العمل](/cells/ar/nodejs-cpp/accessing-cells-of-a-worksheet/)، ناقشنا الأساليب الأساسية للوصول إلى الخلايا في ورقة العمل. يستخدم هذا المقال إحدى تلك الأساليب لإضافة أنواع مختلفة من البيانات إلى الخلايا.

{{% /alert %}}

## **كيفية إضافة بيانات إلى الخلايا**

يوفر Aspose.Cells for Node.js via C++ فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) تتيح الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). كل عنصر في مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) يمثل كائنًا من فئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

يسمح Aspose.Cells للمطورين بإضافة البيانات إلى خلايا ورقة العمل من خلال استدعاء طريقة [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) من فئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). توفر Aspose.Cells نسخ تحميل متراكبة من طريقة [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) التي تتيح للمطورين إضافة أنواع مختلفة من البيانات إلى الخلايا. باستخدام هذه النسخ التحميلية من طريقة [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-)، من الممكن إضافة قيمة Boolean، سلسلة، Double، عدد صحيح، أو تاريخ/وقت، وغيرها إلى الخلية.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AddDataToCells.js" >}}


## **كيفية تحسين الكفاءة**

إذا كنت تستخدم طريقة [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) لوضع كمية كبيرة من البيانات في ورقة العمل، فعليك إضافة القيم إلى الخلايا، أولاً عن طريق الصف ثم العمود. هذا النهج يحسن بشكل كبير من كفاءة تطبيقاتك.

## **كيفية استرداد البيانات من الخلايا**

Aspose.Cells for Node.js via C++ يوفر فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) تتيح الوصول إلى أوراق العمل في الملف. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). كل عنصر في مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) يمثل كائنًا من فئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

توفر فئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) العديد من الخصائص التي تسمح للمطورين باسترجاع القيم من الخلايا وفقًا لأنواع بياناتها. تشمل هذه الخصائص:

- [**getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--): يُرجع القيمة النصية للخلية.
- [**getDoubleValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDoubleValue--): يُرجع القيمة المزدوجة للخلية.
- [**getBoolValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getBoolValue--): يُرجع القيمة المنطقية للخلية.
- [**getDateTimeValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDateTimeValue--): يُرجع قيمة التاريخ/الوقت للخلية.
- [**getFloatValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFloatValue--): يُرجع القيمة العائمة للخلية.
- [**getIntValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getIntValue--): يُرجع القيمة الصحيحة للخلية.

عندما لا يتم ملء حقل، فإن الخلايا التي تحتوي على [**getDoubleValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDoubleValue--) أو [**getFloatValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFloatValue--) ترمي استثناءً.

يمكن أيضًا فحص نوع البيانات المحتواة في الخلية باستخدام طريقة [**getType()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getType--) من فئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). في الواقع، تعتمد طريقة [**getType()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getType--) من فئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) على تعداد [**CellValueType**](https://reference.aspose.com/cells/nodejs-cpp/cellvaluetype) الذي يتم سرد القيم المعرفة مسبقًا أدناه:

|**أنواع قيم الخلية**|**الوصف**|
| :- | :- |
|IsBool| يحدد أن قيمة الخلية هي بولية.
|IsDateTime| يحدد أن قيمة الخلية هي تاريخ/وقت.
|IsNull| تمثل خلية فارغة.
|IsNumeric| يحدد أن قيمة الخلية هي رقمية.
|IsString| يحدد أن قيمة الخلية هي نصية.
|IsUnknown| يحدد أن قيمة الخلية غير معروفة.

يمكنك أيضًا استخدام أنواع قيم الخلية المحددة مسبقًا أعلاه للمقارنة مع نوع البيانات الحاضرة في كل خلية.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-RetrieveDataFromCells.js" >}}


{{% alert color="primary" %}}

أثناء العمل على ورقة العمل، قد يضيف المستخدمون أنواعًا مختلفة من البيانات في الخلايا. قد تتضمن هذه البيانات Boolean، عدد صحيح، نقطة عائمة، نص، أو قيم تاريخ/وقت. مع Aspose.Cells، يمكنك الحصول على القيم المناسبة من الخلايا وفقًا لأنواع البيانات.

{{% /alert %}}

## **مواضيع متقدمة**
- [الوصول إلى الخلايا في ورقة العمل](/cells/ar/nodejs-cpp/accessing-cells-of-a-worksheet/)
- [تحويل بيانات النص الرقمية إلى رقم](/cells/ar/nodejs-cpp/convert-text-numeric-data-to-number/)
- [إنشاء المجاميع الفرعية](/cells/ar/nodejs-cpp/creating-subtotals/)
- [تصفية البيانات](/cells/ar/nodejs-cpp/data-filtering/)
- [فرز البيانات](/cells/ar/nodejs-cpp/sort-data-of-excel/)
- [التحقق من البيانات](/cells/ar/nodejs-cpp/data-validation/)
- [العثور على البيانات أو البحث](/cells/ar/nodejs-cpp/find-or-search-data/)
- [الحصول على قيمة سلسلة الخلية بتنسيق وبدون تنسيق](/cells/ar/nodejs-cpp/get-cell-string-value-with-and-without-formatting/)
- [إضافة نص فائق النص الغني HTML داخل الخلية](/cells/ar/nodejs-cpp/adding-html-rich-text-inside-the-cell/)
- [إدراج الروابط التشعبية في إكسل أو أوبن أوفيس](/cells/ar/nodejs-cpp/insert-hyperlinks-to-excel/)
- [كيفية استخدام العدادات وأين استخدامها](/cells/ar/nodejs-cpp/how-and-where-to-use-enumerators/)
- [قياس عرض وارتفاع قيمة الخلية بوحدة البكسل](/cells/ar/nodejs-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [قراءة قيم الخلية في مواضيع متعددة بشكل متزامن](/cells/ar/nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [التحويل بين اسم الخلية وفهرس الصف/العمود](/cells/ar/nodejs-cpp/names-and-indices/)
- [ملء البيانات أولاً حسب الصف ثم حسب العمود](/cells/ar/nodejs-cpp/populate-data-first-by-row-then-by-column/)
- [الحفاظ على بادئة اقتباس واحدة لقيمة الخلية أو النطاق](/cells/ar/nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [الوصول إلى وتحديث أجزاء النص الغني للخلية](/cells/ar/nodejs-cpp/access-and-update-the-portions-of-rich-text-of-cell/)
{{< app/cells/assistant language="nodejs-cpp" >}}
