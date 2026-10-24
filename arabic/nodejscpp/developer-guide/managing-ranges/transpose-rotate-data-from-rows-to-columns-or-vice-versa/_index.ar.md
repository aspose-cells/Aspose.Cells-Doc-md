---
title: نطاق تبديل الموضع
linktitle: نطاق تبديل الموضع
description: يشرح هذا المقال كيف يمكنك تبديل موضع البيانات أو تدويرها من الصفوف إلى الأعمدة أو العكس في ملفات Excel باستخدام Aspose.Cells for Node.js via C++ بثلاث طرق مختلفة.
keywords: Aspose.Cells, مكتبة Node.js عبر C++, جدول بيانات, نطاق تبديل الموضع, تدوير البيانات, دالة تبديل الموضع, صيغة صفيف ديناميكية, صيغة صفيف, Excel TRANSPOSE, من الصفوف إلى الأعمدة
type: docs
weight: 80
url: /ar/nodejs-cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ يدعم تبديل موضع (تدوير) البيانات بحيث تصبح الصفوف أعمدة وتصبح الأعمدة صفوفًا بثلاث طرق مختلفة. تستخدم الطريقة الأولى أسلوب `range.transpose()` في مكانه ويعمل مع كل إصدار من Excel، بينما تستخدم الثانية `cell.setDynamicArrayFormula()` لكتابة صيغة صفيف ديناميكية حديثة `=TRANSPOSE(...)` تنتشر تلقائيًا في Excel 365 أو Excel 2021. تستخدم الطريقة الثالثة `cell.setArrayFormula()` لكتابة صيغة صفيف كلاسيكية من النوع Ctrl+Shift+Enter (CSE) متوافقة مع إصدارات Excel الأقدم. يستعرض المقال كل نهج مع تعليمات خطوة بخطوة وأمثلة شاملة للشفرات البرمجية.
{{% /alert %}}

## **Introduction**
يعني تبديل موضع نطاق تدويره بحيث يتحول الصف إلى عمود والعمود إلى صف، أي انعكاس البيانات عبر قطره الرئيسي. في Microsoft Excel، تؤدي دالة ورقة العمل `TRANSPOSE` هذه العملية، ويُوثَّق المرجع المفاهيمي في [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). يمكن تطبيق هذا المفهوم برمجيًا على نطاق من الخلايا، وهو أمر مفيد في العديد من السيناريوهات التجارية وسيناريوهات إعداد التقارير.
- إعادة توجيه تقارير المبيعات الفصلية أو السنوية حيث تمتد الأرباع عادةً عبر الصفحة وتظهر المناطق على طولها، أو العكس.
- تبديل اتجاه المحاور في لوحات المعلومات أو الرسوم البيانية بحيث يمتد السلاسل الزمنية على طول الصفحة بدلًا من عرضها عبرها.
- إعادة تشكيل البيانات المستوردة من الأنظمة الخارجية لتتوافق مع التخطيط الذي تتوقعه التحاليل أو قوالب التقارير في الخطوات التالية.
لجعل بقية المقال ملموسة، يستخدم كل مثال جدول المبيعات الصغير التالي حسب المنطقة والربع. في مصنف العينة، يشغل هذا الجدول النطاق **A1:D5**، مع ترك **A1** فارغة كركن أعلى اليسار، وتحتوي **B1:D1** على رؤوس المناطق، وتحتوي **A2:A5** على رؤوس الأرباع.
| المنطقة | أوروبا | آسيا | أمريكا الشمالية |
|---------|--------|------|----------------|
| الربع 1 | 21704714 | 8774099 | 12094215 |
| الربع 2 | 17987034 | 12214447 | 10873099 |
| الربع 3 | 19485029 | 14356879 | 15689543 |
| الربع 4 | 22567894 | 15763492 | 17456723 |
يقدم المقال بعد ذلك ثلاث طرق مختلفة لتبديل موضع هذه البيانات باستخدام Aspose.Cells for Node.js via C++، وتعد كل طريقة مناسبة لإصدار مختلف من Excel وحالة استخدام مختلفة.

## **Approach 1 — Transpose Range in Place (range.transpose)**
استخدم هذا النهج متى أردت تبديل موضع البيانات دون استخدام دالة ورقة العمل `TRANSPOSE`. يعمل على **كل إصدار من Excel** ولا يعتمد على المصفوفات الديناميكية، مما يجعله الخيار الأكثر توافقًا بين الإصدارات. وهو مثالي عندما تحتاج فقط إلى ناتج تبديل الموضع النهائي ولا تحتاج إلى الاحتفاظ بصيغة `TRANSPOSE` الأصلية في المصنف.

