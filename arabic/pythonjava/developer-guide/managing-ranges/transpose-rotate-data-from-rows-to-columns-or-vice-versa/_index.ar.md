---
title: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for Python via Java with three different approaches.
linktitle: تبديل النطاق
url: /ar/python-java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, Python via Java library, spreadsheet, transpose range, rotate data, transpose function, dynamic array formula, array formula, Excel TRANSPOSE, Rows to Columns
type: docs
weight: 80
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells for Python via Java تبديل (تدوير) البيانات بحيث تصبح الصفوف أعمدة والأعمدة صفوفًا بثلاث طرق مختلفة. تستخدم الطريقة الأولى أسلوب `Range.transpose()` في مكانه وتعمل مع كل إصدارات Excel، بينما تستخدم الطريقة الثانية `Cell.setDynamicArrayFormula()` لكتابة صيغة صفيف ديناميكي حديثة `=TRANSPOSE(...)` تنتشر تلقائيًا في Excel 365 أو Excel 2021. أما الطريقة الثالثة فتستخدم `Cell.setArrayFormula()` لكتابة صيغة صفيف كلاسيكية من نوع Ctrl+Shift+Enter (CSE) متوافقة مع إصدارات Excel القديمة. تستعرض هذه المقالة كل طريقة من خلال تعليمات خطوة بخطوة وأمثلة كاملة على الكود.
{{% /alert %}}

## **المقدمة**
يعني تبديل النطاق تدويره بحيث يصبح ما كان صفًا عمودًا وما كان عمودًا صفًا، مما يعكس البيانات بشكل فعال عبر قطرها الرئيسي. في Microsoft Excel، تنفذ دالة ورقة العمل `TRANSPOSE` هذه العملية، ويتوفر المرجع المفاهيمي لها على [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). يمكن تطبيق الفكرة نفسها برمجيًا على نطاق من الخلايا، وهو أمر مفيد في العديد من سيناريوهات الأعمال والتقارير.
تتضمن السيناريوهات الشائعة التي يكون فيها التبديل مفيدًا ما يلي.
- إعادة توجيه تقارير المبيعات ربع السنوية أو السنوية حيث تمتد الأرباع عادةً عبر الصفحة والمناطق إلى أسفلها، أو العكس.
- تبديل توجيه المحور في لوحات المعلومات أو الرسوم البيانية بحيث يتسلسل الوقت إلى أسفل الصفحة بدلاً من أن يمتد عبرها.
- إعادة تشكيل البيانات المستوردة من أنظمة خارجية بحيث تتطابق مع التخطيط المتوقع من قبل أدوات التحليل أو قوالب التقارير اللاحقة.
لتكون بقية المقالة ملموسة، يستخدم كل مثال جدول المبيعات حسب المنطقة حسب الربع التالي. في مصنف العينة، يشغل هذا الجدول النطاق **A1:D5**، حيث تُترك **A1** فارغة كزاوية علوية يسرى، وتحتوي **B1:D1** على رؤوس المناطق، وتحتوي **A2:A5** على رؤوس الأرباع.
| المنطقة          | أوروبا     | آسيا       | أمريكا الشمالية |
|-------------------|-----------|-----------|---------------|
| الربع 1           | 21704714  | 8774099   | 12094215      |
| الربع 2           | 17987034  | 12214447  | 10873099      |
| الربع 3           | 19485029  | 14356879  | 15689543      |
| الربع 4           | 22567894  | 15763492  | 17456723      |
ثم تعرض المقالة ثلاث طرق مختلفة لتبديل هذه البيانات باستخدام Aspose.Cells for Python via Java، وكل منها مناسب لإصدار Excel وحالة استخدام مختلفة.

## **الطريقة الأولى — تبديل النطاق في مكانه (Range.transpose)**
استخدم هذه الطريقة كلما أردت تبديل البيانات دون إشراك دالة ورقة العمل `TRANSPOSE`. تعمل على **كل إصدارات Excel** ولا تعتمد على المصفوفات الديناميكية، مما يجعلها الخيار الأكثر أمانًا من حيث التوافق عبر الإصدارات. وهي مثالية عندما تحتاج فقط إلى الناتج النهائي بعد التبديل ولا تحتاج إلى الاحتفاظ بصيغة `TRANSPOSE` الأصلية في المصنف.

### **واجهة API المستخدمة**
`Range.transpose()` هو أسلوب مثيل في الفئة `com.aspose.cells.Range`. يؤدي استدعاؤه إلى قلب النطاق في مكانه عن طريق تبديل صفوفه وأعمدته، فيصبح ما كان صفًا عمودًا وما كان عمودًا صفًا. يعدّل الأسلوب الخلايا الأساسية مباشرة دون كتابة صيغة.

