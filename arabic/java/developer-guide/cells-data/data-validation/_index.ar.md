---
title: تأكيد صحة البيانات
type: docs
weight: 70
url: /ar/java/data-validation/
---
{{% alert color="primary" %}} 

يوفر Microsoft Excel بعض الميزات الجيدة للتصفية التلقائية أو التحقق من صحة بيانات ورقة العمل.

[تأكيد صحة البيانات](/cells/ar/java/data-validation/) هي القدرة على تعيين القواعد المتعلقة بالبيانات المدخلة في ورقة العمل. على سبيل المثال ، استخدم التحقق من الصحة للتأكد من أن العمود المسمى DATE يحتوي على تواريخ فقط ، أو أن عمودًا آخر يحتوي على أرقام فقط. يمكنك حتى التأكد من أن العمود المسمى DATE يحتوي فقط على تواريخ ضمن نطاق معين. باستخدام التحقق من صحة البيانات ، يمكنك التحكم في ما يتم إدخاله في الخلايا في ورقة العمل. Aspose.Cells يدعم Microsoft بشكل كامل ميزات التحقق من صحة البيانات والتصفية التلقائية في Excel. تشرح هذه المقالة كيفية استخدام الميزات الموجودة في Microsoft Excel ، وكيفية ترميزها باستخدام Aspose.Cells.

{{% /alert %}} 
## **أنواع التحقق من صحة البيانات وتنفيذها**
Microsoft يدعم Excel عددًا من الأنواع المختلفة للتحقق من صحة البيانات. يتم استخدام كل نوع للتحكم في نوع البيانات التي يتم إدخالها في خلية أو نطاق خلية. أدناه ، توضح مقتطفات التعليمات البرمجية كيفية التحقق من صحة ذلك:

- [الأعداد كاملة](/cells/ar/java/data-validation/)، أي أنه ليس لديهم جزء عشري.
- [الأعداد العشرية تتبع الهيكل الصحيح](/cells/ar/java/data-validation/). يحدد مثال الكود أن نطاق الخلايا يجب أن يحتوي على مسافتين عشريتين.
- [القيم مقيدة بقائمة من القيم](/cells/ar/java/data-validation/). يعرّف التحقق من صحة القائمة قائمة منفصلة من القيم التي يمكن تطبيقها على خلية أو نطاق خلية.
- [التواريخ تقع ضمن نطاق معين](/cells/ar/java/data-validation/).
- [الوقت ضمن نطاق معين](/cells/ar/java/data-validation/).
- [النص ضمن طول حرف معين](/cells/ar/java/data-validation/).
### **التحقق من صحة البيانات باستخدام Excel Microsoft**
لإنشاء عمليات التحقق باستخدام Microsoft Excel:

1. في ورقة العمل ، حدد الخلايا التي تريد تطبيق التحقق من الصحة عليها.
1. من**بيانات**القائمة ، حدد**تصديق**.
 يتم عرض مربع حوار التحقق.
1. انقر على**إعدادات**علامة التبويب وأدخل الإعدادات كما هو موضح أدناه.

   **إعدادات التحقق من صحة البيانات** 

![ما يجب القيام به: image_بديل_نص](data-validation_1.png)
### **التحقق من صحة البيانات مع Aspose.Cells**
يعد التحقق من صحة البيانات ميزة قوية للتحقق من صحة المعلومات التي تم إدخالها في أوراق العمل. من خلال التحقق من صحة البيانات ، يمكن للمطورين تزويد المستخدمين بقائمة من الاختيارات ، وتقييد إدخالات البيانات على نوع أو حجم معين ، وما إلى ذلك.
 في Aspose.Cells ، كل منهما[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)فئة لديها[عمليات التحقق](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Validations)الذي يمثل مجموعة من[تصديق](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)أشياء. لإعداد التحقق من الصحة ، قم بتعيين بعض ملفات[تصديق](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)خصائص الفئة:

