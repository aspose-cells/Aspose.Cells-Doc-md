---
title: إضافة واسترداد البيانات
type: docs
weight: 20
url: /ar/cpp/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 في[الوصول إلى Cells من ورقة العمل](/cells/ar/cpp/accessing-cells-of-a-worksheet/)، ناقشنا الأساليب الأساسية للوصول إلى الخلايا في ورقة العمل. تستخدم هذه المقالة أحد هذه الأساليب لإضافة أنواع مختلفة من البيانات إلى الخلايا.

{{% /alert %}} 
## **إضافة البيانات إلى Cells**
 Aspose.Cells يوفر فئة[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) يمثل ملف Excel Microsoft. ال[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) فئة تحتوي على[أوراق العمل](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) صف دراسي. ال[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) فئة توفر[آيسيلس](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) مجموعة. كل عنصر في[آيسيلس](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) تمثل المجموعة كائنًا من[آيسيل](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)صف دراسي.

Aspose.Cells يسمح للمطورين بإضافة بيانات إلى الخلايا في أوراق العمل عن طريق استدعاء[آيسيل](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) صف دراسي[ضع القيمة](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9) طريقة. يوفر Aspose.Cells إصدارات محملة بشكل زائد من[ضع القيمة](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9) طريقة تتيح للمطورين إضافة أنواع مختلفة من البيانات إلى الخلايا. استخدام هذه الإصدارات المحملة بشكل زائد من[ضع القيمة](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)طريقة ، من الممكن إضافة قيم منطقية أو سلسلة أو مزدوجة أو عدد صحيح أو تاريخ / وقت ، إلخ إلى الخلية.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells.cpp" >}}
### **تحسين الكفاءة**
 كما ترى[ضع القيمة](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)طريقة لوضع كمية كبيرة من البيانات في ورقة عمل ، يجب إضافة قيم إلى الخلايا ، أولاً بالصفوف ثم بالأعمدة. يعمل هذا الأسلوب على تحسين كفاءة تطبيقاتك بشكل كبير.
## **استرجاع البيانات من Cells**
 Aspose.Cells يوفر فئة[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) يمثل ملف Excel Microsoft. ال[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) فئة تحتوي على[أوراق العمل](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) مجموعة تسمح بالوصول إلى أوراق العمل الموجودة في الملف. يتم تمثيل ورقة العمل بواسطة[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) صف دراسي. ال[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) فئة توفر أ[آيسيلس](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) مجموعة. كل عنصر في[آيسيلس](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) تمثل المجموعة كائنًا من[آيسيل](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)صف دراسي.

 ال[آيسيل](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)يوفر class عدة طرق تسمح للمطورين باسترداد القيم من الخلايا وفقًا لأنواع بياناتهم. تشمل هذه الطرق:

- [GetStringValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac048c664985e2cadc2404840599d7ac3)، تُرجع قيمة سلسلة الخلية.
- [GetDoubleValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a5f21cd4c755da84135176c74425f230a)، ترجع القيمة المزدوجة للخلية.
- [GetBoolValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac61870c4b1d6a68077092fb043bf8741)، ترجع القيمة المنطقية للخلية.
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7932b40c41141f716b096cc521113a61)، تُرجع قيمة التاريخ / الوقت للخلية.
- [GetFloatValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4e36c4be4c76447f54f8032b17cecf44)، ترجع القيمة العائمة للخلية.
- [GetIntValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7acc93c97c062cbd60a7f1ab00a022d8)، تُرجع قيمة العدد الصحيح للخلية.

 عندما لا يتم ملء أحد الحقول ، فإن الخلايا ذات[GetDoubleValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a5f21cd4c755da84135176c74425f230a) أو[GetFloatValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4e36c4be4c76447f54f8032b17cecf44)يرمي استثناء.

 يمكن أيضًا التحقق من نوع البيانات الموجودة في خلية باستخدام[آيسيل](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) صف دراسي[GetType](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a36708b1bad0bbf45cbf9577ccab101ba) طريقة. في الواقع، فإن[آيسيل](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) صف دراسي[GetType](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a36708b1bad0bbf45cbf9577ccab101ba) الطريقة على أساس[CellValueType](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a745bf00b4815ec8dcf1bd11922fa4b62)التعداد الذي تم سرد قيمه المحددة مسبقًا أدناه:

|**Cell أنواع القيمة**|**وصف**|
|:- |:- |
|CellValueType_IsBool|تحدد أن قيمة الخلية منطقية.|
|CellValueType_IsDateTime|يحدد أن قيمة الخلية هي التاريخ / الوقت.|
|CellValueType_IsNull|يمثل خلية فارغة.|
|CellValueType_IsNumeric|تحدد أن قيمة الخلية رقمية.|
|CellValueType_IsString|تحدد أن قيمة الخلية عبارة عن سلسلة.|
|CellValueType_IsUnknown|يحدد أن قيمة الخلية غير معروفة.|
يمكنك أيضًا استخدام أنواع قيم الخلايا المحددة مسبقًا للمقارنة مع نوع البيانات الموجودة في كل خلية.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells.cpp" >}}
