---
title: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for Python via .NET, with three different approaches.
linktitle: تبديل النطاق
url: /ar/python-net/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells for Python via .NET, spreadsheet, transpose range, rotate data, transpose function, dynamic array formula, array formula, Excel TRANSPOSE, Rows to Columns
type: docs
weight: 80
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells for Python via .NET تبديل (تدوير) البيانات بحيث تصبح الصفوف أعمدة وتصبح الأعمدة صفوفًا بثلاث طرق مختلفة. تستخدم الطريقة الأولى أسلوب `range.transpose()` في مكانه وتعمل في كل إصدار من إصدارات Excel، بينما تستخدم الطريقة الثانية `cell.set_dynamic_array_formula()` لكتابة صيغة مصفوفة ديناميكية حديثة `=TRANSPOSE(...)` تنتشر تلقائيًا في Excel 365 أو Excel 2021. أما الطريقة الثالثة فتستخدم `cell.set_array_formula()` لكتابة صيغة مصفوفة كلاسيكية عبر Ctrl+Shift+Enter (CSE) متوافقة مع إصدارات Excel الأقدم. تستعرض هذه المقالة كل طريقة بخطوات تفصيلية وأمثلة كود كاملة.
{{% /alert %}}

## **المقدمة**
يعني تبديل النطاق تدويره بحيث ما كان صفًا يصبح عمودًا وما كان عمودًا يصبح صفًا، مع عكس البيانات فعليًا عبر القطر الرئيسي لها. في Microsoft Excel، تقوم دالة ورقة العمل `TRANSPOSE` بهذه العملية، كما يتوفر المرجع المفاهيمي في [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). يمكن تطبيق الفكرة نفسها برمجيًا على نطاق من الخلايا، وهو أمر مفيد في العديد من سيناريوهات الأعمال وإعداد التقارير.
تتضمن السيناريوهات الشائعة التي يكون فيها التبديل مفيدًا ما يلي.
- إعادة توجيه تقارير المبيعات ربع السنوية أو السنوية التي تنتشر فيها الأرباع عادةً عبر الصفحة والمناطق إلى الأسفل، أو العكس.
- تبديل توجيه المحاور في لوحات المعلومات أو الرسوم البيانية بحيث يسير التسلسل الزمني إلى الأسفل بدلاً من عرضه عبر الصفحة.
- إعادة تشكيل البيانات المستوردة من الأنظمة الخارجية لتطابق التخطيط المتوقع من قبل قوالب التحليل أو إعداد التقارير اللاحقة.
لتكون الأمثلة في بقية المقالة ملموسة، يستخدم كل مثال جدول المبيعات الصغير التالي حسب المنطقة وربع السنة. يحتل هذا الجدول في مصنف العينة النطاق **A1:D5**، مع ترك **A1** فارغة كزاوية علوية يسرى، وتحمل **B1:D1** رؤوس المناطق، وتحمل **A2:A5** رؤوس الأرباع.
| Region            | Europe    | Asia      | North America |
|-------------------|-----------|-----------|---------------|
| Qtr 1             | 21704714  | 8774099   | 12094215      |
| Qtr 2             | 17987034  | 12214447  | 10873099      |
| Qtr 3             | 19485029  | 14356879  | 15689543      |
| Qtr 4             | 22567894  | 15763492  | 17456723      |
تقدم المقالة بعد ذلك ثلاث طرق مختلفة لتبديل هذه البيانات باستخدام Aspose.Cells for Python via .NET، وكل منها يناسب إصدارًا مختلفًا من Excel وحالة استخدام مختلفة.

## **الطريقة الأولى — تبديل النطاق في مكانه (range.transpose)**
استخدم هذه الطريقة كلما أردت تبديل البيانات دون إشراك دالة ورقة العمل `TRANSPOSE`. تعمل في **كل إصدارات Excel** ولا تعتمد على المصفوفات الديناميكية، مما يجعلها الخيار الأكثر أمانًا للتوافق عبر الإصدارات. وهي مثالية عندما تحتاج فقط إلى الناتج النهائي بعد التبديل ولا تحتاج إلى الاحتفاظ بصيغة `TRANSPOSE` الأصلية في المصنف.

### **واجهة API المستخدمة**
`range.transpose()` هو أسلوب مثيل على فئة `Aspose.Cells.Range`. يُستدعى هذا الأسلوب لقلب النطاق في مكانه عن طريق تبديل صفوفه وأعمدته، فيصبح ما كان صفًا عمودًا وما كان عمودًا صفًا. يقوم الأسلوب بتعديل الخلايا الأساسية مباشرة دون كتابة أي صيغة.

