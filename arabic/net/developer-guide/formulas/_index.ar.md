---
title: إدارة الصيغ لملفات Excel
linktitle: الصيغ
type: docs
weight: 122
url: /ar/net/using-formulas-or-functions-to-process-data/
description: يمكن ل Aspose.Cells ببساطة الحصول على الصيغ وتعيينها وحسابها لملفات Excel.
description: تعلم كيفية إدارة الصيغ لملفات Excel من خلال واجهات برمجة التطبيقات Aspose.Cells for NET.
keywords: كيفية حساب الصيغ في لغة البرمجة C#، الصيغ والوظائف باستخدام C#، إدارة الوظائف المضمنة في C#، كيفية استخدام وظائف الإضافة بواسطة C#، كيفية استخدام الصيغة الصفيفية عبر C#، كيفية استخدام الصيغة R1C1 في C#.
---

## **مقدمة**

واحدة من الميزات المثيرة في Microsoft Excel هي قدرته على معالجة البيانات باستخدام الصيغ والدوال. يوفر Microsoft Excel مجموعة من الدوال والصيغ المدمجة التي تساعد المستخدمين على إجراء حسابات معقدة بسرعة. كما توفر Aspose.Cells مجموعة كبيرة من الدوال والصيغ المدمجة التي تساعد المطورين على حساب القيم بسهولة. كما تدعم Aspose.Cells وظائف الإضافة. بالإضافة إلى ذلك، تدعم Aspose.Cells الصيغ المُصفوفة وصيغ R1C1.

## **كيفية استخدام الصيغ والوظائف**

يوفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تُمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). يمثل كل عنصر في مجموعة Cells كائنًا من الفئة [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

من الممكن تطبيق الصيغ على الخلايا باستخدام الخصائص والأساليب التي يقدمها الفئة [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)، كما هو موضح بالتفصيل أدناه.

- باستخدام الوظائف الداخلية.
- باستخدام وظائف الإضافة.
- العمل مع صيغ الصيغة السابقة.
- إنشاء صيغة R1C1.

## **كيفية استخدام الوظائف المضمنة**

الوظائف المضمنة أو الصيغ يتم توفيرها كوظائف جاهزة لتقليل جهود ووقت المطورين. انظر [قائمة الوظائف المضمنة](/cells/ar/net/supported-formula-functions/) المدعومة بواسطة Aspose.Cells. تم ترتيب الوظائف بترتيب أبجدي. سيتم دعم المزيد من الوظائف في المستقبل.

تدعم Aspose.Cells معظم الصيغ أو الوظائف التي تقدمها Microsoft Excel. يمكن للمطورين استخدام هذه الصيغ من خلال واجهة برمجة التطبيقات API أو [جدول البيانات المصمم](/cells/ar/net/what-is-a-designer-spreadsheet/). تدعم Aspose.Cells مجموعة هائلة من الصيغ الرياضية والنصية والقيم المنطقية والتاريخ/الوقت والإحصائيات وقواعد البيانات والبحث والمراجع.

استخدم خاصية [**Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) للصف ال [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) لإضافة صيغة إلى خلية. **الصيغ المعقدة**, مثل

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, مدعومة أيضًا في Aspose.Cells. عند تطبيق صيغة على خلية، يجب دائمًا بدء السلسلة بعلامة يساوي (=) كما تفعل عند إنشاء صيغة في Microsoft Excel واستخدام فاصلة (,) لفصل معلمات الوظيفة.

في المثال أدناه، يتم تطبيق صيغة معقدة على خلية الصفراء من مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). تستخدم الصيغة الوظيفة المضمنة **IF** المقدمة بواسطة Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

## **كيفية استخدام الوظائف المضافة**

يمكننا أن يكون لدينا بعض الصيغ التي تم تحديدها من قبل المستخدم ونريد تضمينها كوظيفة إكسل إضافية. عند ضبط وظيفة الخلية. تعمل الوظائف المضمنة بشكل جيد ومع ذلك يوجد حاجة لضبط الوظائف المخصصة أو الصيغ باستخدام الوظائف الإضافية.

توفر Aspose.Cells ميزات لتسجيل وظائف الإضافات باستخدام [**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index). بعد ذلك عند ضبط cell.Formula = anyFunctionFromAddIn، يحتوي ملف Excel الناتج على القيمة المحسوبة من وظيفة الإضافة.

يجب تنزيل ملف XLAM التالي لتسجيل وظيفة الإضافة في عينة الكود أدناه. بالمثل، يمكن تنزيل الملف الناتج "test_udf.xlsx" لفحص الناتج.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

## **كيفية استخدام صيغة مصفوفة**

صيغ المصفوفة هي صيغ تأخذ مصفوفات، بدلاً من الأرقام الفردية، كتغيرات لوظائف تكون الصيغة. عند عرض صيغة المصفوفة، يكون محاطًا بالأقواس الإعتيادية ({}).

تعيد بعض وظائف Microsoft Excel مصفوفات القيم. لحساب نتائج متعددة باستخدام صيغة مصفوفة، أدخل المصفوفة في نطاق الخلايا بعدد الصفوف والأعمدة نفس معدلات الوسائط المصفوفات.

من الممكن تطبيق صيغة مصفوفة على خلية عن طريق استدعاء الوظيفة [**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) الخاصة بفئة [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). تأخذ الوظيفة [**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) معلمات التالية:

- **صيغة مصفوفة**, صيغة المصفوفة.
- **عدد الصفوف**, عدد الصفوف لملء نتيجة صيغة المصفوفة.
عدد الأعمدة

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

## **كيفية استخدام الصيغة R1C1**

أضف صيغة مرجعية R1C1 إلى خلية مع خاصية فئة [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) وخاصية [**R1C1Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

## **مواضيع متقدمة**
- [السابقون والموكّلون](/cells/ar/net/precedents-and-dependents/)
- [تعيين الروابط الخارجية في الصيغ](/cells/ar/net/set-external-links-in-formulas/)
- [نشر الصيغة في الجدول أو كائن القائمة تلقائيًا أثناء إدخال البيانات في صفوف جديدة](/cells/ar/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [وضع صيغة لنطاق مسمى](/cells/ar/net/setting-formula-for-named-range/)
- [تعيين الصيغ - إشعار للمستخدمين غير الناطقين بالإنكليزية](/cells/ar/net/setting-formulas-notice-for-non-english-users/)
- [تعيين الصيغ المشتركة](/cells/ar/net/setting-shared-formula/)
- [تحديد الصفوف القصوى للصيغة المشتركة](/cells/ar/net/specify-maximum-rows-of-shared-formula/)
- [الدوال المدعومة في إكسل](/cells/ar/net/supported-formula-functions/)

{{< app/cells/assistant language="csharp" >}}
