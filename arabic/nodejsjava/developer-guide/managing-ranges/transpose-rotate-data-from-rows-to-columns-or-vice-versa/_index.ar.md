---
title: تبديل النطاق
linktitle: تبديل النطاق
description: توضح هذه المقالة كيفية تبديل أو تدوير البيانات من الصفوف إلى الأعمدة أو العكس في ملفات Excel باستخدام Aspose.Cells for Node.js via Java، وذلك من خلال ثلاث طرق مختلفة.
keywords: Aspose.Cells, Node.js via Java library, spreadsheet, transpose range, rotate data, transpose function, dynamic array formula, array formula, Excel TRANSPOSE, Rows to Columns, تبديل النطاق, تدوير البيانات
type: docs
weight: 80
url: /ar/nodejs-java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells for Node.js via Java تبديل (تدوير) البيانات بحيث تصبح الصفوف أعمدة وتصبح الأعمدة صفوفًا بثلاث طرق مختلفة. تستخدم الطريقة الأولى أسلوب `Range.transpose()` الموضعي وتعمل في كل إصدار من إصدارات Excel، بينما تستخدم الطريقة الثانية `Cell.setDynamicArrayFormula()` لكتابة صيغة مصفوفة ديناميكية حديثة من النوع `=TRANSPOSE(...)` تنسكب تلقائيًا في Excel 365 أو Excel 2021. أما الطريقة الثالثة فتستخدم `Cell.setArrayFormula()` لكتابة صيغة مصفوفة كلاسيكية من النوع Ctrl+Shift+Enter (CSE) متوافقة مع إصدارات Excel الأقدم. تتناول هذه المقالة كل طريقة بخطوات تفصيلية وأمثلة كود كاملة.
{{% /alert %}}

## **Introduction**
يعني تبديل النطاق تدويره بحيث يصبح ما كان صفًا عمودًا وما كان عمودًا صفًا، مما يعكس البيانات فعليًا عبر قطرها الرئيسي. في Microsoft Excel، تؤدي دالة ورقة العمل `TRANSPOSE` هذه العملية، كما أن المرجع المفاهيمي موثق على الرابط [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). يمكن تطبيق هذا المفهوم برمجيًا على نطاق من الخلايا، وهو أمر مفيد في كثير من سيناريوهات الأعمال وإعداد التقارير.
- إعادة توجيه تقارير المبيعات ربع السنوية أو السنوية حيث تنتشر الأرباع عادةً عبر الصفحة والمناطق إلى أسفل الصفحة، أو العكس.
- تبديل توجيه المحاور في لوحات المعلومات أو الرسوم البيانية بحيث تمتد السلسلة الزمنية إلى أسفل الصفحة بدلاً من عرضها أفقيًا.
- إعادة تشكيل البيانات المستوردة من أنظمة خارجية بحيث تتطابق مع التخطيط المتوقع بواسطة قوالب التحليل أو إعداد التقارير downstream.
لتكون بقية المقالة ملموسة، يستخدم كل مثال جدول المبيعات حسب المنطقة والربع التالي. في مصنف العينة، يشغل هذا الجدول النطاق **A1:D5**، مع ترك **A1** فارغًا كزاوية علوية يسرى. يحتوي **B1:D1** على رؤوس المناطق، ويحتوي **A2:A5** على رؤوس الأرباع.
| المنطقة          | أوروبا     | آسيا       | أمريكا الشمالية |
|------------------|-----------|-----------|-----------------|
| الربع 1          | 21704714  | 8774099   | 12094215        |
| الربع 2          | 17987034  | 12214447  | 10873099        |
| الربع 3          | 19485029  | 14356879  | 15689543        |
| الربع 4          | 22567894  | 15763492  | 17456723        |
تقدم المقالة بعد ذلك ثلاث طرق مختلفة لتبديل هذه البيانات باستخدام Aspose.Cells for Node.js via Java، وكل منها مناسب لإصدار مختلف من Excel وحالة استخدام مختلفة.

## **Approach 1 — Transpose Range in Place (Range.transpose)**
استخدم هذا النهج كلما أردت تبديل البيانات دون إشراك دالة ورقة العمل `TRANSPOSE`. يعمل في **كل إصدار من إصدارات Excel** ولا يعتمد على المصفوفات الديناميكية، مما يجعله الخيار الأكثر أمانًا للتوافق عبر الإصدارات. وهو مثالي عندما تحتاج فقط إلى الناتج النهائي بعد التبديل ولا تحتاج إلى الاحتفاظ بصيغة `TRANSPOSE` الأصلية في المصنف.

