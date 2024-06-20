---
title: إنشاء الوصول ونسخ نطاقات الأسماء
type: docs
weight: 200
url: /ar/python-net/create-access-and-copy-named-ranges/
description: يوضح هذا المقال كيفية إنشاء ونسخ النطاقات بأسماء في الوصول باستخدام واجهة برمجة تطبيقات Aspose.Cells for Python via .NET.
keywords: مكتبة Python Excel، Python Create Access and Copy Named Ranges، Python Create Named Ranges، Python Copy Named Ranges، وصول Python إلى جميع النطاقات المعتمدة في جدول بيانات.
---

## **مقدمة**

عادةً، يتم استخدام تسميات العمود والصف للإشارة إلى الخلايا الفردية. يُمكن إنشاء أسماء وصفية لتمثيل الخلايا، ونطاقات الخلايا، والصيغ، أو القيم الثابتة. يمكن أن يشير مصطلح **الاسم** إلى سلسلة من الأحرف التي تمثل خليةً، أو نطاقًا من الخلايا، أو صيغةً، أو قيمة ثابتة. إذا كانت لديك نطاقًا من الخلايا يمكن الإشارة إليه بواسطة اسمه. استخدم أسماء سهلة الفهم، مثل المنتجات، للإشارة إلى نطاقات صعبة الفهم، مثل المبيعات!C20:C30. يمكن استخدام التسميات في الصيغ التي تشير إلى بيانات في نفس ورقة العمل؛ إذا كنت ترغب في تمثيل نطاق على ورقة عمل أخرى، فيمكنك استخدام اسمًا. *النطاقات المسماة تعد من بين أقوى ميزات Microsoft Excel، خاصةً عند استخدامها كنطاق مصدر لعناصر التحكم في القوائم، الجداول المحورية، الرسوم البيانية، وما إلى ذلك.

## **العمل مع النطاق المسمى باستخدام Microsoft Excel**

### **إنشاء نطاقات مسماة**

توضح الخطوات التالية كيفية تسمية خلية أو نطاق خلايا باستخدام **MS Excel**. ينطبق هذا الأسلوب على **Microsoft Office Excel 2003**، **Microsoft Excel 97**، **2000**، و **2002**.

1. حدد الخلية أو نطاق الخلايا الذي تريد تسميته.
2. انقر على **مربع الاسم** في الطرف الأيسر من شريط الصيغة.
1. اكتب اسم الخلايا.
1. اضغط على ENTER.

{{% alert color="primary" %}}

لا يمكنك تسمية خلية أثناء تغيير محتويات الخلية.

{{% /alert %}}

## **العمل مع النطاقات المسماة باستخدام Aspose.Cells for Python Excel Library**

هنا، نستخدم واجهة برمجة تطبيقات Aspose.Cells for Python via .NET لأداء المهمة.
Aspose.Cells for Python via .NET يوفر فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) التي تمثل ملف Excel من مايكروسوفت. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. ورقة عمل ممثلة بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) توفر مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)

### **إنشاء نطاق مسمى**

من الممكن إنشاء نطاق مسمى عن طريق استدعاء [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str) الزائدة من مجموعة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). إصدار نموذجي لـ [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str) يأخذ المعلمات التالية:

- اسم الخلية العلوية اليسرى، اسم الخلية العلوية اليسرى في النطاق.
- اسم الخلية السفلي الأيمن، اسم الخلية السفلي الأيمن في النطاق.

عند استدعاء [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str)، فإنه يُرجع نطاق المصنوع حديثًا كنموذج من فئة [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range). استخدم هذا [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) لتكوين النطاق المسمى. على سبيل المثال، قم بتعيين اسم النطاق باستخدام خاصية [**name**](https://reference.aspose.com/cells/python-net/aspose.cells/range/name). يوضح المثال التالي كيفية إنشاء نطاق مسمّى للخلايا التي تمتد عبر B4:G14.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-CreateNamedRangeofCells-1.py" >}}

### **إدخال البيانات في الخلايا في النطاق المسمى**

يمكنك إدخال البيانات في الخلايا الفردية لنطاق وفق النمط

- **C#**: Range[row,column]
- **VB**: Range(row,column)

على سبيل المثال، لديك مجموعة مسماة من الخلايا التي تمتد بين A1:C4. تجعل المصفوفة 4 * 3 = 12 خلية. تتم ترتيب الخلايا الفردية في النطاق بشكل تسلسلي: Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].

استخدم الخصائص التالية لتحديد الخلايا في المدى:

- FirstRow يعيد فهرس الصف الأول في المدى المسمى.
- FirstColumn يعيد فهرس العمود الأول في المدى المسمى.
- RowCount يعيد العدد الكلي للصفوف في المدى المسمى.
- ColumnCount يعيد العدد الكلي للأعمدة في المدى المسمى.

يظهر المثال التالي كيفية إدخال بعض القيم في الخلايا لنطاق معين.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-InputDataInCellsInRange-1.py" >}}

### **تحديد الخلايا في النطاق المسمى**

يمكنك إدراج البيانات في الخلايا الفردية في المجموعة وفق النمط التالي:

- **C#**: Range[row,column]
- **VB**: Range(row,column)

إذا كان لديك مدى يحمل اسم يمتد من A1:C4. المصفوفة تجعل 4 * 3 = 12 خلية. ترتب الخلايا في المدى الفردي بشكل متسلسل: Range[0,0], Range[0,1], Range[0,2], Range[1,0] ,Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].

استخدم الخصائص التالية لتحديد الخلايا في المدى:

- FirstRow يعيد فهرس الصف الأول في المدى المسمى.
- FirstColumn يعيد فهرس العمود الأول في المدى المسمى.
- RowCount يعيد العدد الكلي للصفوف في المدى المسمى.
- ColumnCount يعيد العدد الكلي للأعمدة في المدى المسمى.

يظهر المثال التالي كيفية إدخال بعض القيم في الخلايا لنطاق معين.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-IdentifyCellsinNamedRange-1.py" >}}

### **الوصول إلى المدى المسمى**

#### **الوصول إلى نطاق مسمى محدد**

استدعاء [**get_range_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_range_by_name/#str) الكائن [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) الميثود للحصول على مدى بالاسم المحدد. تأخذ الميثود النموذجية [**get_range_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_range_by_name/#str) الاسم للمدى المسمى وتعيد المدى المحدد كمثيل لفئة [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range). يوضح المثال التالي كيفية الوصول إلى مدى محدد بالاسم.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-AccessSpecificNamedRange-1.py" >}}

#### **الوصول إلى كافة المدى المسمى في ورقة العمل**

استدعاء [**get_named_ranges**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_named_ranges/#) الكائن [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) الميثود للحصول على كافة المدى المسمى في ورقة العمل. تعيد الميثود [**get_named_ranges**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_named_ranges/#) مصفوفة تحتوي على كل المدى المسمى في [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) المجموعة.

يوضح المثال التالي كيفية الوصول إلى جميع النطاقات المسماة في ورق عمل.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-AccessAllNamedRanges-1.py" >}}

### **نسخ المدى المسمى**

توفر Aspose.Cells for Python via .NET طريقة [**Range.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range) لنسخ مجموعة من الخلايا مع التنسيق إلى نطاق آخر.

المثال التالي يوضح كيفية نسخ مدى مصدر من الخلايا إلى مدى مسمى آخر.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-CopyNamedRanges-1.py" >}}
