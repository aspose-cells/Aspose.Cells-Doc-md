---
title: إدارة صيغ ملفات إكسل مع Node.js عبر C++
linktitle: الصيغ
type: docs
weight: 122
url: /ar/nodejs-cpp/using-formulas-or-functions-to-process-data/
description: تعلم كيف تدير صيغ ملفات إكسل عبر Aspose.Cells for Node.js via C++. يمكن لـ Aspose.Cells ببساطة الحصول على الصيغ وتعيينها وحسابها.
keywords: كيفية حساب الصيغ في Node.js عبر C++، الصيغ الدوال باستخدام Node.js عبر C++، إدارة الدوال المدمجة في Node.js عبر C++، كيفية استخدام وظائف الإضافة مع Node.js عبر C++، كيفية استخدام صيغ المصفوفة عبر Node.js عبر C++، كيفية استخدام صيغة R1C1 في Node.js عبر C++.
---

## **مقدمة**

واحدة من الميزات المثيرة في Microsoft Excel هي قدرته على معالجة البيانات باستخدام الصيغ والدوال. يوفر Microsoft Excel مجموعة من الدوال والصيغ المدمجة التي تساعد المستخدمين على إجراء حسابات معقدة بسرعة. كما توفر Aspose.Cells مجموعة كبيرة من الدوال والصيغ المدمجة التي تساعد المطورين على حساب القيم بسهولة. كما تدعم Aspose.Cells وظائف الإضافة. بالإضافة إلى ذلك، تدعم Aspose.Cells الصيغ المُصفوفة وصيغ R1C1.

## **كيفية استخدام الصيغ والوظائف**

يوفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تُمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). يمثل كل عنصر في مجموعة Cells كائنًا من الفئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

من الممكن تطبيق الصيغ على الخلايا باستخدام الخصائص والأساليب التي يقدمها الفئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)، كما هو موضح بالتفصيل أدناه.

- باستخدام الوظائف الداخلية.
- باستخدام وظائف الإضافة.
- العمل مع صيغ الصيغة السابقة.
- إنشاء صيغة R1C1.

## **كيفية استخدام الوظائف المضمنة**

توفر الوظائف أو الصيغ المدمجة كدوال جاهزة لتقليل جهود ووقت المطورين. راجع [قائمة الدوال المدمجة](/cells/ar/nodejs-cpp/supported-formula-functions/) المدعومة من قبل Aspose.Cells. تُذكر الدوال بترتيب أبجدي. سيتم دعم المزيد من الدوال في المستقبل.

تدعم Aspose.Cells معظم الصيغ أو الدوال التي تقدمها Microsoft Excel. يمكن للمطورين استخدام هذه الصيغ من خلال واجهة البرمجة أو [مفكر الجدول](/cells/ar/nodejs-cpp/what-is-a-designer-spreadsheet/). تدعم Aspose.Cells مجموعة ضخمة من الصيغ الرياضية، النصية، المنطقية، التاريخ/الوقت، الإحصائية، قواعد البيانات، البحث، المرجع.

استخدم خاصية [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--) للصف ال [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) لإضافة صيغة إلى خلية. **الصيغ المعقدة**, مثل

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, مدعومة أيضًا في Aspose.Cells. عند تطبيق صيغة على خلية، يجب دائمًا بدء السلسلة بعلامة يساوي (=) كما تفعل عند إنشاء صيغة في Microsoft Excel واستخدام فاصلة (,) لفصل معلمات الوظيفة.

في المثال أدناه، يتم تطبيق صيغة معقدة على خلية الصفراء من مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). تستخدم الصيغة الوظيفة المضمنة **IF** المقدمة بواسطة Aspose.Cells.