### **الخطوات**
1. افتح مصنف المصدر مع ضبط `LoadOptions` على تنسيق `.xlsx` من خلال استدعاء `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))`.
2. استرجع أول ورقة عمل من المصنف باستخدام `workbook.worksheets[0]`.
3. ادخل إلى مجموعة خلايا ورقة العمل من خلال `worksheet.cells`.
4. أنشئ نطاق المصدر الذي يغطي **A1:D5** عن طريق استدعاء `cells.create_range("A1:D5")`.
5. استدعِ `source.transpose()` لتدوير النطاق في مكانه، مع تبديل الصفوف والأعمدة.
6. احفظ المصنف باستخدام `workbook.save(outputFile)`.
بعد التبديل يحتفظ نفس نطاق الإرساء بالبيانات المدوَّرة. تقرأ الصف الأول (فارغ، **Europe**، **Asia**، **North America**) وتقرأ العمود الأول (فارغ، **Qtr 1**، **Qtr 2**، **Qtr 3**، **Qtr 4**). يصبح كل عمود أصلي من المبيعات صفًا في النطاق بعد التبديل.

```python
import aspose.cells as ac
srcFile = "source.xlsx"
outputFile = "transposed.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.XLSX))
worksheet = workbook.worksheets[0]
cells = worksheet.cells
source = cells.create_range("A1:D5")
source.transpose()
workbook.save(outputFile)
```

## **الطريقة الثانية — التبديل باستخدام صيغة مصفوفة ديناميكية (Excel 365 / 2021)**
استخدم هذه الطريقة عندما تريد الحفاظ على صيغة `=TRANSPOSE(A1:D5)` كصيغة حية في مصنف الناتج بحيث يتم تحديث النتيجة تلقائيًا في حال تغيرت بيانات المصدر، وسيتم فتح ملف Excel الناتج في **Excel 365 / Excel 2021 أو الإصدارات الأحدث** التي تدعم المصفوفات الديناميكية ومشغل الانتشار.

### **واجهة API المستخدمة**
`cell.set_dynamic_array_formula(formula, options, calculate_value)` هو أسلوب على `Aspose.Cells.Cell` يقوم بتعيين صيغة الخلية كـ **صيغة مصفوفة ديناميكية**. يقيّم Excel الصيغة مرة واحدة وينشر النتيجة تلقائيًا في الخلايا المحيطة. أما المعامل الثالث، فعند ضبطه على `True`، فإنه يوجّه Aspose.Cells إلى حساب القيم الناتجة أيضًا وقت الكتابة.

### **الخطوات**
1. حمّل مصنف المصدر باستخدام `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))`.
2. استرجع أول ورقة عمل وادخل إلى مجموعة `cells` الخاصة بها.
3. ضع صيغة المصفوفة الديناميكية في الخلية **A6**، أسفل نطاق المصدر مباشرة، عن طريق استدعاء `cells["A6"].set_dynamic_array_formula("=TRANSPOSE(A1:D5)", None, True)`.
4. يمرر الوسيط `None` قيم `FormulaParseOptions` الافتراضية، ويخبر الوسيط الثالث `True` Aspose.Cells بمعاملة الصيغة كمصفوفة ديناميكية وتقييمها بحيث تُكتب القيم المنتشرة في المصنف.
5. احفظ المصنف باستخدام `workbook.save(outputFile)`.
تحتوي الخلية **A6** على الصيغة `=TRANSPOSE(A1:D5)` وينشر Excel النتيجة تلقائيًا في المنطقة **A6:D10**، وهي كتلة من 5 صفوف و4 أعمدة مساوية للبيانات بعد التبديل.

{{% alert color="primary" %}}
تعمل هذه الطريقة **فقط في Excel 365 / 2021 أو الإصدارات الأحدث**. لن تقوم إصدارات Excel الأقدم بنشر صيغ المصفوفات الديناميكية بشكل صحيح.
{{% /alert %}}

```python
import aspose.cells as ac
srcFile = "source.xlsx"
outFile = "output_transpose_dynamic.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.Xlsx))
worksheet = workbook.worksheets[0]
cells = worksheet.cells
cells["A6"].set_dynamic_array_formula("=TRANSPOSE(A1:D5)", ac.FormulaParseOptions(), True)
workbook.save(outFile, ac.SaveFormat.Xlsx)
```

## **الطريقة الثالثة — التبديل باستخدام صيغة مصفوفة كلاسيكية (CSE)**
استخدم هذه الطريقة عندما تريد الاحتفاظ بصيغة `TRANSPOSE` في المصنف ولكن قد يتم فتح ملف Excel الناتج في **إصدارات Excel الأقدم (ما قبل 2021، بما في ذلك 2019 و2016 و2013 وما إلى ذلك)** التي لا تدعم نشر المصفوفات الديناميكية. تعد صيغة المصفوفة الكلاسيكية عبر CSE (Ctrl+Shift+Enter) البديل المتوافق مع الإصدارات السابقة الذي يمكن لجميع إصدارات Excel تقييمه.

