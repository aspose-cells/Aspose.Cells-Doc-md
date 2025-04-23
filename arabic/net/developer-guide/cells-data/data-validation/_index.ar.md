---
title: التحقق من البيانات
type: docs
weight: 90
url: /ar/net/data-validation/
description: تعلم كيفية إضافة التحقق من البيانات من خلال Aspose.Cells for .NET API.
keywords: إضافة التحقق من البيانات، الحصول على قيمة التحقق، إضافة التحقق من البيانات الأرقام الصحيحة، إضافة التحقق من البيانات القائمة، إضافة التحقق من البيانات التاريخية، إضافة التحقق من البيانات الزمنية، إضافة التحقق من طول النص، إضافة CellArea إلى التحقق الحالي، التحقق مما إذا كان التحقق في الخلية ضربة سحرية، إضافة التحقق المخصص  
---

{{% alert color="primary" %}}

يوفر Microsoft Excel بعض الميزات الجيدة لتصفية تلقائية أو التحقق من صحة بيانات ورقة البيانات. Aspose.Cells يدعم بشكل كامل تحقق بيانات Microsoft Excel وميزات تصفية تلقائية. يشرح هذا المقال كيفية استخدام الميزات في Microsoft Excel وكيفية كتابة الكود باستخدام Aspose.Cells.

{{% /alert %}}

## **أنواع التحقق من البيانات والتنفيذ**

التحقق من البيانات هو القدرة على وضع قواعد تتعلق بالبيانات المُدخلة على ورقة العمل. على سبيل المثال، استخدم التحقق لضمان أن العمود المسمى تاريخ يحتوي فقط على تواريخ، أو أن عمودًا آخر يحتوي فقط على أرقام. يمكنك حتى التأكد من أن العمود المسمى تاريخ يحتوي فقط على تواريخ ضمن نطاق معين. باستخدام التحقق من البيانات، يمكنك التحكم في ما يُدخل في الخلايا في ورقة العمل.

يدعم Microsoft Excel عددًا من أنواع التحقق المختلفة للبيانات. يُستخدم كل نوع للتحكم في نوع البيانات التي تُدخل إلى خلية أو نطاق الخلايا. أدناه، مقتطفات الكود توضح كيفية التحقق من:

- أن الأرقام صحيحة، أي أن ليس لديها جزء عشري.
- أن الأرقام العشرية تتبع الهيكل الصحيح. يحدد مثال الكود أن يكون نطاق الخلايا يجب أن يحتوي على اثنين من أماكن العشرية.
- أن القيم مقيدة بقائمة من القيم. يحدد التحقق بالقائمة قائمة منفصلة من القيم التي يمكن تطبيقها على خلية أو نطاق الخلايا.
- يتمثل التواريخ ضمن نطاق محدد.
- أن الوقت يكون ضمن نطاق محدد.
- أن النص يكون ضمن طول حرف معين.

### **التحقق من البيانات مع Microsoft Excel**

لإنشاء التحققات باستخدام Microsoft Excel:

1. في ورقة العمل، حدد الخلايا التي ترغب في تطبيق التحقق عليها.
1. من قائمة **البيانات**، حدد **التحقق**. سيتم عرض حوار التحقق.
1. انقر على علامة التبويب **الإعدادات** ثم أدخل الإعدادات.

### **التحقق من البيانات بواسطة Aspose.Cells**

التحقق من البيانات هو ميزة قوية للتحقق من المعلومات المُدخلة في أوراق العمل. باستخدام التحقق من البيانات، يمكن للمطورين توفير للمستخدمين قائمة من الخيارات، وتقييد إدخالات البيانات إلى نوع معين أو حجم، الخ.
في Aspose.Cells، لكل فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) خاصية [**Validations**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/validations) التي تمثل مجموعة من كائنات [**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation). لإعداد التحقق، قم بتعيين بعض خصائص فئة [**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation) كما يلي:

