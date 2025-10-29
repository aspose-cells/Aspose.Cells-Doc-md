---
title: إدارة الصيغ لملفات Excel
linktitle: الصيغ
type: docs
weight: 122
url: /ar/python-net/using-formulas-or-functions-to-process-data/
description: يمكن لـ Aspose.Cells لبايثون via .NET ببساطة الحصول على الصيغ، تعيينها، وحسابها لملفات Excel.
description: تعلم كيفية إدارة صيغ ملفات Excel من خلال API الخاص بـ Aspose.Cells لبايثون via .NET.
keywords: كيفية حساب الصيغ في بايثون، الصيغ والدوال باستخدام بايثون، إدارة الدوال المدمجة في بايثون، كيفية استخدام وظائف الإضافات مع بايثون، كيفية استخدام الصيغة المجمعة عبر بايثون، كيفية استخدام صيغة R1C1 في بايثون.
---

## **مقدمة**

واحدة من الميزات المثيرة في Microsoft Excel هي قدرتها على معالجة البيانات باستخدام الصيغ والدوال. يوفر Microsoft Excel مجموعة من الوظائف والصيغ المدمجة التي تساعد المستخدمين على إجراء حسابات معقدة بسرعة. كما يوفر Aspose.Cells لبايثون via .NET مجموعة هائلة من الوظائف والصيغ المدمجة التي تساعد المطورين على حساب القيم بسهولة. يدعم Aspose.Cells لبايثون via .NET أيضًا وظائف الإضافة، بالإضافة إلى دعم الصيغ المصفوفة وR1C1.

## **كيفية استخدام الصيغ والوظائف**

يقدم Aspose.Cells لبايثون via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)، تمثل ملف إكسل من مايكروسوفت. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) تتيح الوصول إلى كل ورقة عمل في ملف الإكسل. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). كل عنصر في مجموعة الخلايا يمثل كائن من فئة [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

من الممكن تطبيق الصيغ على الخلايا باستخدام الخصائص والأساليب التي يقدمها الفئة [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)، كما هو موضح بالتفصيل أدناه.

- باستخدام الوظائف الداخلية.
- باستخدام وظائف الإضافة.
- العمل مع صيغ الصيغة السابقة.
- إنشاء صيغة R1C1.

## **كيفية استخدام الوظائف المضمنة**

توفر الوظائف أو الصيغ المدمجة كوظائف جاهزة لتقليل جهود ووقت المطورين. راجع [قائمة الوظائف المدمجة](/cells/ar/python-net/supported-formula-functions/) المدعومة من قبل Aspose.Cells لبايثون via .NET. يتم سرد الوظائف بترتيب أبجدي. سيتم دعم المزيد من الوظائف في المستقبل.

يدعم Aspose.Cells لبايثون via .NET معظم الصيغ أو الدوال التي تقدمها Microsoft Excel. يمكن للمطورين استخدام هذه الصيغ عن طريق API أو [محرر الجدول](/cells/ar/net/what-is-a-designer-spreadsheet/). يدعم Aspose.Cells لبايثون via .NET مجموعة هائلة من الدوال الرياضية، النصية، البوليانية، الزمنية/التاريخية، الإحصائية، قواعد البيانات، البحث والإشارة.

استخدم خاصية [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/formula) للصف ال [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) لإضافة صيغة إلى خلية. **الصيغ المعقدة**, مثل

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, مدعومة أيضًا في Aspose.Cells لبايثون via .NET. عند تطبيق صيغة على خلية، ابدأ دائمًا السلسلة بعلامة يساوي (=) كما تفعل عند إنشاء صيغة في Microsoft Excel واستخدم فاصلة (,) لتقسيم معلمات الوظيفة.

في المثال أدناه، يتم تطبيق صيغة معقدة على أول خلية من مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) في ورقة العمل. تستخدم الصيغة وظيفة **IF** المدمجة التي يوفرها Aspose.Cells لبايثون via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingBuiltinfunction-1.py" >}}

## **كيفية استخدام الوظائف المضافة**

يمكننا أن يكون لدينا بعض الصيغ التي تم تحديدها من قبل المستخدم ونريد تضمينها كوظيفة إكسل إضافية. عند ضبط وظيفة الخلية. تعمل الوظائف المضمنة بشكل جيد ومع ذلك يوجد حاجة لضبط الوظائف المخصصة أو الصيغ باستخدام الوظائف الإضافية.

يوفر Aspose.Cells لبايثون via .NET ميزات لتسجيل وظائف الإضافة باستخدام [**worksheets.register_add_in_function()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/register_add_in_function). بعد ذلك، عند تعيين `cell.Formula =` أية وظيفة من الإضافة، تحتوي ملف الإكسل الناتج على القيمة المحتسبة من وظيفة الإضافة.

يجب تنزيل ملف XLAM التالي لتسجيل وظيفة الإضافة في عينة الكود أدناه. بالمثل، يمكن تنزيل الملف الناتج "test_udf.xlsx" لفحص الناتج.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-RegisterAndCallFuncFromAddIn-1.py" >}}

## **كيفية استخدام صيغة مصفوفة**

صيغ المصفوفة هي صيغ تأخذ مصفوفات، بدلاً من الأرقام الفردية، كتغيرات لوظائف تكون الصيغة. عند عرض صيغة المصفوفة، يكون محاطًا بالأقواس الإعتيادية ({}).

تعيد بعض وظائف Microsoft Excel مصفوفات القيم. لحساب نتائج متعددة باستخدام صيغة مصفوفة، أدخل المصفوفة في نطاق الخلايا بعدد الصفوف والأعمدة نفس معدلات الوسائط المصفوفات.

من الممكن تطبيق صيغة مصفوفة على خلية عن طريق استدعاء الوظيفة [**set_array_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_array_formula) الخاصة بفئة [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). تأخذ الوظيفة [**set_array_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_array_formula) معلمات التالية:

- **صيغة مصفوفة**, صيغة المصفوفة.
- **عدد الصفوف**, عدد الصفوف لملء نتيجة صيغة المصفوفة.
عدد الأعمدة

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingArrayFunction-1.py" >}}

## **كيفية استخدام الصيغة R1C1**

أضف صيغة مرجعية R1C1 إلى خلية مع خاصية فئة [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) وخاصية [**r1c1_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/r1c1_formula).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingR1C1-1.py" >}}

## **مواضيع متقدمة**
- [السابقون والموكّلون](/cells/ar/python-net/precedents-and-dependents/)
- [تعيين الروابط الخارجية في الصيغ](/cells/ar/python-net/set-external-links-in-formulas/)
- [نشر الصيغة في الجدول أو كائن القائمة تلقائيًا أثناء إدخال البيانات في صفوف جديدة](/cells/ar/python-net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [وضع صيغة لنطاق مسمى](/cells/ar/python-net/setting-formula-for-named-range/)
- [تعيين الصيغ - إشعار للمستخدمين غير الناطقين بالإنكليزية](/cells/ar/python-net/setting-formulas-notice-for-non-english-users/)
- [تعيين الصيغ المشتركة](/cells/ar/python-net/setting-shared-formula/)
- [تحديد الصفوف القصوى للصيغة المشتركة](/cells/ar/python-net/specify-maximum-rows-of-shared-formula/)
- [الدوال المدعومة في إكسل](/cells/ar/python-net/supported-formula-functions/)


{{< app/cells/assistant language="python-net" >}}