- [يكتب](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Type): يمثل نوع التحقق ، والذي يمكن تحديده باستخدام إحدى القيم المحددة مسبقًا في ملف[نوع التحقق](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)تعداد.
- [المشغل أو العامل](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Operator): يمثل عامل التشغيل الذي سيتم استخدامه في التحقق ، والذي يمكن تحديده باستخدام إحدى القيم المحددة مسبقًا في[نوع المشغل](https://reference.aspose.com/cells/java/com.aspose.cells/OperatorType)تعداد.
- [فورمولا 1](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula1): يمثل القيمة أو التعبير المرتبط بالجزء الأول من التحقق من صحة البيانات.
- [الصيغة 2](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula2): يمثل القيمة أو التعبير المرتبط بالجزء الثاني من التحقق من صحة البيانات.

عندما[تصديق](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)تم تكوين خصائص الكائن ، يمكن للمطورين استخدام[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)بنية لتخزين معلومات حول نطاق الخلايا التي سيتم التحقق من صحتها باستخدام التحقق الذي تم إنشاؤه.
#### **أنواع التحقق من صحة البيانات**
يسمح لك التحقق من صحة البيانات بإنشاء قواعد عمل في كل خلية بحيث ينتج عن الإدخالات غير الصحيحة رسائل خطأ. قواعد العمل هي السياسات والإجراءات التي تحكم كيفية عمل الشركة. Aspose.Cells يدعم كافة الأنواع الهامة للتحقق من صحة البيانات.

ال[نوع التحقق](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)يتألف التعداد من الأعضاء التالية أسماؤهم:

|**اسم عضو**|**وصف**|
|:- |:- |
|[اي قيمة](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#ANY_VALUE)|تشير إلى قيمة من أي نوع.|
|[الرقم كاملا](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)|تشير إلى نوع التحقق من صحة الأعداد الصحيحة.|
|[عدد عشري](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DECIMAL)|تشير إلى نوع التحقق من صحة الأرقام العشرية.|
|[قائمة](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#LIST)|تشير إلى نوع التحقق من القائمة المنسدلة.|
|[تاريخ](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DATE)|تشير إلى نوع التحقق من صحة التواريخ.|
|[زمن](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TIME)|تشير إلى نوع التحقق من صحة الوقت.|
|[TEXT_LENGTH](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TEXT_LENGTH)|تشير إلى نوع التحقق من طول النص.|
|[العادة](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#CUSTOM)|تشير إلى نوع التحقق المخصص.|
#### **عينة البرمجة: التحقق من صحة بيانات العدد الكامل**
باستخدام هذا النوع من التحقق ، يمكن للمستخدمين إدخال أرقام كاملة فقط ضمن نطاق محدد في الخلايا التي تم التحقق من صحتها. توضح أمثلة التعليمات البرمجية التالية كيفية تنفيذ[الرقم كاملا](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)نوع التحقق. يقوم المثال بإنشاء نفس التحقق من صحة البيانات باستخدام Aspose.Cells الذي أنشأناه باستخدام Microsoft Excel أعلاه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WholeNumberDataValidation-WholeNumberDataValidation.java" >}}



#### **عينة البرمجة: التحقق من صحة البيانات العشرية**
باستخدام هذا النوع من التحقق ، يمكن للمستخدم إدخال أرقام عشرية في الخلايا التي تم التحقق من صحتها. في المثال ، تم تقييد المستخدم لإدخال قيمة عشرية فقط ومنطقة التحقق من الصحة هي A1: A10.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DecimalDataValidation-DecimalDataValidation.java" >}}



#### **عينة البرمجة: قائمة التحقق من البيانات**
يسمح هذا النوع من التحقق من الصحة للمستخدم بإدخال القيم من القائمة المنسدلة. يوفر قائمة: سلسلة من الصفوف التي تحتوي على بيانات. يمكن للمستخدمين تحديد القيم فقط من القائمة. منطقة التحقق من الصحة هي نطاق الخلايا A1: A5 في ورقة العمل الأولى.

من المهم هنا أن تقوم بتعيين ملف[Validation.setInCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) الملكية ل**حقيقي**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ListDataValidation-ListDataValidation.java" >}}



#### **عينة البرمجة: التحقق من صحة بيانات التاريخ**
باستخدام هذا النوع من التحقق ، يقوم المستخدمون بإدخال قيم التاريخ ضمن نطاق محدد ، أو تلبية معايير محددة ، في الخلايا التي تم التحقق من صحتها. في المثال ، تم تقييد المستخدم لإدخال التواريخ بين 1970 و 1999. هنا ، منطقة التحقق من الصحة هي خلية B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DateDataValidation-DateDataValidation.java" >}}



#### **نماذج البرمجة: التحقق من بيانات الوقت**
باستخدام هذا النوع من التحقق ، يمكن للمستخدمين إدخال أوقات ضمن نطاق محدد ، أو تلبية بعض المعايير ، في الخلايا التي تم التحقق من صحتها. في هذا المثال ، تم تقييد المستخدم على إدخال الأوقات بين 09:00 إلى 11:30 صباحًا. هنا ، منطقة التحقق هي خلية B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TimeDataValidation-TimeDataValidation.java" >}}



#### **نماذج البرمجة: التحقق من صحة بيانات طول النص**
باستخدام هذا النوع من التحقق ، يمكن للمستخدمين إدخال قيم نصية بطول محدد في الخلايا التي تم التحقق من صحتها. في المثال ، تم تقييد المستخدم لإدخال قيم سلسلة لا تزيد عن 5 أحرف. منطقة التحقق من الصحة هي خلية B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextLengthDataValidation-TextLengthDataValidation.java" >}}
## **قواعد التحقق من صحة البيانات**
عند تنفيذ عمليات التحقق من صحة البيانات ، يمكن التحقق من التحقق من خلال تعيين قيم مختلفة في الخلايا.[Cell.GetValidationValue ()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue\(\)) لجلب نتيجة التحقق من الصحة. يوضح المثال التالي هذه الميزة بقيم مختلفة. يمكن تنزيل نموذج الملف من الرابط التالي للاختبار:

[SampleDataValidationRules.xlsx](77987849.xlsx)

**عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-VerifyCellValueSatisfiesDataValidationRules-1.java" >}}
## **تحقق مما إذا كان التحقق من الصحة في خلية قائمة منسدلة**
 كما رأينا ، هناك العديد من أنواع عمليات التحقق التي يمكن تنفيذها داخل الخلية. إذا كنت تريد التحقق مما إذا كانت عملية التحقق من الصحة قائمة منسدلة أم لا ،[التحقق من الصحة](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) يمكن استخدام الخاصية لاختبار هذا. يوضح نموذج التعليمات البرمجية التالي استخدام هذه الخاصية. يمكن تنزيل نموذج ملف الاختبار من الرابط التالي:

[sampleDataValidationRules.xlsx](77987849.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-CheckIfValidationInCellDropDown-1.java" >}}
## **إضافة CellArea إلى التحقق الموجود**
قد تكون هناك حالات قد ترغب في إضافتها[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)على القائمة[تصديق](https://reference.aspose.com/cells/java/com.aspose.cells/Validation). عندما تضيف[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)استخدام[Validation.AddArea (CellArea cellArea)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea\)) ، Aspose.Cells يتحقق من كافة المناطق الموجودة لمعرفة ما إذا كانت المنطقة الجديدة موجودة بالفعل. إذا كان الملف يحتوي على عدد كبير من عمليات التحقق من الصحة ، فسيأخذ هذا نجاحًا في الأداء. للتغلب على هذا ، يوفر API[Validation.AddAreaCellArea cellArea، bool checkIntersection، bool checkEdge) التحقق من صحة إضافة منطقة خلية منطقة ، فحص منطقي](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) طريقة. ال*تحقق من التقاطع*تشير المعلمة إلى ما إذا كان سيتم التحقق من تقاطع منطقة معينة مع مناطق التحقق الموجودة. ضبطه على**خاطئة**سيعطل فحص مناطق أخرى. ال*checkEdge*تشير المعلمة إلى ما إذا كان سيتم التحقق من المناطق المطبقة. إذا أصبحت المنطقة الجديدة هي المنطقة العلوية اليسرى ، فسيتم إعادة إنشاء الإعدادات الداخلية. إذا كنت متأكدًا من أن المنطقة الجديدة ليست المنطقة العلوية اليسرى ، فيمكنك تعيين هذا المعامل كـ**خاطئة**.

يوضح مقتطف الشفرة التالي استخدام ملف[Validation.AddAreaCellArea cellArea، bool checkIntersection، bool checkEdge) التحقق من صحة إضافة منطقة خلية منطقة ، فحص منطقي](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) طريقة إضافة جديد[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)على القائمة[تصديق](https://reference.aspose.com/cells/java/com.aspose.cells/Validation).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-AddValidationArea-1.java" >}}

يتم إرفاق ملفات إكسل المصدر والمخرجات كمرجع.

[مصدر الملف](PivotTableHideAndSortSample.xlsx)

[ملف إلاخراج](ValidationsSample_out.xlsx)


## **موضوعات مسبقة**
- [احصل على Cell التحقق من الصحة في ملفات ODS](/cells/ar/java/get-cell-validation-in-ods-files/)
- [احصل على تطبيق التحقق من الصحة على Cell](/cells/ar/java/get-validation-applied-on-a-cell/)
- [تحقق من أن Cell القيمة تلبي قواعد التحقق من صحة البيانات](/cells/ar/java/verify-that-cell-value-satisfies-data-validation-rules/)