### **API used**
`Range.transpose()` هو أسلوب مثيل على الفئة `com.aspose.cells.Range`. عند استدعائه يقلب النطاق في الموقع عن طريق تبديل صفوفه وأعمدته، ليصبح ما كان صفًا عمودًا وما كان عمودًا صفًا. يعدّل الأسلوب الخلايا الأساسية مباشرة دون كتابة صيغة.

### **Steps**
1. افتح مصنف المصدر مع ضبط `LoadOptions` على تنسيق `.xlsx` عن طريق استدعاء `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. استرجع ورقة العمل الأولى من المصنف باستخدام `workbook.getWorksheets().get(0)`.
3. الوصول إلى مجموعة خلايا ورقة العمل من خلال `worksheet.getCells()`.
4. أنشئ نطاق المصدر الذي يغطي **A1:D5** عن طريق استدعاء `cells.createRange("A1:D5")`.
5. استدعِ `source.transpose()` لتدوير النطاق في الموقع، مع تبديل الصفوف والأعمدة.
6. احفظ المصنف باستخدام `workbook.save(outputFile)`.
بعد التبديل يحتفظ نطاق الإرساء الأولي بالبيانات المدوّرة. يقرأ الصف الأول (فارغ، **أوروبا**، **آسيا**، **أمريكا الشمالية**) ويقرأ العمود الأول (فارغ، **الربع 1**، **الربع 2**، **الربع 3**، **الربع 4**). يصبح كل عمود مبيعات أصلي صفًا في النطاق المبدّل.

```python
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outputFile = "transposed.xlsx";
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
const workbook = new AsposeCells.Workbook(srcFile, loadOptions);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
const source = cells.createRange("A1:D5");
source.transpose();
workbook.save(outputFile);
```

## **Approach 2 — Transpose with a Dynamic Array Formula (Excel 365 / 2021)**
استخدم هذا النهج عندما تريد الحفاظ على صيغة `=TRANSPOSE(A1:D5)` كصيغة نشطة في مصنف الإخراج بحيث يتم تحديث النتيجة تلقائيًا إذا تغيرت بيانات المصدر، وسيُفتح ملف Excel الهدف في **Excel 365 / Excel 2021 أو أحدث** حيث تكون المصفوفات الديناميكية ومعة مل الانسكاب مدعومة.

### **API used**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` هو أسلوب على `com.aspose.cells.Cell` يعيّن صيغة الخلية كـ **صيغة مصفوفة ديناميكية**. يقيّم Excel الصيغة مرة واحدة وينسكب النتيجة تلقائيًا في الخلايا المحيطة. تشير المعلمة الثالثة، عند ضبطها على `true`، إلى Aspose.Cells لحساب القيم الناتجة أيضًا في وقت الكتابة.

### **Steps**
1. حمّل مصنف المصدر باستخدام `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. استرجع ورقة العمل الأولى ووصل إلى مجموعة `Cells` الخاصة بها.
3. ضع صيغة المصفوفة الديناميكية على الخلية **A6**، أسفل نطاق المصدر مباشرة، عن طريق استدعاء `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)`.
4. تُمرّر الوسيطة `null` قيمة افتراضية لـ `FormulaParseOptions`، والوسيطة الثالثة `true` تخبر Aspose.Cells بمعاملة الصيغة كمصفوفة ديناميكية وبتقييمها بحيث تُكتب القيم المنسكبة في المصنف.
5. احفظ المصنف باستخدام `workbook.save(outputFile)`.
تحتوي الخلية **A6** على الصيغة `=TRANSPOSE(A1:D5)` وينسكب Excel النتيجة تلقائيًا في المنطقة **A6:D10**، وهي كتلة مكونة من 5 صفوف و4 أعمدة مساوية للبيانات المبدّلة.

{{% alert color="primary" %}}
يعمل هذا النهج **فقط في Excel 365 / 2021 أو أحدث**. لن تنسكب الإصدارات الأقدم من Excel صيغ المصفوفات الديناميكية بشكل صحيح.
{{% /alert %}}

```python
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outFile = "output_transpose_dynamic.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new AsposeCells.FormulaParseOptions(), true);
workbook.save(outFile, AsposeCells.SaveFormat.Xlsx);
```

## **Approach 3 — Transpose with a Classic Array Formula (CSE)**
استخدم هذا النهج عندما تريد صيغة `TRANSPOSE` محفوظة في المصنف ولكن قد يُفتح ملف Excel الهدف في **إصدارات Excel الأقدم (ما قبل 2021، بما في ذلك 2019 و2016 و2013 وما إلى ذلك)** حيث لا يكون انسكاب المصفوفات الديناميكية مدعومًا. صيغة المصفوفة الكلاسيكية من النوع CSE (Ctrl+Shift+Enter) هي البديل المتوافق مع الإصدارات الأقدم الذي يمكن لجميع إصدارات Excel تقييمه.

### **API used**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` هو أسلوب على `com.aspose.cells.Cell` يُسند **صيغة مصفوفة كلاسيكية (CSE)** إلى خلية الإرساء ويعلن عن أبعاد المصفوفة الناتجة. يكتب Aspose.Cells علامة صيغة المصفوفة متعددة الخلايا بحيث يقيّم Excel الصيغة كتعبير مصفوفة واحدة يملأ النطاق المُعلن.

