---
title: إدارة بيانات ملفات إكسل
linktitle: بيانات الخلايا
type: docs
weight: 110
url: /ar/python-net/view-and-edit-excel-data/
description: يصف هذا المقال كيفية عرض وتحرير بيانات ملفات إكسل باستخدام مكتبة Aspose.Cells for Python via .NET.
keywords: مكتبة إكسل Python، Aspose.Cells لإدارة الملفات بيانات إكسل Python، Python إضافة بيانات إلى ملف Excel، Python الحصول على البيانات من ملف إكسل، Python كيفية تحسين كفاءة إضافة البيانات، Python إدارة بيانات الخلايا، Python تحديث بيانات الخلايا، Python الحصول على بيانات الخلايا، Python إدراج بيانات الخلايا.
---

{{% alert color="primary" %}}

في [الوصول إلى الخلايا في ورقة العمل] (/ cells / ar / python-net / accessing-cells-of-a-worksheet /)، ناقشنا الطرق الأساسية للوصول إلى الخلايا في ورقة العمل. يستخدم هذا المقال إحدى تلك الطرق لإضافة أنواع مختلفة من البيانات للخلايا.

{{% /alert %}}

## **كيفية إضافة بيانات إلى الخلايا**

توفر Aspose.Cells for Python via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)، التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/). يمثل كل عنصر في مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) كائنًا من الفئة [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

تسمح Aspose.Cells for Python via .NET للمطورين بإضافة بيانات إلى الخلايا في ورقات العمل من خلال استدعاء الفئة [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) 's الطريقة [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool). توفر Aspose.Cells for Python via .NET إصدارات متعددة من الطريقة [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int) التي تتيح للمطورين إضافة أنواع مختلفة من البيانات للخلايا. باستخدام هذه الإصدارات المتعددة للطريقة [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int)، يمكن إضافة قيم Boolean أو string أو double أو integer أو date / time، وما إلى ذلك إلى الخلية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AddingDataToCells-1.py" >}}

## **كيفية تحسين الكفاءة**

إذا استخدمت الطريقة [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int) لوضع كمية كبيرة من البيانات في ورقة عمل، يجب أولاً إضافة القيم إلى الخلايا حسب الصفوف ثم حسب الأعمدة. هذا النهج يحسن بشكل كبير كفاءة تطبيقاتك.

## **كيفية استرداد البيانات من الخلايا**

توفر Aspose.Cells for Python via .NET فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) التي تسمح بالوصول إلى ورقات العمل في الملف. يتم تمثيل ورقة العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/). يمثل كل عنصر في مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) كائنًا من الفئة [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

توفر الفئة [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) خصائصًا عدة تسمح للمطورين باسترداد القيم من الخلايا وفقًا لأنواع بياناتها. تتضمن هذه الخصائص:

- [**string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/): يعيد قيمة السلسلة للخلية.
- [**double_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/double_value/): يعيد قيمة مزدوجة للخلية.
- [**bool_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/bool_value/): يعيد قيمة Boolean للخلية.
- [**date_time_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/date_time_value/): يعيد قيمة تاريخ / وقت للخلية.
- [**float_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/float_value/): يعيد قيمة عائمة للخلية.
- [**int_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/int_value/): يعيد قيمة العدد الصحيح للخلية.

عندما لا يتم ملؤها، تثير الخلايا مع [**double_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/double_value/) أو [**float_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/float_value/) استثناء.

يمكن أيضًا فحص نوع البيانات الموجود في خلية باستخدام خاصية [**type**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/type/) لفئة [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) . في الواقع، تعتمد خاصية [**type**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/type/) لفئة [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) على تعداد [**CellValueType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvaluetype) والذي تم سرده أسفله:

|**أنواع قيم الخلية**|**الوصف**|
| :- | :- |
|IS_BOOL|يحدد أن قيمة الخلية هي قيمة مقولبة.|
|IS_DATE_TIME|يحدد أن قيمة الخلية هي تاريخ/وقت.|
|IS_NULL|تمثل خلية فارغة.|
|IS_NUMERIC|يحدد أن قيمة الخلية هي رقمية.|
|IS_STRING|يحدد أن قيمة الخلية هي سلسلة نصية.|
|IS_ERROR|يحدد أن قيمة الخلية هي قيمة خطأ.|
|IS_UNKNOWN|يحدد أن قيمة الخلية مجهولة.|

يمكنك أيضًا استخدام أنواع قيم الخلية المحددة مسبقًا أعلاه للمقارنة مع نوع البيانات الحاضرة في كل خلية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-RetrievingDataFromCells-1.py" >}}

{{% alert color="primary" %}}

أثناء العمل على الأوراق العمل، قد يضيف المستخدمون أنواعًا مختلفة من البيانات في الخلايا. قد تشمل هذه الأنواع قيم نطقية، أعداد صحيحة، أعداد عائمة، نص أو قيم تاريخ/وقت. باستخدام Aspose.Cells for Python via .NET ، يمكنك الحصول على القيم المناسبة من الخلايا وفقًا لأنواع البيانات الخاصة بهم.

{{% /alert %}}

## **مواضيع متقدمة**
- [الوصول إلى الخلايا في ورقة العمل](/cells/ar/python-net/accessing-cells-of-a-worksheet/)
- [تحويل بيانات النص الرقمية إلى رقم](/cells/ar/python-net/convert-text-numeric-data-to-number/)
- [إنشاء المجاميع الفرعية](/cells/ar/python-net/creating-subtotals/)
- [تصفية البيانات](/cells/ar/python-net/data-filtering/)
- [فرز البيانات](/cells/ar/python-net/sort-data-of-excel/)
- [التحقق من البيانات](/cells/ar/python-net/data-validation/)
- [الحصول على قيمة سلسلة الخلية بتنسيق وبدون تنسيق](/cells/ar/python-net/get-cell-string-value-with-format-strategy/)
- [إضافة نص فائق النص الغني HTML داخل الخلية](/cells/ar/python-net/adding-html-rich-text-inside-the-cell/)
- [العثور على البيانات أو البحث](/cells/ar/python-net/find-or-search-data/)
- [إدراج الروابط التشعبية في إكسل أو أوبن أوفيس](/cells/ar/python-net/insert-hyperlinks-to-excel/)
- [قياس عرض وارتفاع قيمة الخلية بوحدة البكسل](/cells/ar/python-net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [التحويل بين اسم الخلية وفهرس الصف/العمود](/cells/ar/python-net/names-and-indices/)
- [ملء البيانات أولاً حسب الصف ثم حسب العمود](/cells/ar/python-net/populate-data-first-by-row-then-by-column/)
- [الحفاظ على بادئة اقتباس واحدة لقيمة الخلية أو النطاق](/cells/ar/python-net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [الوصول إلى وتحديث أجزاء النص الغني للخلية](/cells/ar/python-net/access-and-update-the-portions-of-rich-text-of-cell/)
{{< app/cells/assistant language="python-net" >}}
