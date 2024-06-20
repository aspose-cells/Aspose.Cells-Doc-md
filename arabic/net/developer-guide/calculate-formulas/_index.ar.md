---
title: حساب الصيغ
description: يقدم هذا المقال كيفية استخدام مكتبة Aspose.Cells لحساب الصيغ في Microsoft Excel. من خلال تحميل ملف Excel موجود أو إنشاء ملف Excel جديد، يمكننا استخدام الطرق المقدمة من قبل Aspose.Cells لحساب الصيغة والحصول على النتيجة. في النهاية، نقوم بحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells، Excel، صيغ، حسابات، الحساب المباشر للصيغة، حساب الصيغة بشكل متكرر، إضافة الصيغ وحساب النتائج.
type: docs
weight: 125
url: /ar/net/calculate-formulas/
---

## **إضافة صيغ وحساب النتائج**

تحتوي Aspose.Cells على محرك حساب مدمج للصيغ. ليس فقط يمكنه إعادة حساب الصيغ المستوردة من قوالب المصمم بل يدعم أيضًا حساب نتائج الصيغ المضافة في وقت التشغيل.

يدعم Aspose.Cells معظم الصيغ أو الوظائف التي تُعتبر جزءًا من Microsoft Excel (اقرأ [قائمة الوظائف المدعومة من قبل محرك الحساب](/cells/ar/net/supported-formula-functions/)). يمكن استخدام هذه الوظائف من خلال واجهات برمجة التطبيقات أو جداول البيانات التي يصممها المستخدم. تدعم Aspose.Cells مجموعة كبيرة من الصيغ الرياضية والنصية والمنطقية والتاريخية/الزمنية والإحصائية وقواعد البيانات والبحث والمرجعية.

استخدم خصائص [**Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) أو طرق [**SetFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2) لفئة [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) لإضافة صيغة لخلية. عند تطبيق الصيغة، ابدأ دائمًا السلسلة برمز يساوي (=) كما تفعل عند إنشاء صيغة في Microsoft Excel واستخدم فاصلة (،) لفصل معلمات الدالة.

لحساب نتائج الصيغ، يمكن للمستخدم استدعاء الطريقة [**CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1) لفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) التي تقوم بمعالجة جميع الصيغ المضمنة في ملف Excel. أو، يمكن للمستخدم استدعاء الطريقة [**CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula) لفئة [**Worsheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) التي تقوم بمعالجة جميع الصيغ المضمنة في ورقة. أو، يمكن أيضًا للمستخدم استدعاء الطريقة [**Calculate**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate) لفئة [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) التي تقوم بمعالجة صيغة خلية واحدة:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

### **مهم معرفته حول الصيغ**

{{% alert color="primary" %}}

تختلف خاصية **الصيغة** وطرق **SetFormula(...)** لفئة [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) بشكل عملي عن طرق **Calculate** لفئات [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)، [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) و [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). تقوم خاصية **الصيغة** وطرق **SetFormula(...)** ببساطة بإضافة الصيغة إلى خلية ولكن لا تحسب النتيجة في وقت التشغيل. للحصول على نتائج الصيغ، يرجى استدعاء طرق **Calculate**.

{{% /alert %}}

## **حساب مباشر للصيغ**

Aspose.Cells لديه محرك حساب مضمن للصيغ. بالإضافة إلى حساب الصيغ المستوردة من ملف مصمم، يمكن لـ Aspose.Cells حساب نتائج الصيغ مباشرة.

في بعض الأحيان، قد تحتاج إلى حساب نتائج الصيغ مباشرة دون إضافتها إلى ورقة عمل. قد تكون قيم الخلايا المستخدمة في الصيغة موجودة بالفعل في ورقة عمل وكل ما تحتاجه هو إيجاد نتيجة تلك القيم بناءً على بعض صيغ Microsoft Excel دون إضافة الصيغة في ورقة عمل.

يمكنك استخدام واجهات برمجة التطبيقات لمحرك حساب الصيغ في Aspose.Cells لـ [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) لـ [**calculate**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) نتائج مثل هذه الصيغ دون إضافتها إلى ورقة العمل:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

ينتج الكود أعلاه الناتج التالي:
{{< highlight net >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **كيفية حساب الصيغ بشكل متكرر**

عند وجود العديد من الصيغ في دفتر العمل ويحتاج المستخدم إلى حسابها مرارًا مع تعديل جزء صغير فقط منها، يمكن أن يكون من المفيد لأداء الأداء تمكين سلسلة حساب الصيغ: [**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

### **مهم معرفته**

{{% alert color="primary" %}}

بشكل افتراضي، يتم تعطيل سلسلة الحساب. لأن إنشاء السلسلة يحتاج أيضًا إلى وقت إضافي، يمكن أن يستهلك الوقت الأول من حساب الصيغ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)) المزيد من وحدة معالجة المركز والذاكرة مقارنةً بحساب الصيغ بدون سلسلة. إذا لم يكن المستخدم بحاجة إلى حساب الصيغ مرارًا، فإن السلوك الافتراضي (حساب الصيغ مباشرةً دون إنشاء سلسلة حساب) يجب أن يكون الطريقة الأفضل.

{{% /alert %}}


## **مواضيع متقدمة**
- [إضافة الخلايا إلى نافذة مراقبة صيغ Microsoft Excel](/cells/ar/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [حساب وظيفة IFNA باستخدام Aspose.Cells](/cells/ar/net/calculating-ifna-function-using-aspose-cells/)
- [حساب الصيغة الصفية للجداول البيانات](/cells/ar/net/calculation-of-array-formula-of-data-tables/)
- [حساب وظائف MINIFS و MAXIFS في Excel 2016](/cells/ar/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [تقليل وقت الحساب لطريقة Cell.Calculate](/cells/ar/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [اكتشاف المراجعة الدائرية](/cells/ar/net/detecting-circular-reference/)
- [الحساب المباشر للوظيفة المخصصة دون كتابتها في ورقة العمل](/cells/ar/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [تنفيذ محرك الحساب المخصص لتوسيع محرك الحساب الافتراضي لـ Aspose.Cells](/cells/ar/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [إيقاف أو إلغاء حساب الصيغ في سجل العمل](/cells/ar/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [إرجاع مجموعة من القيم باستخدام AbstractCalculationEngine](/cells/ar/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [إرجاع مجموعة من القيم باستخدام ICustomFunction](/cells/ar/net/returning-a-range-of-values-using-icustomfunction/)
- [ضبط وضع حساب الصيغة في سجل العمل](/cells/ar/net/setting-formula-calculation-mode-of-workbook/)
- [استخدام وظيفة FormulaText في Aspose.Cells](/cells/ar/net/using-formulatext-function-in-aspose-cells/)
- [استخدام ميزة ICustomFunction](/cells/ar/net/using-icustomfunction-feature/)
