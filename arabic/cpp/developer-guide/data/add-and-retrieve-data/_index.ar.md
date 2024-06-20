---
title: إضافة واسترداد البيانات
type: docs
weight: 20
url: /ar/cpp/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

في [الوصول إلى الخلايا في ورقة العمل](/cells/ar/cpp/accessing-cells-of-a-worksheet/)، تمت مناقشة النهج الأساسي للوصول إلى الخلايا في ورقة عمل. تستخدم هذه المقالة أحد تلك النهج لإضافة أنواع مختلفة من البيانات إلى الخلايا.

{{% /alert %}} 
## **إضافة بيانات إلى الخلايا**
توفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) التي تسمح بالوصول إلى كل ورقة في ملف Excel. يتم تمثيل ورقة عمل بفئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). توفر فئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). يُمثل كل عنصر في مجموعة [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) كائن من فئة [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

تسمح Aspose.Cells للمطورين بإضافة بيانات إلى الخلايا في ورق العمل عن طريق استدعاء فئة [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) وطريقة [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/). توفر Aspose.Cells نسخًا متعددة من طريقة [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) تتيح للمطورين إضافة أنواع مختلفة من البيانات إلى الخلايا. باستخدام هذه النسخ المتعددة من طريقة [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)، يُمكن إضافة قيم بوليانية، نصية، عددية، صحيحة أو تاريخ/وقت، إلخ للخلية.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells-new.cpp" >}}
### **تحسين الكفاءة**
إذا كنت تستخدم طريقة [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) لوضع كمية كبيرة من البيانات في ورقة عمل، يجب عليك إضافة القيم إلى الخلايا أولاً حسب الصفوف، ثم حسب الأعمدة. يحسن هذا النهج كفاءة تطبيقاتك بشكل كبير.
## **استرداد البيانات من الخلايا**
توفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) التي تسمح بالوصول إلى ورق العمل في الملف. تمثل ورقة عمل بفئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). توفر فئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). كل عنصر في مجموعة [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) يُمثل كائنًا من فئة [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

توفر فئة [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) عدة طرق تسمح للمطورين باسترجاع القيم من الخلايا وفقًا لأنواع بياناتها. تشمل هذه الطرق:

- [GetStringValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/)، تُرجع قيمة السلسلة للخلية.
- [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/)، تُرجع القيمة العددية للخلية.
- [GetBoolValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/)، يعيد قيمة البيان البوليانية للخلية.
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/)، يعيد قيمة التاريخ/الوقت للخلية.
- [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/)، يعيد قيمة العدد العائم للخلية.
- [GetIntValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/)، يعيد قيمة العدد الصحيح للخلية.

عندما لا يتم ملؤها، تقوم الخلايا برمي استثناء عند استخدام [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) أو [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/).

يمكن أيضًا التحقق من نوع البيانات الواردة في الخلية باستخدام فئة [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) وطريقة [GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/). في الواقع، تعتمد طريقة [GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) لفئة [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) على تعداد [CellValueType](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/) التي قيمها المعرفة مسبقا كما هو مدرج أدناه:

|**أنواع قيم الخلية**|**الوصف**|
| :- | :- |
|CellValueType_IsBool|يحدد أن قيمة الخلية هي منطقية.
|CellValueType_IsDateTime|يحدد أن قيمة الخلية هي تاريخ/وقت.
|CellValueType_IsNull|يمثل خلية فارغة.
|CellValueType_IsNumeric|يحدد أن قيمة الخلية هي رقمية.
|CellValueType_IsString|يحدد أن قيمة الخلية هي سلسلة.
|CellValueType_IsUnknown|يحدد أن قيمة الخلية مجهولة.
يمكنك أيضًا استخدام أنواع قيم الخلية المعرفة مسبقًا أعلاه للمقارنة مع نوع البيانات الموجودة في كل خلية.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells-new.cpp" >}}