### **API used**
`range.transpose()` هو أسلوب خاص بكائنات فئة `Aspose.Cells.Range`. استدعاؤه يقلب النطاق في مكانه عبر تبديل صفوفه وأعمدة، بحيث يصبح الصف عمودًا والعمود صفًا. ويعدّل الأسلوب الخلايا التي يتكون منها النطاق مباشرةً من دون كتابة أي صيغة.

### **Steps**
1. افتح مصنف المصدر مع تعيين `LoadOptions` على تنسيق `.xlsx` من خلال استدعاء `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. استرجع ورقة العمل الأولى من المصنف باستخدام `workbook.getWorksheets().get(0)`.
3. استخدم `worksheet.getCells()` للوصول إلى مجموعة خلايا ورقة العمل.
4. أنشئ نطاق المصدر الذي يغطي **A1:D5** من خلال استدعاء `cells.createRange("A1:D5")`.
5. استدعِ `source.transpose()` لتدوير النطاق في مكانه، مع تبديل الصفوف والأعمدة.
6. احفظ المصنف باستخدام `workbook.save(outputFile)`.
بعد تبديل الموضع، يحتوي نطاق الارتكاز الأولي على البيانات المدوارة. يقرأ الصف الأول (فارغ، **أوروبا**، **آسيا**، **أمريكا الشمالية**) ويقرأ العمود الأول (فارغ، **الربع 1**، **الربع 2**، **الربع 3**، **الربع 4**). يتحول كل عمود مبيعات أصلي إلى صف في النطاق المبدّل.

```javascript
const AsposeCells = require("aspose.cells.node");
var srcFile = "source.xlsx";
var outputFile = "transposed.xlsx";
var workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
var worksheet = workbook.getWorksheets().get(0);
var cells = worksheet.getCells();
var source = cells.createRange("A1:D5");
source.transpose();
workbook.save(outputFile);
```

## **Approach 2 — Transpose with a Dynamic Array Formula (Excel 365 / 2021)**
استخدم هذا النهج عندما تريد الاحتفاظ بصيغة `=TRANSPOSE(A1:D5)` كصيغة فعّالة في مصنف الإخراج، بحيث تتحدث النتيجة تلقائيًا إذا تغيرت بيانات المصدر، وسيفتح ملف Excel الهدف في **Excel 365 / Excel 2021 أو إصدار أحدث** حيث تتوفر الدعم للمصفوفات الديناميكية وعامل الانتشار.

### **API used**
`cell.setDynamicArrayFormula(string formula, FormulaParseOptions options, bool calculateValue)` هو أسلوب على فئة `Aspose.Cells.Cell` يعيّن صيغة الخلية بوصفها **صيغة صفيف ديناميكية**. يحسب Excel الصيغة مرة واحدة ثم تنتشر النتيجة تلقائيًا في الخلايا المحيطة. عند ضبط الوسيط الثالث على `true`، يطلب Aspose.Cells حساب القيم الناتجة أيضًا عند وقت الكتابة.

### **Steps**
1. حمّل مصنف المصدر باستخدام `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. استرجع ورقة العمل الأولى واستخدم مجموعة `Cells` الخاصة بها.
3. ضع صيغة الصفيف الديناميكية على الخلية **A6**، أسفل نطاق المصدر مباشرةً، من خلال استدعاء `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)`.
4. تمر الوسيطة `null` خيارات `FormulaParseOptions` الافتراضية، وتخبر الوسيطة الثالثة `true` Aspose.Cells بمعاملة الصيغة على أنها صفيف ديناميكي وتقييمها بحيث تُكتب القيم الناتجة عن انتشارها في المصنف.
5. احفظ المصنف باستخدام `workbook.save(outputFile)`.
تحتوي الخلية **A6** على الصيغة `=TRANSPOSE(A1:D5)`، وتنتشر نتيجة Excel تلقائيًا في النطاق **A6:D10**، وهو كتلة من 5 صفوف × 4 أعمدة تطابق البيانات بعد تبديل الموضع.

