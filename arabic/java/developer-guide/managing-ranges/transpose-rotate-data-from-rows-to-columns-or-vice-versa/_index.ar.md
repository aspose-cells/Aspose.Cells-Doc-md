---
title: تبديل النطاق
linktitle: تبديل النطاق
description: توضح هذه المقالة كيفية تبديل أو تدوير البيانات من الصفوف إلى الأعمدة أو العكس في ملفات Excel باستخدام Aspose.Cells for Java، من خلال ثلاث طرق مختلفة.
keywords: Aspose.Cells, Java library, spreadsheet, transpose range, rotate data, transpose function, dynamic array formula, array formula, Excel TRANSPOSE, Rows to Columns
type: docs
weight: 80
url: /ar/java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells for Java تبديل (تدوير) البيانات بحيث تصبح الصفوف أعمدة والأعمدة صفوفًا بثلاث طرق مختلفة. تستخدم الطريقة الأولى أسلوب `Range.transpose()` الموضعي وتعمل في كل إصدار من Excel، بينما تستخدم الطريقة الثانية `Cell.setDynamicArrayFormula()` لكتابة صيغة مصفوفة ديناميكية حديثة من النوع `=TRANSPOSE(...)` تتدفق تلقائيًا في Excel 365 أو Excel 2021. أما الطريقة الثالثة فتستخدم `Cell.setArrayFormula()` لكتابة صيغة مصفوفة كلاسيكية من النوع Ctrl+Shift+Enter (CSE) متوافقة مع إصدارات Excel الأقدم. تستعرض هذه المقالة كل طريقة من خلال تعليمات خطوة بخطوة وأمثلة شاملة على الكود.
{{% /alert %}}

## **المقدمة**
تبديل النطاق يعني تدويره بحيث يصبح ما كان صفًا عمودًا وما كان عمودًا صفًا، وهو ما يعكس البيانات فعليًا عبر قطرها الرئيسي. في Microsoft Excel، تنفذ دالة ورقة العمل `TRANSPOSE` هذه العملية، والمرجع المفاهيمي موثق على [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). يمكن تطبيق الفكرة نفسها برمجيًا على نطاق من الخلايا، وهو أمر مفيد في كثير من سيناريوهات الأعمال وإعداد التقارير.
تتضمن السيناريوهات الشائعة التي يكون فيها التبديل مفيدًا ما يلي.
- إعادة توجيه تقارير المبيعات الفصلية أو السنوية حيث تمتد الفترات عادةً عبر الصفحة والمناطق إلى الأسفل، أو العكس.
- تبديل توجيه المحاور في لوحات المعلومات أو الرسوم البيانية بحيث يمتد السلسل الزمني إلى الأسفل بدلاً من العبور.
- إعادة تشكيل البيانات المستوردة من أنظمة خارجية لتتطابق مع التخطيط المتوقع من خلال التحليل أو قوالب إعداد التقارير اللاحقة.
لتسهيل بقية المقالة، يستخدم كل مثال جدول المبيعات حسب المنطقة والربع التالي. يحتل هذا الجدول في مصنف العينة النطاق **A1:D5**، مع ترك **A1** فارغًا كزاوية علوية يسرى، و**B1:D1** تحتوي على رؤوس المناطق، و**A2:A5** تحتوي على رؤوس الأرباع.
| المنطقة           | أوروبا     | آسيا       | أمريكا الشمالية |
|-------------------|-----------|-----------|---------------|
| الربع الأول       | 21704714  | 8774099   | 12094215      |
| الربع الثاني      | 17987034  | 12214447  | 10873099      |
| الربع الثالث      | 19485029  | 14356879  | 15689543      |
| الربع الرابع      | 22567894  | 15763492  | 17456723      |
تقدم المقالة بعد ذلك ثلاث طرق مختلفة لتبديل هذه البيانات باستخدام Aspose.Cells for Java، تناسب كل منها إصدار Excel وحالة استخدام مختلفة.

## **الطريقة الأولى — تبديل النطاق في موضعه (Range.transpose)**
استخدم هذه الطريقة كلما أردت تبديل البيانات دون إشراك دالة ورقة العمل `TRANSPOSE`. تعمل في **كل إصدار من Excel** ولا تعتمد على المصفوفات الديناميكية، مما يجعلها الخيار الأكثر أمانًا للتوافق عبر الإصدارات. وهي مثالية عندما تحتاج فقط إلى الناتج النهائي بعد التبديل ولا تحتاج إلى الاحتفاظ بصيغة `TRANSPOSE` الأصلية في المصنف.

