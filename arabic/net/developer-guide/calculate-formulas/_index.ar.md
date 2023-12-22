---
title: حساب الصيغ
description: تقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells لحساب الصيغ في Microsoft Excel. من خلال تحميل ملف Excel موجود أو إنشاء ملف Excel جديد، يمكننا استخدام الطرق التي يوفرها Aspose.Cells لحساب الصيغة والحصول على النتيجة. وأخيرًا، نقوم بحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells, Excel, formulas, calculations, Direct Calculation of Formula, Calculate Formulas repeatedly, add formulas.
type: docs
weight: 125
url: /ar/net/calculate-formulas/
---
##  **إضافة الصيغ وحساب النتائج**

يحتوي Aspose.Cells على محرك حساب الصيغة المضمن. لا يمكنه فقط إعادة حساب الصيغ المستوردة من قوالب المصمم ولكنه يدعم أيضًا حساب نتائج الصيغ المضافة في وقت التشغيل.

 Aspose.Cells يدعم معظم الصيغ أو الوظائف التي تشكل جزءا من Microsoft Excel (قراءة[قائمة الوظائف التي يدعمها محرك الحساب](/cells/ar/net/supported-formula-functions/)). يمكن استخدام هذه الوظائف من خلال واجهات برمجة التطبيقات أو جداول بيانات المصمم. Aspose.Cells يدعم مجموعة ضخمة من الصيغ الرياضية، والسلسلة، والمنطقية، والتاريخ/الوقت، والصيغ الإحصائية، وقاعدة البيانات، والبحث، والمرجع.

 استخدم ال[**معادلة**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) الملكية أو[**صيغة المجموعة (...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2) أساليب[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)فئة لإضافة صيغة إلى خلية. عند تطبيق صيغة، ابدأ دائمًا السلسلة بعلامة التساوي (=) كما تفعل عند إنشاء صيغة في Microsoft Excel واستخدم الفاصلة (،) لتحديد معلمات الدالة.

 لحساب نتائج الصيغ، يمكن للمستخدم استدعاء[**CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1) طريقة[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تعالج جميع الصيغ المضمنة في ملف Excel. أو يمكن للمستخدم الاتصال بـ[**CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula) طريقة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة تعالج جميع الصيغ المضمنة في الورقة. أو يمكن للمستخدم أيضًا الاتصال بـ[**احسب**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate) طريقة[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)الفئة التي تعالج صيغة واحدة Cell:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

###  **من المهم أن نعرف عن الصيغ**

{{% alert color="primary" %}}

 ال**معادلة** الملكية و**صيغة المجموعة (...)** أساليب[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)يعمل الفصل بشكل مختلف عن**احسب** أساليب[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook), [**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) و[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) الطبقات. ال**معادلة** الملكية و**صيغة المجموعة (...)** تقوم الطرق ببساطة بإضافة الصيغة إلى خلية ولكن لا تحسب النتيجة في وقت التشغيل. للحصول على نتيجة المعادلات الرجاء الاتصال على الرقم**احسب** طُرق.

{{% /alert %}}

##  **الحساب المباشر للصيغة**

يحتوي Aspose.Cells على محرك حساب الصيغة المضمن. بالإضافة إلى حساب الصيغ المستوردة من ملف المصمم، يمكن لـ Aspose.Cells حساب نتائج الصيغ مباشرة.

في بعض الأحيان، تحتاج إلى حساب نتائج الصيغة مباشرة دون إضافتها إلى ورقة العمل. قيم الخلايا المستخدمة في الصيغة موجودة بالفعل في ورقة العمل وكل ما تحتاجه هو العثور على نتيجة تلك القيم بناءً على بعض صيغ Excel Microsoft دون إضافة الصيغة في ورقة العمل.

 يمكنك استخدام واجهات برمجة التطبيقات لمحرك حساب الصيغة Aspose.Cells لـ[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) ل[**احسب**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) نتائج هذه الصيغ دون إضافتها إلى ورقة العمل:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

الكود أعلاه ينتج المخرجات التالية:
{{< highlight "net" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

##  **كيفية حساب الصيغ بشكل متكرر**

عندما يكون هناك الكثير من الصيغ في المصنف ويحتاج المستخدم إلى حسابها بشكل متكرر مع تعديل جزء صغير منها فقط، فقد يكون من المفيد للأداء تمكين سلسلة حساب الصيغة:[**FormulaSettings.EnableCaculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

###  **من المهم أن تعرف**

{{% alert color="primary" %}}

بشكل افتراضي، يتم تعطيل سلسلة الحساب. لأن إنشاء السلسلة يحتاج أيضًا إلى وقت إضافي، أول مرة لحساب الصيغ ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)) قد يستهلك المزيد من وقت معالجة وحدة المعالجة المركزية والذاكرة عند مقارنتها بحساب الصيغ بدون سلسلة. إذا لم يكن المستخدم بحاجة إلى حساب الصيغ بشكل متكرر، فيجب أن يكون السلوك الافتراضي (حساب الصيغة مباشرة دون إنشاء سلسلة حسابية) هو الطريقة الأفضل.

{{% /alert %}}


##  **مواضيع متقدمة**
- [أضف Cells إلى Microsoft نافذة مراقبة صيغة Excel](/cells/ar/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [حساب دالة IFNA باستخدام Aspose.Cells](/cells/ar/net/calculating-ifna-function-using-aspose-cells/)
- [حساب صيغة صفيف جداول البيانات](/cells/ar/net/calculation-of-array-formula-of-data-tables/)
- [حساب وظائف MINIFS وMAXIFS في Excel 2016](/cells/ar/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [تقليل وقت الحساب Cell.طريقة الحساب](/cells/ar/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [الكشف عن المرجع الدائري](/cells/ar/net/detecting-circular-reference/)
- [الحساب المباشر للوظيفة المخصصة دون كتابتها في ورقة عمل](/cells/ar/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [قم بتنفيذ محرك الحساب المخصص لتوسيع محرك الحساب الافتراضي لـ Aspose.Cells](/cells/ar/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [مقاطعة أو إلغاء حساب الصيغة للمصنف](/cells/ar/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [إرجاع نطاق من القيم باستخدام AbstractCalculationEngine](/cells/ar/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [إرجاع نطاق من القيم باستخدام ICustomFunction](/cells/ar/net/returning-a-range-of-values-using-icustomfunction/)
- [ضبط وضع حساب الصيغة في المصنف](/cells/ar/net/setting-formula-calculation-mode-of-workbook/)
- [استخدام وظيفة FormulaText في Aspose.Cells](/cells/ar/net/using-formulatext-function-in-aspose-cells/)
- [استخدام ميزة ICustomFunction](/cells/ar/net/using-icustomfunction-feature/)
