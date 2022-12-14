---
title: تأكيد صحة البيانات
type: docs
weight: 90
url: /ar/net/data-validation/
---
{{% alert color="primary" %}}

يوفر Microsoft Excel بعض الميزات الجيدة للتصفية التلقائية أو التحقق من صحة بيانات ورقة العمل. يدعم Aspose.Cells بشكل كامل التحقق من صحة بيانات Excel وميزات التصفية التلقائية. تشرح هذه المقالة كيفية استخدام الميزات الموجودة في Microsoft Excel ، وكيفية ترميزها باستخدام Aspose.Cells.

{{% /alert %}}

## **أنواع التحقق من صحة البيانات وتنفيذها**

التحقق من صحة البيانات هو القدرة على تعيين القواعد المتعلقة بالبيانات المدخلة في ورقة العمل. على سبيل المثال ، استخدم التحقق من الصحة للتأكد من أن العمود المسمى DATE يحتوي على تواريخ فقط ، أو أن عمودًا آخر يحتوي على أرقام فقط. يمكنك حتى التأكد من أن العمود المسمى DATE يحتوي فقط على تواريخ ضمن نطاق معين. باستخدام التحقق من صحة البيانات ، يمكنك التحكم في ما يتم إدخاله في الخلايا في ورقة العمل.

Microsoft يدعم Excel عددًا من الأنواع المختلفة للتحقق من صحة البيانات. يتم استخدام كل نوع للتحكم في نوع البيانات التي يتم إدخالها في خلية أو نطاق خلية. أدناه ، توضح مقتطفات التعليمات البرمجية كيفية التحقق من صحة ذلك:

- الأعداد صحيحة ، أي أنها لا تحتوي على جزء عشري.
- الأعداد العشرية تتبع الهيكل الصحيح. يحدد مثال الكود أن نطاق الخلايا يجب أن يحتوي على مسافتين عشريتين.
- القيم مقيدة بقائمة من القيم. يعرّف التحقق من صحة القائمة قائمة منفصلة من القيم التي يمكن تطبيقها على خلية أو نطاق خلية.
- التواريخ تقع ضمن نطاق معين.
- الوقت ضمن نطاق معين.
- النص ضمن طول حرف معين.

### **التحقق من صحة البيانات باستخدام Excel Microsoft**

لإنشاء عمليات التحقق باستخدام Microsoft Excel:

1. في ورقة العمل ، حدد الخلايا التي تريد تطبيق التحقق من الصحة عليها.
1.  من**بيانات** القائمة ، حدد**تصديق**. سيتم عرض مربع حوار التحقق.
1.  انقر على**إعدادات** علامة التبويب وأدخل الإعدادات.

### **التحقق من صحة البيانات مع Aspose.Cells**

