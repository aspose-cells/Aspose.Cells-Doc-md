---
title: تأكيد صحة البيانات
type: docs
weight: 90
url: /ar/net/data-validation/
description: تعرف على كيفية إضافة التحقق من صحة البيانات من خلال Aspose.Cells for .NET API.
keywords: Add Data Validation, Get Validation Value, Add Whole Number Data Validation, Add List Data Validation, Add Date Data Validation, Add Time Data Validation, Add Text Length Data Validation, Add CellArea to existing Validation, Check if validation in cell is dropdown, Add Custom Valication  
---
{{% alert color="primary" %}}

Microsoft يوفر Excel بعض الميزات الجيدة للتصفية التلقائية أو التحقق من صحة بيانات ورقة العمل. Aspose.Cells يدعم بشكل كامل Microsoft ميزات التحقق من صحة البيانات والتصفية التلقائية في Excel. تشرح هذه المقالة كيفية استخدام الميزات الموجودة في Microsoft Excel، وكيفية ترميزها باستخدام Aspose.Cells.

{{% /alert %}}

##  **أنواع التحقق من صحة البيانات وتنفيذها**

التحقق من صحة البيانات هو القدرة على وضع القواعد المتعلقة بالبيانات المدخلة في ورقة العمل. على سبيل المثال، استخدم التحقق من الصحة للتأكد من أن العمود المسمى DATE يحتوي على تواريخ فقط، أو أن عمود آخر يحتوي على أرقام فقط. يمكنك أيضًا التأكد من أن العمود المسمى DATE يحتوي فقط على تواريخ ضمن نطاق معين. باستخدام التحقق من صحة البيانات، يمكنك التحكم في ما يتم إدخاله في الخلايا في ورقة العمل.

Microsoft يدعم Excel عددًا من الأنواع المختلفة للتحقق من صحة البيانات. يتم استخدام كل نوع للتحكم في نوع البيانات التي يتم إدخالها في الخلية أو نطاق الخلايا. توضح مقتطفات التعليمات البرمجية أدناه كيفية التحقق من صحة ذلك:

- Numbers كاملة، أي أنها لا تحتوي على جزء عشري.
- تتبع الأرقام العشرية البنية الصحيحة. يحدد مثال التعليمات البرمجية أن نطاق الخلايا يجب أن يحتوي على مسافتين عشريتين.
- تقتصر القيم على قائمة القيم. يحدد التحقق من صحة القائمة قائمة منفصلة من القيم التي يمكن تطبيقها على خلية أو نطاق خلايا.
- التواريخ تقع ضمن نطاق معين.
- الوقت يقع ضمن نطاق معين.
- النص ضمن طول حرف معين.

###  **التحقق من صحة البيانات مع Microsoft إكسل**

لإنشاء عمليات التحقق من الصحة باستخدام Microsoft Excel:

1. في ورقة العمل، حدد الخلايا التي تريد تطبيق التحقق من الصحة عليها.
1.  من**بيانات** من القائمة، حدد *التحقق من الصحة**. سيتم عرض مربع حوار التحقق من الصحة.
1.  انقر على**إعدادات** علامة التبويب وأدخل الإعدادات.

###  **التحقق من صحة البيانات مع Aspose.Cells**

