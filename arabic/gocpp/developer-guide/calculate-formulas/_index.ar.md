---
title: حساب الصيغ باستخدام Golang عبر C++
linktitle: حساب الصيغ
description: تقدم هذه المقالة شرحًا لكيفية استخدام مكتبة Aspose.Cells لحساب الصيغ في Microsoft Excel باستخدام Golang عبر C++. عن طريق تحميل ملف Excel موجود أو إنشاء ملف Excel جديد، يمكننا استخدام الطرق التي توفرها Aspose.Cells لحساب الصيغة والحصول على النتيجة. أخيرًا، نحفظ الملف المعدل على القرص.
keywords: Aspose.Cells، Excel، صيغ، حسابات، الحساب المباشر للصيغة، حساب الصيغة بشكل متكرر، إضافة الصيغ وحساب النتائج.
type: docs
weight: 125
url: /ar/go-cpp/calculate-formulas/
---

## **إضافة صيغ وحساب النتائج**

تحتوي Aspose.Cells على محرك حساب الصيغ مدمج. فهي لا يمكنها فقط إعادة حساب الصيغ المستوردة من قوالب المصممين، بل تدعم أيضًا حساب نتائج الصيغ المضافة في وقت التشغيل.

تدعم Aspose.Cells معظم الصيغ أو الوظائف التي تشكل جزءًا من Microsoft Excel (اقرأ [قائمة الوظائف المدعومة بواسطة محرك الحسابات]( /cells/ar/cpp/supported-formula-functions/ )). يمكن استخدام تلك الوظائف عبر واجهات برمجة التطبيقات أو جداول المصممين. تدعم Aspose.Cells مجموعة كبيرة من الصيغ الرياضية، والنصية، والمنطقية، والتاريخ/الوقت، والإحصائية، وقواعد البيانات، والبحث، والإشارة.

استخدم خاصية [**GetFormula**](https://reference.aspose.com/cells/go-cpp/cell/getformula/) أو أساليب [**SetFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setformula/) من فئة [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) لإضافة صيغة إلى خليّة. عند تطبيق صيغة، ابدأ النص بعلامة يساوي (=) كما تفعل عند إنشاء صيغة في Microsoft Excel، واستخدم فاصلة (,) لفصل معلمات الدالة.

لحساب نتائج الصيغ، يمكن للمستخدم استدعاء أسلوب [**CalculateFormula**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) من فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)، الذي يعالج جميع الصيغ المدمجة في ملف Excel. أو، يمكن للمستخدم استدعاء أسلوب [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) من فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)، الذي يعالج جميع الصيغ المدمجة في ورقة. أو، يمكن للمستخدم أيضًا استدعاء أسلوب [**Calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/calculate/) من فئة [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)، الذي يعالج صيغة خلية واحدة:**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas.go" >}}
### **مهم معرفته حول الصيغ**

{{% alert color="primary" %}}

خصيتي **GetFormula** و **SetFormula(...)** من فئة [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) تعمل بشكل مختلف عن أساليب **Calculate** من الفئات [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) و [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) و [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/). تقوم خصائص **GetFormula** و **SetFormula(...)** ببساطة بإضافة الصيغة إلى خلية، ولكنها لا تحسب النتيجة أثناء التشغيل. للحصول على نتيجة الصيغ، يرجى استدعاء أساليب **Calculate**.

{{% /alert %}}

## **حساب مباشر للصيغ**

Aspose.Cells لديه محرك حساب مضمن للصيغ. بالإضافة إلى حساب الصيغ المستوردة من ملف مصمم، يمكن لـ Aspose.Cells حساب نتائج الصيغ مباشرة.

أحيانًا، تحتاج إلى حساب نتائج الصيغ مباشرة دون إضافتها إلى ورقة عمل. القيم المستخدمة في الصيغة موجودة بالفعل في ورقة عمل، وكل ما تحتاج إليه هو العثور على النتيجة لتلك القيم بناءً على صيغة Microsoft Excel دون إضافة الصيغة في ورقة عمل.

يمكنك استخدام واجهات برمجة تطبيقات محرك حساب الصيغ الخاص بـ Aspose.Cells لـ [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) إلى [**calculate**](https://reference.aspose.com/cells/go-cpp/worksheet/calculateformula/) لحساب نتائج مثل هذه الصيغ دون إضافتها إلى ورقة العمل:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas-1.go" >}}
ينتج الكود أعلاه الناتج التالي:
{{< highlight cpp >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **كيفية حساب الصيغ بشكل متكرر**

عندما يكون هناك العديد من الصيغ في دفتر العمل ويحتاج المستخدم إلى حسابها بشكل متكرر مع تعديل جزء صغير فقط منها، قد يكون من المفيد لتحسين الأداء تفعيل سلسلة حساب الصيغة: [**FormulaSettings.GetEnableCalculationChain()**](https://reference.aspose.com/cells/go-cpp/formulasettings/getenablecalculationchain/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas-2.go" >}}
### **مهم معرفته**

{{% alert color="primary" %}}

افتراضيًا، تكون سلسلة الحساب معطلة. لأن إنشاء السلسلة يتطلب وقتًا إضافيًا، قد يستهلك حساب الصيغ ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/)) في المرة الأولى مزيدًا من وقت المعالجة لوحدة المعالجة المركزية والذاكرة مقارنةً بحساب الصيغ بدون سلسلة. إذا لم يكن المستخدم بحاجة إلى حساب الصيغ بشكل متكرر، فإن السلوك الافتراضي (حساب الصيغة مباشرة بدون إنشاء سلسلة حساب) هو الطريقة الأفضل على الأرجح.

{{% /alert %}}

## **الموضوعات المتقدمة**
- [إضافة الخلايا إلى نافذة مراقبة صيغ Microsoft Excel](/cells/ar/cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [حساب وظيفة IFNA باستخدام Aspose.Cells](/cells/ar/cpp/calculating-ifna-function-using-aspose-cells/)
- [حساب الصيغة الصفية للجداول البيانات](/cells/ar/cpp/calculation-of-array-formula-of-data-tables/)
- [حساب وظائف MINIFS و MAXIFS في Excel 2016](/cells/ar/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [تقليل وقت الحساب لطريقة Cell.Calculate](/cells/ar/cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [الحساب المباشر للوظيفة المخصصة دون كتابتها في ورقة العمل](/cells/ar/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [تنفيذ محرك الحساب المخصص لتوسيع محرك الحساب الافتراضي لـ Aspose.Cells](/cells/ar/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [إرجاع مجموعة من القيم باستخدام AbstractCalculationEngine](/cells/ar/cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [ضبط وضع حساب الصيغة في سجل العمل](/cells/ar/cpp/setting-formula-calculation-mode-of-workbook/)
- [استخدام وظيفة FormulaText في Aspose.Cells](/cells/ar/cpp/using-formulatext-function-in-aspose-cells/)
