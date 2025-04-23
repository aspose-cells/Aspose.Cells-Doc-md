---
title: حساب الصيغ
type: docs
weight: 110
url: /ar/java/calculate-formulas/
---

## **إضافة صيغ وحساب النتائج**

تحتوي Aspose.Cells على محرك حساب مدمج للصيغ. ليس فقط يمكنه إعادة حساب الصيغ المستوردة من قوالب المصمم بل يدعم أيضًا حساب نتائج الصيغ المضافة في وقت التشغيل.

تدعم Aspose.Cells معظم الصيغ أو الوظائف التي تشكل جزءًا من Microsoft Excel (اقرأ [قائمة الوظائف المدعومة من قبل محرك الحساب](/cells/ar/java/supported-formula-functions/)). يمكن استخدام هذه الوظائف من خلال واجهات برمجة التطبيقات أو جداول البيانات المصممة. تدعم Aspose.Cells مجموعة ضخمة من الصيغ الرياضية والسلسلة والبوليان والتاريخ / الوقت والاحصائية وقواعد البيانات والبحث والصيغ المرجعية.

استخدم خصائص [**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) أو طرق [**SetFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setFormula-java.lang.String-com.aspose.cells.FormulaParseOptions-java.lang.Object-) لفئة [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) لإضافة صيغة لخلية. عند تطبيق الصيغة، ابدأ دائمًا السلسلة برمز يساوي (=) كما تفعل عند إنشاء صيغة في Microsoft Excel واستخدم فاصلة (،) لفصل معلمات الدالة.

لحساب نتائج الصيغ، قد ينادي المستخدم على [**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions--) وهي طريقة من فئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) والتي تعالج جميع الصيغ المضمنة في ملف Excel. أو، قد ينادي المستخدم على الطريقة [**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula-com.aspose.cells.CalculationOptions-boolean-) من فئة [**Worsheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) التي تعالج جميع الصيغ المضمنة في ورقة. أو، يمكن للمستخدم أيضًا استدعاء الطريقة [**Calculate**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#calculate-com.aspose.cells.CalculationOptions-) من فئة [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) التي تعالج صيغة خلية واحدة:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulas-CalculatingFormulas.java" >}}

### **مهم معرفته**

{{% alert color="primary" %}}

تختلف خاصية **الصيغة** وطرق **SetFormula(...)** لفئة [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) بشكل عملي عن طرق **Calculate** لفئات [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)، [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) و [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell). تقوم خاصية **الصيغة** وطرق **SetFormula(...)** ببساطة بإضافة الصيغة إلى خلية ولكن لا تحسب النتيجة في وقت التشغيل. للحصول على نتائج الصيغ، يرجى استدعاء طرق **Calculate**.

{{% /alert %}}

## **حساب مباشر للصيغ**

Aspose.Cells لديه محرك حساب مضمن للصيغ. بالإضافة إلى حساب الصيغ المستوردة من ملف مصمم، يمكن لـ Aspose.Cells حساب نتائج الصيغ مباشرة.

في بعض الأحيان، قد تحتاج إلى حساب نتائج الصيغ مباشرة دون إضافتها إلى ورقة عمل. قد تكون قيم الخلايا المستخدمة في الصيغة موجودة بالفعل في ورقة عمل وكل ما تحتاجه هو إيجاد نتيجة تلك القيم بناءً على بعض صيغ Microsoft Excel دون إضافة الصيغة في ورقة عمل.

يمكنك استخدام واجهات برمجة التطبيقات لمحرك حساب الصيغ في Aspose.Cells لـ [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) لـ [**calculate**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula-java.lang.String-com.aspose.cells.CalculationOptions-) نتائج مثل هذه الصيغ دون إضافتها إلى ورقة العمل:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DirectCalculationFormula-DirectCalculationFormula.java" >}}

ينتج الكود أعلاه الناتج التالي:
{{< highlight java >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **حساب الصيغ مرارًا**

عند وجود العديد من الصيغ في دفتر العمل ويحتاج المستخدم إلى حسابها مرارًا مع تعديل جزء صغير فقط منها، يمكن أن يكون من المفيد لأداء الأداء تمكين سلسلة حساب الصيغ: [**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#EnableCalculationChain).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulasOnce-CalculatingFormulasOnce.java" >}}

### **مهم معرفته**

{{% alert color="primary" %}}

افتراضيًا، تتعطل سلسلة الحسابات. لأن إنشاء السلسلة يحتاج أيضًا إلى وقت إضافي، فإن أول عملية حساب للصيغ ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions--) قد تستهلك وقت وحدة معالجة مركزية وذاكرة أكثر عند مقارنته بحساب الصيغ بدون سلسلة. إذا لم يكن المستخدم بحاجة إلى حساب الصيغ بشكل متكرر، فإن السلوك الافتراضي (حساب الصيغة مباشرة بدون إنشاء سلسلة حساب) هو الطريقة الأفضل.

{{% /alert %}}

## **مواضيع متقدمة**
- [إضافة الخلايا إلى نافذة مراقبة صيغ Microsoft Excel](/cells/ar/java/add-cells-to-microsoft-excel-formula-watch-window/)
- [محرك حساب الصيغ في Aspose.Cells](/cells/ar/java/aspose-cells-formula-calculation-engine/)
- [حساب وظيفة IFNA باستخدام Aspose.Cells](/cells/ar/java/calculating-ifna-function-using-aspose-cells/)
- [حساب الصيغة الصفية للجداول البيانات](/cells/ar/java/calculation-of-array-formula-of-data-tables/)
- [حساب وظائف MINIFS و MAXIFS في Excel 2016](/cells/ar/java/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [تقليل وقت الحساب لطريقة Cell.Calculate](/cells/ar/java/decrease-the-calculation-time-of-cell-calculate-method/)
- [اكتشاف المراجعة الدائرية](/cells/ar/java/detecting-circular-reference/)
- [الحساب المباشر للوظيفة المخصصة دون كتابتها في ورقة العمل](/cells/ar/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [تنفيذ محرك الحساب المخصص لتوسيع محرك الحساب الافتراضي لـ Aspose.Cells](/cells/ar/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [إيقاف أو إلغاء حساب الصيغ في سجل العمل](/cells/ar/java/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [إرجاع مجموعة من القيم باستخدام AbstractCalculationEngine](/cells/ar/java/returning-a-range-of-values-using-abstractcalculationengine/)
- [إرجاع مجموعة من القيم باستخدام ICustomFunction](/cells/ar/java/returning-a-range-of-values-using-icustomfunction/)
- [استخدام ميزة ICustomFunction](/cells/ar/java/using-icustomfunction-feature/)
{{< app/cells/assistant language="java" >}}