يعد التحقق من صحة البيانات ميزة قوية للتحقق من صحة المعلومات المدخلة في أوراق العمل. من خلال التحقق من صحة البيانات، يمكن للمطورين تزويد المستخدمين بقائمة من الاختيارات، وتقييد إدخالات البيانات بنوع أو حجم معين، وما إلى ذلك.
 في Aspose.Cells لكل[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)فئة لديها[**التحقق من الصحة**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/validations) الممتلكات التي تمثل مجموعة من[**تصديق**](https://reference.aspose.com/cells/net/aspose.cells/validation) أشياء. لإعداد التحقق من الصحة، قم بتعيين بعض[**تصديق**](https://reference.aspose.com/cells/net/aspose.cells/validation)خصائص الفئة على النحو التالي:

- النوع - يمثل نوع التحقق من الصحة، والذي يمكن تحديده باستخدام إحدى القيم المحددة مسبقًا في ملف[**نوع التحقق**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)تعداد.
-  عامل التشغيل - يمثل عامل التشغيل الذي سيتم استخدامه في التحقق من الصحة، والذي يمكن تحديده باستخدام إحدى القيم المحددة مسبقًا في[**نوع المشغل**](https://reference.aspose.com/cells/net/aspose.cells/operatortype)تعداد.
- الصيغة 1 - تمثل القيمة أو التعبير المرتبط بالجزء الأول من التحقق من صحة البيانات.
- Formula2 - تمثل القيمة أو التعبير المرتبط بالجزء الثاني من التحقق من صحة البيانات.

 عندما[**تصديق**](https://reference.aspose.com/cells/net/aspose.cells/validation) تم تكوين خصائص الكائن، ويمكن للمطورين استخدام[**منطقة الخلية**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)بنية لتخزين المعلومات حول نطاق الخلايا الذي سيتم التحقق من صحته باستخدام التحقق الذي تم إنشاؤه.

####  **أنواع التحقق من صحة البيانات**

 ال[**نوع التحقق**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)يحتوي التعداد على الأعضاء التاليين:

|**اسم عضو**|**وصف**|
| :- | :- |
|اي قيمة|يدل على قيمة من أي نوع.|
|الرقم كاملا|يشير إلى نوع التحقق من صحة الأعداد الصحيحة.|
|عدد عشري|يشير إلى نوع التحقق من الصحة للأرقام العشرية.|
|قائمة|يشير إلى نوع التحقق من الصحة للقائمة المنسدلة.|
|تاريخ|يشير إلى نوع التحقق من صحة التواريخ.|
|وقت|يشير إلى نوع التحقق من الوقت.|
|طول النص|يشير إلى نوع التحقق من صحة طول النص.|
|مخصص|يشير إلى نوع التحقق المخصص.|

#####  **التحقق من صحة بيانات العدد الكامل**

باستخدام هذا النوع من التحقق من الصحة، يمكن للمستخدمين إدخال أرقام صحيحة فقط ضمن نطاق محدد في الخلايا التي تم التحقق من صحتها. توضح أمثلة التعليمات البرمجية التالية كيفية تطبيق نوع التحقق من صحة WholeNumber. يقوم المثال بإنشاء نفس التحقق من صحة البيانات باستخدام Aspose.Cells الذي أنشأناه باستخدام Microsoft Excel أعلاه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-WholeNumberDataValidation-1.cs" >}}

#####  **قائمة التحقق من صحة البيانات**

يسمح هذا النوع من التحقق للمستخدم بإدخال القيم من القائمة المنسدلة. يوفر قائمة: سلسلة من الصفوف التي تحتوي على بيانات. في المثال، تتم إضافة ورقة عمل ثانية للاحتفاظ بمصدر القائمة. يمكن للمستخدمين فقط تحديد القيم من القائمة. منطقة التحقق من الصحة هي نطاق الخلايا A1:A5 في ورقة العمل الأولى.

 ومن المهم هنا أن تقوم بتعيين[**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown)الخاصية إلى *صحيح**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-ListDataValidation-1.cs" >}}

#####  **التحقق من صحة بيانات التاريخ**

باستخدام هذا النوع من التحقق من الصحة، يقوم المستخدمون بإدخال قيم التاريخ ضمن نطاق محدد، أو تلبية معايير محددة، في الخلايا التي تم التحقق من صحتها. في المثال، يقتصر على المستخدم إدخال التواريخ بين 1970 إلى 1999. هنا، منطقة التحقق من الصحة هي الخلية B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-DateDataValidation-1.cs" >}}

#####  **التحقق من صحة بيانات الوقت**

باستخدام هذا النوع من التحقق من الصحة، يمكن للمستخدمين إدخال الأوقات ضمن نطاق محدد، أو تلبية بعض المعايير، في الخلايا التي تم التحقق من صحتها. في المثال، يقتصر على المستخدم إدخال الأوقات بين 09:00 إلى 11:30 صباحًا. منطقة التحقق هنا هي الخلية B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TimeDataValidation-1.cs" >}}

#####  **التحقق من صحة بيانات طول النص**

باستخدام هذا النوع من التحقق من الصحة، يمكن للمستخدمين إدخال قيم نصية بطول محدد في الخلايا التي تم التحقق من صحتها. في المثال، يقتصر على المستخدم إدخال قيم سلسلة لا تزيد عن 5 أحرف. منطقة التحقق هي الخلية B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TextLengthDataValidation-1.cs" >}}

###  **قواعد التحقق من صحة البيانات**

 عند تنفيذ عمليات التحقق من صحة البيانات، يمكن التحقق من التحقق من الصحة عن طريق تعيين قيم مختلفة في الخلايا.[**Cell.GetValidationValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) يمكن استخدامها لجلب نتيجة التحقق من الصحة. يوضح المثال التالي هذه الميزة بقيم مختلفة. يمكن تنزيل ملف العينة من الرابط التالي للاختبار:

[SampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}

##  **تحقق مما إذا كان التحقق من الصحة في الخلية هو القائمة المنسدلة**

 كما رأينا، هناك العديد من أنواع عمليات التحقق التي يمكن تنفيذها داخل الخلية. إذا كنت تريد التحقق مما إذا كان التحقق من الصحة مدرجًا في القائمة المنسدلة أم لا،[**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown)يمكن استخدام الخاصية لاختبار ذلك. يوضح نموذج التعليمات البرمجية التالي استخدام هذه الخاصية. يمكن تحميل ملف عينة للاختبار من الرابط التالي:

[SampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckIfValidationInCellDropDown-1.cs" >}}

##  **أضف CellArea إلى التحقق من الصحة الموجود**

 قد تكون هناك حالات قد ترغب في إضافتها[**منطقة الخلية**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)إلى القائمة[**تصديق**](https://reference.aspose.com/cells/net/aspose.cells/validation). عندما تضيف[**منطقة الخلية**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) استخدام[**التحقق من الصحة.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/net/aspose.cells/validation/methods/addarea)، Aspose.Cells يقوم بفحص جميع المناطق الموجودة لمعرفة ما إذا كانت المنطقة الجديدة موجودة بالفعل. إذا كان الملف يحتوي على عدد كبير من عمليات التحقق من الصحة، فإن هذا يتطلب نتيجة أداء. للتغلب على هذا، يوفر API[**Validation.AddAreaCellArea cellArea، bool checkIntersection، bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) طريقة. ال*checkIntersection* تشير المعلمة إلى ما إذا كان سيتم التحقق من تقاطع منطقة معينة مع مناطق التحقق الموجودة. ضبطه على**خطأ شنيع** سيتم تعطيل فحص المناطق الأخرى. ال*com.checkEdge*تشير المعلمة إلى ما إذا كان سيتم التحقق من المناطق المطبقة. إذا أصبحت المنطقة الجديدة هي المنطقة العلوية اليسرى، فسيتم إعادة بناء الإعدادات الداخلية. إذا كنت متأكدًا من أن المنطقة الجديدة ليست المنطقة العلوية اليسرى، فيمكنك تعيين هذه المعلمة على أنها *خطأ**.

يوضح مقتطف التعليمات البرمجية التالي استخدام[**Validation.AddAreaCellArea cellArea، bool checkIntersection، bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) طريقة اضافة جديد[**منطقة الخلية**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)إلى القائمة[**تصديق**](https://reference.aspose.com/cells/net/aspose.cells/validation).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddValidationArea-1.cs" >}}

يتم إرفاق ملفات Excel المصدر والإخراج كمرجع.

[مصدر الملف](96928093.xlsx)

[ملف إلاخراج](96928220.xlsx)


##  **مواضيع متقدمة**
- [احصل على التحقق من صحة Cell في ملفات ODS](/cells/ar/net/get-cell-validation-in-ods-files/)
- [احصل على تطبيق التحقق من الصحة على Cell](/cells/ar/net/get-validation-applied-on-a-cell/)
- [تحقق من أن القيمة Cell تفي بقواعد التحقق من صحة البيانات](/cells/ar/net/verify-that-cell-value-satisfies-data-validation-rules/)