يعد التحقق من صحة البيانات ميزة قوية للتحقق من صحة المعلومات التي تم إدخالها في أوراق العمل. من خلال التحقق من صحة البيانات ، يمكن للمطورين تزويد المستخدمين بقائمة من الاختيارات ، وتقييد إدخالات البيانات على نوع أو حجم معين ، وما إلى ذلك.
 في Aspose.Cells ، كل منهما[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة لديها[**عمليات التحقق**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/validations)الخاصية التي تمثل مجموعة من[**تصديق**](https://reference.aspose.com/cells/net/aspose.cells/validation) أشياء. لإعداد التحقق من الصحة ، قم بتعيين بعض ملفات[**تصديق**](https://reference.aspose.com/cells/net/aspose.cells/validation)خصائص الفئة على النحو التالي:

- النوع - يمثل نوع التحقق ، والذي يمكن تحديده باستخدام إحدى القيم المحددة مسبقًا في ملف[**نوع التحقق**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)تعداد.
-  عامل التشغيل - يمثل العامل الذي سيتم استخدامه في التحقق ، والذي يمكن تحديده باستخدام إحدى القيم المحددة مسبقًا في[**نوع المشغل**](https://reference.aspose.com/cells/net/aspose.cells/operatortype)تعداد.
- الصيغة 1 - تمثل القيمة أو التعبير المرتبط بالجزء الأول من التحقق من صحة البيانات.
- الصيغة 2 - تمثل القيمة أو التعبير المرتبط بالجزء الثاني من التحقق من صحة البيانات.

 عندما[**تصديق**](https://reference.aspose.com/cells/net/aspose.cells/validation) تم تكوين خصائص الكائن ، يمكن للمطورين استخدام[**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)بنية لتخزين معلومات حول نطاق الخلايا التي سيتم التحقق من صحتها باستخدام التحقق الذي تم إنشاؤه.

#### **أنواع التحقق من صحة البيانات**

 ال[**نوع التحقق**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)يتألف التعداد من الأعضاء التالية أسماؤهم:

|**اسم عضو**|**وصف**|
|:- |:- |
|اي قيمة|تشير إلى قيمة من أي نوع.|
|الرقم كاملا|تشير إلى نوع التحقق من صحة الأعداد الصحيحة.|
|عدد عشري|تشير إلى نوع التحقق من صحة الأرقام العشرية.|
|قائمة|تشير إلى نوع التحقق من القائمة المنسدلة.|
|تاريخ|تشير إلى نوع التحقق من صحة التواريخ.|
|زمن|تشير إلى نوع التحقق من الوقت.|
|TextLength|تشير إلى نوع التحقق من طول النص.|
|العادة|تشير إلى نوع التحقق المخصص.|

##### **التحقق من صحة بيانات العدد الكامل**

باستخدام هذا النوع من التحقق ، يمكن للمستخدمين إدخال أرقام كاملة فقط ضمن نطاق محدد في الخلايا التي تم التحقق من صحتها. توضح أمثلة التعليمات البرمجية التالية كيفية تنفيذ نوع التحقق من WholeNumber. يقوم المثال بإنشاء نفس التحقق من صحة البيانات باستخدام Aspose.Cells الذي أنشأناه باستخدام Microsoft Excel أعلاه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-WholeNumberDataValidation-1.cs" >}}

##### **قائمة التحقق من صحة البيانات**

يسمح هذا النوع من التحقق من الصحة للمستخدم بإدخال القيم من القائمة المنسدلة. يوفر قائمة: سلسلة من الصفوف التي تحتوي على بيانات. في المثال ، تتم إضافة ورقة عمل ثانية لتحتوي على مصدر القائمة. يمكن للمستخدمين تحديد القيم فقط من القائمة. منطقة التحقق من الصحة هي نطاق الخلايا A1: A5 في ورقة العمل الأولى.

 من المهم هنا أن تقوم بتعيين ملف[**التحقق من الصحة**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown) الملكية ل**حقيقي**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-ListDataValidation-1.cs" >}}

##### **تاريخ التحقق من صحة البيانات**

باستخدام هذا النوع من التحقق ، يقوم المستخدمون بإدخال قيم التاريخ ضمن نطاق محدد ، أو تلبية معايير محددة ، في الخلايا التي تم التحقق من صحتها. في المثال ، تم تقييد المستخدم لإدخال التواريخ بين 1970 و 1999. هنا ، منطقة التحقق من الصحة هي خلية B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-DateDataValidation-1.cs" >}}

##### **التحقق من صحة بيانات الوقت**

باستخدام هذا النوع من التحقق ، يمكن للمستخدمين إدخال أوقات ضمن نطاق محدد ، أو تلبية بعض المعايير ، في الخلايا التي تم التحقق من صحتها. في هذا المثال ، تم تقييد المستخدم على إدخال الأوقات بين 09:00 إلى 11:30 صباحًا. هنا ، منطقة التحقق هي خلية B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TimeDataValidation-1.cs" >}}

##### **التحقق من صحة بيانات طول النص**

باستخدام هذا النوع من التحقق ، يمكن للمستخدمين إدخال قيم نصية بطول محدد في الخلايا التي تم التحقق من صحتها. في المثال ، تم تقييد المستخدم لإدخال قيم سلسلة لا تزيد عن 5 أحرف. منطقة التحقق من الصحة هي خلية B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TextLengthDataValidation-1.cs" >}}

### **قواعد التحقق من صحة البيانات**

عند تنفيذ عمليات التحقق من صحة البيانات ، يمكن التحقق من التحقق من خلال تعيين قيم مختلفة في الخلايا.[**Cell.GetValidationValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) يمكن استخدامها لجلب نتيجة التحقق من الصحة. يوضح المثال التالي هذه الميزة بقيم مختلفة. يمكن تنزيل نموذج الملف من الرابط التالي للاختبار:

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}

## **تحقق مما إذا كانت عملية التحقق من الصحة في الخلية قائمة منسدلة**

 كما رأينا ، هناك العديد من أنواع عمليات التحقق التي يمكن تنفيذها داخل الخلية. إذا كنت تريد التحقق مما إذا كانت عملية التحقق من الصحة قائمة منسدلة أم لا ،[**التحقق من الصحة**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown) يمكن استخدام الخاصية لاختبار هذا. يوضح نموذج التعليمات البرمجية التالي استخدام هذه الخاصية. يمكن تنزيل ملف نموذج للاختبار من الرابط التالي:

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckIfValidationInCellDropDown-1.cs" >}}

## **إضافة CellArea إلى التحقق الموجود**

 قد تكون هناك حالات قد ترغب في إضافتها[**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)إلى القائمة[**تصديق**](https://reference.aspose.com/cells/net/aspose.cells/validation). عندما تضيف[**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) استخدام[**Validation.AddArea (CellArea cellArea)**](https://reference.aspose.com/cells/net/aspose.cells/validation/methods/addarea)، Aspose.Cells يتحقق من كل المناطق الموجودة لمعرفة ما إذا كانت المنطقة الجديدة موجودة بالفعل. إذا كان الملف يحتوي على عدد كبير من عمليات التحقق من الصحة ، فسيأخذ هذا نجاحًا في الأداء. للتغلب على هذا ، يوفر API[**Validation.AddAreaCellArea cellArea، bool checkIntersection، bool checkEdge) التحقق من صحة إضافة منطقة خلية منطقة ، فحص منطقي**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) طريقة. ال*تحقق من التقاطع* تشير المعلمة إلى ما إذا كان سيتم التحقق من تقاطع منطقة معينة مع مناطق التحقق الموجودة. ضبطه على**خاطئة** سيعطل فحص مناطق أخرى. ال*checkEdge* تشير المعلمة إلى ما إذا كان سيتم التحقق من المناطق المطبقة. إذا أصبحت المنطقة الجديدة هي المنطقة العلوية اليسرى ، فسيتم إعادة إنشاء الإعدادات الداخلية. إذا كنت متأكدًا من أن المنطقة الجديدة ليست المنطقة العلوية اليسرى ، فيمكنك تعيين هذا المعامل كـ**خاطئة**.

يوضح مقتطف الشفرة التالي استخدام ملف[**Validation.AddAreaCellArea cellArea، bool checkIntersection، bool checkEdge) التحقق من صحة إضافة منطقة خلية منطقة ، فحص منطقي**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) طريقة لإضافة جديد[**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)إلى القائمة[**تصديق**](https://reference.aspose.com/cells/net/aspose.cells/validation).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddValidationArea-1.cs" >}}

يتم إرفاق ملفات إكسل المصدر والمخرجات كمرجع.

[مصدر الملف](96928093.xlsx)

[ملف إلاخراج](96928220.xlsx)


## **موضوعات مسبقة**
- [احصل على Cell التحقق من الصحة في ملفات ODS](/cells/ar/net/get-cell-validation-in-ods-files/)
- [احصل على تطبيق التحقق من الصحة على Cell](/cells/ar/net/get-validation-applied-on-a-cell/)
- [تحقق من أن Cell القيمة تلبي قواعد التحقق من صحة البيانات](/cells/ar/net/verify-that-cell-value-satisfies-data-validation-rules/)
