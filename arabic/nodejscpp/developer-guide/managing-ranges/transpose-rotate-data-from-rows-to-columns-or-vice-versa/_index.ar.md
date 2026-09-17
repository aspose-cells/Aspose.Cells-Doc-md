---
title: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for Node.js via C++ with three different approaches.
linktitle: تبديل النطاق
url: /ar/nodejs-cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, Node.js via C++ library, spreadsheet, transpose range, rotate data, transpose function, dynamic array formula, array formula, Excel TRANSPOSE, Rows to Columns
type: docs
weight: 80
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells for Node.js via C++ تبديل (تدوير) البيانات بحيث تصبح الصفوف أعمدة والأعمدة صفوفًا بثلاث طرق مختلفة. تستخدم الطريقة الأولى أسلوب `range.transpose()` في موضعه الأصلي وتعمل على جميع إصدارات Excel، بينما تستخدم الطريقة الثانية `cell.setDynamicArrayFormula()` لكتابة صيغة مصفوفة ديناميكية حديثة `=TRANSPOSE(...)` تنسكب تلقائيًا في Excel 365 أو Excel 2021. أما الطريقة الثالثة فتستخدم `cell.setArrayFormula()` لكتابة صيغة مصفوفة كلاسيكية من نوع Ctrl+Shift+Enter (CSE) متوافقة مع إصدارات Excel القديمة. يستعرض هذا المقال كل طريقة من خلال تعليمات خطوة بخطوة وأمثلة شفرة كاملة.
{{% /alert %}}

## **المقدمة**
يعني تبديل النطاق تدويره بحيث يصبح ما كان صفًا عمودًا وما كان عمودًا صفًا، مما يعكس البيانات فعليًا عبر قطرها الرئيسي. في Microsoft Excel، تؤدي دالة ورقة العمل `TRANSPOSE` هذه العملية، ويوثق المرجع المفاهيمي في [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). يمكن تطبيق الفكرة نفسها برمجيًا على نطاق من الخلايا، وهو أمر مفيد في العديد من سيناريوهات الأعمال وإعداد التقارير.
تتضمن السيناريوهات الشائعة التي يكون فيها التبديل مفيدًا ما يلي.
- إعادة توجيه تقارير المبيعات الفصلية أو السنوية حيث تمتد الفصول عادة عبر الصفحة والمناطق إلى أسفل الصفحة، أو العكس.
- تبديل توجيه المحور في لوحات المعلومات أو الرسوم البيانية بحيث يمتد التسلسل الزمني إلى أسفل الصفحة بدلاً من امتداده عبرها.
- إعادة تشكيل البيانات المستوردة من الأنظمة الخارجية بحيث تتطابق مع التخطيط المتوقع من قبل التحليلات اللاحقة أو قوالب إعداد التقارير.
لجعل بقية المقال ملموسًا، يستخدم كل مثال جدول المبيعات حسب المنطقة حسب الربع التالي. في مصنف العينة يشغل هذا الجدول النطاق **A1:D5**، مع ترك **A1** فارغًا كزاوية علوية يسرى، واحتواء **B1:D1** على رؤوس المناطق، واحتواء **A2:A5** على رؤوس الأرباع.
| المنطقة          | أوروبا     | آسيا       | أمريكا الشمالية |
|------------------|------------|------------|------------------|
| الربع 1          | 21704714   | 8774099    | 12094215         |
| الربع 2          | 17987034   | 12214447   | 10873099         |
| الربع 3          | 19485029   | 14356879   | 15689543         |
| الربع 4          | 22567894   | 15763492   | 17456723         |
يقدم المقال بعد ذلك ثلاث طرق مختلفة لتبديل هذه البيانات باستخدام Aspose.Cells for Node.js via C++، وكل منها مناسب لإصدار Excel وحالة استخدام مختلفة.

## **الطريقة 1 — تبديل النطاق في موضعه الأصلي (range.transpose)**
استخدم هذه الطريقة كلما أردت تبديل البيانات دون إشراك دالة ورقة العمل `TRANSPOSE`. تعمل على **كل إصدار من Excel** ولا تعتمد على المصفوفات الديناميكية، مما يجعلها الخيار الأكثر أمانًا للتوافق عبر الإصدارات. وهي مثالية عندما تحتاج فقط إلى المخرجات المبدلة النهائية ولا تحتاج إلى الاحتفاظ بصيغة `TRANSPOSE` الأصلية في المصنف.

### **واجهة API المستخدمة**
`range.transpose()` هو أسلوب مثيل على فئة `Aspose.Cells.Range`. يؤدي استدعاؤه إلى قلب النطاق في موضعه الأصلي عن طريق تبديل صفوفه وأعمدته، بحيث يصبح ما كان صفًا عمودًا وما كان عمودًا صفًا. يعدّل الأسلوب الخلايا الأساسية مباشرة دون كتابة صيغة.

