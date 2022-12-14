---
title: إضافة واسترداد البيانات
type: docs
weight: 20
url: /ar/java/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 في[الوصول إلى Cells من ورقة العمل](/cells/ar/java/accessing-cells-of-a-worksheet/)، ناقشنا الأساليب الأساسية للوصول إلى الخلايا في ورقة العمل. تستخدم هذه المقالة أحد هذه الأساليب لإضافة أنواع مختلفة من البيانات إلى الخلايا.

{{% /alert %}} 
## **إضافة البيانات إلى Cells**
 Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)، يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) فئة تحتوي على[ورقة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) صف دراسي. ال[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) فئة توفر أ[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) مجموعة. كل عنصر في[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) تمثل المجموعة كائنًا من[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)صف دراسي.

 Aspose.Cells يسمح للمطورين بإضافة البيانات إلى الخلايا في أوراق العمل عن طريق استدعاء[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) صف دراسي'[setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)منشأه. باستخدام ملف[setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)الخاصية ، من الممكن إضافة قيم منطقية ، أو سلسلة ، أو مزدوجة ، أو عدد صحيح أو تاريخ / وقت ، وما إلى ذلك إلى الخلية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingDataToCells-AddingDataToCells.java" >}}
### **تحسين الكفاءة**
{{% alert color="primary" %}} 

 إذا كنت تستخدم ملف[setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)لإضافة كمية كبيرة من البيانات إلى ورقة عمل ، يجب إضافة قيم إلى الخلايا ، أولاً بالصفوف ثم حسب الأعمدة. يعمل هذا الأسلوب على تحسين كفاءة تطبيقاتك بشكل كبير.

{{% /alert %}} 

أثناء العمل على أوراق العمل ، يمكن للمستخدمين إضافة أنواع مختلفة من البيانات في الخلايا. قد تتضمن عناصر البيانات هذه قيمًا منطقية أو عددًا صحيحًا أو فاصلة عائمة أو نصية أو قيمًا للتاريخ / الوقت. يمكنك الحصول على القيم المناسبة من الخلايا وفقًا لأنواع البيانات الخاصة بها باستخدام Aspose.Cells.
## **استرجاع البيانات من Cells**
 Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) يمثل ملف Excel.[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) فئة تحتوي على[ورقة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)صف دراسي. ال[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) فئة توفر أ[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) مجموعة. كل عنصر في[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)تمثل المجموعة كائنًا من[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)صف دراسي.

 ال[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)يوفر class العديد من الخصائص التي تسمح للمطورين باسترداد القيم من الخلايا وفقًا لأنواع البيانات الخاصة بهم. تشمل هذه الخصائص:

- [قيمة السلسلة](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue)، قيمة سلسلة الخلية.
- [ضعف القيمة](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DoubleValue)، تُرجع القيمة المزدوجة للخلية.
- [قيمة منطقية](https://reference.aspose.com/cells/java/com.aspose.cells/cell#BoolValue)، القيمة المنطقية للخلية.
- [DateTimeValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DateTimeValue)، قيمة التاريخ / الوقت للخلية.
- [FloatValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FloatValue)، القيمة العائمة للخلية.
- [IntValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#IntValue)، قيمة العدد الصحيح للخلية.

 علاوة على ذلك ، يمكن أيضًا التحقق من نوع البيانات الموجودة في الخلية باستخدام[يكتب](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) ممتلكات[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) صف دراسي. في الواقع، فإن[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) صف دراسي'[يكتب](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) الممتلكات على أساس[CellValueType](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueType)التعداد الذي تم سرد قيمه المحددة مسبقًا أدناه:

|**Cell أنواع القيمة**|**وصف**|
|:- |:- |
|[IS_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_BOOL)|تحدد أن قيمة الخلية منطقية.|
|[هو_تاريخ_زمن](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_DATE_TIME)|يحدد أن قيمة الخلية هي التاريخ / الوقت.|
|[IS_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_ERROR)|يمثل أن الخلية تحتوي على قيمة خطأ|
|[باطل](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NULL)|يمثل خلية فارغة.|
|[IS_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NUMERIC)|يحدد أن قيمة الخلية رقمية.|
|[IS_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_STRING)|تحدد أن قيمة الخلية عبارة عن سلسلة.|
|[غير معروف](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_UNKNOWN)|يحدد أن قيمة الخلية غير معروفة.|
يمكنك أيضًا استخدام أنواع قيم الخلايا المحددة مسبقًا للمقارنة بنوع البيانات الموجودة في كل خلية.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RetrievingDataFromCells-RetrievingDataFromCells.java" >}}
