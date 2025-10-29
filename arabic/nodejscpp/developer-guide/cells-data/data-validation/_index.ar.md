---  
title: التحقق من البيانات
type: docs  
weight: 90  
url: /ar/nodejs-cpp/data-validation/  
description: تعلم كيف تضيف التحقق من صحة البيانات من خلال واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++.  
keywords: إضافة التحقق من صحة البيانات Node.js عبر C++، الحصول على قيمة التحقق من صحة البيانات Node.js عبر C++، إضافة التحقق من صحة رقم كامل Node.js عبر C++، إضافة قائمة التحقق من الصحة Node.js عبر C++، إضافة صحة التاريخ Node.js عبر C++، إضافة صحة الوقت Node.js عبر C++، إضافة صحة طول النص Node.js عبر C++، إضافة CellArea إلى التحقق الحالي في Node.js عبر C++، التحقق مما إذا كانت صحة البيانات في الخلية هي قائمة منسدلة Node.js عبر C++، إضافة التحقق المخصص في Node.js عبر C++  
---  

{{% alert color="primary" %}}  
يوفر Microsoft Excel بعض الميزات الجيدة لتصفية أو التحقق الآلي من بيانات ورقة العمل. يدعم Aspose.Cells بشكل كامل ميزات التحقق من صحة البيانات والتصفية التلقائية في Microsoft Excel. تشرح هذه المقالة كيفية استخدام الميزات في Microsoft Excel، وكيفية برمجتها باستخدام Aspose.Cells for Node.js via C++.  
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

### **التحقق من صحة البيانات مع Aspose.Cells for Node.js via C++**  

التحقق من البيانات هو ميزة قوية للتحقق من المعلومات المُدخلة في أوراق العمل. باستخدام التحقق من البيانات، يمكن للمطورين توفير للمستخدمين قائمة من الخيارات، وتقييد إدخالات البيانات إلى نوع معين أو حجم، الخ.  
في Aspose.Cells for Node.js via C++، تحتوي كل صنف [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) على طريقة [**getValidations()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getValidations--) والتي تمثل مجموعة من كائنات [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation). لإعداد التحقق، قم بضبط بعض خصائص صنف [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) على النحو التالي:  

