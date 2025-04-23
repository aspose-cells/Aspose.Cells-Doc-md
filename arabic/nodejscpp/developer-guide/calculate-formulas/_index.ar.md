---
title: حساب الصيغ باستخدام Node.js عبر C++
linktitle: حساب الصيغ
description: يقدم هذا المقال كيفية استخدام مكتبة Aspose.Cells لحساب الصيغ في Microsoft Excel باستخدام Node.js عبر C++. عن طريق تحميل ملف Excel موجود أو إنشاء ملف Excel جديد، يمكننا استخدام الطرق التي توفرها Aspose.Cells لحساب الصيغة والحصول على النتيجة. وأخيرًا، نحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells، Excel، الصيغ، الحسابات، الحساب المباشر للصيغة، حساب الصيغ بشكل متكرر، إضافة الصيغ عبر Node.js عبر C++
type: docs
weight: 125
url: /ar/nodejs-cpp/calculate-formulas/
---

## **إضافة صيغ وحساب النتائج**

تحتوي Aspose.Cells على محرك حساب الصيغ مدمج. فهي لا يمكنها فقط إعادة حساب الصيغ المستوردة من قوالب المصممين، بل تدعم أيضًا حساب نتائج الصيغ المضافة في وقت التشغيل.

يدعم Aspose.Cells معظم الصيغ أو الوظائف التي هي جزء من Microsoft Excel (اقرأ [قائمة الوظائف المدعومة بواسطة محرك الحسابات](/cells/ar/nodejs-cpp/supported-formula-functions/)). يمكن استخدام تلك الوظائف من خلال واجهات برمجة التطبيقات أو تصميم جداول البيانات. يدعم Aspose.Cells مجموعة واسعة من الصيغ الرياضية، النصية، المنطقية، الوقت/التاريخ، الإحصائية، قواعد البيانات، البحث، والمرجع.

استخدم خاصية [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--) أو أساليب [**setFormula(string, object)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setFormula-string-object-) من فئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) لإضافة صيغة إلى خليّة. عند تطبيق صيغة، ابدأ النص بعلامة يساوي (=) كما تفعل عند إنشاء صيغة في Microsoft Excel، واستخدم فاصلة (,) لفصل معلمات الدالة.

