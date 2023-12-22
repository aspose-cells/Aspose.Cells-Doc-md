---
title: طرق لحساب الصيغ
type: docs
weight: 30
url: /ar/cpp/ways-to-calculate-formulas/
---
##  **مقدمة**
يحتوي Aspose.Cells على محرك حساب الصيغة المضمن. لا يمكنه إعادة حساب الصيغ المستوردة من قوالب المصمم فحسب، بل يدعم أيضًا حساب نتائج الصيغ المضافة في وقت التشغيل.
##  **إضافة الصيغ وحساب النتائج**
Aspose.Cells يدعم معظم الصيغ أو الوظائف التي تشكل جزءًا من Microsoft Excel. يمكن استخدامها من خلال API أو باستخدام جداول بيانات المصمم. Aspose.Cells يدعم مجموعة ضخمة من الصيغ الرياضية، والسلسلة، والمنطقية، والتاريخ/الوقت، والصيغ الإحصائية، والبحث والمرجع.

استخدم الأسلوب Cell.SetFormula لإضافة صيغة إلى خلية. عند تطبيق صيغة على خلية، ابدأ دائمًا السلسلة بعلامة التساوي (=) كما تفعل عند إنشاء صيغة في Microsoft Excel. استخدم الفاصلة (،) لتحديد معلمات الوظيفة.

لحساب نتائج الصيغ، قم باستدعاء الأسلوب Workbook.CalculateFormula() الذي يعالج كافة الصيغ المضمنة في ملف Excel. الرجاء مراجعة نموذج التعليمات البرمجية التالي الذي يضيف الصيغة ويحسب نتائجها. رجاء تاكد من[إخراج ملف إكسل](38109185.xlsx) تم إنشاؤها باستخدام هذا الرمز.

**عينة من الرموز**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-AddingFormulasAndCalculatingResults-new.cpp" >}}
<!---## **Direct Calculation of Formula**
Sometimes, you need to calculate formula results directly without adding them into a worksheet. The values of the cells used in the formula already exist in a worksheet and all you need is to find the result of those values based on some Microsoft Excel formula without adding the formula in a worksheet.

You can use Worksheet.CalculateFormula(String formula) method to calculate the results of such formulas without adding them to worksheet.

The code below produces the following output.

{{< highlight java >}}

 Value of A1: 20

Value of A2: 30

Result of Sum(A1:A2): 50

{{< /highlight >}}

**Sample Code**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-DirectCalculationOfFormula.cpp" >}}   --->
##  **حساب الصيغ مرة واحدة فقط**
عند استدعاء Workbook.CalculateFormula() لحساب قيم الصيغ في قالب مصنف، يقوم Aspose.Cells بإنشاء سلسلة حسابية. يعمل على زيادة الأداء عند حساب الصيغ للمرة الثانية أو الثالثة.

ومع ذلك، إذا كان القالب يحتوي على الكثير من الصيغ، فإن المرة الأولى التي يتم فيها حساب الصيغة يمكن أن تستهلك الكثير من وقت معالجة وحدة المعالجة المركزية والذاكرة.

Aspose.Cells يسمح لك بإيقاف تشغيل إنشاء سلسلة حسابية وهو أمر مفيد عندما تريد حساب الصيغ مرة واحدة فقط.

 الرجاء الاتصال بـ Workbook.GetISettings().SetCreateCalcChain() باستخدام معلمة خاطئة. يمكنك استخدام ال[تم توفير ملف اكسيل](38109186.xlsx) لاختبار هذا الرمز.

**عينة من الرموز**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-CalculatingFormulasOnceOnly-new.cpp" >}}