```javascript
const path = require("path");
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

## **كيفية استخدام الوظائف المضافة**

يمكننا أن يكون لدينا بعض الصيغ التي تم تحديدها من قبل المستخدم ونريد تضمينها كوظيفة إكسل إضافية. عند ضبط وظيفة الخلية. تعمل الوظائف المضمنة بشكل جيد ومع ذلك يوجد حاجة لضبط الوظائف المخصصة أو الصيغ باستخدام الوظائف الإضافية.

توفر Aspose.Cells ميزات لتسجيل وظائف الإضافات باستخدام [**Worksheets.registerAddInFunction(string, string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#registerAddInFunction-string-string-boolean-). بعد ذلك عند ضبط cell.Formula = anyFunctionFromAddIn، يحتوي ملف Excel الناتج على القيمة المحسوبة من وظيفة الإضافة.

يجب تنزيل ملف XLAM التالي لتسجيل وظيفة الإضافة في عينة الكود أدناه. بالمثل، يمكن تنزيل الملف الناتج "test_udf.xlsx" لفحص الناتج.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Register macro enabled add-in along with the function name
const id = workbook.getWorksheets().registerAddInFunction(path.join(dataDir, "TESTUDF.xlam"), "TEST_UDF", false);

// Register more functions in the file (if any)
workbook.getWorksheets().registerAddInFunction(id, "TEST_UDF1"); // in this way you can add more functions that are in the same file

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first cell
const cell = worksheet.getCells().get("A1");

// Set formula name present in the add-in
cell.setFormula("=TEST_UDF()");

// Save workbook to output XLSX format.
workbook.save(path.join(outputDir, "test_udf.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **كيفية استخدام صيغة مصفوفة**

صيغ المصفوفة هي صيغ تأخذ مصفوفات، بدلاً من الأرقام الفردية، كتغيرات لوظائف تكون الصيغة. عند عرض صيغة المصفوفة، يكون محاطًا بالأقواس الإعتيادية ({}).

تعيد بعض وظائف Microsoft Excel مصفوفات القيم. لحساب نتائج متعددة باستخدام صيغة مصفوفة، أدخل المصفوفة في نطاق الخلايا بعدد الصفوف والأعمدة نفس معدلات الوسائط المصفوفات.

من الممكن تطبيق صيغة مصفوفة على خلية عن طريق استدعاء الوظيفة [**setArrayFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setArrayFormula-string-number-number-) الخاصة بفئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). تأخذ الوظيفة [**setArrayFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setArrayFormula-string-number-number-) معلمات التالية:

- **صيغة مصفوفة**, صيغة المصفوفة.
- **عدد الصفوف**, عدد الصفوف لملء نتيجة صيغة المصفوفة.
عدد الأعمدة

```javascript
const path = require("path");
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

// Adding a value to B1
worksheet.getCells().get("B1").putValue(4);

// Adding a value to "B2" cell
worksheet.getCells().get("B2").putValue(5);

// Adding a value to "B3" cell
worksheet.getCells().get("B3").putValue(6);

// Adding a value to C1
worksheet.getCells().get("C1").putValue(7);

// Adding a value to "C2" cell
worksheet.getCells().get("C2").putValue(8);

// Adding a value to "C3" cell
worksheet.getCells().get("C3").putValue(9);

// Adding a SUM formula to "A4" cell
worksheet.getCells().get("A6").setArrayFormula("=LINEST(A1:A3,B1:C3,TRUE,TRUE)", 5, 3);

// Calculating the results of formulas
workbook.calculateFormula();

// Get the calculated value of the cell
const value = worksheet.getCells().get("A6").getValue().toString();

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **كيفية استخدام الصيغة R1C1**

أضف صيغة مرجعية R1C1 إلى خلية مع خاصية فئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) وخاصية [**getR1C1Formula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getR1C1Formula--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");
// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

const worksheet = workbook.getWorksheets().get(0);

// Setting an R1C1 formula on the "A11" cell, 
// Row and Column indices are relative to destination index
worksheet.getCells().get("A11").setR1C1Formula("=SUM(R[-10]C[0]:R[-7]C[0])");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **مواضيع متقدمة**
- [السابقون والموكّلون](/cells/ar/nodejs-cpp/precedents-and-dependents/)
- [تعيين الروابط الخارجية في الصيغ](/cells/ar/nodejs-cpp/set-external-links-in-formulas/)
- [نشر الصيغة في الجدول أو كائن القائمة تلقائيًا أثناء إدخال البيانات في صفوف جديدة](/cells/ar/nodejs-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [وضع صيغة لنطاق مسمى](/cells/ar/nodejs-cpp/setting-formula-for-named-range/)
- [تعيين الصيغ - إشعار للمستخدمين غير الناطقين بالإنكليزية](/cells/ar/nodejs-cpp/setting-formulas-notice-for-non-english-users/)
- [تعيين الصيغ المشتركة](/cells/ar/nodejs-cpp/setting-shared-formula/)
- [تحديد الصفوف القصوى للصيغة المشتركة](/cells/ar/nodejs-cpp/specify-maximum-rows-of-shared-formula/)
- [الدوال المدعومة في إكسل](/cells/ar/nodejs-cpp/supported-formula-functions/)

{{< app/cells/assistant language="nodejs-cpp" >}}
