---
title: تبديل النطاق
linktitle: تبديل النطاق
description: توضح هذه المقالة كيفية تبديل أو تدوير البيانات من الصفوف إلى الأعمدة أو العكس في ملفات Excel باستخدام Aspose.Cells for C++ بثلاث طرق مختلفة.
keywords: Aspose.Cells, مكتبة C++, جدول بيانات, تبديل النطاق, تدوير البيانات, دالة التبديل, صيغة المصفوفة الديناميكية, صيغة المصفوفة, Excel TRANSPOSE, الصفوف إلى الأعمدة
type: docs
weight: 80
url: /ar/cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells for C++ تبديل (تدوير) البيانات بحيث تصبح الصفوف أعمدة والأعمدة صفوفًا بثلاث طرق مختلفة. تستخدم الطريقة الأولى طريقة `Range.Transpose()` الموضعية وتعمل مع كل إصدار من إصدارات Excel، بينما تستخدم الطريقة الثانية `Cell.SetDynamicArrayFormula()` لكتابة صيغة مصفوفة ديناميكية حديثة `=TRANSPOSE(...)` تنتشر تلقائيًا في Excel 365 أو Excel 2021. أما الطريقة الثالثة فتستخدم `Cell.SetArrayFormula()` لكتابة صيغة مصفوفة تقليدية من نوع Ctrl+Shift+Enter (CSE) متوافقة مع إصدارات Excel الأقدم. تستعرض هذه المقالة كل طريقة بتعليمات خطوة بخطوة وأمثلة كود كاملة.
{{% /alert %}}

## **المقدمة**
يعني تبديل النطاق تدويره بحيث يصبح ما كان صفًا عمودًا وما كان عمودًا صفًا، مع عكس البيانات عبر قطرها الرئيسي. في Microsoft Excel، تؤدي دالة ورقة العمل `TRANSPOSE` هذه العملية، والمرجع المفاهيمي موثق في [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). يمكن تطبيق هذا المفهوم برمجيًا على نطاق من الخلايا، وهو أمر مفيد في العديد من سيناريوهات الأعمال وإعداد التقارير.
- إعادة توجيه تقارير المبيعات الفصلية أو السنوية حيث تمتد الفصول عادةً عبر الصفحة والمناطق إلى أسفل الصفحة، أو العكس.
- تبديل توجيه المحور في لوحات المعلومات أو الرسوم البيانية بحيث تمتد السلسلة الزمنية إلى أسفل الصفحة بدلاً من امتدادها عبرها.
- إعادة تشكيل البيانات المستوردة من الأنظمة الخارجية لتتطابق مع التخطيط المتوقع من قبل أدوات التحليل أو قوالب التقارير اللاحقة.
لجعل بقية المقالة ملموسة، تستخدم كل مثال جدول المبيعات حسب المنطقة والفصل التالي. في مصنف العينة يشغل هذا الجدول النطاق **A1:D5**، مع ترك **A1** فارغًا كزاوية علوية يسرى، وتحتوي **B1:D1** على رؤوس المناطق، وتحتوي **A2:A5** على رؤوس الفصول.
| المنطقة          | أوروبا     | آسيا       | أمريكا الشمالية |
|-------------------|-----------|-----------|---------------|
| الفصل 1           | 21704714  | 8774099   | 12094215      |
| الفصل 2           | 17987034  | 12214447  | 10873099      |
| الفصل 3           | 19485029  | 14356879  | 15689543      |
| الفصل 4           | 22567894  | 15763492  | 17456723      |
تقدم المقالة بعد ذلك ثلاث طرق مختلفة لتبديل هذه البيانات باستخدام Aspose.Cells for C++، وكل منها مناسب لإصدار مختلف من Excel وحالة استخدام مختلفة.

## **الطريقة 1 — تبديل النطاق في مكانه (Range.Transpose)**
استخدم هذه الطريقة كلما أردت تبديل البيانات دون إشراك دالة ورقة العمل `TRANSPOSE`. تعمل مع **كل إصدار من إصدارات Excel** ولا تعتمد على المصفوفات الديناميكية، مما يجعلها الخيار الأكثر أمانًا للتوافق عبر الإصدارات. وهي مثالية عندما تحتاج فقط إلى الناتج المبدل النهائي ولا تحتاج إلى الاحتفاظ بصيغة `TRANSPOSE` الأصلية في المصنف.

### **واجهة API المستخدمة**
`Range.Transpose()` هي طريقة مثيل على الفئة `Aspose.Cells.Range`. استدعاؤها يقلب النطاق في مكانه عن طريق تبديل صفوفه وأعمدته، فما كان صفًا يصبح عمودًا وما كان عمودًا يصبح صفًا. تعدل الطريقة الخلايا الأساسية مباشرة دون كتابة صيغة.

