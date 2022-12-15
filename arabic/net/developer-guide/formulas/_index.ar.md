---
title: إدارة صيغ ملفات Excel
linktitle: الصيغ
type: docs
weight: 122
url: /ar/net/using-formulas-or-functions-to-process-data/
description: يمكن لـ Aspose.Cells ببساطة الحصول على صيغ ملفات Excel وتعيينها وحسابها.
---
## **مقدمة**

تتمثل إحدى ميزات Microsoft الجذابة في Excel في قدرته على معالجة البيانات باستخدام الصيغ والوظائف. يوفر Microsoft Excel مجموعة من الوظائف والصيغ المضمنة التي تساعد المستخدمين على إجراء العمليات الحسابية المعقدة بسرعة. يوفر Aspose.Cells أيضًا مجموعة ضخمة من الوظائف والصيغ المضمنة التي تساعد المطورين على حساب القيم بسهولة. يدعم Aspose.Cells أيضًا الوظائف الإضافية. علاوة على ذلك ، يدعم Aspose.Cells صفيف وصيغ R1C1 في Aspose.Cells.

## **استخدام الصيغ والوظائف**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة توفر أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. يمثل كل عنصر في مجموعة Cells عنصرًا من عناصر[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) صف دراسي.

 من الممكن تطبيق الصيغ على الخلايا باستخدام الخصائص والطرق التي يوفرها[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) الفصل ، بمزيد من التفصيل أدناه.

- استخدام وظائف مدمجة.
- استخدام الوظائف الإضافية.
- العمل مع صيغ الصفيف.
- إنشاء صيغة R1C1.

## **استخدام وظائف مدمجة**

 يتم توفير الوظائف أو الصيغ المضمنة كوظائف جاهزة لتقليل جهود المطورين والوقت. نرى[قائمة الوظائف المضمنة](/cells/ar/net/supported-formula-functions/) يدعمها Aspose.Cells. الوظائف مذكورة بترتيب أبجدي. سيتم دعم المزيد من الوظائف في المستقبل.

 يدعم Aspose.Cells معظم الصيغ أو الوظائف التي يوفرها Microsoft Excel. يمكن للمطورين استخدام هذه الصيغ من خلال API أو[جدول بيانات المصمم](/cells/ar/net/what-is-a-designer-spreadsheet/). يدعم Aspose.Cells مجموعة ضخمة من الصيغ الرياضية ، والسلسلة ، والمنطقية ، والتاريخ / الوقت ، والإحصائية ، وقاعدة البيانات ، والبحث والمراجع.

 استخدم ال[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) صف دراسي'[**معادلة**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)خاصية لإضافة صيغة إلى خلية.**الصيغ المعقدة**، فمثلا

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

، يتم دعمها أيضًا في Aspose.Cells. عند تطبيق صيغة على خلية ، ابدأ دائمًا السلسلة بعلامة يساوي (=) كما تفعل عند إنشاء صيغة في Microsoft Excel واستخدم فاصلة (،) لتحديد معاملات الدالة.

 في المثال أدناه ، يتم تطبيق صيغة معقدة على الخلية الأولى من ورقة العمل[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) مجموعة. تستخدم الصيغة ملف**إذا** الوظيفة المقدمة من Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

## **استخدام الوظائف الإضافية**

يمكن أن يكون لدينا بعض الصيغ التي يحددها المستخدم والتي نريد تضمينها كوظيفة إضافية في Excel. عند ضبط الخلية ، تعمل الوظائف المضمنة لوظيفة الصيغة بشكل جيد ولكن هناك حاجة لتعيين الوظائف أو الصيغ المخصصة باستخدام وظائف الوظيفة الإضافية.

 يوفر Aspose.Cells ميزات لتسجيل الوظائف الإضافية باستخدام[**أوراق العمل.**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index). بعد ذلك عندما قمنا بتعيين cell.Formula = anyFunctionFromAddIn ، يحتوي ملف Excel الناتج على القيمة المحسوبة من الوظيفة الإضافية.

يجب تنزيل ملف XLAM التالي لتسجيل الوظيفة الإضافية في نموذج التعليمات البرمجية أدناه. وبالمثل ، يمكن تنزيل ملف الإخراج "test_udf.xlsx" للتحقق من الإخراج.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

## **باستخدام صيغة المصفوفة**

صيغ الصفيف هي صيغ تأخذ المصفوفات ، بدلاً من الأرقام الفردية ، كوسيطات للدوال التي تشكل الصيغة. عندما يتم عرض صيغة صفيف ، فإنها محاطة بأقواس ({}).

تقوم بعض دالات Microsoft Excel بإرجاع مصفوفات من القيم. لحساب نتائج متعددة باستخدام صيغة صفيف ، أدخل الصفيف في نطاق من الخلايا بنفس عدد الصفوف والأعمدة مثل وسيطات الصفيف.

 من الممكن تطبيق صيغة صفيف على خلية عن طريق استدعاء[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) صف دراسي'[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) طريقة. ال[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) تأخذ الطريقة المعلمات التالية:

- **صيغة المصفوفة**، صيغة الصفيف.
- **عدد الصفوف**، هو عدد الصفوف المراد نشرها نتيجة صيغة الصفيف.
- **عدد الأعمدة**، هو عدد الأعمدة المراد نشرها نتيجة صيغة الصفيف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

## **باستخدام صيغة R1C1**

 إضافة**R1C1** صيغة نمط مرجعي لخلية بامتداد[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) صف دراسي'[**صيغة R1C1**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula) منشأه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

## **موضوعات مسبقة**
- [السوابق والمعالون](/cells/ar/net/precedents-and-dependents/)
- [قم بتعيين الروابط الخارجية في الصيغ](/cells/ar/net/set-external-links-in-formulas/)
- [نشر الصيغة في جدول أو قائمة كائن تلقائيًا أثناء إدخال البيانات في صفوف جديدة](/cells/ar/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [إعداد الصيغة لنطاق مسمى](/cells/ar/net/setting-formula-for-named-range/)
- [إعداد الصيغ - إشعار للمستخدمين غير الإنجليز](/cells/ar/net/setting-formulas-notice-for-non-english-users/)
- [إعداد الصيغة المشتركة](/cells/ar/net/setting-shared-formula/)
- [حدد الحد الأقصى لصفوف الصيغة المشتركة](/cells/ar/net/specify-maximum-rows-of-shared-formula/)
- [وظائف Excel المعتمدة](/cells/ar/net/supported-formula-functions/)