لحساب نتائج الصيغ، يمكن للمستخدم استدعاء طريقة [**calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) من فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) التي تعالج جميع الصيغ المدمجة في ملف Excel. أو، يمكن للمستخدم استدعاء طريقة [**calculateFormula(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-) من فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) التي تعالج جميع الصيغ المدمجة في ورقة. أو، يمكن للمستخدم أيضًا استدعاء طريقة [**calculate(CalculationOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#calculate-calculationoptions-) من فئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) التي تعالج صيغة خلية واحدة:

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a value to "A1" cell
worksheet.getCells().get("A1").putValue(1);

// Adding a value to "A2" cell
worksheet.getCells().get("A2").putValue(2);

// Adding a value to "A3" cell
worksheet.getCells().get("A3").putValue(3);

// Adding a SUM formula to "A4" cell
worksheet.getCells().get("A4").setFormula("=SUM(A1:A3)");

// Calculating the results of formulas
workbook.calculateFormula();

// Get the calculated value of the cell
const value = worksheet.getCells().get("A4").getValue().toString();

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **مهم معرفته حول الصيغ**

{{% alert color="primary" %}}

خصائص **Formula** وطرق **setFormula(...)** من فئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) تعمل بشكل مختلف عن طرق **calculate** من الفئات [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) و[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) و[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). خصائص **Formula** وطرق **setFormula(...)** تضيف ببساطة الصيغة إلى الخلية لكن لا تحسب النتيجة أثناء التشغيل. للحصول على نتيجة الصيغ، يرجى استدعاء طرق **calculate**.

{{% /alert %}}

## **حساب مباشر للصيغ**

Aspose.Cells لديه محرك حساب مضمن للصيغ. بالإضافة إلى حساب الصيغ المستوردة من ملف مصمم، يمكن لـ Aspose.Cells حساب نتائج الصيغ مباشرة.

أحيانًا، تحتاج إلى حساب نتائج الصيغ مباشرة دون إضافتها إلى ورقة عمل. القيم المستخدمة في الصيغة موجودة بالفعل في ورقة عمل، وكل ما تحتاج إليه هو العثور على النتيجة لتلك القيم بناءً على صيغة Microsoft Excel دون إضافة الصيغة في ورقة عمل.

يمكنك استخدام واجهات برمجة تطبيقات محرك حساب الصيغ الخاص بـ Aspose.Cells لـ [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) إلى [**calculateFormula(string, FormulaParseOptions, CalculationOptions, number, number, CalculationData)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-formulaparseoptions-calculationoptions-number-number-calculationdata-) لحساب نتائج مثل هذه الصيغ دون إضافتها إلى ورقة العمل:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put 20 in cell A1
const cellA1 = worksheet.getCells().get("A1");
cellA1.putValue(20);

// Put 30 in cell A2
const cellA2 = worksheet.getCells().get("A2");
cellA2.putValue(30);

// Calculate the Sum of A1 and A2
const results = worksheet.calculateFormula("=Sum(A1:A2)");

// Print the output
console.log("Value of A1: " + cellA1.getStringValue());
console.log("Value of A2: " + cellA2.getStringValue());
console.log("Result of Sum(A1:A2): " + results.toString());
```

ينتج الكود أعلاه الناتج التالي:
{{< highlight nodejs >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **كيفية حساب الصيغ بشكل متكرر**

عندما يكون هناك الكثير من الصيغ في دفتر العمل، ويحتاج المستخدم إلى حسابها بشكل متكرر أثناء تعديل جزء صغير منها، قد يكون من المفيد تمكين سلسلة حساب الصيغة: [**formulaSettings.getEnableCalculationChain()**](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getEnableCalculationChain--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load the template workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Print the time before formula calculation
console.log(new Date());

// Set the CreateCalcChain as true
workbook.getSettings().getFormulaSettings().setEnableCalculationChain(true);

// Calculate the workbook formulas
workbook.calculateFormula();

// Print the time after formula calculation
console.log(new Date());

// Change the value of one cell
workbook.getWorksheets().get(0).getCells().get("A1").putValue("newvalue");

// Re-calculate those formulas which depend on cell A1
workbook.calculateFormula();
```

### **مهم معرفته**

{{% alert color="primary" %}}

افتراضيًا، يتم تعطيل سلسلة الحساب. لأن إنشاء السلسلة يتطلب أيضًا وقتًا إضافيًا، فإن المرة الأولى لحساب الصيغ ([**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)) قد تستهلك مزيدًا من وقت معالجة CPU والذاكرة عند مقارنته بحساب الصيغ بدون سلسلة. إذا لم يكن المستخدم بحاجة إلى حساب الصيغ بشكل متكرر، فإن السلوك الافتراضي (حساب الصيغة مباشرة بدون إنشاء سلسلة حساب) هو الخيار الأفضل.

{{% /alert %}}

## **مواضيع متقدمة**
- [إضافة الخلايا إلى نافذة مراقبة صيغ Microsoft Excel](/cells/ar/nodejs-cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [حساب وظيفة IFNA باستخدام Aspose.Cells](/cells/ar/nodejs-cpp/calculating-ifna-function-using-aspose-cells/)
- [حساب الصيغة الصفية للجداول البيانات](/cells/ar/nodejs-cpp/calculation-of-array-formula-of-data-tables/)
- [حساب وظائف MINIFS و MAXIFS في Excel 2016](/cells/ar/nodejs-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [تقليل زمن حساب طريقة Cell.calculate](/cells/ar/nodejs-cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [اكتشاف المراجعة الدائرية](/cells/ar/nodejs-cpp/detecting-circular-reference/)
- [الحساب المباشر للوظيفة المخصصة دون كتابتها في ورقة العمل](/cells/ar/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [تنفيذ محرك الحساب المخصص لتوسيع محرك الحساب الافتراضي لـ Aspose.Cells](/cells/ar/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [إيقاف أو إلغاء حساب الصيغ في سجل العمل](/cells/ar/nodejs-cpp/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [إرجاع مجموعة من القيم باستخدام AbstractCalculationEngine](/cells/ar/nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [ضبط وضع حساب الصيغة في سجل العمل](/cells/ar/nodejs-cpp/setting-formula-calculation-mode-of-workbook/)
- [استخدام وظيفة FormulaText في Aspose.Cells](/cells/ar/nodejs-cpp/using-formulatext-function-in-aspose-cells/)