### **Steps**
1. حمّل مصنف المصدر كما هو موضح في النهُج السابقة.
2. استرجع ورقة العمل الأولى ووصل إلى مجموعة `Cells` الخاصة بها.
3. استدعِ `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. الوسيطة الثانية `4` هي عدد صفوف مصفوفة الوجهة والوسيطة الثالثة `5` هي عدد الأعمدة.
4. احفظ المصنف باستخدام `workbook.save(outputFile)`.
تعد الخلية **A6** إرساء صيغة المصفوفة وتمتد المصفوفة المُقيّمة عبر 4 صفوف و5 أعمدة بدءًا من A6، مطابقة لأبعاد النطاق A1:D5 بعد التبديل. يكتب Excel علامة صيغة مصفوفة واحدة عبر النطاق الناتج بحيث تقيّمه إصدارات Excel الأقدم بشكل صحيح.

{{% alert color="primary" %}}
صيغ المصفوفة من النوع CSE هي الطريقة الكلاسيكية في Excel لتقييم تعبير `TRANSPOSE` وهذا النهج متوافق عالميًا عبر إصدارات Excel.
{{% /alert %}}

```python
const AsposeCells = require("aspose.cells");
// Load the source workbook with xlsx LoadOptions
const srcFile = "source.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
// Access the first worksheet and its Cells collection
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// Set the classic CSE array formula on cell A6.
// The formula =TRANSPOSE(A1:D5) rotates the 5-row x 4-column source range
// into a 4-row x 5-column array. The second argument (4) is the number of rows
// and the third argument (5) is the number of columns of the resulting array.
// Aspose.Cells writes the CSE array-formula marker so Excel evaluates it as
// a single multi-cell array formula, compatible with older Excel versions
// (2019, 2016, 2013, etc.) that do not support dynamic array spilling.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Save the workbook so the array-formula marker is persisted
workbook.save("output.xlsx");
```

## **Comparison — When to Use Each Approach**
| النهج | API / الطريقة | إصدار Excel | هل الصيغة المصدر محفوظة؟ | نطاق الإخراج |
|--------|--------------|---------------|--------------------------|--------------|
| النهج 1 — التبديل في الموقع | `Range.transpose()` | جميع إصدارات Excel | لا (قيم فقط) | نطاق الإرساء الأولي، 5×4 |
| النهج 2 — صيغة المصفوفة الديناميكية | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | نعم (تنسكب ديناميكيًا) | تنسكب من الإرساء |
| النهج 3 — صيغة المصفوفة الكلاسيكية (CSE) | `Cell.setArrayFormula` | جميع إصدارات Excel | نعم (صيغة مصفوفة متعددة الخلايا) | حجم صريح، 4×5 |
استخدم **النهج 1** عندما تحتاج إلى تحويل سريع متوافق عبر الإصدارات وتحتاج فقط إلى القيم المبدّلة المكتوبة في الملف. استخدم **النهج 2** عندما يكون Excel الحديث مضمونًا وتريد أن تظل الصيغة نشطة وتتحدث إذا تغير المصدر. استخدم **النهج 3** عندما تحتاج إلى أوسع توافق مع صيغة محفوظة عبر جميع إصدارات Excel، بما في ذلك الإصدارات الأقدم التي لا تدعم المصفوفات الديناميكية.

## **Related Articles**
- [عرض المصفوفة ذات الخلية الواحدة لـ SmartMarker | Aspose.Cells for Node.js via Java](/cells/ar/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [إدراج صورة في خلية](/cells/ar/nodejs-java/inserting-an-image-into-a-cell/)
- [تقسيم ملفات Excel إلى ملفات متعددة](/cells/ar/nodejs-java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="nodejs-java" >}}