- النوع - يمثل نوع التحقق، والذي يمكن تحديده باستخدام قيم محددة مُسبقًا في تعداد [**ValidationType**](https://reference.aspose.com/cells/net/aspose.cells/validationtype).
- المشغل – يمثل المشغل الذي سيتم استخدامه في التحقق، والذي يمكن تحديده باستخدام أحد القيم المحددة في التعداد [**OperatorType**](https://reference.aspose.com/cells/net/aspose.cells/operatortype) .
- الصيغة1 - يمثل القيمة أو التعبير المرتبط بالجزء الأول من التحقق من البيانات.
- الصيغة2 - يمثل القيمة أو التعبير المرتبط بالجزء الثاني من التحقق من البيانات.

عند تكوين خصائص كائن [**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation) ، يمكن للمطورين استخدام هيكل [**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) لتخزين المعلومات حول نطاق الخلايا الذي سيتم التحقق من صحته باستخدام التحقق من البيانات الذي تم إنشاؤه.

#### **أنواع التحقق من البيانات**

يحتوي تعداد [**ValidationType**](https://reference.aspose.com/cells/net/aspose.cells/validationtype) على الأعضاء التالية:

| **اسم العضو** | **الوصف** |
| :- | :- |
|AnyValue|يُشير إلى قيمة من أي نوع.|
|WholeNumber|تشير إلى نوع التحقق من صحة للأرقام الكاملة.|
|Decimal|تشير إلى نوع التحقق من صحة للأرقام العشرية.|
|List|تشير إلى نوع التحقق من صحة لقائمة السقط.|
|Date|تشير إلى نوع التحقق من صحة للتواريخ.|
|Time|تشير إلى نوع التحقق من صحة للوقت.|
|TextLength|تشير إلى نوع التحقق من صحة لطول النص.|
|Custom|تشير إلى نوع التحقق من العرف.|

##### **تحقق البيانات من الأعداد الصحيحة**

مع هذا النوع من التحقق، يمكن للمستخدمين إدخال الأرقام الكاملة فقط ضمن نطاق محدد إلى الخلايا المحققة. توضح أمثلة الشيفرة التالية كيفية تنفيذ نوع التحقق من الأرقام الكاملة. يقوم المثال بإنشاء التحقق من البيانات نفسه باستخدام Aspose.Cells الذي قمنا بإنشائه باستخدام Microsoft Excel أعلاه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-WholeNumberDataValidation-1.cs" >}}

##### **تحقق البيانات من القائمة**

يسمح هذا النوع من التحقق للمستخدم بإدخال قيم من قائمة منسدلة. يوفر قائمة: سلسلة من الصفوف التي تحتوي على بيانات. في المثال، يتم إضافة ورقة عمل ثانية لاحتواء مصدر القائمة. يمكن للمستخدمين فقط تحديد القيم من القائمة. منطقة التحقق هي نطاق الخلية A1:A5 في الورقة العمل الأولى.

من المهم هنا تعيين [**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown) إلى **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-ListDataValidation-1.cs" >}}

##### **تحقق البيانات من التاريخ**

مع هذا النوع من التحقق، يقوم المستخدمون بإدخال قيم تاريخية ضمن النطاق المحدد، أو تلبية معايير محددة، داخل الخلايا المحققة. في المثال، يتم تقييد المستخدم لإدخال تواريخ بين 1970 و1999. هنا، منطقة التحقق هي خلية B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-DateDataValidation-1.cs" >}}

##### **تحقق المواقيت الزمنية للبيانات**

مع هذا النوع من التحقق، يمكن للمستخدمين إدخال أوقات ضمن نطاق محدد، أو تلبية بعض المعايير، في الخلايا الموجودة. ففي المثال، يتم تقييد المستخدم بإدخال الأوقات بين الساعة 09:00 و11:30 صباحًا. هنا، مجال التحقق هو خلية B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TimeDataValidation-1.cs" >}}

##### **تحقق طول النصوص للبيانات**

مع هذا النوع من التحقق، يمكن للمستخدمين إدخال قيم نصية من طول محدد في الخلايا الموجودة. في المثال، يتم تقييد المستخدم بإدخال قيم سلسلة نصية بأكثر من 5 أحرف. مجال التحقق هو الخلية B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TextLengthDataValidation-1.cs" >}}

### **قواعد تحقق البيانات**

عندما يتم تنفيذ تحققات البيانات، يمكن فحص التحقق بتعيين قيم مختلفة في الخلايا. يمكن استخدام [**Cell.GetValidationValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) لاسترداد نتيجة التحقق. يوضح المثال التالي هذه الميزة مع قيم مختلفة. يمكن تنزيل الملف العيني من الرابط التالي للاختبار:

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}

## **التحقق مما إذا كان التحقق في الخلية القائمة المنسدلة**

كما رأينا، هناك العديد من أنواع التحقق التي يمكن تنفيذها داخل خلية. إذا أردت التحقق ما إذا كان التحقق منسدلة أم لا، يمكن استخدام [**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown) خاصية لاختبار هذا. يوضح الكود العيني التالي استخدام هذه الخاصية. يمكن تنزيل ملف عينة للفحص من الرابط التالي:

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckIfValidationInCellDropDown-1.cs" >}}

## **إضافة منطقة الخلية إلى التحقق القائم**

قد تكون هناك حالات حيث ترغب في إضافة [**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) إلى [**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation) القائمة بالفعل. عندما تضيف [**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) باستخدام [**Validation.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/net/aspose.cells/validation/methods/addarea)، يقوم Aspose.Cells بفحص جميع المناطق القائمة لمعرفة ما إذا كانت المنطقة الجديدة موجودة بالفعل. إذا كان للملف عدد كبير من التحققات، فإن هذا يؤثر على الأداء. للتغلب على هذا، يوفر الواجهة البرمجية الطريقة *[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1)* . يشير معلم *checkIntersection* إلى ما إذا كان يجب فحص اشتراك منطقة معينة مع مناطق التحقق القائمة. تعيينها على **false** سيعطل فحص المناطق الأخرى. معلم *checkEdge* يشير إلى ما إذا كان يجب فحص المناطق المطبقة. إذا أصبحت المنطقة الجديدة هي المنطقة العلوية اليسرى، يتم إعادة إعدادات الداخلية. إذا كنت متأكدًا من أن المنطقة الجديدة ليست المنطقة العلوية اليسرى، فيمكنك ضبط هذا المعلم على **false**.

الكود البرمجي التالي يوضح استخدام الطريقة [**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) لإضافة [**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) جديدة إلى [**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation) القائمة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddValidationArea-1.cs" >}}

الملفات الإكسل المصدر والناتج مرفقة للرجوع إليها.

[ملف المصدر](96928093.xlsx)

[ملف الإخراج](96928220.xlsx)


## **مواضيع متقدمة**
- [الحصول على التحقق من الخلية في ملفات ODS](/cells/ar/net/get-cell-validation-in-ods-files/)
- [الحصول على التحقق المطبق على خلية](/cells/ar/net/get-validation-applied-on-a-cell/)
- [التحقق من أن قيمة الخلية تلبي قواعد التحقق من البيانات](/cells/ar/net/verify-that-cell-value-satisfies-data-validation-rules/)
{{< app/cells/assistant language="csharp" >}}
