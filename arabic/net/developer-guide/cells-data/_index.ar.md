---
title: إدارة بيانات ملفات Excel.
linktitle: Cells البيانات
type: docs
weight: 110
url: /ar/net/view-and-edit-excel-data/
description: توضح هذه المقالة كيفية عرض وتحرير بيانات ملفات Excel باستخدام مكتبة Aspose.Cells.
---
{{% alert color="primary" %}}

 في[الوصول إلى Cells من ورقة العمل](/cells/ar/net/accessing-cells-of-a-worksheet/)، ناقشنا الأساليب الأساسية للوصول إلى الخلايا في ورقة العمل. تستخدم هذه المقالة أحد هذه الأساليب لإضافة أنواع مختلفة من البيانات إلى الخلايا.

{{% /alert %}}

## **إضافة البيانات إلى Cells**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة توفر أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. كل عنصر في[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) تمثل المجموعة كائنًا من[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)صف دراسي.

Aspose.Cells يسمح للمطورين بإضافة بيانات إلى الخلايا في أوراق العمل عن طريق استدعاء[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) صف دراسي'[**ضع القيمة**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) طريقة. يوفر Aspose.Cells إصدارات محملة بشكل زائد من[**ضع القيمة**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) طريقة تتيح للمطورين إضافة أنواع مختلفة من البيانات إلى الخلايا. استخدام هذه الإصدارات المحملة بشكل زائد من[**ضع القيمة**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)طريقة ، من الممكن إضافة قيم منطقية أو سلسلة أو مزدوجة أو عدد صحيح أو تاريخ / وقت ، إلخ إلى الخلية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

## **تحسين الكفاءة**

 إذا كنت تستخدم[**ضع القيمة**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)طريقة لوضع كمية كبيرة من البيانات في ورقة عمل ، يجب إضافة قيم إلى الخلايا ، أولاً بالصفوف ثم بالأعمدة. يعمل هذا الأسلوب على تحسين كفاءة تطبيقاتك بشكل كبير.

## **استرجاع البيانات من Cells**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) مجموعة تسمح بالوصول إلى أوراق العمل الموجودة في الملف. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة توفر أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. كل عنصر في[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) تمثل المجموعة كائنًا من[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)صف دراسي.

 ال[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)يوفر class العديد من الخصائص التي تسمح للمطورين باسترداد القيم من الخلايا وفقًا لأنواع البيانات الخاصة بهم. تشمل هذه الخصائص:

- [**قيمة السلسلة**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue): إرجاع قيمة سلسلة الخلية.
- [**ضعف القيمة**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue): إرجاع القيمة المزدوجة للخلية.
- [**قيمة منطقية**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue): إرجاع القيمة المنطقية للخلية.
- [**DateTimeValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue): إرجاع قيمة التاريخ / الوقت للخلية.
- [**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): إرجاع القيمة العائمة للخلية.
- [**IntValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue)إرجاع قيمة العدد الصحيح للخلية.

 عندما لا يتم ملء أحد الحقول ، فإن الخلايا ذات[**ضعف القيمة**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue) أو[**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue)يرمي استثناء.

 يمكن أيضًا التحقق من نوع البيانات الموجودة في خلية باستخدام[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) صف دراسي'[**يكتب**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) خاصية. في الواقع، فإن[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) صف دراسي'[**يكتب**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) الممتلكات على أساس[**CellValueType**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype)التعداد الذي تم سرد قيمه المحددة مسبقًا أدناه:

|**Cell أنواع القيمة**|**وصف**|
|:- |:- |
|IsBool|تحدد أن قيمة الخلية منطقية.|
|IsDateTime|يحدد أن قيمة الخلية هي التاريخ / الوقت.|
|باطل|يمثل خلية فارغة.|
|هو رقم|تحدد أن قيمة الخلية رقمية.|
|IsString|تحدد أن قيمة الخلية عبارة عن سلسلة.|
|غير معروف|يحدد أن قيمة الخلية غير معروفة.|

يمكنك أيضًا استخدام أنواع قيم الخلايا المحددة مسبقًا للمقارنة بنوع البيانات الموجودة في كل خلية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

أثناء العمل على أوراق العمل ، يمكن للمستخدمين إضافة أنواع مختلفة من البيانات في الخلايا. قد تتضمن أنواع البيانات هذه القيم المنطقية أو الصحيحة أو الفاصلة العائمة أو النصوص أو قيم التاريخ / الوقت. باستخدام Aspose.Cells ، يمكنك الحصول على القيم المناسبة من الخلايا وفقًا لأنواع البيانات الخاصة بها.

{{% /alert %}}

## **موضوعات مسبقة**
- [الوصول إلى Cells من ورقة العمل](/cells/ar/net/accessing-cells-of-a-worksheet/)
- [تحويل البيانات الرقمية النصية إلى رقم](/cells/ar/net/convert-text-numeric-data-to-number/)
- [تكوين المجاميع الفرعية](/cells/ar/net/creating-subtotals/)
- [تصفية البيانات](/cells/ar/net/data-filtering/)
- [فرز البيانات](/cells/ar/net/sort-data-of-excel/)
- [تأكيد صحة البيانات](/cells/ar/net/data-validation/)
- [تصدير البيانات من ورقة العمل](/cells/ar/net/export-data-from-worksheet/)
- [البحث عن البيانات أو البحث عنها](/cells/ar/net/find-or-search-data/)
- [احصل على Cell String Value with وبدون التنسيق](/cells/ar/net/get-cell-string-value-with-and-without-formatting/)
- [إضافة HTML نص منسق داخل Cell](/cells/ar/net/adding-html-rich-text-inside-the-cell/)
- [أدخل الارتباطات التشعبية في Excel أو OpenOffice](/cells/ar/net/insert-hyperlinks-to-excel/)
- [استيراد البيانات إلى ورقة العمل](/cells/ar/net/import-data-into-worksheet/)
- [كيف وأين تستخدم العدادين](/cells/ar/net/how-and-where-to-use-enumerators/)
- [قم بقياس العرض والارتفاع بقيمة Cell بوحدة البكسل](/cells/ar/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [قراءة Cell القيم في خيوط متعددة في نفس الوقت](/cells/ar/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [التحويل بين اسم الخلية وفهرس الصف / العمود](/cells/ar/net/names-and-indices/)
- [قم بتعبئة البيانات أولاً بصف ثم بالعمود](/cells/ar/net/populate-data-first-by-row-then-by-column/)
- [احتفظ ببادئة اقتباس فردية بقيمة Cell أو نطاق](/cells/ar/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [قم بالوصول إلى أجزاء النص المنسق وتحديثها في Cell](/cells/ar/net/access-and-update-the-portions-of-rich-text-of-cell/)



