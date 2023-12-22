---
title: إدارة صيغ ملفات Excel
linktitle: الصيغ
type: docs
weight: 122
url: /ar/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells يمكنه ببساطة الحصول على صيغ ملفات Excel وتعيينها وحسابها.
description: تعرف على كيفية إدارة صيغ ملفات Excel من خلال Aspose.Cells لـ NET APIs.
keywords: How to calculate formulas in C#, Formulas and Functions using C#, C# Manage Built-in Functions, How to Use Add-in Functions with C#, How to Use Array Formula via C#, How to Use R1C1 Formula in C#.
---
##  **مقدمة**

إحدى ميزات Excel الجذابة Microsoft هي قدرته على معالجة البيانات باستخدام الصيغ والوظائف. Microsoft يوفر Excel مجموعة من الوظائف والصيغ المضمنة التي تساعد المستخدمين على إجراء العمليات الحسابية المعقدة بسرعة. يوفر Aspose.Cells أيضًا مجموعة ضخمة من الوظائف والصيغ المضمنة التي تساعد المطورين على حساب القيم بسهولة. Aspose.Cells يدعم أيضًا وظائف الوظيفة الإضافية. علاوة على ذلك، Aspose.Cells يدعم المصفوفة وصيغ R1C1 في Aspose.Cells.

##  **كيفية استخدام الصيغ والوظائف**

 Aspose.Cells يوفر فئة،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يحتوي الفصل على أ[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) المجموعة التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فصل. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) يوفر الفصل أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. يمثل كل عنصر في مجموعة Cells كائنًا من[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) فصل.

 من الممكن تطبيق الصيغ على الخلايا باستخدام الخصائص والأساليب التي يوفرها[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) الطبقة، والتي تمت مناقشتها بمزيد من التفاصيل أدناه.

- استخدام الوظائف المضمنة.
- استخدام الوظائف الإضافية.
- العمل مع صيغ المصفوفة.
- إنشاء صيغة R1C1.

##  **كيفية استخدام الوظائف المضمنة**

يتم توفير الوظائف أو الصيغ المضمنة كوظائف جاهزة لتقليل جهود المطورين ووقتهم. يرى[قائمة الوظائف المضمنة](/cells/ar/net/supported-formula-functions/) بدعم من Aspose.Cells. يتم سرد الوظائف حسب الترتيب الأبجدي. سيتم دعم المزيد من الوظائف في المستقبل.

 Aspose.Cells يدعم معظم الصيغ أو الوظائف التي يقدمها Microsoft Excel. يمكن للمطورين استخدام هذه الصيغ من خلال API أو[جدول بيانات المصمم](/cells/ar/net/what-is-a-designer-spreadsheet/). Aspose.Cells يدعم مجموعة ضخمة من الصيغ الرياضية، والسلسلة، والمنطقية، والتاريخ/الوقت، والصيغ الإحصائية، وقاعدة البيانات، والبحث والمرجع.

 استخدم ال[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) فصل'[**معادلة**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) خاصية إضافة صيغة إلى خلية. *الصيغ المعقدة**، على سبيل المثال

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

، مدعومة أيضًا في Aspose.Cells. عند تطبيق صيغة على خلية، ابدأ السلسلة دائمًا بعلامة التساوي (=) كما تفعل عند إنشاء صيغة في Microsoft Excel واستخدم الفاصلة (،) لتحديد معلمات الدالة.

 في المثال أدناه، يتم تطبيق صيغة معقدة على الخلية الأولى في ورقة العمل[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)مجموعة. تستخدم الصيغة مدمجًا**IF** الوظيفة المقدمة من Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

##  **كيفية استخدام الوظائف الإضافية**

يمكن أن يكون لدينا بعض الصيغ التي يحددها المستخدم والتي نريد تضمينها كوظيفة إضافية في برنامج Excel. عند تعيين الخلية. تعمل الوظائف المضمنة لوظيفة الصيغة بشكل جيد ولكن هناك حاجة لتعيين الوظائف أو الصيغ المخصصة باستخدام الوظائف الإضافية.

 يوفر Aspose.Cells ميزات لتسجيل الوظائف الإضافية باستخدام[**أوراق العمل.تسجيل AddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index). بعد ذلك عندما نقوم بتعيين cell.Formula = AnyFunctionFromAddIn، يحتوي ملف Excel الناتج على القيمة المحسوبة من وظيفة AddIn.

يجب تنزيل الملف التالي XLAM لتسجيل الوظيفة الإضافية في نموذج التعليمات البرمجية أدناه. وبالمثل، يمكن تنزيل ملف الإخراج "test_udf.xlsx" للتحقق من الإخراج.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

##  **كيفية استخدام صيغة المصفوفة**

صيغ الصفيف هي صيغ تستخدم الصفائف، بدلاً من الأرقام الفردية، كوسائط للوظائف التي تشكل الصيغة. عندما يتم عرض صيغة صفيف، تكون محاطة بأقواس ({}).

تقوم بعض وظائف Excel Microsoft بإرجاع صفائف من القيم. لحساب نتائج متعددة باستخدام صيغة صفيف، أدخل الصفيف في نطاق من الخلايا يحتوي على نفس عدد الصفوف والأعمدة مثل وسيطات الصفيف.

 من الممكن تطبيق صيغة صفيف على خلية عن طريق استدعاء[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) فصل'[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) طريقة. ال[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) تأخذ الطريقة المعلمات التالية:

- *صيغة المصفوفة**، صيغة المصفوفة.
- *عدد الصفوف**، عدد الصفوف المراد ملؤها بنتيجة صيغة الصفيف.
- *عدد الأعمدة**، عدد الأعمدة المراد ملؤها بنتيجة صيغة الصفيف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

##  **كيفية استخدام صيغة R1C1**

 إضافة**R1C1** صيغة النمط المرجعية إلى خلية تحتوي على[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) فصل'[**صيغة R1C1**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula) ملكية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

##  **مواضيع متقدمة**
- [السوابق والمعالين](/cells/ar/net/precedents-and-dependents/)
- [تعيين الروابط الخارجية في الصيغ](/cells/ar/net/set-external-links-in-formulas/)
- [نشر الصيغة في الجدول أو كائن القائمة تلقائيًا أثناء إدخال البيانات في صفوف جديدة](/cells/ar/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [إعداد الصيغة للنطاق المسمى](/cells/ar/net/setting-formula-for-named-range/)
- [ضبط الصيغ - إشعار للمستخدمين غير الناطقين باللغة الإنجليزية](/cells/ar/net/setting-formulas-notice-for-non-english-users/)
- [إعداد الصيغة المشتركة](/cells/ar/net/setting-shared-formula/)
- [تحديد الحد الأقصى لصفوف الصيغة المشتركة](/cells/ar/net/specify-maximum-rows-of-shared-formula/)
- [وظائف Excel المدعومة](/cells/ar/net/supported-formula-functions/)