### **الخطوات**
1. افتح المصنف المصدر مع ضبط `LoadOptions` على تنسيق `.xlsx` بإنشاء `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))`.
2. استرجع ورقة العمل الأولى من المصنف باستخدام `workbook.GetWorksheets().Get(0)`.
3. الوصول إلى مجموعة خلايا ورقة العمل من خلال `worksheet.GetCells()`.
4. أنشئ النطاق المصدر الذي يغطي **A1:D5** عن طريق استدعاء `cells.CreateRange(u"A1:D5")`.
5. استدعِ `source.Transpose()` لتدوير النطاق في مكانه، مع تبديل الصفوف والأعمدة.
6. احفظ المصنف باستخدام `workbook.Save(outputFile)`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    U16String srcFile(u"source.xlsx");
    U16String outputFile(u"transposed.xlsx");
    LoadOptions loadOptions(LoadFormat::Xlsx);
    Workbook workbook(srcFile, loadOptions);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    Range source = cells.CreateRange(u"A1:D5");
    source.Transpose();
    workbook.Save(outputFile);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **الطريقة 2 — التبديل باستخدام صيغة مصفوفة ديناميكية (Excel 365 / 2021)**
استخدم هذه الطريقة عندما تريد الاحتفاظ بصيغة `=TRANSPOSE(A1:D5)` كصيغة حية في مصنف الناتج بحيث يتم تحديث النتيجة تلقائيًا إذا تغيرت البيانات المصدر، وسيُفتح ملف Excel الهدف في **Excel 365 / Excel 2021 أو أحدث** حيث يتم دعم المصفوفات الديناميكية ومعامل الانتشار.

### **واجهة API المستخدمة**
`Cell.SetDynamicArrayFormula(const char* formula, FormulaParseOptions options, bool calculateValue)` هي طريقة على `Aspose.Cells.Cell` تضبط صيغة الخلية كـ **صيغة مصفوفة ديناميكية**. يقيّم Excel الصيغة مرة واحدة وينتشر الناتج تلقائيًا في الخلايا المحيطة. المعامل الثالث، عند ضبطه على `true`، يوجه Aspose.Cells إلى حساب القيم الناتجة أيضًا وقت الكتابة.

### **الخطوات**
1. حمّل المصنف المصدر بإنشاء `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))`.
2. استرجع ورقة العمل الأولى عبر `workbook.GetWorksheets().Get(0)` والوصول إلى مجموعة `Cells` الخاصة بها من خلال `worksheet.GetCells()`.
3. ضع صيغة المصفوفة الديناميكية على الخلية **A6**، أسفل النطاق المصدر مباشرة، عن طريق استدعاء `cells.Get(u"A6").SetDynamicArrayFormula(u"=TRANSPOSE(A1:D5)", nullptr, true)`.
4. المعامل `nullptr` يمرر `FormulaParseOptions` الافتراضية، والمعامل الثالث `true` يخبر Aspose.Cells بمعاملة الصيغة كمصفوفة ديناميكية وتقييمها بحيث تُكتب القيم المنتشرة إلى المصنف.
5. احفظ المصنف باستخدام `workbook.Save(outputFile)`.
تحتوي الخلية **A6** على الصيغة `=TRANSPOSE(A1:D5)` وينتشر Excel النتيجة تلقائيًا في المنطقة **A6:D10**، وهو كتلة من 5 صفوف و4 أعمدة تساوي البيانات المبدلة.

