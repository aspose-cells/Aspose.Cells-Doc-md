---
title: إنشاء الوصول ونسخ نطاقات الأسماء
type: docs
weight: 200
url: /ar/net/create-access-and-copy-named-ranges/
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

## **العمل مع نطاق مسمى باستخدام Aspose.Cells**

هنا، نستخدم واجهة برمجة التطبيقات Aspose.Cells للقيام بالمهمة.
توفر Aspose.Cells فئةً تمثل ملف Microsoft Excel، وتحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. ورقة العمل تمثل بواسطة فئة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells).

### **إنشاء نطاق مسمى**

من الممكن إنشاء نطاق مسمى عن طريق استدعاء [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) الزائدة من مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). إصدار نموذجي لـ [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) يأخذ المعلمات التالية:

- اسم الخلية العلوية اليسرى، اسم الخلية العلوية اليسرى في النطاق.
- اسم الخلية السفلي الأيمن، اسم الخلية السفلي الأيمن في النطاق.

عند استدعاء [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3)، فإنه يُرجع نطاق المصنوع حديثًا كنموذج من فئة [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range). استخدم هذا [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) لتكوين النطاق المسمى. على سبيل المثال، قم بتعيين اسم النطاق باستخدام خاصية [**Name**](https://reference.aspose.com/cells/net/aspose.cells/range/properties/name). يوضح المثال التالي كيفية إنشاء نطاق مسمّى للخلايا التي تمتد عبر B4:G14.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CreateNamedRangeofCells-1.cs" >}}

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-InputDataInCellsInRange-1.cs" >}}

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IdentifyCellsinNamedRange-1.cs" >}}

### **الوصول إلى المدى المسمى**

#### **الوصول إلى نطاق مسمى محدد**

استدعاء [**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) الكائن [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) الميثود للحصول على مدى بالاسم المحدد. تأخذ الميثود النموذجية [**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) الاسم للمدى المسمى وتعيد المدى المحدد كمثيل لفئة [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range). يوضح المثال التالي كيفية الوصول إلى مدى محدد بالاسم.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessSpecificNamedRange-1.cs" >}}

#### **الوصول إلى كافة المدى المسمى في ورقة العمل**

استدعاء [**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) الكائن [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) الميثود للحصول على كافة المدى المسمى في ورقة العمل. تعيد الميثود [**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) مصفوفة تحتوي على كل المدى المسمى في [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) المجموعة.

يوضح المثال التالي كيفية الوصول إلى جميع النطاقات المسماة في ورق عمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessAllNamedRanges-1.cs" >}}

### **نسخ المدى المسمى**

توفر Aspose.Cells [**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index) الميثود لنسخ مدى من الخلايا مع التنسيق في مدى آخر.

المثال التالي يوضح كيفية نسخ مدى مصدر من الخلايا إلى مدى مسمى آخر.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CopyNamedRanges-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
