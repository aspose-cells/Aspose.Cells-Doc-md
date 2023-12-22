---
title: إدارة بيانات ملفات Excel
linktitle: Cells بيانات
type: docs
weight: 110
url: /ar/net/view-and-edit-excel-data/
description: توضح هذه المقالة كيفية عرض وتحرير بيانات ملفات Excel باستخدام مكتبة Aspose.Cells.
keywords: Aspose.Cells C# Manage data of Excel file, add data to Excel file, get data from excel file, How to Improve Efficiency of adding data, manage cells data, update cells data, get cells data, insert cells data
---
{{% alert color="primary" %}}

 في[الوصول إلى Cells من ورقة العمل](/cells/ar/net/accessing-cells-of-a-worksheet/)ناقشنا الأساليب الأساسية للوصول إلى الخلايا في ورقة العمل. تستخدم هذه المقالة أحد هذه الطرق لإضافة أنواع مختلفة من البيانات إلى الخلايا.

{{% /alert %}}

##  **كيفية إضافة البيانات إلى Cells**

 Aspose.Cells يوفر فئة،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يحتوي الفصل على أ[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) المجموعة التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فصل. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) يوفر الفصل أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. كل عنصر في[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) تمثل المجموعة كائنًا من[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)فصل.

 Aspose.Cells يسمح للمطورين بإضافة بيانات إلى الخلايا في أوراق العمل عن طريق استدعاء[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)فصل'[**ضع القيمة**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) طريقة. Aspose.Cells يوفر إصدارات مثقلة من[**ضع القيمة**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) طريقة تتيح للمطورين إضافة أنواع مختلفة من البيانات إلى الخلايا. باستخدام هذه الإصدارات المحملة بشكل زائد من[**ضع القيمة**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)الطريقة، من الممكن إضافة قيم منطقية، أو سلسلة، أو مزدوجة، أو عدد صحيح، أو تاريخ/وقت، وما إلى ذلك إلى الخلية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

##  **كيفية تحسين الكفاءة**

 إذا كنت تستخدم[**ضع القيمة**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)لإضافة كمية كبيرة من البيانات إلى ورقة العمل، يجب عليك إضافة قيم إلى الخلايا، أولاً حسب الصفوف ثم حسب الأعمدة. يعمل هذا الأسلوب على تحسين كفاءة تطبيقاتك بشكل كبير.

##  **كيفية استرجاع البيانات من Cells**

 Aspose.Cells يوفر فئة،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) الذي يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يحتوي الفصل على أ[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) المجموعة التي تسمح بالوصول إلى أوراق العمل الموجودة في الملف. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فصل. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) يوفر الفصل أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. كل عنصر في[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) تمثل المجموعة كائنًا من[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)فصل.

 ال[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)يوفر class العديد من الخصائص التي تسمح للمطورين باسترداد القيم من الخلايا وفقًا لأنواع البيانات الخاصة بهم. تشمل هذه الخصائص:

- [**قيمة السلسلة**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue): تقوم بإرجاع قيمة السلسلة للخلية.
- [**قيمة مزدوجة**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue): إرجاع القيمة المزدوجة للخلية.
- [**قيمة منطقية**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue): إرجاع القيمة المنطقية للخلية.
- [**قيمة التاريخ والوقت**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue): إرجاع قيمة التاريخ/الوقت للخلية.
- [**القيمة العائمة**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): إرجاع القيمة العائمة للخلية.
- [**قيمة دولية**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue): إرجاع القيمة الصحيحة للخلية.

 عندما لا يتم ملء الحقل، يتم استخدام الخلايا[**قيمة مزدوجة**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue) أو[**القيمة العائمة**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue)يلقي استثناء.

 يمكن أيضًا التحقق من نوع البيانات الموجودة في الخلية باستخدام[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)فصل'[**يكتب**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) ملكية. في الواقع، فإن[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)فصل'[**يكتب**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) الملكية مبنية على[**CellValueType**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype)التعداد الذي تم إدراج قيمه المحددة مسبقًا أدناه:

|**Cell أنواع القيمة**|**وصف**|
| :- | :- |
|IsBool|يحدد أن قيمة الخلية هي منطقية.|
|IsDateTime|يحدد أن قيمة الخلية هي التاريخ/الوقت.|
|باطل|يمثل خلية فارغة.|
|IsNumeric|يحدد أن قيمة الخلية رقمية.|
|IsString|يحدد أن قيمة الخلية هي سلسلة.|
|غير معروف|يحدد أن قيمة الخلية غير معروفة.|

يمكنك أيضًا استخدام أنواع قيم الخلايا المحددة مسبقًا أعلاه للمقارنة مع نوع البيانات الموجودة في كل خلية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

أثناء العمل على أوراق العمل، يمكن للمستخدمين إضافة أنواع مختلفة من البيانات في الخلايا. قد تتضمن أنواع البيانات هذه قيمًا منطقية، أو عددًا صحيحًا، أو نقطة عائمة، أو نصًا، أو قيمًا للتاريخ/الوقت. مع Aspose.Cells يمكنك الحصول على القيم المناسبة من الخلايا حسب أنواع البيانات الخاصة بها.

{{% /alert %}}

##  **مواضيع متقدمة**
- [الوصول إلى Cells من ورقة العمل](/cells/ar/net/accessing-cells-of-a-worksheet/)
- [تحويل البيانات الرقمية النصية إلى رقم](/cells/ar/net/convert-text-numeric-data-to-number/)
- [إنشاء الإجماليات الفرعية](/cells/ar/net/creating-subtotals/)
- [تصفية البيانات](/cells/ar/net/data-filtering/)
- [فرز البيانات](/cells/ar/net/sort-data-of-excel/)
- [تأكيد صحة البيانات](/cells/ar/net/data-validation/)
- [تصدير البيانات من ورقة العمل](/cells/ar/net/export-data-from-worksheet/)
- [البحث عن البيانات أو البحث عنها](/cells/ar/net/find-or-search-data/)
- [احصل على قيمة سلسلة Cell مع التنسيق وبدونه](/cells/ar/net/get-cell-string-value-with-and-without-formatting/)
- [إضافة HTML نص منسق داخل Cell](/cells/ar/net/adding-html-rich-text-inside-the-cell/)
- [إدراج الارتباطات التشعبية في Excel أو OpenOffice](/cells/ar/net/insert-hyperlinks-to-excel/)
- [استيراد البيانات إلى ورقة العمل](/cells/ar/net/import-data-into-worksheet/)
- [كيف وأين يتم استخدام العدادين](/cells/ar/net/how-and-where-to-use-enumerators/)
- [قم بقياس العرض والارتفاع لقيمة Cell بوحدة البكسل](/cells/ar/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [قراءة Cell القيم في مواضيع متعددة في وقت واحد](/cells/ar/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [التحويل بين اسم الخلية وفهرس الصف/العمود](/cells/ar/net/names-and-indices/)
- [تعبئة البيانات أولاً حسب الصف ثم حسب العمود](/cells/ar/net/populate-data-first-by-row-then-by-column/)
- [احتفظ ببادئة الاقتباس المفردة ذات القيمة أو النطاق Cell](/cells/ar/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [الوصول إلى أجزاء النص المنسق لـ Cell وتحديثها](/cells/ar/net/access-and-update-the-portions-of-rich-text-of-cell/)



