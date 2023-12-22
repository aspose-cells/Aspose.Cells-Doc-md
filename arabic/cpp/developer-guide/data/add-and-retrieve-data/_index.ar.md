---
title: إضافة واسترجاع البيانات
type: docs
weight: 20
url: /ar/cpp/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 في[الوصول إلى Cells من ورقة العمل](/cells/ar/cpp/accessing-cells-of-a-worksheet/)ناقشنا الأساليب الأساسية للوصول إلى الخلايا في ورقة العمل. تستخدم هذه المقالة أحد هذه الطرق لإضافة أنواع مختلفة من البيانات إلى الخلايا.

{{% /alert %}} 
##  **إضافة البيانات إلى Cells**
 Aspose.Cells يوفر فئة[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) الذي يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) يحتوي الفصل على[أوراق عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) المجموعة التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) فصل. ال[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) يوفر الفصل[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) مجموعة. كل عنصر في[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) تمثل المجموعة كائنًا من[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)فصل.

 Aspose.Cells يسمح للمطورين بإضافة بيانات إلى الخلايا في أوراق العمل عن طريق استدعاء[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) فصل[ضع القيمة](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) طريقة. Aspose.Cells يوفر إصدارات مثقلة من[ضع القيمة](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) طريقة تتيح للمطورين إضافة أنواع مختلفة من البيانات إلى الخلايا. باستخدام هذه الإصدارات المحملة بشكل زائد من[ضع القيمة](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)الطريقة، من الممكن إضافة قيم منطقية، أو سلسلة، أو مزدوجة، أو عدد صحيح، أو تاريخ/وقت، وما إلى ذلك إلى الخلية.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells-new.cpp" >}}
###  **تحسين الكفاءة**
 إذا كنت تستخدم[ضع القيمة](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)لوضع كمية كبيرة من البيانات في ورقة العمل، يجب عليك إضافة قيم إلى الخلايا، أولاً حسب الصفوف ثم حسب الأعمدة. يعمل هذا الأسلوب على تحسين كفاءة تطبيقاتك بشكل كبير.
##  **استرجاع البيانات من Cells**
 Aspose.Cells يوفر فئة[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) الذي يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) يحتوي الفصل على[أوراق عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) المجموعة التي تسمح بالوصول إلى أوراق العمل الموجودة في الملف. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) فصل. ال[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) يوفر الفصل أ[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) مجموعة. كل عنصر في[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) تمثل المجموعة كائنًا من[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)فصل.

 ال[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)يوفر class عدة طرق تسمح للمطورين باسترداد القيم من الخلايا وفقًا لأنواع البيانات الخاصة بهم. وتشمل هذه الأساليب:

- [GetStringValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/)، تقوم بإرجاع قيمة السلسلة للخلية.
- [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/)، تقوم بإرجاع القيمة المزدوجة للخلية.
- [GetBoolValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/)، تقوم بإرجاع القيمة المنطقية للخلية.
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/)، تقوم بإرجاع قيمة التاريخ/الوقت للخلية.
- [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/)، تقوم بإرجاع القيمة العائمة للخلية.
- [GetIntValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/)، تقوم بإرجاع القيمة الصحيحة للخلية.

 عندما لا يتم ملء الحقل، يتم استخدام الخلايا[GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) أو[GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/)يلقي استثناء.

 يمكن أيضًا التحقق من نوع البيانات الموجودة في الخلية باستخدام[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) فصل[GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) طريقة. في الواقع، فإن[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) فصل[GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) تعتمد الطريقة على[CellValueType](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/)التعداد الذي تم إدراج قيمه المحددة مسبقًا أدناه:

|**Cell أنواع القيمة**|**وصف**|
| :- | :- |
|CellValueType_IsBool|يحدد أن قيمة الخلية هي منطقية.|
|CellValueType_IsDateTime|يحدد أن قيمة الخلية هي التاريخ/الوقت.|
|CellValueType_IsNull|يمثل خلية فارغة.|
|CellValueType_IsNumeric|يحدد أن قيمة الخلية رقمية.|
|CellValueType_IsString|يحدد أن قيمة الخلية هي سلسلة.|
|CellValueType_IsUnknown|يحدد أن قيمة الخلية غير معروفة.|
يمكنك أيضًا استخدام أنواع قيم الخلايا المحددة مسبقًا أعلاه للمقارنة مع نوع البيانات الموجودة في كل خلية.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells-new.cpp" >}}
