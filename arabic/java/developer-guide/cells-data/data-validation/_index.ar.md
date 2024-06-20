---
title: التحقق من البيانات
type: docs
weight: 70
url: /ar/java/data-validation/
---

{{% alert color="primary" %}} 

توفر Microsoft Excel بعض الميزات الجيدة لتصفية البيانات تلقائيًا أو التحقق من صحة بيانات ورقة العمل.

[التحقق من البيانات](/cells/ar/java/data-validation/) هو القدرة على تحديد قواعد تتعلق بالبيانات المدخلة في ورقة العمل. على سبيل المثال، يمكنك استخدام التحقق لضمان أن العمود المسمى DATE يحتوي فقط على تواريخ، أو أن عمودًا آخر يحتوي فقط على أرقام. يمكنك حتى التأكد من أن العمود المسمى DATE يحتوي فقط على تواريخ ضمن نطاق معين. باستخدام التحقق من البيانات، يمكنك التحكم في ما يتم إدخاله في الخلايا في ورقة العمل. تدعم Aspose.Cells بشكل كامل التحقق من البيانات وميزات التصفية التلقائية في Microsoft Excel. يشرح هذا المقال كيفية استخدام الميزات في Microsoft Excel، وكيفية تغذية برمجتها باستخدام Aspose.Cells.

{{% /alert %}} 
## **أنواع التحقق من البيانات والتنفيذ**
يدعم Microsoft Excel عددًا من أنواع التحقق المختلفة للبيانات. يُستخدم كل نوع للتحكم في نوع البيانات التي تُدخل إلى خلية أو نطاق الخلايا. أدناه، مقتطفات الكود توضح كيفية التحقق من:

- [الأرقام هي أعداد صحيحة](/cells/ar/java/data-validation/)، وهذا يعني أنها لا تحتوي على جزء عشري.
- [الأرقام العشرية تتبع الهيكل الصحيح](/cells/ar/java/data-validation/). يعرف مثال الكود أن يتم تعيين مجموعة من الخلايا بأن يكون لديها عدد محدد من الأماكن العشرية.
- [القيم مقيدة بقائمة من القيم](/cells/ar/java/data-validation/). يعرف التحقق المشترك قائمة منفصلة من القيم يمكن تطبيقها على خلية أو مجموعة خلايا.
- [التواريخ تقع ضمن نطاق محدد](/cells/ar/java/data-validation/).
- [الوقت ضمن نطاق محدد](/cells/ar/java/data-validation/).
- [النص النصي ضمن طول محدد](/cells/ar/java/data-validation/).
### **التحقق من البيانات مع Microsoft Excel**
لإنشاء التحققات باستخدام Microsoft Excel:

1. في ورقة العمل، حدد الخلايا التي ترغب في تطبيق التحقق عليها.
1. من قائمة **البيانات**، حدد **التحقق**.
   يتم عرض مربع الحوار للتحقق.
1. انقر على علامة التبويب **الإعدادات** وأدخل الإعدادات كما هو موضح أدناه. 

   **إعدادات التحقق من البيانات** 