### **واجهة API المستخدمة**
`Range.transpose()` هو أسلوب مثيل على الفئة `com.aspose.cells.Range`. يستدعيه لتبديل النطاق في موضعه عن طريق تبديل صفوفه وأعمدته، بحيث يصبح ما كان صفًا عمودًا وما كان عمودًا صفًا. يعدل الأسلوب الخلايا الأساسية مباشرة دون كتابة صيغة.

### **الخطوات**
1. افتح مصنف المصدر مع تعيين `LoadOptions` على تنسيق `.xlsx` باستدعاء `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. استرجع ورقة العمل الأولى من المصنف باستخدام `workbook.getWorksheets().get(0)`.
3. الوصول إلى مجموعة الخلايا في ورقة العمل من خلال `worksheet.getCells()`.
4. أنشئ نطاق المصدر الذي يغطي **A1:D5** باستدعاء `cells.createRange("A1:D5")`.
5. استدعِ `source.transpose()` لتدوير النطاق في موضعه، مع تبديل الصفوف والأعمدة.
6. احفظ المصنف باستخدام `workbook.save(outputFile)`.
بعد التبديل، يحتفظ نفس نطاق الإرساء بالبيانات المدارة. يقرأ الصف الأول (فارغًا، **Europe**، **Asia**، **North America**) ويقرأ العمود الأول (فارغًا، **Qtr 1**، **Qtr 2**، **Qtr 3**، **Qtr 4**). يصبح كل عمود أصلي من أعمدة المبيعات صفًا في النطاق الذي تم تبديله.

```java
import com.aspose.cells.*;
String srcFile = "source.xlsx";
String outputFile = "transposed.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
source.transpose();
workbook.save(outputFile);
```

## **الطريقة الثانية — التبديل باستخدام صيغة مصفوفة ديناميكية (Excel 365 / 2021)**
استخدم هذه الطريقة عندما تريد الاحتفاظ بصيغة `=TRANSPOSE(A1:D5)` كصيغة حية في مصنف الإخراج بحيث يتم تحديث النتيجة تلقائيًا إذا تغيرت بيانات المصدر، وسيتم فتح ملف Excel الناتج في **Excel 365 / Excel 2021 أو الإصدارات الأحدث** حيث يتم دعم المصفوفات الديناميكية ومشغل التدفق.

### **واجهة API المستخدمة**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` هو أسلوب على `com.aspose.cells.Cell` يعيّن صيغة الخلية كصيغة **مصفوفة ديناميكية**. يقيّم Excel الصيغة مرة ويتدفق الناتج تلقائيًا إلى الخلايا المحيطة. المعامل الثالث، عند تعيينه إلى `true`، يوجّه Aspose.Cells إلى حساب القيم الناتجة أيضًا عند وقت الكتابة.

### **الخطوات**
1. حمّل مصنف المصدر باستخدام `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. استرجع ورقة العمل الأولى ووصل إلى مجموعتها `Cells`.
3. ضع صيغة المصفوفة الديناميكية في الخلية **A6**، أسفل نطاق المصدر مباشرة، باستدعاء `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)`.
4. الوسيط `null` يمرر `FormulaParseOptions` الافتراضية، والوسيط الثالث `true` يخبر Aspose.Cells بمعاملة الصيغة كمصفوفة ديناميكية وتقييمها بحيث تُكتب القيم المتدفقة في المصنف.
5. احفظ المصنف باستخدام `workbook.save(outputFile)`.
تحتوي الخلية **A6** على الصيغة `=TRANSPOSE(A1:D5)` ويقوم Excel بتدفق الناتج تلقائيًا إلى المنطقة **A6:D10**، وهي كتلة من 5 صفوف × 4 أعمدة مساوية للبيانات المبدلة.

{{% alert color="primary" %}}
تعمل هذه الطريقة **فقط في Excel 365 / 2021 أو الإصدارات الأحدث**. لن تقوم إصدارات Excel الأقدم بتدفق صيغ المصفوفات الديناميكية بشكل صحيح.
{{% /alert %}}

```java
import com.aspose.cells.*;
String srcFile = "source.xlsx";
String outFile = "output_transpose_dynamic.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true);
workbook.save(outFile, SaveFormat.XLSX);
```

## **الطريقة الثالثة — التبديل باستخدام صيغة مصفوفة كلاسيكية (CSE)**
استخدم هذه الطريقة عندما تريد الاحتفاظ بصيغة `TRANSPOSE` في المصنف ولكن قد يتم فتح ملف Excel الناتج في **إصدارات Excel الأقدم (قبل 2021، بما في ذلك 2019 و2016 و2013 وما إلى ذلك)** حيث لا يتم دعم تدفق المصفوفات الديناميكية. صيغة المصفوفة الكلاسيكية من النوع CSE (Ctrl+Shift+Enter) هي البديل المتوافق مع الإصدارات الأقدم الذي يمكن لكل إصدارات Excel تقييمه.

### **واجهة API المستخدمة**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` هو أسلوب على `com.aspose.cells.Cell` يعيّن **صيغة مصفوفة كلاسيكية (CSE)** على خلية الإرساء ويعلن عن أبعاد المصفوفة الناتجة. يكتب Aspose.Cells علامة صيغة المصفوفة متعددة الخلايا بحيث يقيّم Excel الصيغة كتعبير مصفوفة واحد يملأ النطاق المعلن.