- النوع - يمثل نوع التحقق، والذي قد يتم تحديده باستخدام أحد القيم المعرفة مسبقًا في تعداد [**ValidationType**](https://reference.aspose.com/cells/nodejs-cpp/validationtype).  
- المشغل - يمثل العامل المستخدم في التحقق، والذي قد يتم تحديده باستخدام أحد القيم المعرفة مسبقًا في تعداد [**OperatorType**](https://reference.aspose.com/cells/nodejs-cpp/operatortype).  
- الصيغة1 - يمثل القيمة أو التعبير المرتبط بالجزء الأول من التحقق من البيانات.  
- الصيغة2 - يمثل القيمة أو التعبير المرتبط بالجزء الثاني من التحقق من البيانات.  

عند تكوين خصائص كائن [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation)، يمكن للمطورين استخدام بنية [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) لتخزين معلومات حول نطاق الخلية الذي سيتم التحقق منه باستخدام التحقق الذي تم إنشاؤه.  

#### **أنواع التحقق من البيانات**  

يحتوي تعداد [**ValidationType**](https://reference.aspose.com/cells/nodejs-cpp/validationtype) على الأعضاء التالية:  

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

مع هذا النوع من التحقق، يمكن للمستخدمين إدخال أعداد صحيحة فقط ضمن نطاق معين في الخلايا التي تم التحقق منها. تظهر أمثلة التعليمات البرمجية التالية كيفبة تنفيذ نوع التحقق من الأعداد الكاملة. ينشئ المثال التحقق من صحة البيانات نفسه باستخدام Aspose.Cells for Node.js via C++ الذي أنشأناه باستخدام Microsoft Excel أعلاه.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-WholeNumber.js" >}}


##### **تحقق البيانات من القائمة**  

يسمح هذا النوع من التحقق للمستخدم بإدخال قيم من قائمة منسدلة. يوفر قائمة: سلسلة من الصفوف التي تحتوي على بيانات. في المثال، يتم إضافة ورقة عمل ثانية لاحتواء مصدر القائمة. يمكن للمستخدمين فقط تحديد القيم من القائمة. منطقة التحقق هي نطاق الخلية A1:A5 في الورقة العمل الأولى.  

من المهم هنا أن تقوم بضبط خاصية [**Validation.setInCellDropDown(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#setInCellDropDown-boolean-) على **true**.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-ListData.js" >}}


##### **تحقق البيانات من التاريخ**  

مع هذا النوع من التحقق، يقوم المستخدمون بإدخال قيم تاريخية ضمن النطاق المحدد، أو تلبية معايير محددة، داخل الخلايا المحققة. في المثال، يتم تقييد المستخدم لإدخال تواريخ بين 1970 و1999. هنا، منطقة التحقق هي خلية B1.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-DateData.js" >}}

##### **تحقق المواقيت الزمنية للبيانات**  

مع هذا النوع من التحقق، يمكن للمستخدمين إدخال أوقات ضمن نطاق محدد، أو تلبية بعض المعايير، في الخلايا الموجودة. ففي المثال، يتم تقييد المستخدم بإدخال الأوقات بين الساعة 09:00 و11:30 صباحًا. هنا، مجال التحقق هو خلية B1.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-TimeData.js" >}}


##### **تحقق طول النصوص للبيانات**  

مع هذا النوع من التحقق، يمكن للمستخدمين إدخال قيم نصية من طول محدد في الخلايا الموجودة. في المثال، يتم تقييد المستخدم بإدخال قيم سلسلة نصية بأكثر من 5 أحرف. مجال التحقق هو الخلية B1.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-TextLengthData.js" >}}


### **قواعد تحقق البيانات**  

عند تنفيذ عمليات التحقق من الصحة، يمكن فحص صحة التحقق من خلال تعيين قيم مختلفة في الخلايا. يمكن استخدام [**Cell.getValidationValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) لاسترداد نتيجة التحقق. يوضح المثال التالي هذه الميزة مع قيم مختلفة. يمكن تنزيل الملف النموذجي للاختبار من الرابط التالي:  

[sampleDataValidationRules.xlsx](77496339.xlsx)  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-DataValidationRules.js" >}}


## **التحقق مما إذا كان التحقق في الخلية القائمة المنسدلة**  

كما رأينا، هناك العديد من أنواع التحققات التي يمكن تنفيذها داخل خلية. إذا أردت التحقق مما إذا كانت التحقق من الصحة قائمة منسدلة أم لا، يمكن استخدام طريقة [**Validation.getInCellDropDown()**](https://reference.aspose.com/cells/nodejs-cpp/validation/#getInCellDropDown--) لاختبار ذلك. توضح الشفرة النموذجية التالية استخدام هذه الخاصية. يمكن تنزيل ملف اختبار من الرابط التالي:  

[sampleValidation.xlsx](79527947.xlsx)  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-CheckValidationIsDropDown.js" >}}


## **إضافة منطقة الخلية إلى التحقق القائم**  

قد تكون هناك حالات ترغب فيها في إضافة [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) إلى [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) الموجودة. عند إضافة [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) باستخدام [**Validation.addArea(CellArea)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-)، يتحقق Aspose.Cells من جميع المناطق الموجودة مسبقًا لمعرفة ما إذا كانت المنطقة الجديدة موجودة بالفعل. إذا كانت هناك العديد من التحققات في الملف، فإن ذلك يؤثر على الأداء. لتجاوز ذلك، توفر الواجهة البرمجية طريقة [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-boolean-boolean-). يشير المعامل *checkIntersection* إلى ما إذا كان يتم التحقق من تقاطع المنطقة المعطاة مع مناطق التحقق الموجودة. ضبطه على **false** سيؤدي إلى تعطيل التحقق من المناطق الأخرى. المعامل *checkEdge* يشير إلى ما إذا كان سيتم التحقق من المناطق المطبقة. إذا أصبحت المنطقة الجديدة المنطقة العليا اليسرى، يتم إعادة بناء الإعدادات الداخلية. إذا كنت متأكدًا من أن المنطقة الجديدة ليست المنطقة العليا اليسرى، يمكنك ضبط هذا المعامل على **false**.  

يوضح مقتطف الكود التالي استخدام طريقة [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-boolean-boolean-) لإضافة [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) جديد إلى [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) موجودة.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-AddCellAreaToExistingValidation.js" >}}

الملفات الإكسل المصدر والناتج مرفقة للرجوع إليها.  

[ملف المصدر](96928093.xlsx)  

[ملف الإخراج](96928220.xlsx)  

## **مواضيع متقدمة**  
- [الحصول على التحقق من الخلية في ملفات ODS](/cells/ar/nodejs-cpp/get-cell-validation-in-ods-files/)  
- [الحصول على التحقق المطبق على خلية](/cells/ar/nodejs-cpp/get-validation-applied-on-a-cell/)  
- [التحقق من أن قيمة الخلية تلبي قواعد التحقق من البيانات](/cells/ar/nodejs-cpp/verify-that-cell-value-satisfies-data-validation-rules/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