### **الخطوات**
1. افتح مصنف المصدر مع تعيين `LoadOptions` على تنسيق `.xlsx` عن طريق استدعاء `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. استرجع ورقة العمل الأولى من المصنف باستخدام `workbook.getWorksheets().get(0)`.
3. ادخل إلى مجموعة الخلايا في ورقة العمل من خلال `worksheet.getCells()`.
4. أنشئ نطاق المصدر الذي يغطي **A1:D5** عن طريق استدعاء `cells.createRange("A1:D5")`.
5. استدعِ `source.transpose()` لتدوير النطاق في موضعه الأصلي، مع تبديل الصفوف والأعمدة.
6. احفظ المصنف باستخدام `workbook.save(outputFile)`.
بعد التبديل يحتفظ نفس نطاق الإرساء بالبيانات المدوارة. يقرأ الصف الأول (فارغ، **أوروبا**، **آسيا**، **أمريكا الشمالية**) ويقرأ العمود الأول (فارغ، **الربع 1**، **الربع 2**، **الربع 3**، **الربع 4**). يصبح كل عمود مبيعات أصلي صفًا في النطاق المبدل.

```javascript
var srcFile = "source.xlsx";
var outputFile = "transposed.xlsx";
var workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
var worksheet = workbook.getWorksheets().get(0);
var cells = worksheet.getCells();
var source = cells.createRange("A1:D5");
source.transpose();
workbook.save(outputFile);
```

## **الطريقة 2 — التبديل باستخدام صيغة المصفوفة الديناميكية (Excel 365 / 2021)**
استخدم هذه الطريقة عندما تريد الاحتفاظ بصيغة `=TRANSPOSE(A1:D5)` كصيغة حية في مصنف الإخراج بحيث يتم تحديث النتيجة تلقائيًا في حالة تغير بيانات المصدر، وسيتم فتح ملف Excel المستهدف في **Excel 365 / Excel 2021 أو الإصدارات الأحدث** حيث يتم دعم المصفوفات الديناميكية ومشغل الانسكاب.

### **واجهة API المستخدمة**
`cell.setDynamicArrayFormula(string formula, FormulaParseOptions options, bool calculateValue)` هو أسلوب على `Aspose.Cells.Cell` يعين صيغة الخلية كـ **صيغة مصفوفة ديناميكية**. يقيّم Excel الصيغة مرة واحدة وينسكب النتيجة تلقائيًا في الخلايا المحيطة. تشير المعلمة الثالثة، عند تعيينها إلى `true`، إلى Aspose.Cells بأن يحسب أيضًا القيم الناتجة في وقت الكتابة.

### **الخطوات**
1. حمّل مصنف المصدر باستخدام `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. استرجع ورقة العمل الأولى وادخل إلى مجموعة `Cells` الخاصة بها.
3. ضع صيغة المصفوفة الديناميكية على الخلية **A6**، أسفل نطاق المصدر مباشرة، عن طريق استدعاء `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)`.
4. تمرر الوسيطة `null` قيم `FormulaParseOptions` الافتراضية، وتخبر الوسيطة الثالثة `true` Aspose.Cells بمعاملة الصيغة كمصفوفة ديناميكية وتقييمها بحيث تُكتب القيم المنسكبة في المصنف.
5. احفظ المصنف باستخدام `workbook.save(outputFile)`.
تحتوي الخلية **A6** على الصيغة `=TRANSPOSE(A1:D5)` وينسكب Excel النتيجة تلقائيًا في المنطقة **A6:D10**، وهي كتلة من 5 صفوف × 4 أعمدة تساوي البيانات المبدلة.