![todo:image_alt_text](data-validation_1.png)
### **التحقق من البيانات بواسطة Aspose.Cells**
التحقق من البيانات هو ميزة قوية للتحقق من المعلومات المُدخلة في أوراق العمل. باستخدام التحقق من البيانات، يمكن للمطورين توفير للمستخدمين قائمة من الخيارات، وتقييد إدخالات البيانات إلى نوع معين أو حجم، الخ.
في Aspose.Cells، كل [نموذج البيانات](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) يحتوي على كائن [التحقق](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#التحقق) الذي يمثل مجموعة من أثبات صحة [التحقق](https://reference.aspose.com/cells/java/com.aspose.cells/Validation). لتعيين التحقق، قم بتعيين بعض خصائص [التحقق](https://reference.aspose.com/cells/java/com.aspose.cells/Validation) الصنف:

- [النوع](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Type): يمثل نوع التحقق، والذي يمكن تحديده باستخدام أحد قيم محددة في تعداد [نوع التحقق](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType).
- [المشغل](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Operator): يمثل المشغل الذي يجب استخدامه في التحقق، والذي يمكن تحديده باستخدام أحد القيم المحددة في تعداد [نوع المشغل](https://reference.aspose.com/cells/java/com.aspose.cells/OperatorType).
- [الصيغة1](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula1): تمثل القيمة أو التعبير المرتبط بالجزء الأول من التحقق من البيانات.
- [الصيغة2](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula2): تمثل القيمة أو التعبير المرتبط بالجزء الثاني من التحقق من البيانات.

عند تكوين خصائص كائن التحقق، يمكن للمطورين استخدام هيكل مجال الخلية لتخزين المعلومات حول نطاق الخلية الذي سيتم التحقق منه باستخدام عملية التحقق التي تم إنشاؤها.
#### **أنواع التحقق من البيانات**
يتيح التحقق من البيانات بناء قواعد الأعمال في كل خلية بحيث تؤدي الإدخالات غير الصحيحة إلى رسائل خطأ. قواعد الأعمال هي السياسات والإجراءات التي تحكم كيفية عمل الأعمال. تدعم Aspose.Cells جميع الأنواع الهامة للتحقق من البيانات.

تحتوي تعداد تحقق البيانات على الأعضاء التالية:

| **اسم العضو** | **الوصف** |
| :- | :- |
|[ANY_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#ANY_VALUE)|يشير إلى قيمة من أي نوع.
|[WHOLE_NUMBER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)|يشير إلى نوع التحقق للأرقام الصحيحة بأكملها.
|[DECIMAL](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DECIMAL)|يشير إلى نوع التحقق للأرقام العشرية.
|[LIST](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#LIST)|يشير إلى نوع التحقق لقائمة منسدلة.
|[DATE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DATE)|يشير إلى نوع التحقق للتواريخ.
|[TIME](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TIME)|يشير إلى نوع التحقق للتوقيت.
|[TEXT_LENGTH](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TEXT_LENGTH)|يشير إلى نوع التحقق لطول النص.
|[CUSTOM](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#CUSTOM)|يشير إلى نوع التحقق المخصص.
#### **عينة برمجية: التحقق من البيانات لأرقام صحيحة كاملة**
مع هذا النوع من التحقق، يمكن للمستخدمين إدخال أرقام صحيحة فقط ضمن نطاق محدد في الخلايا المحققة. تظهر الأمثلة البرمجية التالية كيفية تنفيذ نوع التحقق WHOLE_NUMBER. تقوم الأمثلة بإنشاء نفس التحقق من البيانات باستخدام Aspose.Cells الذي أنشأناه باستخدام Microsoft Excel أعلاه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WholeNumberDataValidation-WholeNumberDataValidation.java" >}}



#### **عينة برمجية: التحقق من البيانات لأرقام عشرية**
مع هذا النوع من التحقق، يمكن للمستخدم إدخال أرقام عشرية في الخلايا المحققة. في المثال، يتم تقييد المستخدم لإدخال قيمة عشرية فقط ومنطقة التحقق هي A1:A10.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DecimalDataValidation-DecimalDataValidation.java" >}}



#### **عينة برمجية: التحقق من البيانات لقائمة منسدلة**
يتيح هذا النوع من التحقق للمستخدم إدخال قيم من قائمة منسدلة. يوفر قائمة: سلسلة من الصفوف التي تحتوي على بيانات. يمكن للمستخدمين اختيار قيم فقط من القائمة. منطقة التحقق هي نطاق الخلية A1:A5 في ورقة العمل الأولى.

من المهم هنا أن تقوم بتعيين خاصية Validation.setInCellDropDown إلى **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ListDataValidation-ListDataValidation.java" >}}



#### **عينة برمجة: التحقق من صحة بيانات التاريخ**
مع هذا النوع من التحقق، يقوم المستخدمون بإدخال قيم تاريخية ضمن النطاق المحدد، أو تلبية معايير محددة، داخل الخلايا المحققة. في المثال، يتم تقييد المستخدم لإدخال تواريخ بين 1970 و1999. هنا، منطقة التحقق هي خلية B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DateDataValidation-DateDataValidation.java" >}}



#### **عينات البرمجة: التحقق من صحة بيانات الوقت**
مع هذا النوع من التحقق، يمكن للمستخدمين إدخال أوقات ضمن نطاق محدد، أو تلبية بعض المعايير، في الخلايا الموجودة. ففي المثال، يتم تقييد المستخدم بإدخال الأوقات بين الساعة 09:00 و11:30 صباحًا. هنا، مجال التحقق هو خلية B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TimeDataValidation-TimeDataValidation.java" >}}



#### **عينات البرمجة: التحقق من صحة طول النص**
مع هذا النوع من التحقق، يمكن للمستخدمين إدخال قيم نصية من طول محدد في الخلايا الموجودة. في المثال، يتم تقييد المستخدم بإدخال قيم سلسلة نصية بأكثر من 5 أحرف. مجال التحقق هو الخلية B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextLengthDataValidation-TextLengthDataValidation.java" >}}
## **قواعد تحقق البيانات**
عندما يتم تنفيذ التحققات من البيانات، يمكن التحقق من التحقق من خلال تعيين قيم مختلفة في الخلايا. يمكن استخدام [Cell.GetValidationValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue%5C(%5C)) لاحضار نتيجة التحقق. يوضح المثال التالي هذه الميزة مع قيم مختلفة. يمكن تنزيل الملف العيني من الرابط التالي للفحص:

[SampleDataValidationRules.xlsx](77987849.xlsx)

**كود عينة**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-VerifyCellValueSatisfiesDataValidationRules-1.java" >}}
## **تحقق مما إذا كان التحقق في خلية قائمة منسدلة**
كما رأينا، هناك العديد من أنواع التحققات التي يمكن تنفيذها داخل خلية. إذا كنت ترغب في التحقق مما إذا كان التحقق قائمة منسدلة أم لا، يمكن استخدام [Validation.InCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) الخاصية لاختبار هذا. يوضح الكود النموذجي التالي استخدام هذه الخاصية. يمكن تنزيل الملف العيني للفحص من الرابط التالي:

[sampleDataValidationRules.xlsx](77987849.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-CheckIfValidationInCellDropDown-1.java" >}}
## **إضافة منطقة الخلية إلى التحقق القائم**
قد تكون هناك حالات ترغب في إضافة [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) إلى [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation) الموجود. عند إضافة [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) باستخدام [Validation.AddArea(CellArea cellArea)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea%5C(com.aspose.cells.CellArea%5C))، يقوم Aspose.Cells بفحص جميع المناطق الموجودة لمعرفة ما إذا كانت المنطقة الجديدة موجودة بالفعل. إذا كان للملف عدد كبير من التحققات، فإن هذا يؤدي إلى تقليل الأداء. للتغلب على ذلك، تقدم الواجهة البرمجية طريقة [Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea%5C(com.aspose.cells.CellArea,%20boolean,%20boolean%5C)). يشير المعلمة *checkIntersection* إلى ما إذا كان يجب التحقق من تقاطع المنطقة المعطاه مع المناطق التحقق الموجودة. يتوفر تعيينها إلى **false** لتعطيل التحقق من المناطق الأخرى. تشير المعلمة *checkEdge* إلى ما إذا كان يجب التحقق من المناطق المطبقة. إذا كانت المنطقة الجديدة تصبح المنطقة العليا اليسرى، يتم إعادة بناء الإعدادات الداخلية. إذا كنت متأكدًا من أن المنطقة الجديدة ليست المنطقة العليا اليسرى، يمكنك ضبط هذه المعلمة على **false**.

يوضح مقتطف الكود التالي استخدام طريقة [Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea%5C(com.aspose.cells.CellArea,%20boolean,%20boolean%5C)) لإضافة منطقة الخلية الجديدة إلى التحقق الموجود.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-AddValidationArea-1.java" >}}

الملفات الإكسل المصدر والناتج مرفقة للرجوع إليها.

[ملف المصدر](PivotTableHideAndSortSample.xlsx)

[ملف الناتج](ValidationsSample_out.xlsx)


## **مواضيع متقدمة**
- [الحصول على التحقق من الخلية في ملفات ODS](/cells/ar/java/get-cell-validation-in-ods-files/)
- [الحصول على التحقق المطبق على خلية](/cells/ar/java/get-validation-applied-on-a-cell/)
- [التحقق من أن قيمة الخلية تلبي قواعد التحقق من البيانات](/cells/ar/java/verify-that-cell-value-satisfies-data-validation-rules/)
