---
title: التحقق من البيانات
type: docs
weight: 90
url: /ar/python-net/data-validation/
description: تعلم كيفية إضافة التحقق من البيانات من خلال واجهة برمجة التطبيقات Aspose.Cells for Python via .NET.
keywords: مكتبة Excel لغة Python، إضافة التحقق من البيانات في Python، الحصول على قيمة التحقق في Python، إضافة التحقق من العدد الكلي في Python، إضافة التحقق من قائمة البيانات في Python، إضافة التحقق من التاريخ في Python، إضافة التحقق من الوقت في Python، إضافة التحقق من طول النص في Python، إضافة منطقة الخلية إلى التحقق الموجود، التحقق مما إذا كان التحقق في الخلية هو منسدل، إضافة التحقق المخصص  
---

{{% alert color="primary" %}}

توفر Microsoft Excel بعض الميزات الجيدة لتصفية تلقائية أو تحقق صحة بيانات ورقة العمل. تدعم Aspose.Cells for Python via .NET بشكل كامل ميزات تصفية البيانات والتحقق من صحتها في Microsoft Excel. يشرح هذا المقال كيفية استخدام الميزات في Microsoft Excel وكيفية برمجتها باستخدام Aspose.Cells for Python via .NET.

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

### **التحقق من البيانات بمكتبة Aspose.Cells لبرنامج Python Excel**

التحقق من البيانات هو ميزة قوية للتحقق من المعلومات المُدخلة في أوراق العمل. باستخدام التحقق من البيانات، يمكن للمطورين توفير للمستخدمين قائمة من الخيارات، وتقييد إدخالات البيانات إلى نوع معين أو حجم، الخ.
في Aspose.Cells لبرنامج Python via .NET، لكل صنف [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) ميزة [**validations**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/validations/) التي تمثل مجموعة من [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) الكائنات. لإعداد التحقق، قم بتعيين بعض خصائص صنف [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) كما يلي:

- النوع – يمثل نوع التحقق، الذي يمكن تحديده باستخدام أحد القيم المحددة في التعداد [**ValidationType**](https://reference.aspose.com/cells/python-net/aspose.cells/validationtype) .
- المشغل – يمثل المشغل الذي سيتم استخدامه في التحقق، والذي يمكن تحديده باستخدام أحد القيم المحددة في التعداد [**OperatorType**](https://reference.aspose.com/cells/python-net/aspose.cells/operatortype) .
- الصيغة 1 – يمثل القيمة أو التعبير المرتبط بالجزء الأول من التحقق البيانات.
- الصيغة2 - تمثل القيمة أو التعبير المرتبط بالجزء الثاني من التحقق من البيانات.

عند تكوين خصائص كائن [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) ، يمكن للمطورين استخدام هيكل [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) لتخزين المعلومات حول نطاق الخلايا الذي سيتم التحقق من صحته باستخدام التحقق من البيانات الذي تم إنشاؤه.

#### **أنواع التحقق من البيانات**

يحتوي تعداد [**ValidationType**](https://reference.aspose.com/cells/python-net/aspose.cells/validationtype) على الأعضاء التالية:

| **اسم العضو** | **الوصف** |
| :- | :- |
|ANY_VALUE| يشير إلى قيمة من أي نوع.
|WHOLE_NUMBER| يشير إلى نوع التحقق للأرقام الصحيحة.
| عشري | يشير إلى نوع التحقق للأرقام العشرية.
| قائمة | يشير إلى نوع التحقق لقائمة منسدلة.
|DATE| يشير إلى نوع التحقق للتواريخ.
| الوقت | يشير إلى نوع التحقق للوقت.
|TEXT_LENGTH| يشير إلى نوع التحقق لطول النص.
| مخصص | يشير إلى نوع التحقق المخصص.

##### **تحقق البيانات من الأعداد الصحيحة**

مع هذا النوع من التحقق، يمكن للمستخدمين إدخال أعداد صحيحة فقط داخل النطاق المحدد في الخلايا المحققة. تُظهر الأمثلة البرمجية التالية كيفية تنفيذ نوع التحقق WholeNumber. ينشئ المثال نفس التحقق من البيانات باستخدام Aspose.Cells for Python via .NET الذي أنشأناه باستخدام Microsoft Excel أعلاه.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-WholeNumberDataValidation-1.py" >}}

##### **تحقق البيانات من القائمة**

يسمح هذا النوع من التحقق للمستخدم بإدخال قيم من قائمة منسدلة. يوفر قائمة: سلسلة من الصفوف التي تحتوي على بيانات. في المثال، يتم إضافة ورقة عمل ثانية لاحتواء مصدر القائمة. يمكن للمستخدمين فقط تحديد القيم من القائمة. منطقة التحقق هي نطاق الخلية A1:A5 في الورقة العمل الأولى.

من المهم هنا تعيين [**Validation.in_cell_drop_down**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/in_cell_drop_down/) إلى **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-ListDataValidation-1.py" >}}

##### **تحقق البيانات من التاريخ**

مع هذا النوع من التحقق، يقوم المستخدمون بإدخال قيم تاريخية ضمن النطاق المحدد، أو تلبية معايير محددة، داخل الخلايا المحققة. في المثال، يتم تقييد المستخدم لإدخال تواريخ بين 1970 و1999. هنا، منطقة التحقق هي خلية B1.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DateDataValidation-1.py" >}}

##### **تحقق المواقيت الزمنية للبيانات**

مع هذا النوع من التحقق، يمكن للمستخدمين إدخال أوقات ضمن نطاق محدد، أو تلبية بعض المعايير، في الخلايا الموجودة. ففي المثال، يتم تقييد المستخدم بإدخال الأوقات بين الساعة 09:00 و11:30 صباحًا. هنا، مجال التحقق هو خلية B1.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-TimeDataValidation-1.py" >}}

##### **تحقق طول النصوص للبيانات**

مع هذا النوع من التحقق، يمكن للمستخدمين إدخال قيم نصية من طول محدد في الخلايا الموجودة. في المثال، يتم تقييد المستخدم بإدخال قيم سلسلة نصية بأكثر من 5 أحرف. مجال التحقق هو الخلية B1.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-TextLengthDataValidation-1.py" >}}

### **قواعد تحقق البيانات**

عند تنفيذ التحقق من البيانات، يمكن فحص عملية التحقق من خلال تعيين قيم مختلفة في الخلايا. يمكن استخدام [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) لاسترجاع نتيجة التحقق. يوضح المثال التالي هذه الميزة مع قيم مختلفة. يمكن تنزيل الملف العيني من الرابط التالي للفحص:

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DataValidationRules-1.py" >}}

## **التحقق مما إذا كان التحقق في الخلية القائمة المنسدلة**

كما رأينا، هناك العديد من أنواع التحقق التي يمكن تنفيذها داخل خلية. إذا أردت التحقق ما إذا كان التحقق منسدلة أم لا، يمكن استخدام [**Validation.in_cell_drop_down**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/in_cell_drop_down/) خاصية لاختبار هذا. يوضح الكود العيني التالي استخدام هذه الخاصية. يمكن تنزيل ملف عينة للفحص من الرابط التالي:

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-CheckIfValidationInCellDropDown-1.py" >}}

## **إضافة منطقة الخلية إلى التحقق القائم**

قد تكون هناك حالات حيث ترغب في إضافة [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) إلى [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) القائمة بالفعل. عندما تضيف [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) باستخدام [**Validation.add_area(cell_area)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea)، يقوم Aspose.Cells بفحص جميع المناطق القائمة لمعرفة ما إذا كانت المنطقة الجديدة موجودة بالفعل. إذا كان للملف عدد كبير من التحققات، فإن هذا يؤثر على الأداء. للتغلب على هذا، يوفر الواجهة البرمجية الطريقة *[**Validation.add_area(cell_area, check_intersection, check_edge)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea-bool-bool)* . يشير معلم *checkIntersection* إلى ما إذا كان يجب فحص اشتراك منطقة معينة مع مناطق التحقق القائمة. تعيينها على **false** سيعطل فحص المناطق الأخرى. معلم *checkEdge* يشير إلى ما إذا كان يجب فحص المناطق المطبقة. إذا أصبحت المنطقة الجديدة هي المنطقة العلوية اليسرى، يتم إعادة إعدادات الداخلية. إذا كنت متأكدًا من أن المنطقة الجديدة ليست المنطقة العلوية اليسرى، فيمكنك ضبط هذا المعلم على **false**.

الكود البرمجي التالي يوضح استخدام الطريقة [**Validation.add_area(cell_area, check_intersection, check_edge)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea-bool-bool) لإضافة [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) جديدة إلى [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) القائمة.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AddValidationArea-1.py" >}}

الملفات الإكسل المصدر والناتج مرفقة للرجوع إليها.

[ملف المصدر](96928093.xlsx)

[ملف الإخراج](96928220.xlsx)


## **مواضيع متقدمة**
- [الحصول على التحقق من الخلية في ملفات ODS](/cells/ar/python-net/get-cell-validation-in-ods-files/)
- [الحصول على التحقق المطبق على خلية](/cells/ar/python-net/get-validation-applied-on-a-cell/)
- [التحقق من أن قيمة الخلية تلبي قواعد التحقق من البيانات](/cells/ar/python-net/verify-that-cell-value-satisfies-data-validation-rules/)
{{< app/cells/assistant language="python-net" >}}