{{% alert color="primary" %}}
لا يعمل هذا النهج **إلا في Excel 365 / 2021 أو إصدار أحدث**. لن تنتشر صيغ المصفوفات الديناميكية بصورة صحيحة في إصدارات Excel الأقدم.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
const srcFile = "source.xlsx";
const outFile = "output_transpose_dynamic.xlsx";
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
const workbook = new AsposeCells.Workbook(srcFile, opts);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new AsposeCells.FormulaParseOptions(), true);
workbook.save(outFile, AsposeCells.SaveFormat.Xlsx);
```

## **Approach 3 — Transpose with a Classic Array Formula (CSE)**
استخدم هذا النهج عندما تريد الاحتفاظ بصيغة `TRANSPOSE` في المصنف، لكن قد يُفتح ملف Excel الهدف في **إصدارات Excel الأقدم (ما قبل 2021، بما في ذلك 2019 و2016 و2013 وما إلى ذلك)** حيث لا يتم دعم انتشار المصفوفات الديناميكية. صيغة المصفوفة الكلاسيكية CSE (Ctrl+Shift+Enter) هي البديل المتوافق مع الإصدارات القديمة، وهو بديل يمكن لجميع إصدارات Excel تقييمه.

### **API used**
`cell.setArrayFormula(string arrayFormula, int nRows, int nColumns)` هو أسلوب على فئة `Aspose.Cells.Cell` يعيّن **صيغة صفيف كلاسيكية (CSE)** إلى خلية الارتكاز ويحدد أبعاد المصفوفة الناتجة. يكتب Aspose.Cells علامة صيغة المصفوفة متعددة الخلايا، بحيث يقيّم Excel الصيغة كتعبير مصفوفة واحد يملأ النطاق المعلن.

### **Steps**
1. حمّل مصنف المصدر كما هو موضح في النهجين السابقين.
2. استرجع ورقة العمل الأولى واستخدم مجموعة `Cells` الخاصة بها.
3. استدعِ `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. الوسيطة الثانية `4` هي عدد صفوف مصفوفة الوجهة، والوسيطة الثالثة `5` هي عدد الأعمدة.
4. احفظ المصنف باستخدام `workbook.save(outputFile)`.
الخلية **A6** هي خلية الارتكاز لصيغة المصفوفة، وتمتد المصفوفة المقيمة على 4 صفوف × 5 أعمدة بدءًا من A6، بما يطابق أبعاد النطاق A1:D5 بعد تبديل الموضع. يكتب Excel علامة صيغة مصفوفة واحدة عبر النطاق الناتج بأكمله، بحيث تقيمها إصدارات Excel الأقدم بصورة صحيحة.

{{% alert color="primary" %}}
صيغ مصفوفات CSE هي طريقة Excel الكلاسيكية لتقييم تعبير `TRANSPOSE`، وهذا النهج متوافق مع جميع إصدارات Excel.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
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
| النهج | API / الأسلوب | إصدار Excel | هل صيغة المصدر محفوظة؟ | نطاق الإخراج |
|-------|---------------|-------------|------------------------|-------------|
| النهج 1 — التبديل في المكان | `range.transpose()` | جميع إصدارات Excel | لا (القيم فقط) | نطاق الارتكاز الأولي، 5×4 |
| النهج 2 — صيغة صفيف ديناميكية | `cell.setDynamicArrayFormula` | Excel 365 / 2021+ | نعم (تنتشر ديناميكيًا) | تنتشر من خلية الارتكاز |
| النهج 3 — صيغة صفيف كلاسيكية (CSE) | `cell.setArrayFormula` | جميع إصدارات Excel | نعم (صيغة مصفوفة متعددة الخلايا) | حجم صريح، 4×5 |
استخدم **النهج 1** عندما تحتاج إلى تحويل سريع متوافق عبر الإصدارات ولا تحتاج سوى إلى القيم بعد تبديل الموضع في الملف. استخدم **النهج 2** عندما يكون استخدام Excel الحديث مضمونًا وتريد أن تبقى الصيغة فعّالة وتتحدث عند تغير المصدر. استخدم **النهج 3** عندما تحتاج إلى أقصى توافق مع صيغة محفوظة عبر جميع إصدارات Excel، بما في ذلك الإصدارات القديمة التي لا تدعم المصفوفات الديناميكية.

## **Related Articles**
- [عرض صفيف SmartMarker في خلية واحدة](/cells/ar/nodejs-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [إدراج صورة في خلية](/cells/ar/nodejs-cpp/inserting-an-image-into-a-cell/)
- [تقسيم ملفات Excel إلى ملفات متعددة](/cells/ar/nodejs-cpp/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="nodejs-cpp" >}}