### **الخطوات**
1. افتح مصنف المصدر مع ضبط `LoadOptions` على تنسيق `.xlsx` عن طريق استدعاء `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))`.
2. استرجع ورقة العمل الأولى من المصنف باستخدام `workbook.getWorksheets().get(0)`.
3. قم بالوصول إلى مجموعة خلايا ورقة العمل عبر `worksheet.getCells()`.
4. أنشئ نطاق المصدر الذي يغطي **A1:D5** عن طريق استدعاء `cells.createRange("A1:D5")`.
5. استدعِ `source.transpose()` لتدوير النطاق في مكانه، مع تبديل الصفوف والأعمدة.
6. احفظ المصنف باستخدام `workbook.save(outputFile)`.
بعد التبديل، يحتفظ نفس النطاق المرجعي بالبيانات المدوَّرة. يقرأ الصف الأول (فارغ، **أوروبا**، **آسيا**، **أمريكا الشمالية**) ويقرأ العمود الأول (فارغ، **الربع 1**، **الربع 2**، **الربع 3**، **الربع 4**). يصبح كل عمود أصلي من أعمدة المبيعات صفًا في النطاق المُبدَّل.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, LoadOptions, LoadFormat
srcFile = "source.xlsx"
outputFile = "transposed.xlsx"
loadOptions = LoadOptions(LoadFormat.Xlsx)
workbook = Workbook(srcFile, loadOptions)
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
source = cells.createRange("A1:D5")
source.transpose()
workbook.save(outputFile)
jpype.shutdownJVM()
```

## **الطريقة الثانية — التبديل باستخدام صيغة صفيف ديناميكي (Excel 365 / 2021)**
استخدم هذه الطريقة عندما تريد الحفاظ على صيغة `=TRANSPOSE(A1:D5)` كصيغة حية في مصنف الناتج بحيث تُحدَّث النتيجة تلقائيًا إذا تغيرت بيانات المصدر، وسيُفتح ملف Excel الناتج في **Excel 365 / Excel 2021 أو الإصدارات الأحدث** التي تدعم المصفوفات الديناميكية وعامل الانتشار.

### **واجهة API المستخدمة**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` هو أسلوب في `com.aspose.cells.Cell` يضبط صيغة الخلية كـ **صيغة صفيف ديناميكي**. يُقيّم Excel الصيغة مرة واحدة وينشر النتيجة تلقائيًا في الخلايا المحيطة. أما المعامل الثالث، عند ضبطه على `True`، فيُوجّه Aspose.Cells إلى حساب القيم الناتجة أيضًا وقت الكتابة.

### **الخطوات**
1. حمّل مصنف المصدر باستخدام `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))`.
2. استرجع ورقة العمل الأولى واطلع على مجموعة `Cells` الخاصة بها.
3. ضع صيغة الصفيف الديناميكي في الخلية **A6**، أسفل نطاق المصدر مباشرة، عن طريق استدعاء `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", None, True)`.
4. تمرر الوسيطة `None` القيمة الافتراضية لـ `FormulaParseOptions`، وتخبر الوسيطة الثالثة `True` Aspose.Cells بمعاملة الصيغة كمصفوفة ديناميكية وبتقييمها بحيث تُكتب القيم المنتشرة في المصنف.
5. احفظ المصنف باستخدام `workbook.save(outputFile)`.
تحتوي الخلية **A6** على الصيغة `=TRANSPOSE(A1:D5)` وينشر Excel النتيجة تلقائيًا في المنطقة **A6:D10**، وهي كتلة بأبعاد 5 صفوف في 4 أعمدة مساوية للبيانات المُبدَّلة.

{{% alert color="primary" %}}
تعمل هذه الطريقة **فقط على Excel 365 / 2021 أو الإصدارات الأحدث**. لن تنشر إصدارات Excel القديمة صيغ المصفوفات الديناميكية بشكل صحيح.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, LoadOptions, LoadFormat, FormulaParseOptions, SaveFormat
# الكود المنقول هنا
srcFile = "source.xlsx"
outFile = "output_transpose_dynamic.xlsx"
workbook = Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", FormulaParseOptions(), True)
workbook.save(outFile, SaveFormat.Xlsx)
jpype.shutdownJVM()
```

## **الطريقة الثالثة — التبديل باستخدام صيغة صفيف كلاسيكية (CSE)**
استخدم هذه الطريقة عندما تريد الاحتفاظ بصيغة `TRANSPOSE` في المصنف ولكن قد يُفتح ملف Excel الهدف في **إصدارات Excel الأقدم (ما قبل 2021، بما في ذلك 2019 و2016 و2013 وما إلى ذلك)** التي لا تدعم انتشار المصفوفات الديناميكية. تُعد صيغة الصفيف الكلاسيكية من نوع CSE (Ctrl+Shift+Enter) البديل المتوافق مع الإصدارات الأقدم الذي يمكن لكل إصدارات Excel تقييمه.

### **واجهة API المستخدمة**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` هو أسلوب في `com.aspose.cells.Cell` يعين **صيغة صفيف كلاسيكية (CSE)** على الخلية المرجعية ويُعلن عن أبعاد المصفوفة الناتجة. يكتب Aspose.Cells علامة صيغة المصفوفة متعددة الخلايا لكي يُقيّم Excel الصيغة كتعبير مصفوفة واحد يملأ النطاق المعلن.