### **واجهة API المستخدمة**
`cell.set_array_formula(array_formula, n_rows, n_columns)` هو أسلوب على `Aspose.Cells.Cell` يقوم بتعيين **صيغة مصفوفة كلاسيكية (CSE)** لخلية الإرساء ويحدد أبعاد المصفوفة الناتجة. يكتب Aspose.Cells علامة صيغة المصفوفة متعددة الخلايا لكي يقيّم Excel الصيغة كتعبير مصفوفة واحد يملأ النطاق المحدد.

### **الخطوات**
1. حمّل مصنف المصدر بنفس الطريقة المستخدمة في الطرق السابقة.
2. استرجع أول ورقة عمل وادخل إلى مجموعة `cells` الخاصة بها.
3. استدعِ `cells["A6"].set_array_formula("=TRANSPOSE(A1:D5)", 4, 5)`. الوسيط الثاني `4` هو عدد صفوف المصفوفة الناتجة والوسيط الثالث `5` هو عدد الأعمدة.
4. احفظ المصنف باستخدام `workbook.save(outputFile)`.
تعد الخلية **A6** إرساء صيغة المصفوفة وتمتد المصفوفة المقيّمة عبر 4 صفوف و5 أعمدة بدءًا من A6، مطابقة لأبعاد نطاق المصدر A1:D5 بعد التبديل. يكتب Excel علامة صيغة المصفوفة الواحدة عبر النطاق الناتج لكي تقوم إصدارات Excel الأقدم بتقييمها بشكل صحيح.

{{% alert color="primary" %}}
تعد صيغ المصفوفة الكلاسيكية CSE هي الطريقة التقليدية في Excel لتقييم تعبير `TRANSPOSE` وهذه الطريقة متوافقة عالميًا عبر جميع إصدارات Excel.
{{% /alert %}}

```python
import aspose.cells as ac
# تحميل مصنف المصدر باستخدام خيارات تحميل xlsx
srcFile = "source.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.Xlsx))
# الوصول إلى ورقة العمل الأولى ومجموعة الخلايا الخاصة بها
worksheet = workbook.worksheets[0]
cells = worksheet.cells
# تعيين صيغة الصفيف الكلاسيكية CSE على الخلية A6.
# الصيغة =TRANSPOSE(A1:D5) تدور نطاق المصدر الذي يحتوي على 5 صفوف × 4 أعمدة
# إلى مصفوفة 4 صفوف × 5 أعمدة. الوسيط الثاني (4) هو عدد الصفوف
# والوسيط الثالث (5) هو عدد الأعمدة في المصفوفة الناتجة.
# Aspose.Cells يكتب علامة صيغة الصفيف CSE بحيث يقوم Excel بتقييمها كـ
# صيغة صفيف متعددة الخلايا واحدة، متوافقة مع إصدارات Excel القديمة
# (2019، 2016، 2013، إلخ) التي لا تدعم انسكاب الصفيف الديناميكي.
cells["A6"].set_array_formula("=TRANSPOSE(A1:D5)", 4, 5)
# حفظ المصنف بحيث يتم الاحتفاظ بعلامة صيغة الصفيف
workbook.save("output.xlsx")
```

## **المقارنة — متى تستخدم كل طريقة**
| Approach | API / Method | Excel Version | Source formula preserved? | Output range |
|----------|--------------|---------------|--------------------------|--------------|
| Approach 1 — In-place transpose | `range.transpose()` | All Excel versions | No (values only) | Initial anchor range, 5×4 |
| Approach 2 — Dynamic array formula | `cell.set_dynamic_array_formula` | Excel 365 / 2021+ | Yes (spills dynamically) | Spilled from anchor |
| Approach 3 — Classic array formula (CSE) | `cell.set_array_formula` | All Excel versions | Yes (multi-cell array formula) | Explicit size, 4×5 |
استخدم **الطريقة الأولى** عندما تحتاج إلى تحويل سريع متوافق عبر الإصدارات وتريد فقط كتابة القيم بعد التبديل في الملف. استخدم **الطريقة الثانية** عندما يكون Excel الحديث مضمونًا وتريد أن تظل الصيغة حية وتتحدث إذا تغير المصدر. استخدم **الطريقة الثالثة** عندما تحتاج إلى أوسع توافق مع الاحتفاظ بالصيغة عبر جميع إصدارات Excel، بما في ذلك الإصدارات الأقدم التي لا تدعم المصفوفات الديناميكية.

## **مقالات ذات صلة**
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for Python via .NET](/cells/ar/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Inserting an Image into a Cell](/cells/ar/python-net/inserting-an-image-into-a-cell/)
- [Splitting Excel Files into Multiple Files](/cells/ar/python-net/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="python-net" >}}