{{% alert color="primary" %}}
تعمل هذه الطريقة **فقط على Excel 365 / 2021 أو أحدث**. لن تقوم إصدارات Excel الأقدم بنشر صيغ المصفوفات الديناميكية بشكل صحيح.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    std::string srcFile = "source.xlsx";
    std::string outFile = "output_transpose_dynamic.xlsx";
    LoadOptions loadOptions(LoadFormat::Xlsx);
    Workbook workbook(U16String(srcFile.c_str()), loadOptions);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    Cell cell = cells.Get(u"A6");
    FormulaParseOptions options;
    cell.SetDynamicArrayFormula(U16String("=TRANSPOSE(A1:D5)"), options, true);
    workbook.Save(U16String(outFile.c_str()), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **الطريقة 3 — التبديل باستخدام صيغة مصفوفة تقليدية (CSE)**
استخدم هذه الطريقة عندما تريد الاحتفاظ بصيغة `TRANSPOSE` في المصنف ولكن قد يُفتح ملف Excel الهدف في **إصدارات Excel الأقدم (ما قبل 2021، بما في ذلك 2019 و2016 و2013 وما إلى ذلك)** حيث لا يتم دعم نشر المصفوفات الديناميكية. صيغة المصفوفة التقليدية CSE (Ctrl+Shift+Enter) هي البديل المتوافق مع الإصدارات السابقة الذي يمكن لجميع إصدارات Excel تقييمه.

### **واجهة API المستخدمة**
`Cell.SetArrayFormula(const char* arrayFormula, int nRows, int nColumns)` هي طريقة على `Aspose.Cells.Cell` تخصص **صيغة مصفوفة تقليدية (CSE)** للخلية المرجعية وتعلن عن أبعاد المصفوفة الناتجة. يكتب Aspose.Cells علامة صيغة المصفوفة متعددة الخلايا بحيث يقيّم Excel الصيغة كتعبير مصفوفة واحد يملأ النطاق المعلن.

### **الخطوات**
2. استرجع ورقة العمل الأولى عبر `workbook.GetWorksheets().Get(0)` والوصول إلى مجموعة `Cells` الخاصة بها من خلال `worksheet.GetCells()`.
3. استدعِ `cells.Get(u"A6").SetArrayFormula(u"=TRANSPOSE(A1:D5)", 4, 5)`. المعامل الثاني `4` هو عدد صفوف مصفوفة الوجهة، والمعامل الثالث `5` هو عدد الأعمدة.
4. احفظ المصنف باستخدام `workbook.Save(outputFile)`.
تعد الخلية **A6** الخلية المرجعية لصيغة المصفوفة وتمتد المصفوفة المقيمة على 4 صفوف و5 أعمدة بدءًا من A6، مطابقة لأبعاد النطاق A1:D5 المصدر بعد التبديل. يكتب Excel علامة صيغة مصفوفة واحدة عبر النطاق الناتج بحيث تقوم إصدارات Excel الأقدم بتقييمها بشكل صحيح.

{{% alert color="primary" %}}
صيغ المصفوفة CSE هي الطريقة التقليدية في Excel لتقييم تعبير `TRANSPOSE` وهذه الطريقة متوافقة عالميًا عبر إصدارات Excel.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // تحميل المصنف المصدر باستخدام خيارات التحميل xlsx
    std::string srcFile = "source.xlsx";
    Workbook workbook(U16String(srcFile.c_str()), LoadOptions(LoadFormat::Xlsx));
    // الوصول إلى ورقة العمل الأولى ومجموعة الخلايا الخاصة بها
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // تعيين صيغة المصفوفة الكلاسيكية CSE على الخلية A6.
    // الصيغة =TRANSPOSE(A1:D5) تدور نطاق المصدر ذو الـ 5 صفوف و 4 أعمدة
    // إلى مصفوفة ذات 4 صفوف و 5 أعمدة. الوسيط الثاني (4) هو عدد الصفوف
    // والوسيط الثالث (5) هو عدد أعمدة المصفوفة الناتجة.
    // يقوم Aspose.Cells بكتابة علامة صيغة المصفوفة CSE بحيث يقوم Excel بتقييمها كـ
    // صيغة مصفوفة واحدة متعددة الخلايا، متوافقة مع إصدارات Excel الأقدم
    // (2019، 2016، 2013، إلخ) التي لا تدعم الانسكاب الديناميكي للمصفوفات.
    cells.Get(u"A6").SetArrayFormula(u"=TRANSPOSE(A1:D5)", 4, 5);
    // حفظ المصنف بحيث تتحدث بعلامة صيغة المصفوفة
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **المقارنة — متى تستخدم كل طريقة**
| الطريقة | واجهة API / الطريقة | إصدار Excel | هل الصيغة المصدر محفوظة؟ | نطاق الناتج |
|----------|--------------|---------------|--------------------------|--------------|
| الطريقة 1 — تبديل في المكان | `Range.Transpose()` | كل إصدارات Excel | لا (القيم فقط) | نطاق مرجعي أولي، 5×4 |
| الطريقة 2 — صيغة مصفوفة ديناميكية | `Cell.SetDynamicArrayFormula` | Excel 365 / 2021+ | نعم (تنتشر ديناميكيًا) | تنتشر من الخلية المرجعية |
| الطريقة 3 — صيغة مصفوفة تقليدية (CSE) | `Cell.SetArrayFormula` | كل إصدارات Excel | نعم (صيغة مصفوفة متعددة الخلايا) | حجم صريح، 4×5 |
استخدم **الطريقة 1** عندما تحتاج إلى تحويل سريع متوافق عبر الإصدارات وتحتاج فقط إلى كتابة القيم المبدلة في الملف. استخدم **الطريقة 2** عندما يكون Excel الحديث مضمونًا وتريد أن تظل الصيغة حية وتتحدث إذا تغير المصدر. استخدم **الطريقة 3** عندما تحتاج إلى أوسع توافق مع صيغة محفوظة عبر كل إصدار من إصدارات Excel، بما في ذلك الإصدارات الأقدم التي لا تدعم المصفوفات الديناميكية.

## **مقالات ذات صلة**
- [عرض المصفوفة لخلية واحدة من SmartMarker | Aspose.Cells for C++](/cells/ar/cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [إدراج صورة في خلية](/cells/ar/cpp/inserting-an-image-into-a-cell/)
- [تقسيم ملفات Excel إلى ملفات متعددة](/cells/ar/cpp/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="" >}}