### **الخطوات**
1. حمّل مصنف المصدر بنفس الطريقة المستخدمة في الطرق السابقة.
2. استرجع ورقة العمل الأولى ووصل إلى مجموعتها `Cells`.
3. استدعِ `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. الوسيط الثاني `4` هو عدد صفوف المصفوفة الناتجة والوسيط الثالث `5` هو عدد الأعمدة.
4. احفظ المصنف باستخدام `workbook.save(outputFile)`.
تكون الخلية **A6** هي إرساء صيغة المصفوفة وتمتد المصفوفة المقيمة عبر 4 صفوف × 5 أعمدة بدءًا من A6، مطابقة لأبعاد المصدر A1:D5 بعد التبديل. يكتب Excel علامة صيغة مصفوفة واحدة عبر النطاق الناتج بحيث تقوم إصدارات Excel الأقدم بتقييمها بشكل صحيح.

{{% alert color="primary" %}}
صيغ المصفوفة من النوع CSE هي الطريقة الكلاسيكية في Excel لتقييم تعبير `TRANSPOSE` وهذه الطريقة متوافقة عالميًا عبر إصدارات Excel.
{{% /alert %}}

```java
import com.aspose.cells.*;
// تحميل المصنف المصدر مع خيارات التحميل بصيغة xlsx
String srcFile = "source.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
// الوصول إلى ورقة العمل الأولى ومجموعة الخلايا الخاصة بها
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
// تعيين صيغة المصفوفة الكلاسيكية CSE في الخلية A6.
// الصيغة =TRANSPOSE(A1:D5) تدور نطاق المصدر الذي يتكون من 5 صفوف × 4 أعمدة
// إلى مصفوفة من 4 صفوف × 5 أعمدة. الوسيط الثاني (4) هو عدد الصفوف
// والوسيط الثالث (5) هو عدد الأعمدة في المصفوفة الناتجة.
// يقوم Aspose.Cells بكتابة علامة صيغة المصفوفة CSE بحيث يقوم Excel بتقييمها كـ
// صيغة مصفوفة واحدة متعددة الخلايا، متوافقة مع إصدارات Excel القديمة
// (2019، 2016، 2013، إلخ) التي لا تدعم الانسكاب الديناميكي للمصفوفات.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// حفظ المصنف بحيث يتم الاحتفاظ بعلامة صيغة المصفوفة
workbook.save("output.xlsx");
```

## **المقارنة — متى تستخدم كل طريقة**
| الطريقة | واجهة API / الأسلوب | إصدار Excel | هل الصيغة المصدر محفوظة؟ | نطاق الإخراج |
|----------|--------------|---------------|--------------------------|--------------|
| الطريقة الأولى — تبديل في الموضع | `Range.transpose()` | كل إصدارات Excel | لا (قيم فقط) | نفس نطاق الإرساء، 5×4 |
| الطريقة الثانية — صيغة مصفوفة ديناميكية | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | نعم (تتدفق ديناميكيًا) | متدفق من الإرساء |
| الطريقة الثالثة — صيغة مصفوفة كلاسيكية (CSE) | `Cell.setArrayFormula` | كل إصدارات Excel | نعم (صيغة مصفوفة متعددة الخلايا) | حجم صريح، 4×5 |
استخدم **الطريقة الأولى** عندما تحتاج إلى تحويل سريع متوافق عبر الإصدارات وتحتاج فقط إلى القيم المبدلة المكتوبة في الملف. استخدم **الطريقة الثانية** عندما يكون Excel الحديث مضمونًا وتريد أن تظل الصيغة حية وتتحدث إذا تغير المصدر. استخدم **الطريقة الثالثة** عندما تحتاج إلى أوسع توافق مع صيغة محفوظة عبر كل إصدار من Excel، بما في ذلك الإصدارات الأقدم التي لا تدعم المصفوفات الديناميكية.

## **مقالات ذات صلة**
- [SmartMarker Single Cell Array Rendering | Aspose.Cells Java](/cells/ar/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Inserting an Image into a Cell](/cells/ar/java/inserting-an-image-into-a-cell/)
- [Splitting Excel Files into Multiple Files](/cells/ar/java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="java" >}}