### **الخطوات**
1. حمّل مصنف المصدر بنفس الطريقة المستخدمة في الطرق السابقة.
2. استرجع ورقة العمل الأولى واطلع على مجموعة `Cells` الخاصة بها.
3. استدعِ `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. الوسيطة الثانية `4` هي عدد صفوف مصفوفة الوجهة، والوسيطة الثالثة `5` هي عدد الأعمدة.
4. احفظ المصنف باستخدام `workbook.save(outputFile)`.
تُعد الخلية **A6** هي المرجع لصيغة الصفيف، وتمتد المصفوفة المُقيّمة على 4 صفوف في 5 أعمدة بدءًا من A6، مطابقة لأبعاد نطاق المصدر A1:D5 بعد التبديل. يكتب Excel علامة صيغة المصفوفة الواحدة عبر النطاق الناتج لكي تُقيّمها إصدارات Excel الأقدم بشكل صحيح.

{{% alert color="primary" %}}
تُعد صيغ الصفيف من نوع CSE هي طريقة Excel الكلاسيكية لتقييم تعبير `TRANSPOSE` وهذه الطريقة متوافقة عالميًا عبر جميع إصدارات Excel.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, LoadOptions, LoadFormat, Worksheet, Cells
# تحميل ملف العمل المصدر باستخدام خيارات تحميل xlsx
srcFile = "source.xlsx"
workbook = Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))
# الوصول إلى ورقة العمل الأولى ومجموعة الخلايا الخاصة بها
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
# تعيين صيغة المصفوفة الكلاسيكية CSE على الخلية A6.
# الصيغة =TRANSPOSE(A1:D5) تدور نطاق المصدر الذي يحتوي على 5 صفوف × 4 أعمدة
# إلى مصفوفة من 4 صفوف × 5 أعمدة. الوسيط الثاني (4) هو عدد الصفوف
# والوسيط الثالث (5) هو عدد الأعمدة في المصفوفة الناتجة.
# يقوم Aspose.Cells بكتابة علامة صيغة المصفوفة CSE بحيث يقوم Excel بتقييمها كـ
# صيغة مصفوفة واحدة متعددة الخلايا، متوافقة مع إصدارات Excel الأقدم
# (2019، 2016، 2013، إلخ) التي لا تدعم فيضان المصفوفة الديناميكية.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)
# حفظ ملف العمل بحيث يتم الاحتفاظ بعلامة صيغة المصفوفة
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **المقارنة — متى تستخدم كل طريقة**
| الطريقة | واجهة API / الأسلوب | إصدار Excel | هل الصيغة المصدر محفوظة؟ | نطاق الناتج |
|----------|--------------|---------------|--------------------------|--------------|
| الطريقة الأولى — التبديل في مكانه | `Range.transpose()` | كل إصدارات Excel | لا (القيم فقط) | نفس النطاق المرجعي، 5×4 |
| الطريقة الثانية — صيغة صفيف ديناميكي | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | نعم (تنتشر ديناميكيًا) | تنتشر من الخلية المرجعية |
| الطريقة الثالثة — صيغة صفيف كلاسيكية (CSE) | `Cell.setArrayFormula` | كل إصدارات Excel | نعم (صيغة صفيف متعددة الخلايا) | حجم صريح، 4×5 |
استخدم **الطريقة الأولى** عندما تحتاج إلى تحويل سريع متوافق عبر الإصدارات وتريد فقط القيم المُبدَّلة مكتوبة في الملف. استخدم **الطريقة الثانية** عندما يكون Excel الحديث مضمونًا وتريد أن تظل الصيغة حية وتُحدَّث إذا تغير المصدر. استخدم **الطريقة الثالثة** عندما تحتاج إلى أوسع توافق مع صيغة محفوظة عبر كل إصدارات Excel، بما في ذلك الإصدارات الأقدم التي لا تدعم المصفوفات الديناميكية.

## **مقالات ذات صلة**
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for Python via Java](/cells/ar/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Inserting an Image into a Cell](/cells/ar/python-java/inserting-an-image-into-a-cell/)
- [Splitting Excel Files into Multiple Files](/cells/ar/python-java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="python" >}}