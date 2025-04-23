---
title: إضافة واسترداد البيانات
type: docs
weight: 20
url: /ar/java/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

في [الوصول إلى الخلايا لورقة العمل](/cells/ar/java/accessing-cells-of-a-worksheet/) ، تمت مناقشة الطرق الأساسية للوصول إلى الخلايا في ورقة العمل. يستخدم هذا المقال إحدى تلك الطرق لإضافة أنواع مختلفة من البيانات إلى الخلايا.

{{% /alert %}} 
## **إضافة بيانات إلى الخلايا**
توفر Aspose.Cells فئة تمثل ملف Microsoft Excel تسمى [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). تحتوي فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) على [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة عمل بفئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). توفر فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). يمثل كل عنصر في مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) كائنًا من فئة [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

تسمح Aspose.Cells للمطورين بإضافة البيانات إلى الخلايا في ورقات العمل عن طريق استدعاء [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) و [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value). باستخدام خاصية [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) ، يمكن إضافة قيم مثل قيم Boolean و string و double و integer أو date/time وغيرها إلى الخلية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingDataToCells-AddingDataToCells.java" >}}
### **تحسين الكفاءة**
{{% alert color="primary" %}} 

إذا كنت تستخدم خاصية [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) لإضافة كمية كبيرة من البيانات إلى ورقة عمل ، فيجب عليك إضافة القيم إلى الخلايا أولاً حسب الصفوف ومن ثم حسب الأعمدة. يحسن هذا النهج كفاءة التطبيقات بشكل كبير.

{{% /alert %}} 

أثناء العمل على ورقات العمل ، قد يقوم المستخدمون بإضافة أنواع مختلفة من البيانات في الخلايا. قد تتضمن هذه العناصر البيانية قيمًا منطقية وصحيحة وقيمًا صحيحة ، نصية أو تاريخ/وقت. يمكنك الحصول على القيم المناسبة من الخلايا وفقًا لأنواع بياناتها باستخدام Aspose.Cells.
## **استرداد البيانات من الخلايا**
توفر Aspose.Cells فئة تمثل ملف Excel تسمى [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) التي تحتوي على مجموعة [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة عمل بفئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). توفر فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). يمثل كل عنصر في مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) كائنًا من فئة [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

توفر الفئة [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) العديد من الخصائص التي تسمح للمطورين باسترداد القيم من الخلايا وفقًا لأنواع بياناتها. تشمل هذه الخصائص:

- [StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue)، قيمة السلسلة في الخلية.
- [DoubleValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DoubleValue)، تعيد قيمة الرقم العشري في الخلية.
- [BoolValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#BoolValue)، قيمة بيانية في الخلية.
- [DateTimeValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DateTimeValue)، قيمة الوقت/التاريخ في الخلية.
- [FloatValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FloatValue)، قيمة عائمة في الخلية.
- [IntValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#IntValue)، قيمة العدد الصحيح للخلية.

وبالإضافة إلى ذلك، يمكن التحقق أيضًا من نوع البيانات الواردة في الخلية باستخدام خاصية [Type](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) لفئة [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell). في الواقع، تعتمد خاصية [Type](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) لفئة [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) على تعداد [CellValueType](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueType) والتي تحتوي على القيم المحددة مُسبقًا على النحو الوارد أدناه:

|**أنواع قيم الخلية**|**الوصف**|
| :- | :- |
|[IS_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS-BOOL)| يحدد أن قيمة الخلية بوليانية.|
|[IS_DATE_TIME](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS-DATE-TIME)| يحدد أن قيمة الخلية تاريخ/وقت.|
|[IS_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS-ERROR)| يمثل أن الخلية تحتوي على قيمة خطأ|
|[IS_NULL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS-NULL)| يمثل خلية فارغة.|
|[IS_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS-NUMERIC)| يحدد أن قيمة الخلية رقمية.|
|[IS_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS-STRING)| يحدد أن قيمة الخلية سلسلة.|
|[IS_UNKNOWN](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS-UNKNOWN)| يحدد أن قيمة الخلية غير معروفة.|
يمكنك أيضًا استخدام أنواع قيم الخلية المُحددة مُسبقًا أعلاه للمقارنة مع نوع البيانات الموجودة في كل خلية. 



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RetrievingDataFromCells-RetrievingDataFromCells.java" >}}
{{< app/cells/assistant language="java" >}}