{{% alert color="primary" %}}
تعمل هذه الطريقة **فقط على Excel 365 / 2021 أو الإصدارات الأحدث**. لن تنسكب صيغ المصفوفات الديناميكية بشكل صحيح في إصدارات Excel القديمة.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outFile = "output_transpose_dynamic.xlsx";
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
const workbook = new AsposeCells.Workbook(srcFile, opts);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new AsposeCells.FormulaParseOptions(), true);
workbook.save(outFile, AsposeCells.SaveFormat.Xlsx);
```

## **الطريقة 3 — التبديل باستخدام صيغة المصفوفة الكلاسيكية (CSE)**
استخدم هذه الطريقة عندما تريد صيغة `TRANSPOSE` محفوظة في المصنف ولكن قد يتم فتح ملف Excel المستهدف في **إصدارات Excel القديمة (قبل 2021، بما في ذلك 2019 و2016 و2013 وما إلى ذلك)** حيث لا يتم دعم انسكاب المصفوفات الديناميكية. صيغة المصفوفة الكلاسيكية من نوع CSE (Ctrl+Shift+Enter) هي البديل المتوافق مع الإصدارات القديمة الذي يمكن لجميع إصدارات Excel تقييمه.

### **واجهة API المستخدمة**
`cell.setArrayFormula(string arrayFormula, int nRows, int nColumns)` هو أسلوب على `Aspose.Cells.Cell` يعين **صيغة مصفوفة كلاسيكية (CSE)** على خلية الإرساء ويصرح بأبعاد المصفوفة الناتجة. يكتب Aspose.Cells علامة صيغة المصفوفة متعددة الخلايا بحيث يقيّم Excel الصيغة كتعبير مصفوفة واحد يملأ النطاق المعلن.

### **الخطوات**
1. حمّل مصنف المصدر بنفس الطريقة كما في الطرق السابقة.
2. استرجع ورقة العمل الأولى وادخل إلى مجموعة `Cells` الخاصة بها.
3. استدعِ `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. الوسيطة الثانية `4` هي عدد صفوف مصفوفة الوجهة والوسيطة الثالثة `5` هي عدد الأعمدة.
4. احفظ المصنف باستخدام `workbook.save(outputFile)`.
تكون الخلية **A6** هي خلية إرساء صيغة المصفوفة وتمتد المصفوفة المُقيّمة على 4 صفوف × 5 أعمدة بدءًا من A6، مطابقة للأبعاد المبدّلة لمصدر A1:D5. يكتب Excel علامة صيغة مصفوفة واحدة عبر النطاق الناتج بحيث تقوم إصدارات Excel القديمة بتقييمها بشكل صحيح.

{{% alert color="primary" %}}
صيغ المصفوفة من نوع CSE هي الطريقة الكلاسيكية في Excel لتقييم تعبير `TRANSPOSE` وهذا الأسلوب متوافق عالميًا عبر إصدارات Excel.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
// تحميل مصنف المصدر باستخدام خيارات تحميل xlsx
const srcFile = "source.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
// الوصول إلى ورقة العمل الأولى ومجموعة الخلايا الخاصة بها
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// تعيين صيغة الصفيف الكلاسيكية CSE على الخلية A6.
// الصيغة =TRANSPOSE(A1:D5) تدور نطاق المصدر الذي يحتوي على 5 صفوف × 4 أعمدة
// إلى صفيف من 4 صفوف × 5 أعمدة. الوسيط الثاني (4) هو عدد الصفوف
// والوسيط الثالث (5) هو عدد الأعمدة للصفيف الناتج.
// يقوم Aspose.Cells بكتابة علامة صيغة الصفيف CSE بحيث يقوم Excel بتقييمها كـ
// صيغة صفيف أحادية الخلية متعددة الخلايا، متوافقة مع إصدارات Excel الأقدم
// (2019، 2016، 2013، إلخ) التي لا تدعم الانسكاب الديناميكي للصفيف.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// حفظ المصنف بحيث يتم الاحتفاظ بعلامة صيغة الصفيف
workbook.save("output.xlsx");
```

## **المقارنة — متى تستخدم كل طريقة**
| الطريقة | واجهة API / الأسلوب | إصدار Excel | هل الصيغة المصدر محفوظة؟ | نطاق الإخراج |
|---------|----------------------|--------------|---------------------------|---------------|
| الطريقة 1 — تبديل في موضعه الأصلي | `range.transpose()` | جميع إصدارات Excel | لا (قيم فقط) | نفس نطاق الإرساء، 5×4 |
| الطريقة 2 — صيغة المصفوفة الديناميكية | `cell.setDynamicArrayFormula` | Excel 365 / 2021+ | نعم (تنسكب ديناميكيًا) | تنسكب من الإرساء |
| الطريقة 3 — صيغة المصفوفة الكلاسيكية (CSE) | `cell.setArrayFormula` | جميع إصدارات Excel | نعم (صيغة مصفوفة متعددة الخلايا) | حجم صريح، 4×5 |
استخدم **الطريقة 1** عندما تحتاج إلى تحويل سريع متوافق عبر الإصدارات وتحتاج فقط إلى القيم المبدلة المكتوبة في الملف. استخدم **الطريقة 2** عندما يكون Excel الحديث مضمونًا وتريد أن تظل الصيغة حية وتتحدث إذا تغير المصدر. استخدم **الطريقة 3** عندما تحتاج إلى أوسع توافق مع صيغة محفوظة عبر جميع إصدارات Excel، بما في ذلك الإصدارات القديمة التي لا تدعم المصفوفات الديناميكية.

## **مقالات ذات صلة**
- [عرض المصفوفة ذات الخلية الواحدة لـ SmartMarker](/cells/ar/nodejs-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [إدراج صورة في خلية](/cells/ar/nodejs-cpp/inserting-an-image-into-a-cell/)
- [تقسيم ملفات Excel إلى ملفات متعددة](/cells/ar/nodejs-cpp/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="nodejs-cpp" >}}